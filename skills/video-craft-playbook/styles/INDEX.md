# 风格总目录

共 109 种：lemo-opuscar 99 种、cinecode 独有 7 种、claude-animated-shorts 1 种、ClaudeAnimationBase 1 种、本 skill 的《红笔》1 种。

## 怎么用

1. 先按用途或名字找：用户说的风格名（"Vox 那种""像素风""水墨"）先查 `vendor/cinecode/styles/aliases.json`，它把常见叫法映射到最接近的风格。
2. 看海报确认长相，读该风格的 `STYLE.md`：媒介、材料与渲染、配色、字体与字幕、运动、镜头语法、声音、招牌手法、禁忌。
3. 有 `demo/` 的风格是一支能跑的完整演示片源码，先读同目录的 `DEMO.md`（怎么做出来的、踩过的坑），再借它的引擎和写法。演示片的音乐、配音、字体、素材没有收入，运行前要换成自己的。
4. 把选中的风格写成本片的风格规格卡（SKILL.md 第 3 节），只借语法，不照搬演示片的内容。

许可：lemo-opuscar 的 `STYLE.md`、`DEMO.md` 等文档是 CC BY-NC 4.0（非商业；用它们来做自己的片子，包括商业片，作者另有授权），代码 MIT，海报 CC BY 4.0（已缩小到 640 宽）。cinecode 的风格文档是 MIT。详见 `../THIRD_PARTY.md`。

## 仪器实证（8）

### 档案看片台 · Archive Light Table
- 目录：`vendor/lemo-opuscar/styles/archive-lighttable/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/archive-lighttable/poster.jpg`
- 适合：Brand history、Archive stories、Museums
- 演示片《差两秒》：电报说最长飞了 57 秒；放大镜下，莱特兄弟的底片和档案说是 59 秒。
- 要义：Real archive objects (glass negatives, slides, letters, telegrams, clippings, drawings) lie on a cool, backlit light table. A loupe comes down on one of them, and inside the glass the object comes alive: a negative turns positive, a line of type lights up, a number lifts off the page, a photograph opens into depth. Precise catalogue numbers, dates and readings are pinned to the objects. Clean, modern and quiet, with no vintage filter.

### 工程简报板 · Engineering Briefing Board
- 目录：`vendor/lemo-opuscar/styles/briefing-board/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/briefing-board/poster.jpg`
- 适合：Engineering、Option comparisons、Briefings
- 演示片《船说了算》：一条河要架桥，四种桥型在一面简报墙上逐个受检，拍板的是桥下要过的船。
- 要义：One real whiteboard wall, filmed: window light on enamel, ghosts of erased marker, frame and tray. Cut-out photographs of real things land on it with weight; tags, magnets, a ruler and stamps are pinned to it; marker ink draws itself in three colours with fixed meanings. The camera rides the lines from fact to fact and only at the end pulls back to show the whole briefing.

### 雷达扫描纪录片 · Radar Sweep Documentary
- 目录：`vendor/lemo-opuscar/styles/dark-documentary/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/dark-documentary/poster.jpg`
- 适合：History of science and engineering、Archaeology, sites and reconstructions、Astronomy, deep space and survey
- 演示片《狂风里接住登月直播》：1969 年 7 月 21 日帕克斯的风暴里，一面放倒到极限的 64 米天线顶住了风，替全世界接住了登月直播。
- 要义：The world is black until a scan passes. A plane of light sweeps across terrain, machines and rooms; what it has touched lights up, then settles into echoes (contour lines, range rings, wireframe edges) that slowly fade. Facts arrive as instrument readings: thin titles, small monospaced type, gauges and timelines written on by the same scan, placed beside the thing they describe.

### 点云测绘 · LiDAR Survey
- 目录：`vendor/lemo-opuscar/styles/lidar-survey/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/lidar-survey/poster.jpg`
- 适合：Heritage、Environment、Site surveys
- 演示片《林下的田》：激光点云剥掉一片森林的树冠，露出当年农田的石墙：3.4 公里。
- 要义：Real airborne laser points of a real place, floating in the dark as a measured cloud; a scan line or a cutting plane passes through them and the points condense into a solid, raking-lit surface, which is then measured with hairline instruments. One designed camera move carries the whole film: the cloud is something you fly through, not a picture you look at.

### 显微镜下 · Under the Microscope
- 目录：`vendor/lemo-opuscar/styles/microscope/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/microscope/poster.jpg`
- 适合：Biomedicine、Materials science、Skincare science
- 演示片《量出来的蓝》：一镜从肝组织玻片推到单个细胞核，两个圆逐像素数出 2.4 倍的蓝。
- 要义：Real, licence-clean microscopy of a real specimen, seen as it is, and one continuous change of scale that carries the viewer from the glass slide in the hand to a single cell. Focus breathes when the magnification changes, a focal plane sweeps when the camera lands, and every scale bar, field of view and reading comes from the image's own metadata.

### 卫星简报 · Satellite Briefing
- 目录：`vendor/lemo-opuscar/styles/satellite-briefing/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/satellite-briefing/poster.jpg`
- 适合：Climate、News explainers、Geography
- 演示片《地图上还写着海》：卫星照着地图去找咸海，找到的是沙漠；只有筑了坝的那一块回来了。
- 要义：Real satellite imagery of a real place, graded down to an analyst's grey, with thin white measurement lines drawn on the ground: a lock-on reticle, outlines, a range line, one reading. One continuous zoom built from stacked imagery plates carries the viewer from orbit to the ground and back, and time can run inside one locked frame.

### 安检 X 光 · Security X-ray
- 目录：`vendor/lemo-opuscar/styles/security-xray/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/security-xray/poster.jpg`
- 适合：Airport and customs screening、Parcel and cargo inspection、Product internals
- 演示片《安检口的夜班》：机场安检机屏幕上的一个夜班：一个充电宝、一瓶水，还有在 CT 里动了一下腿的六只活蟹。
- 要义：The film is seen through a baggage-screening console: objects are never shown, only their dual-energy X-ray image, where every material has its colour (organic orange, mixed green, metal blue, impenetrable black) and every outline comes from thickness, not from a drawing. The operator exists only as actions on the screen: a box dragged around an object, a zoom, a measurement, a material filter, a verdict.

### 热成像 · Thermal Camera
- 目录：`vendor/lemo-opuscar/styles/thermal-camera/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/thermal-camera/poster.jpg`
- 适合：Building and energy inspection、Wildlife at night、Machines and electrics
- 演示片《冬夜，一栋楼的体温》：雪夜里，一台热像仪绕着一栋老居民楼转：漏风的窗、墙里的暖气管、睡在热车盖上的猫，还有一年后改造完的同一栋楼。
- 要义：The film is seen through a radiometric thermal camera: a low-resolution, slightly noisy picture in an iron palette where brightness means temperature, with the camera's own instruments on screen (colour scale, spot meters, area boxes, isotherm, hot-spot tracker). A scan line or a split turns the ordinary night picture into heat, and every number on screen is read off the temperature image itself.

## 平面排版（8）

### 装饰艺术 · Art Deco
- 目录：`vendor/lemo-opuscar/styles/art-deco/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/art-deco/poster.jpg`
- 适合：Luxury & hospitality、Galas、Invitations
- 演示片《星光饭店的午夜》：1930 年的大饭店，门童赶在午夜前把一封信送上顶楼。
- 要义：Black lacquer, engraved gold line and airbrushed geometry: a 1930s poster that moves. Every composition has a centre axis, transitions open or close along it, and light arrives as bulbs switching on one by one.

### 包豪斯几何 · Bauhaus Shapes
- 目录：`vendor/lemo-opuscar/styles/bauhaus-shapes/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/bauhaus-shapes/poster.jpg`
- 适合：Finance and economics explainers、Mechanisms and principles、Titles and chapter cards
- 演示片《复利是怎么滚起来的》：一个点每十年翻一倍：七十年后是 128，不复利只有 6.02，最后十年抵得上之前的全部。
- 要义：An explainer told only with circles, squares, triangles, arcs and straight lines, set in opaque colour on a light, matte paper. Every shape is a quantity drawn to scale (area is the amount), the shapes are the characters, and type only names them. A thin construction grid lays out each scene before anything lands, and folds away when it is done.

