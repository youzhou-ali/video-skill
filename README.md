# 电影拍摄与视听设计 · Cinematic Filmmaking

一个以中文为主的电影与视频制作技能，将故事意图转化为可执行的分镜、摄影、运镜、布光、场面调度、曝光色彩、声音与剪辑方案，同时提供实拍方案向 AI 视频镜头和提示词的转换方法。

**技能名：** `cinematic-filmmaking`  
**技能入口：** [SKILL.md](skills/cinematic-filmmaking/SKILL.md)  
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

建议遵循“目的 → 选择 → 执行 → 检查 → 资源不足时的替代”。单个技巧可以简答，完整短片则按需生成镜头表、灯位表和执行方案。

## 导入与使用

本仓库的可安装技能目录是 **[`skills/cinematic-filmmaking/`](skills/cinematic-filmmaking/)**。

1. 获取本仓库，例如：

   ```bash
   git clone https://github.com/youzhou-ali/video-skill.git
   cd video-skill
   ```

2. 在支持 `SKILL.md` 的客户端中，导入或安装 `skills/cinematic-filmmaking/` **整个目录**，保留 `references/`、`assets/`、`scripts/` 和 `agents/`。具体入口与安装路径以所用客户端的当前说明为准。
3. 选择“电影拍摄与视听设计”技能，再描述故事、目标时长、画幅、实拍或 AI、可用器材和人员等条件。支持显式技能语法的客户端可以使用 `$cinematic-filmmaking`；实际调用方式以客户端为准。

只复制 `SKILL.md` 会丢失参考模块和模板；克隆仓库本身也不会自动完成客户端安装。也可以直接阅读本仓库，把各模块作为拍摄设计参考。

### 使用示例

**低预算实拍**

> 使用 cinematic-filmmaking。我要拍一段 30 秒、两人对话的悬疑短片。只有一台手机、三脚架、一盏 LED 灯和白色泡沫板，两位演员都要出镜，没有其他工作人员。请给出人物走位、镜头表、灯位、收音、拍摄顺序和关键测试项。

**运镜设计**

> 人物起初相信对方，发现桌上证据后开始怀疑。请设计三种有不同叙事作用的镜头方案，说明起止构图、运动触发点、速度、焦点和空间不足时的替代。

**AI 视频转换**

> 把这个故事设计成 45 秒竖屏 AI 短片。先建立角色、场景、道具和光源连续性，再给逐镜镜头卡、可视化动作、提示词和接片条件。模型尚未确定，请标明后续需要核实的能力。

## 内容导航

| 模块 | 内容 |
|---|---|
| [技能主流程](skills/cinematic-filmmaking/SKILL.md) | 任务判断、按需阅读、设计步骤、交付结构与质量要求 |
| [叙事、调度与覆盖](skills/cinematic-filmmaking/references/story-blocking-coverage.md) | 节拍、轴线、走位、视线、信息揭示与镜头覆盖 |
| [摄影与构图](skills/cinematic-filmmaking/references/camera-and-composition.md) | 景别、观察距离、焦距、画幅、透视、景深与对焦 |
| [运镜](skills/cinematic-filmmaking/references/camera-movement.md) | 推拉摇移跟升降、手持、长镜头、运动动机与路径 |
| [布光设计](skills/cinematic-filmmaking/references/lighting-design.md) | 光质、光比、负补光、动机光、日夜内外景与低预算执行 |
| [曝光与色彩](skills/cinematic-filmmaking/references/exposure-color.md) | 帧率、快门、频闪、Log、EI、监看与色彩管理 |
| [剪辑、声音与执行](skills/cinematic-filmmaking/references/editing-sound-production.md) | 剪辑点、声音桥、收音、现场排序与素材交接 |
| [场景应用](skills/cinematic-filmmaking/references/scene-recipes.md) | 可调整的实拍与 AI 场景范例 |
| [AI 视频转换](skills/cinematic-filmmaking/references/ai-video.md) | 镜头卡、参考资产、连续性、模型适配与分段迭代 |
| [诊断与检查](skills/cinematic-filmmaking/references/quality-control.md) | 证据、问题优先级、最小修复与验收 |
| [资料索引](skills/cinematic-filmmaking/references/source-map.md) | 39 条专业来源、阅读范围与适用边界 |
| [拍摄方案模板](skills/cinematic-filmmaking/assets/production-plan-template.md) | 可复用的拍摄交付结构 |
| [镜头数据范例](skills/cinematic-filmmaking/assets/shot-plan-template.json) | 8 个镜头、48 秒的原创计划范例 |
| [时长检查器](skills/cinematic-filmmaking/scripts/check_shot_plan.py) | 顺序镜头计划的数据与时长核算 |

## 离线核算镜头时长

检查器仅使用 Python 3 标准库，无需安装第三方依赖。从仓库根目录运行：

```bash
python3 skills/cinematic-filmmaking/scripts/check_shot_plan.py \
  skills/cinematic-filmmaking/assets/shot-plan-template.json --json
```

使用自己的计划时，复制并改写 JSON 范例，然后将命令的输入路径换成该文件。

检查器核算顺序镜头时长、两镜转场重叠、素材前后余量与目标总长，并检查镜号重复及无效数值。它只读取 JSON，不修改输入、不联网、不生成视频；不支持三镜同时重叠。素材长度按时间线播放速度解释，音频跨镜不会额外增加画面时长。

核算通过不代表表演、构图、连续性或实际素材可用性已经得到验证。范例中的 `usable_source_s` 为 `null`，因此会提示尚未核实素材长度；这是计划数据，不是已经拍摄或生成的素材。

## 资料与适用边界

本技能综合了 **39 条专业来源**：摄影 9 条、布光与色彩 16 条、叙事与制作 10 条、AI 转换 4 条。来源包括 ARRI、ZEISS、ASC、Sony、Academy、BFI、Shure、ACES、Runway 和 Google 等公开资料，具体链接、实际阅读章节和适用边界保留在各模块文末，并由[资料索引](skills/cinematic-filmmaking/references/source-map.md)统一导航。

工作流、案例、模板和检查器是综合设计；示例参数是可调整的起点。机型、固件、软件、平台规格、AI 模型能力和价格应在实际使用时核实当前官方资料。技能不会把三分法、三点布光、180 度轴线或 180 度快门当作所有作品必须遵守的规则。

仓库保留原始来源链接，不包含来源网站的整本手册、课程或影音素材；引用不表示来源机构认可本项目，也不改变原始资料的权利归属。
