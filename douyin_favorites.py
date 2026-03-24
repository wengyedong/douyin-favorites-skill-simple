import argparse
import os
import json
import sys

# 添加子模块路径
sys.path.append(os.path.join(os.path.dirname(__file__), 'douyin-downloader'))

from douyin_downloader import download_douyin_video, validate_douyin_url

def main():
    # 解析命令行参数
    parser = argparse.ArgumentParser(description="抖音视频收藏工具")
    parser.add_argument("--url", required=True, help="抖音视频链接（支持短链接和长链接）")
    parser.add_argument("--output", default=os.getcwd(), help="输出目录（目录不存在则创建）")
    args = parser.parse_args()
    
    # 检查链接有效性
    if not validate_douyin_url(args.url):
        print("错误：无效的抖音视频链接")
        return 1
    
    # 下载视频
    print(f"开始下载视频: {args.url}")
    success = download_douyin_video(args.url, args.output)
    if not success:
        print("错误：视频下载失败")
        return 1

    # 解析视频ID并读取信息文件
    import re
    # 从原始URL提取视频ID
    video_id = None
    # 匹配长链接格式 https://www.douyin.com/video/123456789
    long_link_match = re.search(r'https?://(www\.)?douyin\.com/video/(\d+)', args.url)
    if long_link_match:
        video_id = long_link_match.group(2)
    else:
        # 对于短链接，我们需要从下载后的目录结构中获取
        # 遍历输出目录下的output文件夹
        output_dir = os.path.join(args.output, "output")
        if os.path.exists(output_dir):
            for item in os.listdir(output_dir):
                item_path = os.path.join(output_dir, item)
                if os.path.isdir(item_path):
                    # 假设目录名就是视频ID
                    video_id = item
                    break
    
    if not video_id:
        print("错误：无法获取视频ID")
        return 1
    
    # 构建信息文件路径
    info_file_path = os.path.join(args.output, "output", video_id, f"{video_id}_info.json")
    if not os.path.exists(info_file_path):
        print(f"错误：信息文件不存在: {info_file_path}")
        return 1
    
    # 读取信息文件
    try:
        with open(info_file_path, 'r', encoding='utf-8') as f:
            video_info = json.load(f)
    except Exception as e:
        print(f"错误：读取信息文件失败: {str(e)}")
        return 1
    
    # 生成Markdown文件
    md_file_path = os.path.join(args.output, "output", video_id, f"{video_id}.md")
    md_content = f"# {video_info.get('title', '未命名视频')}\n\n"
    md_content += f"- **视频时长**: {video_info.get('duration', '未知')}\n"
    md_content += f"- **视频ID**: {video_info.get('tiktok_id', video_id)}\n"
    md_content += f"- **原始链接**: {video_info.get('original_url', args.url)}\n\n"
    md_content += "## 视频预览\n\n"
    md_content += f"<video width=\"800\" controls>\n"
    md_content += f"  <source src=\"{video_id}.mp4\" type=\"video/mp4\">\n"
    md_content += "  您的浏览器不支持视频播放。\n"
    md_content += "</video>"
    
    try:
        with open(md_file_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"Markdown文件已生成: {md_file_path}")
    except Exception as e:
        print(f"错误：生成Markdown文件失败: {str(e)}")
        return 1
    
    # 移动文件到指定输出目录
    print("正在整理文件...")
    source_dir = os.path.join(args.output, "output", video_id)
    target_dir = os.path.join(args.output, video_id)
    
    # 创建目标目录
    os.makedirs(target_dir, exist_ok=True)
    
    # 移动文件
    files_to_move = [
        f"{video_id}.mp4",
        f"{video_id}_info.json",
        f"{video_id}.md"
    ]
    
    for file_name in files_to_move:
        source_path = os.path.join(source_dir, file_name)
        target_path = os.path.join(target_dir, file_name)
        if os.path.exists(source_path):
            os.replace(source_path, target_path)
            print(f"已移动: {file_name} -> {target_path}")
        else:
            print(f"警告：文件不存在: {source_path}")
    
    # 删除output目录
    import shutil
    output_dir = os.path.join(args.output, "output")
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
        print(f"已删除: {output_dir}")
    
    print("视频收藏成功！")
    return 0

if __name__ == "__main__":
    sys.exit(main())