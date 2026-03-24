# 抖音视频收藏工具

这是一个命令行工具，用于下载和收藏抖音视频，并生成包含视频信息和本地视频预览的 Markdown 文件。

## 项目结构

```
douyin-favorites-skill-simple/
├── douyin_favorites.py     # 主程序
├── douyin-downloader/      # 抖音下载器子模块
│   ├── douyin_downloader.py  # 下载核心代码
│   └── requirements.txt      # 依赖文件
├── .gitignore              # Git 忽略文件
├── LICENSE                 # 许可证文件
├── README.md               # 说明文档
└── SKILL.md                # 智能体技能配置文件
```

## 功能特性

- 支持抖音短链接和长链接
- 自动下载视频到指定目录
- 生成包含视频信息的 Markdown 文件
- 自动处理目录创建
- 支持视频信息提取和格式化

## 依赖

- Python 3.6+
- requests
- beautifulsoup4
- tqdm

## 安装依赖

```bash
pip install -r douyin-downloader/requirements.txt
```

## 使用方法

### 基本用法

```bash
python douyin_favorites.py --url 抖音视频链接
```

### 指定输出目录

```bash
python douyin_favorites.py --url 抖音视频链接 --output 输出目录
```

### 示例

```bash
# 使用长链接
python douyin_favorites.py --url https://www.douyin.com/video/7618556354252393734

# 使用短链接
python douyin_favorites.py --url https://v.douyin.com/abc123

# 指定输出目录
python douyin_favorites.py --url https://www.douyin.com/video/7618556354252393734 --output D:\Downloads
```

## 输出结构

程序会在指定的输出目录下创建以下结构：

```
output/
  <视频ID>/
    <视频ID>.mp4          # 下载的视频文件
    <视频ID>_info.json    # 视频信息文件
    <视频ID>.md           # 生成的 Markdown 文件
```

## Markdown 文件内容

生成的 Markdown 文件包含以下内容：

- 视频标题
- 视频时长
- 视频ID
- 原始抖音链接
- 本地视频预览（HTML5 视频播放器）

## 子模块说明

本项目使用了 `douyin-downloader` 子模块来处理视频下载功能，该子模块提供了：

- 抖音链接有效性验证
- 短链接解析
- 视频信息提取
- 视频文件下载
- 信息文件生成

## 故障排除

### 常见问题

1. **链接无效**：确保输入的是有效的抖音视频链接
2. **下载失败**：可能是网络问题或抖音反爬机制导致，可尝试再次运行
3. **信息文件不存在**：可能是下载过程中出现错误，检查日志信息
4. **Markdown 文件生成失败**：检查文件权限和目录结构

### 解决方法

- 确保网络连接正常
- 确保 Python 版本 >= 3.6
- 确保所有依赖已正确安装
- 尝试使用不同的抖音视频链接

## 许可证

本项目采用 MIT 许可证，详见 LICENSE 文件。

## 智能体技能配置

本项目包含 `SKILL.md` 文件，用于配置常用智能体（如 Claude Code、OpenClaw 等）的技能，方便智能体快速了解和使用本工具。

### SKILL.md 内容

- 工具基本信息
- 核心功能说明
- 使用方法和示例
- 输出结构
- 依赖和安装方法
- 故障排除
- 注意事项

### 使用建议

将 `SKILL.md` 文件内容复制到智能体的技能配置中，以便智能体能够：
- 了解工具的功能和用途
- 掌握正确的使用方法
- 快速定位和解决常见问题

## 注意事项

- 本工具使用第三方 API 下载视频，可能会受到抖音反爬机制的影响
- 请遵守相关法律法规，不要用于非法用途
- 视频下载速度取决于网络状况
- 本工具仅用于个人学习和研究目的