### 扁平尺度漫游 · Scale Zoom Explainer
- 目录：`vendor/lemo-opuscar/styles/flat-space-explainer/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/flat-space-explainer/poster.jpg`
- 适合：Science explainers、Scale and size、Classroom
- 演示片《一路往下缩》：眼睛就是变焦镜头的小探测器，一站站打出点线，带我们从银河一路缩到病毒。
- 要义：Solid flat shapes on a deep night-blue ground, each with one shade step and hard-edged ring "glows", drawn to true scale inside each frame, guided by a small character who is the camera's own lens. A continuous change of scale carries the viewer through orders of magnitude while a scale ribbon in the corner reads the field of view.

### 象形运动图形 · Pictogram Motion
- 目录：`vendor/lemo-opuscar/styles/pictogram-motion/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/pictogram-motion/poster.jpg`
- 适合：Public services and city stories、Brand and event identity films、Explainers told through signs and objects
- 演示片《被落下的伞》：一把被落在公交车上的黄伞，晴天里在失物招领的货架上等了一整天，暴雨回来时和另外 312 把一起撑开：物件、交通、天气和标识，都是卡着节拍的几何象形符号。
- 要义：A beat-locked film built from three things only: a **square-grid "core graphic"** of circles, half-discs and tiny patterned cells whose rows slide past each other; **geometric pictograms** (objects, vehicles, weather, signs, and a disc-headed figure when one is needed) made of round-capped bars, discs and capsules; and **bold bilingual type** that slides up out of masks. Every cut lands on a drum hit.

### 剪影律动 · Silhouette Rhythm
- 目录：`vendor/lemo-opuscar/styles/silhouette-rhythm/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/silhouette-rhythm/poster.jpg`
- 适合：Music videos、Sports and team films、Nature and festival openers
- 演示片《慢半拍》：一群踩着拍子的火烈鸟里，只有一只小火烈鸟总慢半拍；鸟群留在水面上的涟漪，教会了它拍子。
- 要义：Pure black silhouettes against a saturated sunset, changing pose on every beat; on the key beat everything freezes and only the sky keeps moving. The water is the second canvas: reflections, ripples and back-lit droplets.

### 60s 间谍片头 · 60s Spy Title Sequence
- 目录：`vendor/lemo-opuscar/styles/spy-titles/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/spy-titles/poster.jpg`
- 适合：Title sequences、Event openers、Trailers
- 演示片《天鹅绒密码》：虚构 1964 年间谍片的片头：追一把被偷的钥匙，几何碎片最后拼成片名。
- 要义：A cut-paper, four-ink opening title sequence for a film that never existed: silhouettes move through sets built out of the credits themselves, every brass stab is a cut, and a title is assembled from the pieces.

### 瑞士动态排版 · Swiss Motion Graphics
- 目录：`vendor/lemo-opuscar/styles/swiss-motion/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/swiss-motion/poster.jpg`
- 适合：Brand identity、Events、Design education
- 演示片《海报的五条规则》：一张音乐会海报按瑞士设计的五条规则自己排版，第五条是只打破一条。
- 要义：International Typographic Style in motion: a modular grid, one typeface, one signal colour, and movement as exact as a printing press.

### 文字闪切 · Text Flash Cuts
- 目录：`vendor/lemo-opuscar/styles/text-flash-cuts/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/text-flash-cuts/poster.jpg`
- 适合：Suspense & drama trailers、Title sequences、Manifesto films
- 演示片《身后》：一封信、一通电话、一面窗墙、十三级台阶：叫他别回头的她每一话都更近一步，直到她自己猛地回头。
- 要义：Avant-garde TV anime in the manner of the early-2000s "text frame" school: full-screen heavy Mincho title cards cut in for two to nine frames, architecture reduced to symbolic geometry, a red-black-white palette, characters as silhouettes or extreme close-ups, and the signature over-the-shoulder head tilt. Painted characters come from image generation; everything else (cards, buildings, rain, cuts, inversions) is code.

## 胶片录像（5）

### CRT 字符终端 · CRT ASCII Terminal
- 目录：`vendor/lemo-opuscar/styles/ascii-crt/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/ascii-crt/poster.jpg`
- 适合：Developer tools、Sci-fi、Tech brands
- 演示片《静海日志》：月球基地的 AI 沉睡 40 年后被唤醒，用字符画出“家”来回复。
- 要义：Everything on screen is a real character on a monospace grid, lit by the phosphor of an old monochrome CRT.

### 后室录像带 · Liminal Found Footage
- 目录：`vendor/lemo-opuscar/styles/backrooms/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/backrooms/poster.jpg`
- 适合：Horror、Mystery & ARG、Game teasers
- 演示片《夜班入职培训》：新夜班员工拍下入职第一晚：无尽的黄色办公空间，和墙上的员工守则。
- 要义：Camcorder tapes recovered from empty, endless, fluorescent-lit spaces. Rules instead of monsters.

### 双重曝光 · Double Exposure
- 目录：`vendor/lemo-opuscar/styles/double-exposure/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/double-exposure/poster.jpg`
- 适合：Brand and city films、Documentary and series openings、Music video intros
- 演示片《山海》：天黑下来的这一路，从山到海：鹿、狼、鹰、鲑鱼、鲸，每只动物的剪影里装着它的那片天地；最后鲸身体里的港湾落在真的海岸上。
- 要义：A silhouette is a window. A dark animal shape from the first exposure holds a second photograph, the place that animal carries with it, while the world outside the shape is where it is now. Monochrome photographs, warm lamps as the only colour, and a camera that moves the outline and the world inside it at different speeds, so the window and the place slide past each other.

### 胶片直刻 · Scratch Film
- 目录：`vendor/lemo-opuscar/styles/scratch-film/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/scratch-film/poster.jpg`
- 适合：Things that happen in the dark、One mark to a whole system、Small adventures told in light and shadow
- 演示片《夜里往上游》：一条手指长的灯笼鱼摸黑往上游半公里，用自己的光藏起影子；镜头拉远，原来每晚有无数动物和它一起升起。
- 要义：Direct animation: every picture looks scratched through black emulsion with a needle and tinted with transparent dye, redrawn by hand fifteen times a second and projected. Black is the ground; everything bright is a cut. Lines boil from drawing to drawing, light glows through every cut, colour lies in the grooves like dye.

### 1920s 默片 · 1920s Silent Film
- 目录：`vendor/lemo-opuscar/styles/silent-film/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/silent-film/poster.jpg`
- 适合：Comedy、Retro brands、Silent storytelling
- 演示片《逃跑的面包》：面包店学徒追一个滚走的面包，最后掰成两半分给饿肚子的小女孩。
- 要义：An engraved-illustration silent film projected in a picture house: ink line and silver wash, a 4:3 print that flickers and weaves between velvet curtains, intertitles instead of voices, and a cinema pianist who plays every beat.

## 线稿图解（8）

### 流水线图解 · Assembly-Line Diagram
- 目录：`vendor/lemo-opuscar/styles/assembly-line-diagram/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/assembly-line-diagram/poster.jpg`
- 适合：How a process works、Biology and medicine、Supply chains and pipelines
- 演示片《拆解流水线》：把人体剖成一座倒着开的工厂：12:30 的一份三明治被一站一站拆开，六小时后变成追公交车的力气。
- 要义：A process explained as a factory cut open in elevation: a silhouette (a body, a machine, a building, a city) is sliced like a doll's house into rooms on floors, each room a work station with a machine, a numbered plaque and tiny workers; coloured pipes carry the goods between them, and the colour of a pipe is the legend. The camera rides one piece of cargo through the whole line, and every station starts working the moment it arrives.

### 工程蓝图 · Blueprint
- 目录：`vendor/lemo-opuscar/styles/blueprint/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/blueprint/poster.jpg`
- 适合：Engineering、Hardware launches、Tech explainers
- 演示片《专利申请中：接云机》：发明家的蓝图自己画出一台接云机器，修订云线变成了真的雨云。
- 要义：Engineering drawings that come alive on a sheet of cyanotype paper: white technical line work on Prussian blue, drawn in drafting order, with annotations that move.

### 线稿剖面图解 · Line-Art Cutaway
- 目录：`vendor/lemo-opuscar/styles/hardcore-info/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/hardcore-info/poster.jpg`
- 适合：Hardware explainers、Product engineering、Science education
- 演示片《你手机的天线在哪》：一部手机握住底角就掉信号；拆开才发现金属边框就是天线，被切成几段，手一握就把缝连上了。
- 要义：A real-sized object, modelled in 3D and traced live into a black-line technical drawing on warm white paper: it turns, comes apart, is cut open and is flown into, while numbered leaders, dimension lines and section hatching stay attached to its parts. One single accent colour belongs to the one path the film explains (a signal, a current, an airflow).

