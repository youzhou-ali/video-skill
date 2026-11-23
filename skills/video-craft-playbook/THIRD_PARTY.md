# 第三方资产与许可

本 skill 的 `vendor/` 目录收入了以下开源项目的资产。各目录保留原仓库的 LICENSE 文件。收入时间：2026-11-23，取各仓库 main 分支当日版本。

| 目录 | 来源 | 许可 | 收入了什么 |
|---|---|---|---|
| `vendor/lemo-opuscar/` | [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)，Lemo-Opuscar by Lemomo (LemoLab) | 文档（所有 .md，含每种风格的 STYLE.md、DEMO.md）：**CC BY-NC 4.0**；代码：MIT；海报：CC BY 4.0（部分含 CC BY 2.0/3.0、CC0、公有领域素材，见 REUSE.toml） | 99 种风格的说明、演示片代码、海报（已缩小到 640 宽，属于修改）；共享引擎 core/ 的代码；DIRECTOR.md、TECHNIQUE.md、MY-STYLES.md |
| `vendor/cinecode/` | [sarpstar/cinecode](https://github.com/sarpstar/cinecode) | MIT（其中 51 个风格文档来自 lemo-opuscar 当时的 MIT 版本，见 styles/LICENSE-lemo-opuscar） | SKILL.md、全部参考文档、脚本（qc.py 等）、模板、starter、61 个风格文档与 aliases.json |
| `vendor/claude-animated-shorts/` | [mromidev/claude-animated-shorts](https://github.com/mromidev/claude-animated-shorts) | MIT | SKILL.md、STYLE_BIBLE.md、7 份测量报告、Remotion + three.js 模板、音频与脚本模板 |
| `vendor/ClaudeAnimationBase/` | [JohnHeibel/ClaudeAnimationBase](https://github.com/JohnHeibel/ClaudeAnimationBase) | MIT | ANIMATION_GUIDE.md、引擎 src/core.js 等、render.mjs、studio.html |
| `vendor/awesome-ai-motion/` | [gongnyang/awesome-ai-motion](https://github.com/gongnyang/awesome-ai-motion) | MIT（卡片、配方、片段实现均为原创；引用的概念来源见 ATTRIBUTIONS.md） | 637 张动效卡片（md 与 html 实现）、11 个配方、7 条路线、决策表、总目录 |
| `vendor/awesome-opus-5-5-videos/` | [athemeroy/awesome-opus-5-5-videos](https://github.com/athemeroy/awesome-opus-5-5-videos) | 原创文字与图表 CC BY 4.0 | docs/ 下的制作简报、提示词手册、提示词矩阵、工作流分析等文档 |

## lemo-opuscar 文档的使用边界

- CC BY-NC 4.0：可以非商业地复制、分享、改编，须署名"Lemo-Opuscar by Lemomo (LemoLab)"、附许可链接 https://creativecommons.org/licenses/by-nc/4.0/ 、说明是否修改。
- 作者额外授权：你和参与同一部片子的人，可以阅读、照做、复制、改编这些文档来做自己的片子（包括商业片和客户片），并放进交付给该片的项目文件里。
- 把这些文档用于商业产品或服务、出售它们，需要向作者申请商业许可（lemomo.studio@gmail.com）。
- 用这个库做出来的片子归你，不需要署名；片中用到的第三方素材按其自身条款处理。
- Memphis Diorama 由 EianLu 贡献，Crayon World 3D 由 2nd1st 贡献，署名时一并写上。

## 没有收入的内容

- lemo-opuscar/styles/flow-field/poster.jpg（IBTrACS 数据许可不明确）
- lemo-opuscar/styles/living-screencast/demo/clawd.js（Clawd/第三方界面）
- lemo-opuscar/styles/living-screencast/demo/ui.js（Clawd/第三方界面）
- lemo-opuscar/styles/living-screencast/demo/index.html（Clawd/第三方界面）
- lemo-opuscar/styles/living-screencast/poster.jpg（Clawd）
- claude-animated-shorts/references/frames/、sheets/（作者限定只供风格研究，内容来自别人的短片）
- ClaudeAnimationBase/src/clawd.js、src/sheets.js 与 src/scenes/demo.js（Clawd 角色属于 Anthropic，仓库的 MIT 许可不覆盖）
- awesome-ai-motion 的示例片段 mp4/gif/jpg 与 lib/gsap.min.js（体积；GSAP 另有许可）
- awesome-opus-5-5-videos 的 data/、assets/（内容是别人作品的元数据和截图）
- lemo-opuscar/styles/living-screencast/demo/ 整个目录（演示片以 Clawd 和 Claude 应用界面为主体）
- lemo-opuscar 演示片的音乐、配音、字体、图片、视频、数据和第三方库（目录 music/、voices/、tts/、fonts/、assets/、vendor/ 等），以及 300 KB 以上的单个文件：多为第三方素材或体积过大。演示代码引用到它们时需要自己替换。
- lemo-opuscar 的图片生成提示词（styles/*/demo/prompts/）。
- [JohnHeibel/PDoomVideo](https://github.com/JohnHeibel/PDoomVideo)：没有 LICENSE，只学思路。
- [awesomeclaude.ai 的动态图形风格页](https://awesomeclaude.ai/claude-motion-graphics)：网站内容没有许可，只在项目调研文档里做了归纳和链接。
- guanmo-ai/awesome-ai-motion、yihui-dev/awesome-opus5-5-videos 等案例库里的提示词：版权属于各作者，只留链接。

## 角色与商标

Clawd 及其名称属于 Anthropic，以上任何仓库的许可都不覆盖它。本 skill 没有收入任何绘制 Clawd 的代码或含 Clawd 的图片。
