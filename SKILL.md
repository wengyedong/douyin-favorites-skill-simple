# 抖音视频收藏工具 - 智能体技能配置

本文件用于配置常用智能体（如 Claude Code、OpenClaw 等）的技能，方便智能体快速了解和使用本工具。

## 工具信息

- **名称**：抖音视频收藏工具
- **版本**：1.0.0
- **用途**：下载和收藏抖音视频，生成包含视频信息和本地视频预览的 Markdown 文件
- **运行环境**：Python 3.6+

## 核心功能

1. **视频下载**：支持抖音短链接和长链接
2. **信息提取**：自动提取视频标题、时长、ID 等信息
3. **Markdown 生成**：生成包含视频信息和本地视频预览的 Markdown 文件
4. **目录管理**：自动创建输出目录结构

## 使用方法

### 基本命令

```bash
python douyin_favorites.py --url 抖音视频链接
```

### 参数说明

- `--url`：抖音视频链接（必填）
- `--output`：输出目录（可选，默认为当前目录）

### 示例

```bash
# 下载视频并收藏
python douyin_favorites.py --url https://www.douyin.com/video/7618556354252393734

# 指定输出目录
python douyin_favorites.py --url https://v.douyin.com/abc123 --output D:\Downloads
```

## 输出结构

```
<输出目录>/
  <视频ID>/
    <视频ID>.mp4          # 视频文件
    <视频ID>_info.json    # 视频信息
    <视频ID>.md           # Markdown 文件
```

## 依赖

- requests
- beautifulsoup4
- tqdm

## 安装依赖

```bash
pip install -r douyin-downloader/requirements.txt
```

## 故障排除

- **链接无效**：确保输入有效的抖音视频链接
- **下载失败**：可能是网络问题或反爬机制，尝试重试
- **信息文件不存在**：检查下载过程是否成功
- **Markdown 生成失败**：检查文件权限和目录结构

## 注意事项

- 本工具使用第三方 API 下载视频
- 请遵守相关法律法规
- 仅用于个人学习和研究目的