### 说明书插画 · Instruction Manual Art
- 目录：`vendor/lemo-opuscar/styles/instruction-manual/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/instruction-manual/poster.jpg`
- 适合：Assembly and set-up guides、Safety instructions、Product onboarding
- 演示片《第十步》：两个从没装过家具的新手照说明书装婴儿床，十步排在同一张 45° 说明书上；第十步，说明书里没有。
- 要义：The film is a printed assembly manual: one sheet of off-white paper, black line art in true isometric (45°), flat white parts, faceless people at real proportions, and the manual's own signs (step numbers, parts call-outs, dotted guide lines, flat arrows, magnifier circles, a do/don't box) telling the story. The view never turns; the camera only travels over the page.

### 等距信息图 · Isometric Infographic
- 目录：`vendor/lemo-opuscar/styles/iso-infographic/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/iso-infographic/poster.jpg`
- 适合：Process explainers、Supply chains、Annual reports
- 演示片《从豆到杯》：一杯咖啡从种植园到你手里的旅程。
- 要义：A system diagram comes alive: an isometric diorama of flat three-tone blocks, thin ink labels and Isotype numbers, where things open up to show their insides and the numbers are drawn, not stated.

### 笔式绘图仪 · Pen Plotter
- 目录：`vendor/lemo-opuscar/styles/pen-plotter/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/pen-plotter/poster.jpg`
- 适合：Maps and terrain、Measurements and records、Generative and data drawings
- 演示片《8848.86》：深夜台灯下，一台笔式绘图仪用四支笔按真实高程画出珠穆朗玛峰，最后一笔写下它的高度。
- 要义：A pen plotter on a desk draws the subject one stroke at a time: real pens, real ink on paper, real machine motion. Maps, charts and lettering appear as polylines a gantry lays down, with pen changes at a rack, pen-up travel and pen-down ink, and the camera lives on the desk with the machine.

### 分色机械图解 · Color-Coded Mechanism
- 目录：`vendor/lemo-opuscar/styles/precise-mechanism/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/precise-mechanism/poster.jpg`
- 适合：How machines work、Product and engineering explainers、Science teaching
- 演示片《三套系统走时》：剖开一块不用电的表：三套系统按能量流向逐一染色，抽走擒纵后齿轮疯转，最后放慢到 1/40 等那一声滴答。
- 要义：A real mechanism built in 3D and coloured like an anatomy plate: a pale ground, one flat colour per subsystem, the part being explained in a single accent. The machine runs truthfully (true ratios, true rates, true physics), and the camera cuts it open, explodes it by system and follows the force through it.

### 产品拆解 · Exploded Teardown
- 目录：`vendor/lemo-opuscar/styles/teardown/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/teardown/poster.jpg`
- 适合：Hardware launches、Product pages、Spec explainers
- 演示片《二十一键》：开源键盘的一半在一次环绕中逐层拆开，看到主控再合拢，标上真实尺寸。
- 要义：A real product, built from its own engineering files (CAD, PCB layout, bill of materials), lit like a studio packshot and taken apart in front of the camera: the layers lift on one axis, the camera travels between them, every part is named with the numbers its files contain, and it closes again into one object.

## 立体微缩（8）

### 积木玩具 · Brick Toy
- 目录：`vendor/lemo-opuscar/styles/brick-toy/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/brick-toy/poster.jpg`
- 适合：Toys & kids、Product builds、Space
- 演示片《零件拼出的火箭》：积木宇航员用零件拼出火箭，飞向积木月亮。
- 要义：Stop-motion toy-brick films shot like macro photography on a real desk: a world built from interlocking plastic bricks with round studs, animated a pose at a time.

### 蜡笔立体世界 · Crayon World 3D
- 目录：`vendor/lemo-opuscar/styles/crayon-world/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/crayon-world/poster.jpg`
- 适合：Short stories、Tributes、Journeys
- 演示片《蝴蝶》：第一人称飞过蜡笔画的村子，落在老人花园里的一朵花上；最后换成他的眼睛，和他说的一句话。
- 要义：A whole world built in 3D and redrawn in wax crayon, by a child's hand, twelve times a second, while a camera moves through it: real depth and parallax, a flight or a walk in first person, and every frame still a crayon drawing on the same sheet of paper.

### 玻璃质感产品 · Glass Product Render
- 目录：`vendor/lemo-opuscar/styles/glass-product/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/glass-product/poster.jpg`
- 适合：Product launches、Consumer tech、Beauty
- 演示片《Aura：听见光》：虚构玻璃耳机 Aura 的开箱与特写。
- 要义：Launch-film product rendering in transparent and frosted glass: a dark-field studio, strip-light sweeps, dispersion, caustics, light travelling inside the object, slow exploded views that snap shut on a downbeat.

### 等距小人场景 · Isometric People Scene
- 目录：`vendor/lemo-opuscar/styles/isometric-picture-book/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/isometric-picture-book/poster.jpg`
- 适合：Everyday rules、Queues、Comparisons
- 演示片《七十二个座位》：等距的登机口和机舱里，小人按顺序登机，讲清哪种叫法快将近一半。
- 要义：A calm explainer of an everyday rule, set in one real place drawn in true isometric with flat colour: small faceless people seen from behind do the thing in order, while serif type lands on the ground, character by character, as if painted there. Whatever hides the action (a roof, a wall) is cut away or lifts off like a paper flap. The order of movement is the explanation.

### 低多边形等距 · Low-poly Isometric Island
- 目录：`vendor/lemo-opuscar/styles/lowpoly-island/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/lowpoly-island/poster.jpg`
- 适合：Game trailers、World building、Calm content
- 演示片《长出来的岛》：空海里一格格长出小岛和村庄，每放一块响一个音符，直到星空。
- 要义：A tiny faceted world seen through an orthographic isometric lens: everything is a geometric block, and everything that appears arrives with a bounce and a note.

### 孟菲斯微缩景观 · Memphis Diorama
- 目录：`vendor/lemo-opuscar/styles/memphis-diorama/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/memphis-diorama/poster.jpg`
- 适合：Web heroes、Ambient loops、Seasons
- 演示片《柚子城的四季》：一个河湾一镜过完四季，大树一蹲一弹，就换一季。
- 要义：A place built as a tabletop model: on warm white paper an organic, grainy frame grows open, and inside it a small world in flat Memphis colours, ink outlines, hard purple shadows and tiny patterns, full of small motions under a slow camera. Calm, bright and warm; a place you watch, not a story you follow.

### 纸片立体书 · Paper Pop-up Book
- 目录：`vendor/lemo-opuscar/styles/paper-popup/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/paper-popup/poster.jpg`
- 适合：Children's books、Game trailers、Story films
- 演示片《小精灵冒险记》：立体书在书桌上打开，小精灵 Pip 在纸片世界冒险，最后跳出书外。
- 要义：A pop-up book on a real desk becomes a stage: flat cut-paper actors with white borders perform in front of paper sets that spring up from the page, under real lamp light and a real macro lens.

### 移轴微缩 · Tilt-Shift Miniature
- 目录：`vendor/lemo-opuscar/styles/tilt-shift/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/tilt-shift/poster.jpg`
- 适合：City promos、Real estate、Transport
- 演示片《玩具城早高峰》：玩具城的早高峰，一切都像模型。
- 要义：A real-looking place photographed from high above with a tilted lens and a time-lapse camera, so the whole world reads as a tabletop model.

## 剪辑纪实（8）

### 字幕新闻 · Caption News
- 目录：`vendor/lemo-opuscar/styles/caption-news/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/caption-news/poster.jpg`
- 适合：Social news、Report explainers、Data shorts
- 演示片《蜜蜂账本》：美国一年死掉 130 万箱蜜蜂，总数却涨了 6%：静音也能看懂的新闻。
- 要义：Social-video news that reads with the sound off. Real footage, photos and the source document are the ground; huge captions are the lead actor, slammed in a chunk at a time with one keyword on a yellow block. Hard cuts on a music grid, numbers that roll, a source tag that slides in whenever a figure appears, and the original document highlighted on screen before its number is believed. 16:9, built for a feed.

