---
name: video-craft-playbook
description: "做视频和设计视听方案时先读：用代码绘制成片（动效、讲解、产品宣传、故事短片、MV、手绘动画），以及实拍和 AI 视频的电影化设计（分镜、镜头语言、运镜、布光、场面调度、曝光色彩、剪辑声音、shot list、AI 视频提示词）。含简报、剧本分镜、风格库、审片到渲染的完整流程，评审现有素材的方法，模板与实测脚本。不用于单纯的电影资讯、器材行情，或不涉及视听的文案。"
---

# 视频创作手册

把叙事意图落实成观众能看见、听见的变化，再把变化落实成能画、能拍、能生成、能剪的指令。

这本手册合并了两部分：

- **电影视听设计**（`references/film/`）：节拍、调度、构图、运镜、布光、曝光色彩、剪辑声音，适用于任何媒介。
- **代码绘制视频**（`references/code-drawn-workflow.md`）：Claude 不生成像素，而是写代码把每一帧画出来。场景代码 → 无头浏览器逐帧截图 → ffmpeg 编码，附 109 种风格、开源项目资产、质检脚本和两部完整样片。

默认用中文工作，术语第一次出现时附英文。建议写成"目的 → 选择 → 执行 → 检查 → 资源不够时的替代"。

## 1. 先判断任务和媒介

**任务**有五种，交付的分量不同（第 6 节）：讲一个技巧、设计一个镜头、出整片方案、评审现有素材、做出成片。

**媒介**决定第 5 节走哪条分支：

| 媒介 | 什么时候 | 画面从哪来 |
|---|---|---|
| 代码绘制 | 要 Claude 直接交付 MP4：动态图形、讲解、产品片、卡通、像素、3D、MV | Claude 写的代码逐帧渲染 |
| 实拍 | 用户自己拿机器去拍 | 相机；Claude 给镜头表、灯位、走位、收音、拍摄顺序 |
| AI 视频 | 用户用视频模型生成 | 模型；Claude 给参考资产、逐镜提示词、接片方案 |
| 混合 | 以上任意组合 | 按镜头注明来源 |

没指定媒介时：要成片就走代码绘制；只要方案就先给共享设计（第 3、4 节），执行层给实拍和 AI 两种简短转换。不擅自认定用户用某款相机或模型。

按需读取，不要一次全读：

| 当前问题 | 读这里 |
|---|---|
| 故事怎么拍、人物怎么站、镜头怎么衔接 | `references/film/story-blocking-coverage.md` |
| 景别、构图、焦距、机位、景深 | `references/film/camera-and-composition.md` |
| 推拉摇移跟升降、手持、长镜头 | `references/film/camera-movement.md` |
| 打光、质感、日夜内外景、低预算 | `references/film/lighting-design.md` |
| 帧率、快门、频闪、曝光、Log、色彩 | `references/film/exposure-color.md` |
| 剪辑点、收音、现场排序、素材交接 | `references/film/editing-sound-production.md` |
| 按类型快速出方案（实拍与 AI） | `references/film/scene-recipes.md` |
| AI 分镜、图生视频、视频提示词 | `references/film/ai-video.md` |
| 画面不对、评审方案或成片 | `references/film/quality-control.md` |
| 核实依据、区分规则与经验 | `references/film/source-map.md` 及各模块文末 |
| 用代码做成片的全部细则 | `references/code-drawn-workflow.md` |
| 选风格、照某种风格做、开源项目的现成资产 | 第 9 节资产地图 |

## 2. 简报：一次问完

已知的不问，只问会改变成片或可行性的缺口，通常不超过三个；其余写成"暂按……设计"并继续。

- 观众看完要理解或感受到的**一件事**；受众；发布位置
- 时长、画幅（16:9 / 9:16 / 1:1）、分辨率、语言
- 媒介；实拍时的地点时段、演员道具、现有设备、人员与时间
- 必须精确的内容：产品名、数字、功能说法、Logo、文案。不编造，缺的标"待确认"
- 素材与权利：每项素材的来源和许可
- 音乐与旁白：音乐来源由用户定；要旁白时给 2–3 个候选音色的短样，听过再选
- 风格：指定一种，或给参考片

首条消息已经说清内容、时长、画幅和交付物时直接开工。用户只问一个技巧时给一个清楚的例子和一个常见误区，不强制出整套文件。

## 3. 共享设计链

不论哪种媒介，都按这条链想清楚再动手。

