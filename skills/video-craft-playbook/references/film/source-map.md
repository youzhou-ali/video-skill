# 资料索引与使用边界

资料核读日期：2026-11-16。采纳39条专业来源，分为摄影9条、布光与色彩16条、叙事与制作10条、AI转换4条。每条的准确URL、实际读取章节和适用边界位于对应模块文末。

本包基于实际可访问的公开网页正文及PDF相关章节整理；不声称通读未获取的书籍、完整手册、课程或观看未播放的视频。检索结果、付费墙导语和营销描述不替代技术证据。

## 按问题找资料

| 来源编号 | 机构/作者与资料主题 | 在哪里核对 |
|---|---|---|
| C01 | ASC / Jay Holben：机位与故事、调度 | camera-and-composition.md |
| C02 | Hasselblad：焦距、画幅、透视 | camera-and-composition.md |
| C03 | ZEISS / H. H. Nasse：景深与散景 | camera-and-composition.md |
| C04 | ZEISS：手动对焦与焦点精度 | camera-and-composition.md |
| C05 | ZEISS / Vladan Blahnik：镜头光圈及呼吸相关章节 | camera-and-composition.md |
| C06 | ARRI：电子/机械快门与运动呈现 | camera-movement.md |
| C07 | ASC：运镜工具 | camera-movement.md |
| C08 | ASC：移动摄影与Dolly Grip | camera-movement.md |
| C09 | ASC：采访摄影 | camera-and-composition.md |
| L01 | ARRI / Bill Holshevnikoff：Lighting Handbook理论部分 | lighting-design.md |
| L02 | ASC / Jay Holben：光质、相对大小 | lighting-design.md |
| L03 | ASC / Jay Holben：平方反比及面光源实测边界 | lighting-design.md |
| L04 | Sekonic / Jim Zuckerman：主补光贡献比 | lighting-design.md |
| L05 | Sony / Chris Ross：场景拆解、负补光 | lighting-design.md |
| L06 | ASC / Jon Joffin：有限器材外景布光 | lighting-design.md |
| L07 | Academy：Spectral Similarity Index | exposure-color.md |
| L08 | Sony：Gamma/Color Mode与灰卡基准 | exposure-color.md |
| L09 | Sony：Exposure Index | exposure-color.md |
| L10 | ARRI：LogC False Color规范 | exposure-color.md |
| L11 | ARRI：色彩管理FAQ | exposure-color.md |
| L12 | Sony：电影拍摄基础与频闪 | exposure-color.md |
| L13 | Sony ILCE-7CM2：Anti-flicker Set. | exposure-color.md |
| L14 | ARRI：SkyPanel模式与频率FAQ | exposure-color.md |
| L15 | ACES Documentation：Input Transforms | exposure-color.md |
| L16 | ACES Documentation：Output Transforms | exposure-color.md |
| P01–P02 | Sony Cine / Steven Bernstein：场面调度两篇 | story-blocking-coverage.md |
| P03 | ASC / Michael Goi：导演与视觉叙事访谈段 | story-blocking-coverage.md |
| P04 | Adobe：180度轴线惯例 | story-blocking-coverage.md |
| P05 | BFI / Alex Barrett：《圣女贞德蒙难记》的规则突破 | story-blocking-coverage.md |
| P06 | Academy：剪辑教学资料 | editing-sound-production.md |
| P07 | Adobe：J-cut与L-cut | editing-sound-production.md |
| P08 | Shure / Chris Lyons：影视录音指南相关章节 | editing-sound-production.md |
| P09 | Academy：声音与音乐教学资料 | editing-sound-production.md |
| P10 | Adobe：竖屏构图与重构 | story-blocking-coverage.md |
| A01–A02 | Runway：Gen-4及图生视频提示指南 | ai-video.md |
| A03 | Google DeepMind：Veo 3提示维度 | ai-video.md |
| A04 | Google Cloud：Veo 3.1提示与工作流 | ai-video.md |

## 如何使用证据

- **物理关系**：优先采用可说明条件的公式或技术资料；给适用假设，再推导，不靠权威名号替代校核。
- **设备实现**：绑定机型、固件、记录与监看模式；未知设备不填猜测值。
- **行业惯例**：解释解决什么问题与何时可以偏离；不把惯例写成所有作品必须遵守的规则。
- **创作者案例**：标明作者与场景，只用实际读取内容；不要把个人习惯外推为唯一做法。
- **原创综合**：本包的工作流、案例、模板、优先级和检查器是综合设计；数值例子是起点，不是来源保证或成功率数据。
- **AI策略**：供应商文档反映其特定产品；不同模型的提示策略不同，复杂动作的稳定性以当前实测为准。

## 已处理的证据冲突

1. 光比资料使用不一致口径：明确K:F与(K+F):F后重新计算，不沿用模糊的「3:1」。
2. 平方反比入门解释可能忽略大型面光源和近场：保留点源近似条件，实际效果测试。
3. 旧机型和历史教材有旧产品、旧菜单、旧平台规格：只保留仍成立的基础概念。
4. 曝光经验常把一种Log曲线、肤色或EI行为外推到所有设备：拆开编码、监看和实际曝光。
5. AI指南既有简短迭代也有详细描述策略：按模型和任务适配，不设唯一提示词公式。

## 使用时更新哪些内容

需要精确机型参数、灯具高速模式、相机/软件菜单、当前色彩管理版本、平台发布限制、AI接口或价格时，重新查当前官方资料并标注日期。
新来源与既有条目矛盾时，先比较适用设备、定义和测量条件；保留差异而不是悄悄把旧规则覆盖成新的绝对化规则。
更新本技能须由用户的创建/修改请求授权；不要将每次普通拍摄问答自动变成永久修改或定时任务。