### 城市交响曲 · City Symphony
- 目录：`vendor/lemo-opuscar/styles/city-symphony/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/city-symphony/poster.jpg`
- 适合：City films、Music montages、Openers
- 演示片《纽约的一天》：纽约的一天：延时光河、踩着十六分音符的网格，1899 年和今天并排。
- 要义：A city film cut like a piece of minimalist music: time-lapse turns traffic, crowds and clouds into rivers of light, the cuts get denser with the score's subdivisions, one thing is slowed almost to a stop, and the film ends on a hard cut to black on a downbeat. No narrator. The music carries it.

### 实时倒计时分屏 · Live Countdown Split-screen
- 目录：`vendor/lemo-opuscar/styles/countdown/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/countdown/poster.jpg`
- 适合：Launches、Countdowns、Live events
- 演示片《自己倒数》：阿尔忒弥斯二号发射的最后一分钟，一秒不剪：格子从 1 开到 9，点火合成 1。
- 要义：An edit style, not a look. Real footage of one event with a known zero (a launch, a verdict, a final whistle, polls closing), shown in real time: screen time equals event time, a clock ticks every second, and the screen splits into more and more cells as the moment nears, every cell showing the same second. At zero the cells merge into one picture and the clock flips.

### 构成主义蒙太奇 · Constructivist Montage
- 目录：`vendor/lemo-opuscar/styles/kino-montage/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/kino-montage/poster.jpg`
- 适合：Industry histories、Milestones、Collective effort
- 演示片《410 天》：帝国大厦的小册子写着建造者，工地实拍和老照片给出答案：每天 2,500 人。
- 要义：Real archive footage, photographs and documents, printed as one ink-and-paper poster with a single red, and cut on a machine beat. Diagonal bands carry the type; windows cut along the axis hold the film; people are scissored out of photographs and stacked into structures; numbers count, documents are marked in red, and two images collide to make a third idea.

### 电视新闻包装 · Broadcast News Package
- 目录：`vendor/lemo-opuscar/styles/news-package/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/news-package/poster.jpg`
- 适合：News round-ups、Bulletins、Market updates
- 演示片《本周 AI 四件事》：一周四条 AI 新闻，一整套电视台包装：串联单、标题条、翻牌价格表、规格卡。
- 要义：A television newsroom's on-air package, built entirely in code: a sting that becomes the channel bug, a rundown of today's stories that opens and closes the bulletin, a lower-third strap that never leaves the bottom of the frame, and full-frame graphics (split-flap price boards, a line breaking a threshold, explainer maps, documents flying out of a city, quote cards, spec cards with proportion bars, stamps) that carry the facts. The style is the **package system plus its cutting rules**, not a drawing style. 16:9, a clean frame: no burned-in subtitles, no news crawl.

### 1920s 新闻影片 · 1920s Newsreel
- 目录：`vendor/lemo-opuscar/styles/newsreel/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/newsreel/poster.jpg`
- 适合：History stories、Fads & eras、Anniversaries
- 演示片《膝盖警报》：1926 年报纸说查尔斯顿会跳坏膝盖，福特工人野餐会上的孩子照跳不误。
- 要义：A sound newsreel of the late 1920s, cut from real archive material: a searchlight-and-globe ident with a brass fanfare, a newspaper that spins into the lens, a fast and cheerful announcer on an optical soundtrack, place-and-date cards, maps, magazine pages and documents, wipes, flips and irises, and a hot band that can stop dead for the punchline.

### 体育战术板 · Sports Telestrator
- 目录：`vendor/lemo-opuscar/styles/telestrator/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/telestrator/poster.jpg`
- 适合：Sports analysis、Match recaps、Coaching
- 演示片《定格》：半场 0–3，费内巴切 12 分钟连进三球：冻住画面、画线、分屏、射门图。
- 要义：The TV football analysis segment: play the clip at full speed, rewind, freeze it, and draw on the broadcast picture — rings under players' feet, marker arrows for the ball, a red patch for the space nobody covered — then play on, switch angles, count the frames, and flatten the pitch into a board. Real match footage is the ground; every line is drawn on top of it and moves with it. A studio show's packaging (sting, corner bug, score bar, a yellow wipe) holds it together. 16:9.

### 视觉调查 · Visual Investigation
- 目录：`vendor/lemo-opuscar/styles/visual-investigation/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/visual-investigation/poster.jpg`
- 适合：Reconstructions、Fact-checks、Incident reports
- 演示片《兴登堡号：四分钟与三十二秒》：新闻片、照片、证词和调查报告排上同一条时间轴，五路来源指向一处。
- 要义：A cold investigation desk: footage, photographs, documents, sound and maps from one real event, laid out on one shared clock so they check each other. The clock lives inside the picture — timestamps on the evidence, a playhead on a data chart, a stopwatch over the decisive seconds; frozen frames are circled and magnified; quotes are highlighted on the page they come from; a plan shows where cameras stood and where they looked; what is known and what is not are kept apart; at the end every piece of evidence is pulled into one map.

## 卡通动画（6）

### 80 年代赛璐璐动画 · 80s Cel Anime
- 目录：`vendor/lemo-opuscar/styles/cel-anime-80s/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/cel-anime-80s/poster.jpg`
- 适合：Music videos、Game trailers、Nostalgia
- 演示片《城市灯火，1987》：快递少女骑车穿过雨后霓虹都市，赶在黎明发射前送到一盘磁带。
- 要义：Hand-painted cel animation from the golden age of Japanese OVAs, re-created in code: flat two-tone cels over airbrushed backgrounds, backlit neon, limited-animation timing, played back as a late-80s videotape on a CRT television.

### 搞笑历史卡通 · Comic History Cartoon
- 目录：`vendor/lemo-opuscar/styles/comic-history/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/comic-history/poster.jpg`
- 适合：Territorial changes in history、Light explainers on geopolitics、Market share and turf-war stories
- 演示片《一块纸》：阿尔萨斯-洛林在 1871 到 1945 年间四次换主人：每次都有人撕下那块纸、贴上新的，住在上面的她一步没挪。
- 要义：Countries are paper puppets joined with brass split pins, standing on a map printed on paper; whoever takes a piece of land cuts a scrap of paper and slaps it onto the map. The whole film is one comic page on a table, a panel per moment, and the camera travels between the panels.

### 黑白漫画分格 · Manga Panels
- 目录：`vendor/lemo-opuscar/styles/manga-panels/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/manga-panels/poster.jpg`
- 适合：Music videos、Product launches、Anime openings
- 演示片《KOMA ONE · 一秒三十格》：街拍摄影师追着一束跑动的光，等到鸽群腾起的那一秒；她的口袋相机把这一秒拆成三十格。
- 要义：A black-and-white Japanese manga page that moves: G-pen ink, screentone dots, one spot colour, panels that open on the beat, sound effects slammed in letter by letter, and a camera that travels across the paper and through the gutters. The panel is the cut.

### 50s 扁平卡通 · Mid-century Cartoon
- 目录：`vendor/lemo-opuscar/styles/midcentury-toon/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/midcentury-toon/poster.jpg`
- 适合：Set-up guides、Help centres、How-to
- 演示片《认识一下 Pip》：用 50 年代教育片的口吻，三步教你装好一台扫地机。
- 要义：1950s flat colour and limited animation for "follow along" films: colour printed a few pixels off its broken ink line, bodies that hold still while hands do the work, abstract colour-block rooms, a calm classroom narrator, and a cool-jazz combo.

### 1930s 橡皮管卡通 · 1930s Rubber Hose Cartoon
- 目录：`vendor/lemo-opuscar/styles/rubber-hose/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/rubber-hose/poster.jpg`
- 适合：Food & drink、Retro ads、Kids
- 演示片《咖啡杯追方糖》：一只咖啡杯满厨房追一块逃跑的方糖。
- 要义：Black-and-white hand-inked cartoons where every object is alive and swings to a hot jazz band.

### 科幻情景喜剧卡通 · Sci-Fi Sitcom Toon
- 目录：`vendor/lemo-opuscar/styles/scifi-toon/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/scifi-toon/poster.jpg`
- 适合：Comedy、Tech brands、Social shorts
- 演示片《跑腿买咖啡》：厌世天才开传送门只想买杯咖啡，却穿过越来越离谱的平行宇宙。
- 要义：Adult-animation sci-fi sitcom: thick boiling outlines, flat colour, a duo whose reactions don't match, a glowing portal, and one palette per world.