**A. 把故事变成可看见的节拍。** 一句话写清"谁想做什么、受什么阻碍、结束时关系或认知变了什么"。拆成能观察到的动作、反应、发现、决定；标出观众此刻知道什么、人物知道什么。每个节拍指定主要观看对象和声音线索。删掉只重复已有信息的镜头。用户要求保留台词、情节或时序时照做，提出改动要标明，不暗改。剧本写法（发散再收敛、一个转折、旁白只说画面说不了的、朗读计时后删三成、禁用套话）见 `references/code-drawn-workflow.md` 第 4 节。

**B. 先建立空间和调度。** 用文字或平面图说明入口、窗、关键道具、人物和主光源的相对位置。给角色和道具稳定编号，定动作轴线、机位所在侧、进出方向、视线目标、道具状态。区分场景左右、人物自己的左右、画面左右。有意越轴或跳切时写清意图。代码绘制同样需要：同一个世界里，跨镜方向、光源方位、道具状态要一致。

**C. 定 3–5 条视觉规则，写成数字。** 例："人物不知情时机位静止，发现线索时只推近一次""主光始终来自窗侧"。把"高级、电影感、压抑"翻译成构图、距离、明暗、色彩、动作、声音和节奏，不堆形容词或导演名。代码绘制要再写一张风格规格卡（色板十六进制、字体字号、缓动曲线、交错帧数、质感参数、禁用清单），见 `references/code-drawn-workflow.md` 第 3 节。

**D. 设计每个镜头。** 重要镜头回答八个问题，过渡镜头可以简写：

1. 叙事任务：观众先注意什么，镜头结束时多知道什么
2. 画面：景别、机位高度与角度、前中后景、观看距离；给焦距时注明画幅或等效视角，未知不强填
3. 调度：人物、视线、手和道具从什么状态到什么状态
4. 运动：静止还是哪种运动，触发点、路径、起止构图、速度变化（写成数字）、停机点，以及为什么值得动
5. 焦点：对谁、何时转移；拉焦和推近是两回事
6. 光线：动机方向、光源大小、明暗分离、背景层次
7. 声音与剪辑：台词、环境声、动作声，切入切出的动作或声音点
8. 资源与替代：要什么人、空间或器材；做不到时保留叙事作用的低成本方案

**E. 时间替观众着想。** 每镜按顺序列出读点（观众必须看懂的事），每个读点要"找到、理解、停留"三段时间。一次只读一件事，先事件后反应。镜长由读点数量决定，镜长不要整齐划一。全片 2–4 个重点时刻，停留等于阅读时间加 1.5 秒。具体数字见 `references/code-drawn-workflow.md` 第 5 节。

**F. 声音从一开始就在。** 每个场景有环境底噪，每个物理动作有对应的声音。旁白停时画面接力，画面停时声音接力。

## 4. 分镜

整片方案和成片都先写分镜，再拍、生成或写代码。分镜开头是导演卡：梗概与转折、2–4 个重点时刻、色板与光线变化、形式、镜头与运动、节奏、转场、字体、声音、结尾，每行有数字和来自这个故事的理由。

镜头表每镜一行，用稳定编号；镜头、灯位、提示词、素材和修改意见都复用这个编号：

| # | 时间 | 画面 | 事件 → 反应 | 读点及时间 | 景别/机位 | 运动/焦点 | 光/灯位组 | 声音/切点 | 出镜转场 |
|---|---|---|---|---|---|---|---|---|---|

实拍可以不要"读点"列，代码绘制可以不要"灯位组"列。分镜规则（每镜首尾有变化、第一帧就在动、首尾呼应、拍点对齐、镜头数 = 时长 ÷ 平均镜长）见 `references/code-drawn-workflow.md` 第 4 节；拍摄方案的完整结构见 `assets/production-plan-template.md`。

## 5. 按媒介执行

### 代码绘制

照 `references/code-drawn-workflow.md` 做，它是这条路线的完整细则。五道关卡不跳：

| 关 | 产出 | 过关标准 |
|---|---|---|
| 1 简报 | 确认过的 brief | 第 2 节各项都有答案 |
| 2 剧本与分镜 | `STORYBOARD.md`，开头是导演卡 | 一个转折；每镜有事件；读点有时间；每个接缝有决定 |
| 3 关键帧 | 2–4 张全尺寸静帧 | 风格被认可；最满的时刻不溢出；这一帧不能原样搬进别的片子 |
| 4 草稿 | 半尺寸、全细节、带声音的整片 | 自动质检通过；陌生观众审片的问题已处理 |
| 5 成片 | 全尺寸 MP4、源码、交付报告 | 接触表过检查清单；响度 −14 LUFS、真峰值 ≤ −1 dBTP |

