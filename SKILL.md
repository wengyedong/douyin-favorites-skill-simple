---
name: douyin-favorites
description: 下载抖音视频，并生成视频信息文件，用于收藏用户提供的抖音视频。
required:
  bins: ["python", "pip"]
---

# 抖音视频收藏技能

当用户提供抖音视频链接（长链或短链）并表达收藏、下载或整理意图时，触发此技能。

## 1. 参数获取与路径决策
- **提取 URL**：从用户输入中精准提取抖音链接。
- **确定输出目录 (`--output-dir`)**：
    1. 优先使用用户在对话中显式指定的路径。
    2. 若用户未指定，使用 OpenClaw 配置中的 `default_output_dir`。
    3. 若以上均无，默认使用 `./favorites`。

## 2. 执行流程
1. **前置告知**：
    - 告知用户正在处理链接。
2. **调用核心脚本**：
    - 执行命令：`python douyin-favorites.py <URL> --output-dir <CONFIRMED_DIR>`。
3. **最终交付**：
    - 脚本运行完成后，定位到输出目录下的 `./<视频ID>/` 目录
    - 读取 `<视频ID>_info.json` 文件，提取视频标题（title）、时常（duration）、视频ID（tiktok_id）、原始链接（original_url）
    - 向用户确认视频已保存，并展示“视频信息 + 保存路径”

## 3. 注意事项
- **处理反馈**：系统在开始收藏前给用户一个“处理中”的反馈。