## 速写板书（7）

### 黑板粉笔 · Chalkboard
- 目录：`vendor/lemo-opuscar/styles/chalkboard/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/chalkboard/poster.jpg`
- 适合：Word origins、Myth-busting、Lessons
- 演示片《汉字的故事》：粉笔写下网上的说法，再一擦，把「射」写回三千年前。
- 要义：A real classroom blackboard on which chalk writes itself, stroke by stroke in true stroke order, with no hand, no chalk stick and no eraser in sight. One idea is taught the way a teacher does it: write what people think, wipe it with one pass, write what is true in the same place.

### 平板速写讲解 · Tablet Sketch Explainer
- 目录：`vendor/lemo-opuscar/styles/ipad-sketch/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/ipad-sketch/poster.jpg`
- 适合：Food & drink explainers、Craft and how-to、Lifestyle science
- 演示片《一杯咖啡，从一颗果子开始》：杯里的咖啡变成一颗红果子，再一路走回杯子：成熟、晒干、烘焙、磨粉，一张铅笔速写页上一次换一种颜色。
- 要义：The whole frame is a cream drawing canvas on a tablet, seen while someone draws and explains: grainy pencil lines go down first, flat colour blocks come after, shifted off the line and not quite filled, and the canvas itself is pinched, panned and turned between ideas.

### 马克笔白纸速写 · Marker on Paper
- 目录：`vendor/lemo-opuscar/styles/marker-paper/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/marker-paper/poster.jpg`
- 适合：Worked problems、Science explainers、Lessons
- 演示片《你能看多远？》：一支马克笔在白纸上算出海边能看多远，再告诉你：爬高 100 倍，只能多看远 10 倍。
- 要义：A pad of matte white paper and one bullet-tip permanent marker in black, with a red and a blue marker for meaning only: blue is what we know, red is what we want. A problem is drawn, reasoned out and answered one sheet at a time, stroke by stroke, with no hand and no pen in sight. When a sheet is done it is pushed through or peeled away and the next one begins.

### 一笔画 · One-line Drawing
- 本 skill 的完整示例：`examples/one-line/`（《回家的线》，引擎自写，可直接渲染）
- 目录：`vendor/lemo-opuscar/styles/one-line/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/one-line/poster.jpg`
- 适合：Brand stories、Life milestones、Minimal ads
- 演示片《笔不离纸》：一根不离纸的线画完一个人的一生，再把笔交给孩子。
- 要义：A single ink line that never leaves the paper. Everything on screen is that one line being drawn; scenes don't cut, they morph.

### 视觉笔记 · Sketchnote
- 目录：`vendor/lemo-opuscar/styles/sketchnote/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/sketchnote/poster.jpg`
- 适合：Lecture notes、Science explainers、One-page summaries
- 演示片《蜜蜂怎样酿蜜》：一只蜜蜂一辈子只酿 1/12 茶匙蜜；笔跟着一滴黄从花走到罐子，最后整页成了一张海报。
- 要义：One page of visual notes on dot-grid paper, drawn while you watch: a black fineliner writes and draws, a grey marker gives volume and shadow, one yellow marker carries the single thing that matters. Banners, rounded boxes, fat arrows, icons and hand lettering grow stroke by stroke; the camera rides the pen across the page and ends by pulling back until the whole page reads as a poster.

### 火柴人讲解 · Stick-figure Explainer
- 目录：`vendor/lemo-opuscar/styles/stick-explainer/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/stick-explainer/poster.jpg`
- 适合：Science explainers、Networks & social ideas、Data comparisons
- 演示片《隔着几只手》：从你到一个陌生人，一串手拉起来：1967 年用信验证，一圈圈的人算到超过地球，最后围着地球合上。
- 要义：Plain stick people on warm paper, one accent colour, and a logic you can watch: people stand on a "system line", react to each other, and hold hands. A held hand is not two arms touching but one continuous curve from one shoulder to the next, so a crowd can join into a line, a ring or a shape, and a red pulse can run through all of them.

### 白板讲解 · Whiteboard Explainer
- 目录：`vendor/lemo-opuscar/styles/whiteboard/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/whiteboard/poster.jpg`
- 适合：Explainers、Online courses、Science
- 演示片《口袋里的爱因斯坦》：手机怎么知道你在哪：GPS、原子钟，和相对论每天多出的 38 微秒。
- 要义：An explainer drawn live on one glossy dry-erase board: single-line handwriting that is actually *written* stroke by stroke, floating markers with no hand, magnets that can move, an eraser that can rewind, and a camera that travels across the board instead of cutting.

## 发光线条（5）

### 电路板 · Circuit Board
- 目录：`vendor/lemo-opuscar/styles/circuit-board/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/circuit-board/poster.jpg`
- 适合：Energy、Supply chains、Devices
- 演示片《七毫秒》：江河变成电路板上的走线，电流从水坝跑 2,080 公里进手机充电器。
- 要义：The subject is drawn as a printed circuit board seen from straight above: the world is copper under green solder mask, routes are traces, places are pads, words are white silkscreen, and what flows (power, water, signals, goods) is light running along the copper. The camera rides that light and jumps between the scale of a map and the scale of a single component.

### 萤火光点 · Firefly Pointillism
- 目录：`vendor/lemo-opuscar/styles/firefly-pointillism/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/firefly-pointillism/poster.jpg`
- 适合：Picture-book stories、Many becoming one、Night and nature lyric
- 演示片《你亮，我就亮》：萤火虫闪一下就是在发问：女孩得到的回答是一只鹿，暴风雨吹灭了所有的光，她用最后一只问遍了整片黑夜。
- 要义：Thousands of soft, breathing points of light on black make up the people, animals, grass, moon, rain and words. The points are never created or destroyed: they scatter, fly off and gather somewhere else as something new, and that is how this style tells a story. A moving pointillist painting, or a summer night of fireflies.

### 流场风线 · Flow-field Wind Lines
- 目录：`vendor/lemo-opuscar/styles/flow-field/`（演示代码：有）；海报：未收入
- 适合：Storms, monsoons and other weather、Ocean currents and river floods、Any flow measured against a threshold
- 演示片《摩羯过琼州》：几千条从最佳路径算出来的墨色风线，画出超强台风摩羯的一生：在南海睁开风眼，在文昌登陆，在越南散开，一整周最后收成一条线。
- 要义：An invisible field — wind, current, traffic, any flow — made visible as thousands of thin ink streamlines engraved on warm paper, with darker strokes running along them at the local speed. The lines are computed from data or a physical model, never drawn by hand; they bend round coasts, mountains and objects, change colour as the magnitude crosses meaningful thresholds, and the camera travels over the printed world beneath them.

### 霓虹灯管 · Neon Tubes
- 目录：`vendor/lemo-opuscar/styles/neon-tubes/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/neon-tubes/poster.jpg`
- 适合：Shop openings and mascot stories、Nightlife and city-pop music videos、City and festival night idents
- 演示片《夜宵》：一只霓虹猫去街尾招牌上偷金鱼当夜宵，一爪子拍漏了鱼缸，又叼着快灭的鱼冒雨跑回家，放进自家招牌上的冰饮杯。
- 要义：Real neon signs on a rainy night street: bent glass tubes filled with gas on painted boards, striking with a flicker, lighting the wet walls and doubling in every puddle. The figures on the signs are alive: an animal or a mascot made of one bent tube per pose moves from sign to sign by switching, frame by frame, like an animated sign, and the street answers on the beat.

### 示波器数学 · Oscilloscope Math
- 目录：`vendor/lemo-opuscar/styles/oscilloscope-math/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/oscilloscope-math/poster.jpg`
- 适合：Maths and physics lessons、Signals and electronics、Science explainers
- 演示片《吉布斯现象》：方方正正的波，怎么由圆滚出来？一个个圆叠成方波，直到镜头扎进一个角：那里有一个永远消不掉的 9% 尖角。
- 要义：Mathematics drawn by an electron beam on a phosphor screen: thin glowing green lines on near-black, a dotted graticule, monospace readouts and TeX formulas, every number on screen computed from the same values that draw the picture. The screen is a window onto a mathematical world larger than the frame, and the camera moves through it: it follows a point, dives into a corner, pulls back over a whole wave. Zooming is turning the instrument's knobs: the graticule refines and the TIME/DIV and V/DIV readouts change with the zoom.