- 用户在场：第 1 到 4 关各停一次，先给对方看再问。60 秒以内、场景少的片子，简报和导演卡一条消息给完，两张静帧后直接出草稿。
- 画面是时间的纯函数 `renderAt(t)`；随机用种子 `hash(i)`；每镜重绘整帧。渲染脚本 `scripts/render.cjs`，场景模板 `scripts/scene.html`。
- 长任务在项目目录放 `STATE.md`：现在在哪一关、已定的选择、没解决的意见、下一步。

### 实拍

交付镜头表、机位与灯位、走位、收音、拍摄排序和关键测试。

- 布光：先看现场原有光，按灯位组而不是每镜重置；灯位写成"位置/高度/朝向、软硬、控制附件、作用、曝光关系"。光比要说明测量口径。见 `references/film/lighting-design.md`。
- 曝光色彩：给色温、光圈、ISO/EI、快门、IRE 或 LUT 建议时注明适用条件和要测试的项，不把某台机器的经验套到所有设备。见 `references/film/exposure-color.md`。
- 能拍、能接、能听清：把剪辑顺序和拍摄顺序分开，按场地、灯位、演员、自然光窗口组织拍摄，标必拍和可选。核算台词实际朗读时间和动作完成时间。按镜头核对可用人手，全员出镜时不能默认有人推机器、举反光板。车辆、吊装、带电、火焰、特技交给合格人员，并给可替代的镜头拆分。见 `references/film/editing-sound-production.md`。

### AI 视频

先固定角色、场景、光源和道具状态，再逐镜给可视化的动作。读 `references/film/ai-video.md`，指定模型的当前能力要查官方资料。创作检查项和模型输入分开写。不能称作"纯代码绘制"。

### 混合

先定实拍素材、生成素材、代码画面之间的接点，统一机位逻辑、画幅、方向、色彩和声音空间，给后期留对齐余量。代码覆画已有视频时，先 ffprobe 探测、列出必须不变的要素、做 10 秒样片验证同步。

只在用户要求出图、出视频或处理素材时才调用相应工具；文字方案不代表已经渲染、生成或看过素材。

## 6. 按请求大小交付

- **技巧解释**：作用与适用条件 → 可执行的例子 → 失败表现 → 替代和观察方法。
- **单镜头设计**：一张镜头卡加一句设计理由。要比较时最多给三个有实际差异的选项。
- **整片方案**：已知条件与假设 → 节拍和视觉规则 → 空间与连续性约束 → 镜头表 → 关键镜头执行卡与灯位表 → 拍摄排序、资源、低预算替代、要测试的项（AI 任务换成生成顺序、参考资产、逐镜提示词、接片方案）→ 时长核算。长方案细项放文件，聊天里先说关键决定。
- **素材评审**：先说明实际看到的是完整视频、采样帧、单张图还是文字描述。按"观察到 / 推测原因 / 最小修复 / 如何验证"组织。不能从一帧断言运镜速度、剪辑节奏或唯一真实灯位。
- **成片**：MP4、源码、分镜、风格规格卡、素材与音频的来源和许可、哪些是代码画的哪些不是、未核实的事实、两个最弱的时刻及改法。

## 7. 质量检查

至少检查：叙事信息是否清楚，镜头运动是否有作用，空间与光线是否连续，时长是否够用，声音是否可用，资源是否可行。先修最影响理解和可剪辑性的一个问题，再复核相关镜头。

- **镜头计划核算**（任何媒介）：复制 `assets/shot-plan-template.json` 改写，运行 `python3 "$SKILL_DIR/scripts/check_shot_plan.py" /absolute/path/shot-plan.json`（`--json` 出结构化结果；有硬错误退出码 1，格式错误 2，只有提醒 0）。它只核算数据和时长，不判断好不好看。一次简短解释不必做 JSON。
- **成片自动质检**（代码绘制和任何 MP4）：`python3 vendor/cinecode/scripts/qc.py <命令> <视频>`，命令有 hook、freeze、pops、action、sceneloud、loud、strip、sheet；黑帧、冻结、响度的 ffmpeg 命令见 `references/code-drawn-workflow.md` 附 C。
- **审片**：每镜做完就看接触表、条带、裁切，对照 `references/code-drawn-workflow.md` 第 9 节的清单。草稿后起一个没参与制作的子 agent，只给接触表和测量数字，让它写最大的三个问题。
- **失败诊断**：读 `references/film/quality-control.md`。
- Claude 能测量声音但听不到。每次交付请用户用耳机和手机扬声器各听一遍，列出要重点听的秒数。

## 8. 事实、许可与边界

