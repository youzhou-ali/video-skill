# 视频创作手册 · video-craft-playbook

一个以中文为主的视频制作技能，两部分合在一起：

- **电影视听设计**：将故事意图转化为可执行的分镜、摄影、运镜、布光、场面调度、曝光色彩、声音与剪辑方案，同时提供实拍方案向 AI 视频镜头和提示词的转换方法。
- **代码绘制视频**：让 Claude 写代码逐帧绘制成片。流程是简报 → 剧本分镜 → 关键帧 → 半尺寸草稿 → 成片。收入 6 个开源项目的风格库、参考文档和质检脚本，共 109 种风格，附两支 30 秒示例：《红笔》和《回家的线》。

两部分共用同一条设计链（节拍 → 空间调度 → 视觉规则 → 镜头设计 → 时间 → 声音），再按媒介分支：代码绘制、实拍、AI 视频或混合。

**技能名：** `video-craft-playbook`  
**技能入口：** [skills/video-craft-playbook/SKILL.md](skills/video-craft-playbook/SKILL.md)  
**代码绘制细则：** [skills/video-craft-playbook/references/code-drawn-workflow.md](skills/video-craft-playbook/references/code-drawn-workflow.md)  
**风格总目录：** [skills/video-craft-playbook/styles/INDEX.md](skills/video-craft-playbook/styles/INDEX.md)  
**第三方资产与许可：** [skills/video-craft-playbook/THIRD_PARTY.md](skills/video-craft-playbook/THIRD_PARTY.md)  
**资料核读日期：** 2026-11-16

## 能做什么

- 根据剧本、场景或创作目标，拆解叙事节拍，确定观看对象、信息揭示顺序和视觉规则。
- 设计景别、构图、机位、焦距与焦点；为运镜明确动机、路径、起止构图、速度和低预算替代。
- 建立人物走位、动作轴线、视线、进出方向和道具状态，检查镜头之间的空间连续性。
- 设计动机光、主辅光、负补光、反射与遮挡，兼顾整段表演、反打和实际人员配置。
- 分析帧率、快门、频闪、曝光、Log、监看和色彩流程，并标明设备与测量条件。
- 规划剪辑点、声音桥、现场收音、拍摄排序和素材交接。
- 将分镜转换为 AI 视频镜头卡、连续性约束、逐镜提示词和接片方案。
- 根据实际可见的图片或视频证据，提出优先级明确的诊断与最小修复方案。
- 用代码逐帧绘制成片：动态图形、讲解、产品宣传、手绘卡通、像素、3D、竖屏故事短片、MV，交付 MP4、源码、分镜和交付报告。
- 从 109 种风格里选一种照着做，每种有配色、材料、运动、镜头、声音、禁忌和可运行的演示代码。
- 自动质检成片（开场钩子、冻结、突跳、响度等），并用不知情的子 agent 做陌生观众审片。

建议遵循“目的 → 选择 → 执行 → 检查 → 资源不足时的替代”。单个技巧可以简答，完整短片则按需生成镜头表、灯位表和执行方案。

## 导入与使用

本仓库的可安装技能目录是 **[`skills/video-craft-playbook/`](skills/video-craft-playbook/)**。

1. 获取本仓库，例如：

   ```bash
   git clone https://github.com/youzhou-ali/video-skill.git
   cd video-skill
   ```

2. 在支持 `SKILL.md` 的客户端中，导入或安装 `skills/video-craft-playbook/` **整个目录**，保留 `references/`、`assets/`、`scripts/`、`agents/`、`styles/`、`vendor/` 和 `examples/`。Claude Code 可以这样装：

   ```bash
   mkdir -p ~/.claude/skills
   cp -R skills/video-craft-playbook ~/.claude/skills/
   ```
具体入口与安装路径以所用客户端的当前说明为准。
3. 选择“视频创作手册”技能，再描述故事、目标时长、画幅、实拍或 AI、可用器材和人员等条件。支持显式技能语法的客户端可以使用 `$video-craft-playbook`；实际调用方式以客户端为准。

只复制 `SKILL.md` 会丢失参考模块和模板；克隆仓库本身也不会自动完成客户端安装。也可以直接阅读本仓库，把各模块作为拍摄设计参考。

### 使用示例

**低预算实拍**

> 使用 video-craft-playbook。我要拍一段 30 秒、两人对话的悬疑短片。只有一台手机、三脚架、一盏 LED 灯和白色泡沫板，两位演员都要出镜，没有其他工作人员。请给出人物走位、镜头表、灯位、收音、拍摄顺序和关键测试项。

**运镜设计**

> 人物起初相信对方，发现桌上证据后开始怀疑。请设计三种有不同叙事作用的镜头方案，说明起止构图、运动触发点、速度、焦点和空间不足时的替代。

**代码绘制成片**

> 用 video-craft-playbook 做一支 30 秒、16:9 的一笔画风格短片，讲一个人回家的路。先给我看剧本和分镜，再出关键帧和草稿。

**AI 视频转换**