## 绘画插画（5）

### 彩铅科普插画 · Colored-Pencil Science Illustration
- 目录：`vendor/lemo-opuscar/styles/colored-pencil/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/colored-pencil/poster.jpg`
- 适合：Natural-science cutaways、Picture-book explainers、Hidden structures and processes
- 演示片《树的另一半》：树会互相喂食吗？一张彩铅画沉到草地下面，跟着一粒糖沿菌丝走到下一棵树，再拉开看整片森林在地下连在一起。
- 要义：A real 3D cutaway world (ground, soil horizons, stones, buried structures, living things) redrawn every frame as a colored-pencil plate on toothed paper: four layers of pencil, a wobbling graphite contour, labels pencilled on cream paper tags. The camera can sink below the ground, and the drawing can be *drawn in* while you watch: horizons coloured in stroke by stroke, growing things drawn out from their base, fine lines spreading white over dark soil.

### 蜡笔儿童绘本 · Crayon Picture Book
- 目录：`vendor/lemo-opuscar/styles/crayon-book/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/crayon-book/poster.jpg`
- 适合：Picture books、Bedtime stories、Kids' learning
- 演示片《月亮睡不着》：月亮失眠了，小女孩爬上屋顶给它唱摇篮曲。
- 要义：A picture-book page drawn live in wax crayon on toothy paper, with a watercolour wash that reveals what the crayon was hiding.

### 油画厚涂 · Impasto Oil Painting
- 目录：`vendor/lemo-opuscar/styles/impasto/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/impasto/poster.jpg`
- 适合：Music videos、Art & culture、Emotional ads
- 演示片《雨的颜色》：灰色雨中广场，第一把红伞撑开，圆舞曲把整个广场刷上颜色。
- 要义：Thick oil paint laid with a palette knife: big, flat, sharp-edged planes of colour, raked by light so every ridge of paint shows. Clarity first: value structure before texture, hard edges at the focus, calm planes everywhere else.

### 钢笔淡彩 · Urban Sketch · Pen & Wash
- 目录：`vendor/lemo-opuscar/styles/urban-sketch/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/urban-sketch/poster.jpg`
- 适合：City & travel、Architecture、Lifestyle brands
- 演示片《风去了哪里》：公园只是一张钢笔速写，风把草帽吹到哪里，哪里才有颜色。
- 要义：A sketchbook page drawn on location: fine sepia fineliner lines that wobble, overshoot and never quite close, with loose transparent watercolour dropped on top. The colour sits slightly off the lines, spills over them, and dissolves into cream cold-press paper at the page edge.

### 水彩笔刷 · Watercolor Brush
- 目录：`vendor/lemo-opuscar/styles/watercolor/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/watercolor/poster.jpg`
- 适合：Nature documentary、Travel、Science explainers
- 演示片《跟着雨走》：跟着降雨从澳洲红色腹地一路画到绿色海岸，一镜到底。
- 要义：A hand-painted journal page that paints itself: translucent brush strokes with dry-brush flying white on warm cotton paper, hand-written notes beside what is painted, nothing drawn with a vector line.

## 屏幕界面（6）

### 暗色科技发布 · Dark Tech Keynote
- 目录：`vendor/lemo-opuscar/styles/dark-keynote/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/dark-keynote/poster.jpg`
- 适合：Product launches、SaaS、Keynotes
- 演示片《思考的空间》：虚构 app Tidy 的发布片：被埋掉的光标一键把几百个窗口归位。
- 要义：A software launch film where the interface itself is the star: near-black gradient, hairline grid, soft light, one brand accent, and UI that moves with snap-grid precision. Light reveals, one giant number, and a sound design that is as ordered as the pixels.

### 桌面卡片穿梭 · Tabletop App Flythrough
- 目录：`vendor/lemo-opuscar/styles/desktop-flythrough/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/desktop-flythrough/poster.jpg`
- 适合：App explainers、Workflows、Products
- 演示片《叮之前》：一张猫照片跳过桌上的应用卡片，从一台手机飞到朋友手机里，一镜跟到底。
- 要义：App screens and tools lie on a sunlit desk as printed paper cards; small pixel characters, popped up into voxel toys, carry the work from card to card, while one unbroken camera flies after them, whips between stops and finally pulls back over the whole desk.

### 科幻全息界面 · Sci-fi Hologram HUD
- 目录：`vendor/lemo-opuscar/styles/hologram-hud/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/hologram-hud/poster.jpg`
- 适合：Spec walkthroughs、Launch videos、Trade shows
- 演示片《Volt 规格扫描》：电助力车被扫描成全息线框，目标框依次锁定电池、电机、刹车。
- 要义：An object is scanned into a glowing wireframe. Target boxes lock onto its parts; each opens in a local exploded view, a leader pulls out, and its number rolls from garbage glyphs into the real value. It may light up, once, into a solid hologram.

### 像素小人录屏 · Mascot Screencast
- 目录：`vendor/lemo-opuscar/styles/living-screencast/`（演示代码：无）；海报：未收入
- 适合：Product tutorials、Feature launches、Onboarding
- 演示片《Clawd 搬进来了》：像素小人 Clawd 搬进 Claude 应用，一镜到底演示 Plan 模式和自检。
- 要义：A product walkthrough that looks like a real screen recording, where a low-resolution mascot lives inside a high-resolution interface and acts out what the software is doing.

### 1-bit 点阵 · 1-bit Dither
- 目录：`vendor/lemo-opuscar/styles/one-bit-dither/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/one-bit-dither/poster.jpg`
- 适合：History told through a chain of media、Printing, scanning and signals、Night scenes and space
- 演示片《月亮的传真》：1966 年 2 月，月面的第一张近照被英国一座射电望远镜当成报社传真收下，一行一行印出来：早了一天，比例却拉高了。
- 要义：A real 3D world shown with exactly two inks: every grey becomes a pattern of dots that is fixed to the surfaces, outlines come from depth and normal breaks, and printed things (fax prints, newspapers, labels) carry their own physical dots. The camera moves freely through it; the pattern never swims.

### 表格动画 · Spreadsheet Film
- 目录：`vendor/lemo-opuscar/styles/spreadsheet/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/spreadsheet/poster.jpg`
- 适合：Data literacy、Finance & costs、Analytics explainers
- 演示片《藏起来的那一列》：总数说 B 更好；把藏起来的结石大小列打开，A 在每一组都赢。一张表讲清辛普森悖论，一格就是一位病人。
- 要义：A whole film inside one spreadsheet window. Cells are the pixels, conditional formatting paints the pictures, the formula bar speaks the lines, and the camera is the sheet's own zoom and scroll. Every picture is made of numbers, and the picture turns out to be the answer.

## 数据地图（6）

### 数据实物化 · Data Physicalization
- 目录：`vendor/lemo-opuscar/styles/data-physical/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/data-physical/poster.jpg`
- 适合：Annual reports、Investor decks、Energy data
- 演示片《两条螺旋》：十二年风电和太阳能装机叠成实物，绕表盘升成两条螺旋，2021 年太阳能反超。
- 要义：Real statistics built as real objects: every unit is a countable piece of material (a plate, a block, a coin, a bar) stacked to exact scale on a crafted base, shot like a product in a studio — soft key, long shadows, shallow depth of field, physically based materials. The camera reads a number at the edge of one plate, follows the data as it grows, and pulls back until the chart is an installation.

### 数据叙事 · Data Storytelling
- 目录：`vendor/lemo-opuscar/styles/dataviz/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/dataviz/poster.jpg`
- 适合：Data journalism、Reports、Climate & science
- 演示片《一百个夏天》：一百年的夏季气温，图表本身就是故事。
- 要义：A chart that tells a story: real data, drawn mark by mark on cream paper by a red–blue pencil, with handwritten notes pinned to the numbers. The chart itself is the camera, the rhythm and the plot.

### 立体地图解说 · 3D Map Explainer
- 目录：`vendor/lemo-opuscar/styles/map-explainer/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/map-explainer/poster.jpg`
- 适合：News and geopolitics、Energy, trade and shipping、Rivers, borders and terrain
- 演示片《霍尔木兹海峡》：从地球一路落进这道海峡：世界约五分之一的石油挤过两条航道，剖开看水下有多深，再看绕行的管道只能分走多少。
- 要义：Real elevation and real imagery built into a three-dimensional map with the vertical exaggerated, lit by one warm, low sun; a sea coloured by its real depth; and over it a layer of data that glows, flows and lights up along true geography: routes, lanes, measurements, pillars. One camera falls from space into the place, flies over it, cuts it open, and climbs back out.