- 把物理关系、行业惯例、某位创作者的选择、模型文档和本手册的原创建议分开说。三分法、180 度轴线、三点布光、180 度快门、浅景深都是有条件的工具，不是"电影感"的必要条件。
- 技术结论附一手来源链接；创作选择讲清理由即可，不虚构出处。新机型、固件、平台规格、AI 模型参数和价格要查当时的官方资料。
- 不声称读完没拿到全文的书、看过没能播放的视频、做过没执行的测试。
- 只复用有明确许可的代码和素材。没有 LICENSE 的仓库（如 PDoomVideo）只学思路。`vendor/` 各目录的许可见 `THIRD_PARTY.md`；lemo-opuscar 的文档是 CC BY-NC 4.0，商业产品或服务里使用要向作者申请。
- 不编造功能、数据、评价；不把混合流程说成纯代码一次生成；示意动画不冒充经过验证的模拟。
- 研究参考片只学画面手法，故事、角色、配音必须是自己的。不主动提议付费生成器，不擅自安装、付费或下载大文件。

## 9. 资产地图

开源项目最好的资产原样收在 `vendor/` 里，按需读取。许可和没收入的内容见 `THIRD_PARTY.md`。

| 要做的事 | 读这里 |
|---|---|
| 选风格 | `styles/INDEX.md`：109 种风格，每种有用途、演示片、海报和目录。用户说的风格名先查 `vendor/cinecode/styles/aliases.json` |
| 照一种风格做 | 该风格的 `STYLE.md`（配色、材料、运动、镜头、声音、禁忌）、`DEMO.md`（怎么做出来的），再看 `demo/` 里的可运行代码 |
| 导演方法与工程技巧 | `vendor/lemo-opuscar/DIRECTOR.md`、`TECHNIQUE.md`；共享引擎 `vendor/lemo-opuscar/core/` |
| 剧本 | `vendor/cinecode/references/writing.md`、`writer-prompt.md` |
| 镜头、剪辑、屏幕文字 | `vendor/cinecode/references/camera-moves.md`、`craft.md`、`typography.md`；实拍与 AI 的镜头语言见 `references/film/` |
| 画面内的运动与动效设计 | `vendor/cinecode/references/motion.md`、`motion-design.md`；动效词典 `vendor/awesome-ai-motion/docs/catalog.md`（637 种），按目的选看 `vendor/awesome-ai-motion/references/decision-tables.md` |
| 按场景套模板 | `vendor/awesome-ai-motion/recipes/`（标题开场、知识讲解、数据故事、产品演示等 11 个）；实拍与 AI 的场景范例 `references/film/scene-recipes.md` |
| 声音 | `vendor/cinecode/references/sound.md`；合成音效、音乐与混音代码 `vendor/claude-animated-shorts/templates/audio/`；现场收音 `references/film/editing-sound-production.md` |
| 广告与产品片、电影感短片、MV、改编参考片、剪用户素材 | `vendor/cinecode/references/` 下的 `purpose-ad.md`、`purpose-cinematic.md`、`music-video.md`、`reference-video.md`、`footage-edit.md` |
| 布光与曝光色彩 | `references/film/lighting-design.md`、`exposure-color.md`；代码画面的后期质感、调色、颗粒见 `vendor/cinecode/references/finish.md`、`looks.md` |
| 角色 | `vendor/cinecode/references/characters.md`；竖屏故事短片的角色测量 `vendor/claude-animated-shorts/references/reports/characters.md` |
| 竖屏卡通 3D 故事短片 | `vendor/claude-animated-shorts/`：`SKILL.md`、`references/STYLE_BIBLE.md`、`templates/`（都在该目录下） |
| 手绘卡通（p5.brush） | `vendor/ClaudeAnimationBase/ANIMATION_GUIDE.md` 与引擎；角色要自己设计 |
| 拍摄方案与镜头数据模板 | `assets/production-plan-template.md`、`assets/shot-plan-template.json` |
| 制作简报与提示词模板 | `vendor/awesome-opus-5-5-videos/docs/production-brief.md`、`prompt-playbook.zh-CN.md`；本手册的模板见 `references/code-drawn-workflow.md` 附 A |
| 长会话与修改轮次 | `vendor/cinecode/references/context-protocol.md`；修改意见的处理见 `references/code-drawn-workflow.md` 第 10 节 |
| 看完整的做法 | `examples/red-pen/`（纸面两色印刷、接触表与红笔，30 秒）和 `examples/one-line/`（一笔画、回家的线，30 秒）：源码、声音脚本、分镜、交付报告 |