> 把这个故事设计成 45 秒竖屏 AI 短片。先建立角色、场景、道具和光源连续性，再给逐镜镜头卡、可视化动作、提示词和接片条件。模型尚未确定，请标明后续需要核实的能力。

## 内容导航

| 模块 | 内容 |
|---|---|
| [技能主流程](skills/video-craft-playbook/SKILL.md) | 任务与媒介判断、简报、共享设计链、按媒介执行、交付结构、质量检查、资产地图 |
| [代码绘制细则](skills/video-craft-playbook/references/code-drawn-workflow.md) | 五道关卡、风格规格卡、分镜、时间、动画原则、转场、工程铁律、审片、渲染、声音、提示词模板、渲染脚本、质检命令 |
| [风格总目录](skills/video-craft-playbook/styles/INDEX.md) | 109 种风格的用途、演示片、海报和目录 |
| [示例](skills/video-craft-playbook/examples/) | 《红笔》《回家的线》的源码、声音脚本、分镜、交付报告 |
| [叙事、调度与覆盖](skills/video-craft-playbook/references/film/story-blocking-coverage.md) | 节拍、轴线、走位、视线、信息揭示与镜头覆盖 |
| [摄影与构图](skills/video-craft-playbook/references/film/camera-and-composition.md) | 景别、观察距离、焦距、画幅、透视、景深与对焦 |
| [运镜](skills/video-craft-playbook/references/film/camera-movement.md) | 推拉摇移跟升降、手持、长镜头、运动动机与路径 |
| [布光设计](skills/video-craft-playbook/references/film/lighting-design.md) | 光质、光比、负补光、动机光、日夜内外景与低预算执行 |
| [曝光与色彩](skills/video-craft-playbook/references/film/exposure-color.md) | 帧率、快门、频闪、Log、EI、监看与色彩管理 |
| [剪辑、声音与执行](skills/video-craft-playbook/references/film/editing-sound-production.md) | 剪辑点、声音桥、收音、现场排序与素材交接 |
| [场景应用](skills/video-craft-playbook/references/film/scene-recipes.md) | 可调整的实拍与 AI 场景范例 |
| [AI 视频转换](skills/video-craft-playbook/references/film/ai-video.md) | 镜头卡、参考资产、连续性、模型适配与分段迭代 |
| [诊断与检查](skills/video-craft-playbook/references/film/quality-control.md) | 证据、问题优先级、最小修复与验收 |
| [资料索引](skills/video-craft-playbook/references/film/source-map.md) | 39 条专业来源、阅读范围与适用边界 |
| [拍摄方案模板](skills/video-craft-playbook/assets/production-plan-template.md) | 可复用的拍摄交付结构 |
| [镜头数据范例](skills/video-craft-playbook/assets/shot-plan-template.json) | 8 个镜头、48 秒的原创计划范例 |
| [时长检查器](skills/video-craft-playbook/scripts/check_shot_plan.py) | 顺序镜头计划的数据与时长核算 |

## 离线核算镜头时长

检查器仅使用 Python 3 标准库，无需安装第三方依赖。从仓库根目录运行：

```bash
python3 skills/video-craft-playbook/scripts/check_shot_plan.py \
  skills/video-craft-playbook/assets/shot-plan-template.json --json
```

使用自己的计划时，复制并改写 JSON 范例，然后将命令的输入路径换成该文件。

检查器核算顺序镜头时长、两镜转场重叠、素材前后余量与目标总长，并检查镜号重复及无效数值。它只读取 JSON，不修改输入、不联网、不生成视频；不支持三镜同时重叠。素材长度按时间线播放速度解释，音频跨镜不会额外增加画面时长。

核算通过不代表表演、构图、连续性或实际素材可用性已经得到验证。范例中的 `usable_source_s` 为 `null`，因此会提示尚未核实素材长度；这是计划数据，不是已经拍摄或生成的素材。

## 资料与适用边界

电影视听设计部分综合了 **39 条专业来源**：摄影 9 条、布光与色彩 16 条、叙事与制作 10 条、AI 转换 4 条。来源包括 ARRI、ZEISS、ASC、Sony、Academy、BFI、Shure、ACES、Runway 和 Google 等公开资料，具体链接、实际阅读章节和适用边界保留在各模块文末，并由[资料索引](skills/video-craft-playbook/references/film/source-map.md)统一导航。

工作流、案例、模板和检查器是综合设计；示例参数是可调整的起点。机型、固件、软件、平台规格、AI 模型能力和价格应在实际使用时核实当前官方资料。技能不会把三分法、三点布光、180 度轴线或 180 度快门当作所有作品必须遵守的规则。

仓库保留原始来源链接，不包含来源网站的整本手册、课程或影音素材；引用不表示来源机构认可本项目，也不改变原始资料的权利归属。

## 代码绘制的环境与许可

渲染示例需要 Node.js、Playwright（带 Chromium）、ffmpeg；示例的声音需要 Python 的 numpy 和 scipy。

`vendor/` 里的内容保留各自原许可，其中 lemo-opuscar 的文档是 CC BY-NC 4.0（非商业），详见 [THIRD_PARTY.md](skills/video-craft-playbook/THIRD_PARTY.md)。