### 小人模拟实验 · Blob Simulation
- 目录：`vendor/lemo-opuscar/styles/pip-simulation/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/pip-simulation/poster.jpg`
- 适合：Evolution and natural selection、Game theory and agent-based models、Epidemics, queues and markets
- 演示片《跑得快，就更好吗？》：160 只植绒小人抢豆子：快的先抢到也先跑不动，跑完 20 代，整块台面都变蓝了。
- 要义：A crowd of small flocked characters, the Pips, runs a real simulation on a warm paper lab board: evolution, games, epidemics, queues, markets. The rules are written in code, the outcome is computed, and the result is shown with the Pips themselves: they are the data points, and at the end they line up into the chart.

### 地铁线路图 · Transit Map
- 目录：`vendor/lemo-opuscar/styles/transit-map/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/transit-map/poster.jpg`
- 适合：Transport、Growth over time、Networks
- 演示片《6 公里》：一张纸上的线路图，从 1993 年的 6 公里长到 21 条线、906 公里。
- 要义：A metro schematic printed on a physical sheet: lines held to eight directions, white stops, black-outlined interchange capsules, water as a flat blue band. The network is drawn on by glowing pen tips while a real perspective camera moves over the paper: it rides a tip, drops low where a line dives under water, pulls back through levels of detail and sweeps across the densest knot at a low angle with a shallow focus.

### 白模投影 · Projection-Mapped Model
- 目录：`vendor/lemo-opuscar/styles/white-model/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/white-model/poster.jpg`
- 适合：Urban planning、Exhibitions、City data
- 演示片《被炸平的城市怎样长回来》：投影机把数据一层层刷上鹿特丹白模：从 1940 年的空洞到今天的塔楼。
- 要义：A pure white massing model of a real place stands on a plinth in a dark room, and a projector paints data onto it as light: one layer at a time, falling on the surfaces that face it, spilling a little past the plate. The model never changes; only the light on it does.

## 印刷版画（8）

### 铜版画 · Copperplate Engraving
- 目录：`vendor/lemo-opuscar/styles/engraving/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/engraving/poster.jpg`
- 适合：Museum labels、Science explainers、Brand heritage
- 演示片《蜜蜂，图版七》：一张博物志图版自己刻出来：雕刀推开铜版，蜜蜂一线线成形，最后手工水彩上色。
- 要义：An intaglio plate that engraves itself: a burin cuts swelling lines into copper, a proof is pulled, and the figure builds up — outline, hatching, cross-hatching — until engraved lettering, magnified details and a hand-laid wash make a finished plate.

### 网点档案 · Halftone Dossier
- 目录：`vendor/lemo-opuscar/styles/halftone-dossier/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/halftone-dossier/poster.jpg`
- 适合：Humour、Pet content、Social shorts
- 演示片《胖橘案卷》：橘猫胖橘被立案审查：测试重力、凌晨跑酷，最后无罪释放。
- 要义：A retro print case file: cream archive paper, overprinted halftone dots in a few flat inks, huge heavy headlines with misregistered shadows, rubber stamps that slam, and thick-outlined characters. The film is a file that is read out one exhibit at a time.

### 波普艺术 · Pop Art
- 目录：`vendor/lemo-opuscar/styles/pop-art/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/pop-art/poster.jpg`
- 适合：Everyday-object explainers、Brand and product posters、Small data stories
- 演示片《同一根香蕉》：超市里几乎每根香蕉都是同一株植物的复制：一面一模一样的版画墙，一根被网点吃黑的老香蕉，最后一波换色翻出上千种香蕉。
- 要义：Sixties screen-print and pop-art poster language used to tell something: Ben-Day dots fixed to the paper, heavy black key lines, flat red, yellow and blue, plates that never quite register. Every frame is one whole printed poster; the camera pushes into the dots, pulls back to the wall of prints, and moves through the shapes of the print itself.

### 刮版画长镜头 · Scratchboard Long Take
- 目录：`vendor/lemo-opuscar/styles/printed-long-take/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/printed-long-take/poster.jpg`
- 适合：Journeys、Wildlife、Landscapes
- 演示片《三十三只》：刮版画的北海道河谷一镜到底，丹顶鹤从 33 只数回到 1,927 只。
- 要义：A three-dimensional world rendered as a scratchboard print, ink and paper with one red, crossed by one unbroken camera move. Depth, weather and light are all cut lines; the camera travels through the print instead of the print being turned page by page.

### 孔版印刷 · Risograph Print
- 目录：`vendor/lemo-opuscar/styles/risograph/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/risograph/poster.jpg`
- 适合：Indie brands、Zines、Lifestyle
- 演示片《周日骑行》：周日早晨骑车穿过城市：面包店、公园、河边，每到一处加一版油墨，最后三版套印。
- 要义：Animation that looks printed, frame by frame, on a stencil duplicator: two or three translucent spot inks overprinted on warm paper, halftone dots, ink grain, and plates that never quite line up.

### 丝印旅行海报 · Silkscreen Travel Poster
- 目录：`vendor/lemo-opuscar/styles/silkscreen-poster/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/silkscreen-poster/poster.jpg`
- 适合：Destination guides、Tourism、Event posters
- 演示片《绕远路回家》：一张满屏丝印海报一座城，票根数着离家的公里数，走到世界的另一头，才发现那是回家的路。
- 要义：Opaque, hard-edged flat inks pulled one colour at a time through a screen: 4–6 inks per poster, stepped colour bands instead of gradients, thin paper-white gaps where the registration slips. Information is revealed the way the print is made: one layer, one beat.

### 复古版画拼贴 · Vintage Engraving Collage
- 目录：`vendor/lemo-opuscar/styles/vintage-collage/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/vintage-collage/poster.jpg`
- 适合：The history of an object、Magazine-style explainers on ideas and society、Archive and collecting stories
- 演示片《倒置的珍妮》：1918 年一整版印反了的航空邮票：24 美元买下、剪开散落，66 号至今下落不明。
- 要义：A magazine collage made on a paper table: public-domain engravings, stamps, old photographs and printed ephemera are cut out with a white paper margin and laid over torn sheets of flat colour, and the pieces move like cut-out animation, on twos, with paper thickness and real shadows. Numbers are drawn as our own "data engravings": engraved lines that swell with the value.

### 木刻版画 · Woodcut Print
- 目录：`vendor/lemo-opuscar/styles/woodcut/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/woodcut/poster.jpg`
- 适合：Folk tales、Craft brands、Book trailers
- 演示片《铸钟人》：村子用一整个冬天铸一口钟，钟声第一次响起，雪停了。
- 要义：A relief print that carves itself: every frame is a black wood block, and light only exists where a knife has cut it away. One colour at most, and only for the thing that burns.

## 电子游戏（4）

### 节奏综艺 · Rhythm Game Show
- 目录：`vendor/lemo-opuscar/styles/game-show/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/game-show/poster.jpg`
- 适合：Tech timelines、Year in review、Variety shows
- 演示片《AI 进化节拍》：把 AI 发展史做成一局节奏游戏，模型踩着拍登场，最后发成绩单。
- 要义：A rhythm-game variety show in flat vector: toy-like mascots with thick ink outlines on candy-coloured stripes and sunbursts, every hit landing on a fixed tempo grid, call-and-response patterns, and a judgement word when each round is won.

### 2.5D 像素 · 2.5D Pixel Art
- 目录：`vendor/lemo-opuscar/styles/hd-2d/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/hd-2d/poster.jpg`
- 适合：Game trailers、Fantasy、Story films
- 演示片《守灯人》：灯塔熄灭，孙女提着最后一簇火穿过夜林、爬上风暴悬崖。
- 要义：Hand-made pixel sprites standing like paper cut-outs inside a lit, fogged, fully 3D diorama, shot from a high three-quarter angle through a tilt-shift lens: a toy world where every lamp throws a real shadow.

### 微游戏快闪 · Microgame Frenzy
- 目录：`vendor/lemo-opuscar/styles/microgame/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/microgame/poster.jpg`
- 适合：Game trailers、Onboarding、Social shorts
- 演示片《五秒宇航员》：见习宇航员闯五秒训练营，越来越快，Boss 关亲手降落回地球。
- 要义：A rapid-fire party-game film: one command word, a few seconds, one action. Every microgame is drawn in a completely different art style, and the film keeps getting faster.

### 16-bit 像素 RPG · 16-bit Pixel RPG
- 目录：`vendor/lemo-opuscar/styles/pixel-rpg/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/pixel-rpg/poster.jpg`
- 适合：Game trailers、Recaps、Nostalgia
- 演示片《最后的存档点》：勇士在最终 Boss 门前存档，存档画面闪回一路冒险。
- 要义：A short film that looks, sounds and *behaves* like a mid-90s console role-playing game: 320×180 pixels, a limited indexed palette, text boxes that type, menus, save files, chip music with echo.

## 传统工艺（7）

### 金箔彩绘 · Gilded Illumination
- 目录：`vendor/lemo-opuscar/styles/gilded-illumination/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/gilded-illumination/poster.jpg`
- 适合：Fables and picture-book stories、Holiday and festival shorts、Brand and origin stories
- 演示片《借来的光》：画里的世界只有金子会发光，可太阳熄了；一个女孩提着最后一盏灯上山，把光还给了太阳。
- 要义：The whole frame is one gilded miniature painting, and the story happens inside it: flat mineral pigments inside firm ink outlines, white-lead highlights and dots, and real gold leaf (laid in squares, with seams, burnished) that only shines when a light inside the picture moves across it. No book, no page, no desk: the picture fills the screen edge to edge, and at the end it can be revealed as one whole painting inside its own border.

### 中国水墨 · Chinese Ink Wash
- 目录：`vendor/lemo-opuscar/styles/ink-wash/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/ink-wash/poster.jpg`
- 适合：Wuxia、Cultural brands、Poetry
- 演示片《剑客与江》：侠客踏水过江，一剑断流。
- 要义：Xieyi ink painting on rice paper, animated: blank paper is space, one brushstroke is a mountain, a wave, a gesture or a cut.

### 纸雕灯影 · Paper-cut Lightbox
- 目录：`vendor/lemo-opuscar/styles/paper-lantern/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/paper-lantern/poster.jpg`
- 适合：Journeys and travel、Farewells and anniversaries、Places and their stories
- 演示片《末班夜车》：一列老夜车跑最后一趟：从雪山小站穿过长隧道开到海边，到站后车窗一扇扇熄灭。
- 要义：A layered paper-cut shadow box (纸雕灯) lit from behind: 6–9 sheets of cut card stacked in a shallow box, a warm light glowing through the paper, windows and moons burning through holes, soft shadows falling from each layer onto the next. The camera is a macro lens inside a lamp: it can show the box, or let the paper scenery fill the whole screen.

### 红色窗花剪纸 · Red Paper-cut
- 目录：`vendor/lemo-opuscar/styles/papercut-red/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/papercut-red/poster.jpg`
- 适合：Lunar New Year、Festive greetings、Folk tales
- 演示片《年兽进村》：除夕年兽进村，小女孩剪出的大窗花照亮全村，把它吓跑。
- 要义：Chinese window-flower paper-cuts brought to life: jointed red cut-outs on paper grounds, where the cut *is* the drawing and the holes are where the light gets in.

### 皮影戏 · Shadow Puppetry
- 目录：`vendor/lemo-opuscar/styles/shadow-puppet/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/shadow-puppet/poster.jpg`
- 适合：Myths & folklore、Heritage、Festivals
- 演示片《后羿射日》：十日炙烤大地，后羿张弓射日。
- 要义：Chinese shadow theatre: translucent dyed-hide puppets, carved like lace, pressed against a cotton screen and lit from behind by oil lamps.

### 彩色玻璃窗 · Stained Glass
- 目录：`vendor/lemo-opuscar/styles/stained-glass/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/stained-glass/poster.jpg`
- 适合：Legends、Heritage、Holiday stories
- 演示片《东窗之龙》：阳光从清晨移到黄昏，照到哪一格花窗，哪一格的故事就动起来。
- 要义：A medieval stained-glass window seen from inside a dark stone hall, alive only where the sun touches it: light is the clock, the camera and the story.

### 浮世绘 · Ukiyo-e
- 目录：`vendor/lemo-opuscar/styles/ukiyoe/`（演示代码：有）；海报：`vendor/lemo-opuscar/styles/ukiyoe/poster.jpg`
- 适合：Travel、Japanese culture、Poetry
- 演示片《走向远山》：旅人走向远山，每个镜头都是一幅版画；巨浪是高潮，结尾是远山与整幅画轴拉远。
- 要义：Edo-period woodblock prints brought to life: flat colour blocks, carved ink lines, bokashi skies, paper you can feel, and a camera that moves over the print like an unrolling handscroll.

## cinecode 独有（7）

### Line Boil: Style Prompt
- 文件：`vendor/cinecode/styles/line-boil.md`
- 要义：Hand-drawn cel animation that breathes: every outline trembles a little from drawing to drawing, poses hold on

### Shape Morph Chain: Style Prompt
- 文件：`vendor/cinecode/styles/shape-morph.md`
- 要义：One hero shape keeps becoming the next meaningful thing, on the beat: a coffee cup becomes the sun, the sun a

### Visual Proof: Style Prompt
- 文件：`vendor/cinecode/styles/visual-proof.md`
- 要义：Mathematics and science explained the way a good teacher draws it: one idea built on screen from shapes, every

### Liquid Motion: Style Prompt
- 文件：`vendor/cinecode/styles/liquid-motion.md`
- 要义：Shapes that behave like thick, glossy liquid: drops fall and squash, blobs merge with stretched necks and snap

### Vox Explainer: Style Prompt
- 文件：`vendor/cinecode/styles/vox-explainer.md`
- 要义：A documentary "why" film made of paper: torn cards, cut-out archive photos and documents laid on a warm desk, a marker that circles the one detail that matters, bold condensed type on paper strips, and a narrator who walks the viewer from a question to an answer, one sourced fact per shot.

### Variety Captions: Style Prompt
- 文件：`vendor/cinecode/styles/variety-captions.md`
- 要义：Emotional, decorated captions straight out of TV variety-show editing: fat rounded letters with layered outlines

### Sticker Explainer: Style Prompt
- 文件：`vendor/cinecode/styles/sticker-explainer.md`
- 要义：A knowledge film on one huge calm canvas: cut-out photos with thick white borders like stickers, flat icons and

## 其他来源（3）

### 竖屏卡通 3D 故事短片 · claude-animated-shorts
- 目录：`vendor/claude-animated-shorts/`。扁平"豆形头"2D 角色站在彩色 3D 小镇里，墨线、景深、滑动运镜；55–70 秒竖屏，配音先行、逐词对时。
- 要读：`SKILL.md`、`references/STYLE_BIBLE.md`（20 部参考片测出的脚本与视觉公式）、`references/reports/`（运动、景深、纹理、角色、光照、描边、调色 7 份测量报告）。代码在 `templates/`（Remotion + three.js）。

### 手绘卡通（p5.brush）· ClaudeAnimationBase
- 目录：`vendor/ClaudeAnimationBase/`。纸面水彩笔刷、手绘描边沸腾、角色表演；先读 `ANIMATION_GUIDE.md`。
- 原仓库的角色 Clawd 属于 Anthropic，没有收入：引擎可用，角色要自己设计。

### 纸面两色印刷 · 本 skill 示例《红笔》
- 规格卡见 `examples/red-pen/交付报告.md`，代码见 `examples/red-pen/film.html`。

## 按用途的配方（不是风格，是场景模板）

- `vendor/awesome-ai-motion/recipes/`：11 个配方（标题开场、知识讲解、数据故事、产品演示、前后对比、短视频钩子、章节转场、引言卡片等），每个配方说明用哪些动效、多长、怎么排。
- `vendor/awesome-ai-motion/routes/`：7 条设计路线（韩文），按交付物（短视频、宣传、信息图、缩略图、剪辑、演示稿与网站、简报）给出动效选择。
- `vendor/awesome-ai-motion/effects/`：637 张动效卡片，每张有定义、参数和可直接用的提示词；总表 `docs/catalog.md`，按目的选动效看 `references/decision-tables.md`。
