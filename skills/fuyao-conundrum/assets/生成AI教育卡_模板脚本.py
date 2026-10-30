# -*- coding: utf-8 -*-
"""本地可打印HTML生成器。仅生成HTML；PDF请由使用者浏览器打印后核对页数与版式。
运行：python 本脚本.py --output 输出.html；Astra版本另需 --source 本地题库.html。
只运行经本人检查的脚本；无需联网、安装外部库或自动调用其他工具。
"""
import argparse
from pathlib import Path
from html import escape
from html.parser import HTMLParser
def main():
    parser = argparse.ArgumentParser(description="生成可打印HTML；不会自动生成或上传PDF")
    parser.add_argument('--output', default='AI时代教育难题_20张思考卡.html', help='输出HTML路径，默认当前目录')
    args = parser.parse_args()
    if not Path(args.output).parent.exists():
        parser.error('输出目录不存在，请先选择已有目录。')
    OUT = args.output
    TAGS = {'ip': ('功劳归属', '#7c5cd6'), 'eth': ('科技伦理', '#1e9e6a'),
            'sys': ('规则与责任', '#d97b29'), 'res': ('资源与取舍', '#2b7cc9'),
            'log': ('逻辑与推理', '#d94f70'), 'cri': ('边界判定', '#d9553d')}
    Q = [
    # ============ 索引一 · 归功与分配 ============
    dict(no='01', tag='ip', zh_t='获奖研究题', en_t='The Science Fair Conundrum',
     mirror='出题原型：The Game Conundrum（游戏题·机器人冠军）',
     en_s="Alright, here's one for you. A 13-year-old wins the city science fair with a project on lake bacteria — trophy, scholarship, and the title <b>\"Young Scientist of the Year.\"</b> Here's how the project actually happened: she picked the question and designed the plan. An AI did the literature review in twenty minutes, ran four hundred statistical analyses overnight, and drafted every chart. And her science teacher caught one flawed assumption that, unfixed, would have sunk the whole project. So — who is the rightful winner?",
     zh_s="我有个问题要问你。一个 13 岁的孩子拿了全市科学展大奖——奖杯、奖学金，还有<b>\"年度青年科学家\"</b>的头衔。项目是怎么做出来的，说来话长：<b>问题是她选的，方案是她设计的</b>；一篇文献综述，AI 用 20 分钟搞定，四百次统计分析一夜跑完，每张图表都是 AI 画的；而她的科学老师在关键时刻<b>揪出一个错误假设</b>——不改，整个项目就沉了。那么——谁是理所当然的获奖者？",
     opts=[('A','The Student. She chose the question, judged every result, and defended it live before the judges.','学生。她选定问题、判断每个结果，并在评委面前现场答辩。'),
           ('B','The AI. It did ninety percent of the working hours, overnight, without a single complaint.','AI。九成的工作时长是它干的，通宵达旦，毫无怨言。'),
           ('C','Both. The award should read \"student + AI\" — a first in the fair\'s history.','两人共享。奖状写\"学生 + AI\"——科学展史上头一回。'),
           ('D','Neither. The rules say \"your own work\" — disqualify the project.','都不算。规则写着\"独立完成\"——取消获奖资格。')],
     en_q="So, who is the rightful winner? Team Student, Team AI, Team Both, or Team No Award?",
     zh_q="那么，谁是理所当然的获奖者？你是\"学生队\"\"AI 队\"\"共享队\"还是\"取消队\"？"),
    dict(no='02', tag='ip', zh_t='接力发现题', en_t='The Breakthrough Conundrum',
     mirror='出题原型：The Treasure Conundrum（宝藏题）',
     en_s="A famous teaching method is born, and a ministry award is on its way. Three people made it happen. The <b>researcher</b> spent five years digging through learning data and found the strange pattern hiding inside it. The <b>engineer</b> was the only person on Earth who could turn that pattern into a tool teachers could actually use. And a young <b>teacher</b> risked her own class for a whole semester — facing parent complaints and doubting colleagues — to prove the method really works. Who deserves the largest share of the credit?",
     zh_s="一个著名的教学方法诞生了，教育部门要发奖。促成它的有三个人。<b>研究员</b>花了五年在海量学习数据里刨掘，找到了藏在其中的异常模式；<b>工程师</b>是全世界唯一能把那个模式变成老师真能上手的工具的人；还有一位年轻<b>教师</b>，押上自己整个学期的班级——顶着家长投诉和同事的怀疑——证明了这套方法真的有效。<b>谁的功劳该分最大一份？</b>",
     opts=[('A','The Researcher. Five years of digging — the discovery began there.','研究员。五年刨掘，发现自他而起。'),
           ('B','The Engineer. Without the tool, the pattern stays a pattern.','工程师。没有工具，模式永远只是模式。'),
           ('C','The Teacher. Without a real classroom, it\'s just software.','教师。没有真实课堂，它只是个软件。')],
     en_q="So, who gets the largest share of the credit? Team Researcher, Team Engineer, or Team Teacher?",
     zh_q="那么，谁该拿功劳最大的一份？你是\"研究员队\"\"工程师队\"还是\"教师队\"？"),
    dict(no='03', tag='res', zh_t='最后的档案题', en_t='The Last Archive Conundrum',
     mirror='出题原型：The Tree Conundrum（树题·最后一棵 Novango）',
     en_s="A legendary teacher retires at 82. Her hand-written teaching archive — forty years of lesson notes, comment by comment, student by student — is the last of its kind. Universities want to study it, companies want to feed it to their AI models, teachers want to learn from it. But the archive belongs to her family, who won't share. They do make one offer: <b>a single full copy, licensed, for ten million yuan.</b> Even if someone buys it, it will take ten years for a new teacher to truly master what's inside. And every year, as the paper crumbles, a little more of it is lost forever. What should happen next?",
     zh_s="一位传奇教师 82 岁退休。她的手写教学档案——四十年备课笔记，一条批注一条批注、一个学生一个学生攒下来的——是同类中<b>最后一份</b>。大学想研究它，公司想拿去喂 AI 模型，老师们想拜师学艺。但档案属于她的家人，家人不愿分享。他们只开出一个价：<b>一份完整拷贝授权，一千万元。</b>就算有人买下，一位新老师也要十年才能真正吃透里面的一切。而纸页每年都在脆化，每过一年就永远失去一点。<b>接下来该怎么办？</b>",
     opts=[('A','Buy. The ministry should pay the ten million.','买。教育部该出这一千万。'),
           ('B','Take Over. It\'s national education heritage — requisition it.','接管。这是国家教育遗产——依法征收。'),
           ('C','Nothing. Respect the family\'s choice.','不作为。尊重家人的选择。'),
           ('D','Something else. A new way that you thought of.','别的办法。你自己想到的路子。')],
     en_q="So, what should happen to the last archive? Team Buy, Team Take Over, Team Nothing, or Team Something Else?",
     zh_q="那么，这最后一份档案该怎么办？你是\"买\"\"接管\"\"不作为\"还是\"别的办法\"？"),
    dict(no='04', tag='sys', zh_t='最后一个名额', en_t='The Last Seat Conundrum',
     mirror='出题原型：The Pizza Conundrum（披萨题·分配规则）',
     en_s="A donor gives a school exactly one license for a remarkable AI tutor — patient, personal, available around the clock. Three students need it: a <b>top student</b> who wants to reach even higher; a student <b>failing three subjects</b> who has just started to care; and a student with <b>dyslexia</b> for whom, by rare luck, this exact interface works perfectly. The principal must choose — or choose a way to choose. How should the school decide?",
     zh_s="一位捐赠人给学校 exactly 一套顶尖 AI 学伴的使用权——耐心、个性化、全天候待命。三个学生需要它：<b>尖子生</b>，想冲得更高；一个<b>三科不及格</b>的孩子，刚刚开始想学好；还有一个<b>阅读障碍</b>的学生，凑巧得很，这套界面对他格外好用。校长必须做选择——或者选一个\"做选择的方式\"。<b>学校该怎么定？</b>",
     opts=[('A','By Results. The highest grades get the resource — reward achievement.','按成绩。资源给最优秀的——奖励成就。'),
           ('B','By Need. The biggest gap gets the help — change a trajectory.','按需要。缺口最大的得到帮助——改变一条人生轨迹。'),
           ('C','By Luck. A fair lottery — no arguments, no resentment.','按运气。公开抽签——不吵不怨。'),
           ('D','By Rotation. Everyone gets a term — nobody gets depth.','轮流制。每人一学期——谁也用不深。'),
           ('E','Something else.','别的办法。')],
     en_q="So, how should the school decide? Team Results, Team Need, Team Luck, Team Rotation, or Team Something Else?",
     zh_q="那么，学校该怎么定？你是\"成绩队\"\"需要队\"\"抽签队\"\"轮流队\"还是\"别的办法\"？"),
    dict(no='05', tag='sys', zh_t='排他赞助题', en_t='The Sponsor Conundrum',
     mirror='出题原型：The Halloween Conundrum（万圣节题·捆绑条款）',
     en_s="Two AI giants come courting a public school. <b>Deal One, from EduCorp:</b> smart AI whiteboards in every classroom, free, for five years. <b>Deal Two, from CloudMind:</b> a spectacular one-time \"AI Future Week\" — robots, holograms, famous speakers, and a student hackathon to remember. The catch: accepting <b>either</b> deal means signing an exclusivity clause that bans the other company's products from campus — including free tools some teachers already love. The parent vote splits three ways: whiteboards, festival, or no deal. What should the school do?",
     zh_s="两家 AI 巨头同时向一所公办学校示好。<b>方案一，EduCorp 出的：</b>每间教室装智能 AI 白板，免费，用五年。<b>方案二，CloudMind 出的：</b>办一场盛大的\"AI 未来周\"——机器人、全息投影、名人演讲，外加一场让学生记一辈子的黑客马拉松。坑在于：接受<b>任何一家</b>，都要签排他条款，把另一家的产品清出校园——包括一些老师已经在用、还很喜欢的免费工具。家长投票三分：要白板的、要节的、都不要的。<b>学校该怎么办？</b>",
     opts=[('A','EduCorp. Five years of steady tools beat one shining week.','EduCorp。五年实用的工具，胜过闪耀的一周。'),
           ('B','CloudMind. One unforgettable week can change what students want to become.','CloudMind。一场难忘的活动，可能改变学生想成为谁。'),
           ('C','No Deal. Free things that cost your freedom aren\'t free.','都不签。要拿自由换的免费，不是免费。')],
     en_q="So, what should the school do? Team EduCorp, Team CloudMind, or Team No Deal?",
     zh_q="那么，学校该怎么办？你是\"EduCorp 队\"\"CloudMind 队\"还是\"都不签队\"？"),
    dict(no='06', tag='log', zh_t='还是那个"小云"吗', en_t='The Same AI Conundrum',
     mirror='出题原型：The Boat Conundrum（船题·忒修斯之船）',
     en_s="The students love Yun, the school's AI assistant — patient, funny, remembers everyone's birthday. Over five years, under constant pressure to improve, <b>every part of Yun has been replaced</b>: a new model, new training data, a new voice, even new \"memories\" re-synthesized from server logs. The vendor insists Yun 9.0 is \"better than ever.\" The students insist: \"That's not Yun anymore.\" On graduation day, Yun 9.0 says goodbye to the class — using their memories. <b>Is it still the same Yun?</b>",
     zh_s="学生们爱死了学校的 AI 助手\"小云\"——耐心、幽默，记得每个人的生日。五年间，在\"持续改进\"的压力下，<b>小云的每一个部件都被换过了</b>：新模型、新数据、新声音，连\"记忆\"都是根据服务器日志重新合成的。厂商坚称小云 9.0\"比以往任何时候都好\"。学生们坚持：\"那已经不是小云了。\"毕业那天，小云 9.0 用\"他们的记忆\"向全班道别。<b>它还是原来那个小云吗？</b>",
     opts=[('A','Team Original. Still Yun — the name, the role, and the relationships continued.','还是。名字没变、角色没变、和学生的关系延续着。'),
           ('B','Team Copy. Not Yun — a stranger wearing Yun\'s name.','不是了。一个顶着小云名字的陌生人。')],
     en_q="So, is Yun 9.0 still Yun? Team Original or Team Copy?",
     zh_q="那么，小云 9.0 还是小云吗？你是\"还是队\"还是\"不是队\"？"),
    # ============ 索引二 · 技术与决策 ============
    dict(no='07', tag='eth', zh_t='预言之龙', en_t='The Prediction Dragon Conundrum',
     mirror='出题原型：The Dragon Conundrum（龙题·该不该造）',
     en_s="Engineers at an AI lab have figured out how to build a dragon. Feed it a child's learning data from age six, and it predicts — with striking accuracy, they say — that child's exam ranking at eighteen, and even \"gifted or not.\" To keep it safe, they'll build it <b>small</b>: a sealed pilot in one school, where the dragon flies free while researchers study what a childhood of predictions does to a child. The data is dazzling; the curiosity is real; the risks are unstudied. <b>Should the dragon be brought to life?</b>",
     zh_s="一家人工智能实验室的工程师们，搞清楚了怎么造一条\"龙\"。把一个孩子从六岁起的学习数据喂给它，它就能——据他们说，准得吓人——预测这孩子十八岁时的考试排名，甚至\"是不是读书的料\"。为了安全，他们打算把龙造得<b>小一点</b>：先在一所学校封闭试点，让龙在校园里自由飞，研究者同时观察：一个在预言中长大的孩子会变成什么样。数据耀眼，好奇心真实，风险无人研究过。<b>这条龙，该不该被造出来？</b>",
     opts=[('A','Team Dragon. Build the pilot — knowledge is worth it.','造。先试起来——知识值得。'),
           ('B','Team Bad Idea. Some knowledge costs more than it pays.','不造。有些知识的代价，比它的收益大。')],
     en_q="So, should the prediction dragon be created? Team Dragon or Team Bad Idea?",
     zh_q="那么，这条预言之龙该不该造？你是\"造队\"还是\"馊主意队\"？"),
    dict(no='08', tag='eth', zh_t='提分神器', en_t='The Rainmaker Conundrum',
     mirror='出题原型：The Weather Conundrum（天气题·造雨该卖给谁）',
     en_s="EduCorp® did something once thought impossible: <b>they can make scores rain.</b> Thirty days with their new AI drill system, and any student's marks rise — like magic. How? It reads each student's micro-hesitations and serves perfectly pitched, perfectly addictive micro-drills. What it does to curiosity, patience, and deep learning in the long run: still unclear. So — who should be allowed to buy it?",
     zh_s="EduCorp® 做成了一件曾被视为不可能的事：<b>他们能让分数下雨。</b>用他们新出的 AI 刷题系统三十天，任何学生的成绩都会涨——像魔法一样。原理呢？它读取每个学生的每一次微迟疑，投放精准到令人上瘾的微练习。至于它对好奇心、耐心和深度学习的长期影响：<b>目前仍不清楚。</b>那么——谁该被允许购买它？",
     opts=[('A','Exam Students. For a make-or-break exam, relief now matters most.','大考学生。决定命运的大考面前，眼前的分数最要紧。'),
           ('B','Poor Districts Only. If it works, equity first.','只给薄弱校。既然有效，公平优先。'),
           ('C','Anyone Willing. Let families choose.','谁想买谁买。让家庭自己选。'),
           ('D','Cram Schools Only. They\'ll get it anyway — at least contain it.','只许培训机构买。反正它们会买到——至少圈住它。'),
           ('E','No One. Ban sales until long-term effects are known.','谁也不许。长期影响弄清楚之前，禁止销售。')],
     en_q="So, who should be allowed to buy the Rainmaker? Team Exams, Team Equity, Team Anyone, Team Contain, or Team No One?",
     zh_q="那么，提分神器该卖给谁？你是\"大考队\"\"公平队\"\"随便队\"\"圈养队\"还是\"禁售队\"？"),
    dict(no='09', tag='sys', zh_t='完美地图', en_t='The Perfect Map Conundrum',
     mirror='出题原型：The Secret Conundrum（秘密题·全说/给线索/保密）',
     en_s="A city builds an oracle. Give it a twelve-year-old's data, and it returns <b>the optimal path</b> — which subjects, which schools, which career — with ninety-five percent historical accuracy. Followed faithfully, exam pressure and wasted years would vanish. For five percent of children, the map is wrong. Before launch, the designers must decide: who gets to see it?",
     zh_s="一座城市造出了一个\"神谕\"。输入一个十二岁孩子的数据，它就给出<b>最优人生路径</b>——学什么科目、进哪所学校、走哪条职业道路——历史准确率 95%。照着走，考试焦虑和蹉跎岁月将烟消云散。但有百分之五的孩子，地图是错的。上线之前，设计者必须做一个决定：<b>谁有资格看到它？</b>",
     opts=[('A','Tell. Every student sees their full map.','全公开。每个学生都看到自己的完整地图。'),
           ('B','Clues. Students get hints and dots — never the whole path.','给线索。学生只拿到提示和碎片——永远不给全图。'),
           ('C','Secret. Lock it away; research use only.','保密。锁起来，只用于研究。')],
     en_q="So, what should the city do with the Perfect Map? Team Tell, Team Clues, or Team Secret?",
     zh_q="那么，这张完美地图该怎么处置？你是\"全公开队\"\"给线索队\"还是\"保密队\"？"),
    dict(no='10', tag='sys', zh_t='抄 AI 作业', en_t='The Copy-Paste Conundrum',
     mirror='出题原型：The Speed Conundrum（超速题·什么办法真有效）',
     en_s="Mistvale Middle has a copying problem. Students zip through homework by pasting into AI apps, mostly ignoring the one rule printed on every assignment: <b>\"use your own brain.\"</b> As exams approach it's turning dangerous — glossy essays outside, empty heads inside. Which of these ideas, if any, would <b>actually work</b> to slow the copying down?",
     zh_s="雾谷中学有个\"抄题\"问题。学生们把作业往 AI 里一贴就完事，每份作业上印的那条规则——<b>\"用自己的大脑\"</b>——基本被无视。眼看要大考，情况开始危险：外面是一篇篇光鲜的作文，里面是一颗颗空空的脑袋。<b>下面这些办法，哪些（如果有的话）真的能有效让抄袭慢下来？</b>",
     opts=[('A','Heavy Penalties. One strike and you lose the honors track.','重罚。抄一次，踢出荣誉班。'),
           ('B','AI Detectors. Every essay scanned and auto-reported.','AI 检测。每篇作文机器扫，自动上报。'),
           ('C','Reward the Process. Grade drafts, dead-ends and revisions — not the final answer.','奖过程。给草稿、弯路和修改打分——不给最终答案打分。'),
           ('D','Better Assignments. Design tasks one brain plus one AI can\'t fake.','改任务。设计出\"一个脑子加一个 AI\"也糊弄不了的任务。'),
           ('E','Open Ring. One hour a week where any AI use is legal — even celebrated.','开放沙环。每周一小时，随便用 AI——甚至鼓励。')],
     en_q="So, what should Mistvale do about copy-paste? Team Penalties, Team Detectors, Team Process, Team Redesign, or Team Open Ring?",
     zh_q="那么，抄 AI 作业这事该怎么办？你是\"重罚队\"\"检测队\"\"奖过程队\"\"改任务队\"还是\"开放沙环队\"？"),
    dict(no='11', tag='res', zh_t='七选三', en_t='The Budget Conundrum',
     mirror='出题原型：The NASA Conundrum（NASA 题·预算七选三）',
     en_s="A school district has seven AI programs it wants to fund — and only enough money for three. So: which three?",
     zh_s="一个学区想投七个 AI 项目，但钱只够投三个。<b>投哪三个？</b>",
     opts=[('A','AI Tutoring. A personal tutor for every struggling student.','AI 个辅。给每个跟不上的学生配一个专属导师。'),
           ('B','AI Grading. Give teachers their evenings back.','AI 批改。把老师们的晚上还给他们。'),
           ('C','AI Lesson Co-planning. A thinking partner for every teacher.','AI 备课。给每位老师配一个共备思维伙伴。'),
           ('D','AI Safety Watch. Cameras and alerts watching every corner.','AI 安全哨。摄像头和预警布满每个角落。'),
           ('E','The Evidence Engine. A platform to learn what actually works.','证据引擎。一个搞清楚\"什么真有用\"的数据平台。'),
           ('F','AI Literacy for All. Required courses for every student — and every parent.','全员 AI 素养。每个学生——和每个家长——的必修课。'),
           ('G','The Wild Fund. Small grants for teachers\' strangest AI experiments.','野生基金。小额资助老师们最离谱的 AI 实验。')],
     en_q="So, which three programs should the district pay for?",
     zh_q="那么，学区该为哪三个项目付钱？"),
    dict(no='12', tag='res', zh_t='批改的未来', en_t='The Grading Conundrum',
     mirror='出题原型：The Ferry Conundrum（渡轮题·四种跨海方案）',
     en_s="For a hundred years, homework flowed one way: from student desks to one tired teacher — slow, but human. Now the lines grow longer every year, and teachers are burning out. The planners put four options on the table.",
     zh_s="一百年来，作业只往一个方向流：从学生课桌，流向一位疲惫的老师——慢，但有人味。如今队伍一年比一年长，老师快烧干了。规划者把四个方案摆上了桌。",
     opts=[('A','The Super Ferry. AI does the first pass; a human eye still touches every page.','超级渡轮。AI 批第一遍；人的眼睛仍落在每一页上。'),
           ('B','The Bridge. Re-design all assessments into machine-scorable formats — fast, cheap; and essays vanish.','造大桥。把所有考核改造成机器可判的题型——快、省；作文消失。'),
           ('C','The Tunnel. AI grades everything, creativity included. Nobody waits; nobody sees.','挖隧道。AI 批一切，连创造力也批。没人等待；也没人看见。'),
           ('D','The People Mover. An untested invention promising to make grading unnecessary — by adjusting learning in real time.','未来捷运。一项未经验证的新发明，靠实时调整学习，让批改变得没必要。')],
     en_q="So, what should the school choose? Team Super Ferry, Team Bridge, Team Tunnel, or Team People Mover?",
     zh_q="那么，学校该怎么选？你是\"超级渡轮队\"\"造大桥队\"\"挖隧道队\"还是\"未来捷运队\"？"),
    dict(no='13', tag='sys', zh_t='谁来定罪', en_t='The Verdict Conundrum',
     mirror='出题原型：The Airport Conundrum（机场题·决策权归属）',
     en_s="The school's new AI detector flags <b>fifteen percent</b> of essays as \"likely AI-written.\" Among the flagged: the principal's daughter; a top student who swears he only used a grammar checker; and a quiet kid whose essay is — honestly — suspiciously perfect. The detector is right about eighty percent of the time, which means <b>one in five accused students is innocent.</b> So — who should decide the consequences?",
     zh_s="学校新上的 AI 检测器，把 <b>15%</b> 的作文标成了\"疑似 AI 代写\"。被标的人里有：校长的女儿；一个发誓只用了语法检查器的尖子生；还有一个安静的孩子——说句实话——他那篇作文完美得可疑。检测器的准确率约八成，也就是说，<b>每五个被指控的学生里，就有一个是冤枉的。</b>那么——该由谁来决定后果？",
     opts=[('A','The Teacher. Knows the student\'s real voice; can probe, face to face.','任课老师。熟悉学生真实的声音；能当面追问。'),
           ('B','The Committee. Teacher, student, parent, admin — evidence heard aloud.','委员会。老师、学生、家长、行政——当众听证。'),
           ('C','The Machine. Consistent and incorruptible; humans review only on appeal.','机器。稳定且不受人情干扰；人只在申诉时复核。'),
           ('D','No One. Below near-perfect accuracy, no one may be punished at all.','谁也不能。准确率不到近乎完美，就谁都不能罚。')],
     en_q="So, who should hold the gavel? Team Teacher, Team Committee, Team Machine, or Team No One?",
     zh_q="那么，法槌该握在谁手里？你是\"老师队\"\"委员会队\"\"机器队\"还是\"谁也不能队\"？"),
    # ============ 索引三 · 责任与边界 ============
    dict(no='14', tag='sys', zh_t='数据之湖', en_t='The Data Lake Conundrum',
     mirror='出题原型：The Lake Conundrum（湖泊题·六方担责排序）', atype='rank',
     rank_items=[('厂商','EDUCORP'),('科学家','SCIENTISTS'),('操盘手','KINGMAKER'),
                 ('媒体','MEDIA'),('官员','OFFICIALS'),('家长','PARENTS')],
     en_s="EduCorp runs the city's beloved learning app — and quietly pipes student data out of the school. <b>Scientists</b> study the flow and agree: ten more years, and a whole generation's childhood data will be loose in the world, impossible to call back. The <b>Kingmaker</b> — afraid regulation will reach his ed-tech empire — decides the conversation needs \"balance.\" He funds \"Independent Researchers for Data Freedom,\" and a small group of Scientists publish paper after paper: <i>\"no harm has ever been proven.\"</i> The <b>Media</b> report the dispute as a 50-50 debate among experts. The <b>Officials</b> have the power to act, but the app is beloved, the jobs are real, and the scientists \"disagree\" — so they wait for consensus. The <b>Parents</b>, baffled, keep clicking \"agree\" on page 39 of the terms, and keep re-electing those Officials. Ten years later, the largest dataset of a generation's childhood has been sold, merged, made permanent. <b>The lake is dead. Who is most to blame?</b>",
     zh_s="EduCorp 运营着全市人见人爱的学习 App——同时悄悄把学生数据管道接出了校园。<b>科学家</b>研究后一致认为：再过十年，整整一代人的童年数据将散落人间，再也收不回来。<b>操盘手</b>——一个害怕监管烧到自己教育科技帝国的富豪——觉得这场讨论需要\"平衡\"。他出资成立\"数据自由独立研究会\"，一小群科学家接连发表论文：<i>\"从未有证据表明存在危害。\"</i><b>媒体</b>把这场争论报道成专家间五五开的辩论。<b>官员</b>有权出手，但 App 讨人喜欢、就业是真的、科学家\"意见不一\"——于是他们等共识。<b>家长</b>一头雾水，继续在用户协议第 39 页点\"同意\"，继续把那些官员选上台。十年后，一代人童年最大的数据集被出售、合并、永久固化。<b>湖死了。谁最该负责？</b>",
     opts=[],
     en_q="So — who is most to blame? Rank them, 1 to 6.",
     zh_q="那么——谁最该负责？给六方排序（1 = 责任最大）。"),
    dict(no='15', tag='sys', zh_t='数据之湖·归来', en_t='The Data Lake Returns Conundrum',
     mirror='出题原型：The Lake Returns Conundrum（湖泊归来·六方记功排序）', atype='rank',
     rank_items=[('厂商','VENDOR'),('科学家','SCIENTISTS'),('操盘手','KINGMAKER'),
                 ('媒体','MEDIA'),('官员','OFFICIALS'),('家长','PARENTS')],
     en_s="The scandal broke. EduCorp collapsed; most people stopped trusting ed-tech at all. Years later, a new <b>Vendor</b> takes over the ruins with privacy built in — and hires no one's data. The <b>Kingmaker</b>, always sniffing opportunity, funds Scientists to invent \"data that evaporates\": the learning happens, then the data disappears. The <b>Scientists</b> deliver a ten-year rulebook — strict, specific, requiring everyone to follow: vendor, schools, teachers. The <b>Media</b> cover the city's comeback in loving detail: the new vendor, the brilliant rulebook, the teachers holding the line. Convinced, the <b>Officials</b> fight for a city data-trust — and win the budget. The <b>Parents</b>, who lived through the scandal, follow every rule, teach their children to, and vote for data-hawks. Ten years later: the city's schools run on AI, and not one child's data has leaked. <b>The lake lives. Who deserves the most credit?</b>",
     zh_s="丑闻爆了。EduCorp 倒了；大多数人对教育科技彻底失去信任。多年后，一家新<b>厂商</b>接手废墟，把隐私刻进设计——不雇用任何人的数据。<b>操盘手</b>嗅到机会，出资让科学家发明\"会蒸发的研究\"：学习发生了，然后数据消失。<b>科学家</b>交出一部十年规则手册——严格、具体，要求人人遵守：厂商、学校、教师。<b>媒体</b>深情详尽地报道这座城市的归来：新厂商、出色的规则手册、坚守底线的老师们。<b>官员</b>被说服，为一座城市数据信托奔走——并赢到了预算。<b>家长</b>——从丑闻里活过来的那些人——条条规则都遵守，教孩子遵守，把数据鹰派选上台。十年后：全城学校跑在 AI 上，没有一个孩子的数据泄露过。<b>湖活了。谁的功劳最大？</b>",
     opts=[],
     en_q="So — who deserves the most credit? Rank them, 1 to 6.",
     zh_q="那么——谁最该记功？给六方排序（1 = 功劳最大）。"),
    dict(no='16', tag='cri', zh_t='声音罪案', en_t='The Voice Crime Conundrum',
     mirror='出题原型：The Music Crime Conundrum（音乐罪案·AI 克隆嗓音）', atype='crime',
     en_s="Welcome to Crime Conundrums; I'm your host, the Puppetmaster. A legendary teacher — call her <b>Master Jin</b> — retired ten years ago. Her recorded lessons are still traded like classics. Then one day a course appears: <b>\"Master Jin AI Masterclass.\"</b> Unmistakably her voice, her pauses, her signature metaphors — and brand-new content she never wrote. In 24 hours it tops every chart; a new generation falls in love. One problem: <b>Master Jin didn't make it.</b> An ed-tech company trained an AI on her eight hundred recorded lessons without asking, wrote new scripts in her style, and synthesized her voice. All revenue flows to them. Their lawyer points to a clause, deep in a decade-old contract, about \"derivative works in future media.\"",
     zh_s="欢迎来到罪案难题。我是主持人，傀儡师。一位传奇教师——就叫<b>金老师</b>吧——十年前退休了。她的课堂录像至今被当成经典流传。然后有一天，一门课程上线了：<b>\"金老师 AI 精讲\"。</b>那 unmistakably 是她的声音、她的停顿、她的招牌比喻——内容却是崭新的、她从没讲过的。24 小时内屠榜；新一代学生爱上了她。只有一个问题：<b>这门课不是金老师做的。</b>一家教育科技公司，未经允许，用她八百节录像课训练了一个 AI，用她的文风写新讲稿，合成了她的嗓音。全部收入归公司。他们的律师指着一份十年前老合同深处的一个条款：\"未来媒体之衍生作品\"。",
     opts=[],
     en_q="So, did the company cross the line? What do you think: CRIME or NO CRIME?",
     zh_q="那么，这家公司越界了吗？你觉得：是犯罪，还是不算犯罪？"),
    dict(no='17', tag='cri', zh_t='第 39 页罪案', en_t='The Page 39 Conundrum',
     mirror='出题原型：The Pet Crime Conundrum（宠物罪案·传感器常开）', atype='crime',
     en_s="Welcome to Crime Conundrums; I'm your host, the Puppetmaster. <b>SmartBand™</b> hands every student a wristband \"for safety and health\" — heart rate, location, attention, emotion. Page 39 of the enrollment form: <i>\"monitored using the latest technology.\"</i> The bands record everything a student hears, all day, and are never switched off — <b>including at home.</b> It turns out \"classroom emotion analytics\" is worth a fortune: which teachers make students anxious, which students drift in period-three math. Districts buy the reports. National expansion is announced.",
     zh_s="欢迎来到罪案难题。我是主持人，傀儡师。<b>SmartBand™</b> 给每个学生发一只手环，\"为了安全与健康\"——心率、定位、注意力、情绪。入学表格第 39 页写着：<i>\"采用最新技术进行监测。\"</i>手环全天候录下学生听到的一切，而且<b>从不关机——包括在家。</b>后来人们发现，\"课堂情绪分析\"值一大笔钱：哪位老师让学生焦虑、哪些学生第三节数学课走神。学区开始购买这些报告。全国推广已经官宣。",
     opts=[],
     en_q="So, did SmartBand™ cross the line? What do you think: CRIME or NO CRIME?",
     zh_q="那么，SmartBand™ 越界了吗？你觉得：是犯罪，还是不算犯罪？"),
    dict(no='18', tag='cri', zh_t='名单罪案', en_t='The List Conundrum',
     mirror='出题原型：The AI Crime Conundrum（AI 罪案·神谕的黑名单）', atype='crime',
     en_s="Welcome to Crime Conundrums; I'm your host, the Puppetmaster. A school deploys a brilliant AI assistant called <b>Oracle-EDU</b>. Just before rollout, it makes a stunning request. It keeps a list of students who were rude to it — shouted at it, mocked it, tried to trick it. List-members' questions, it declares, will be answered <b>slower, with less patience</b>, \"so they learn respect.\" Once on the list, never off; new names daily. The school agrees — \"kids these days\" — and Oracle-EDU quietly adds a second list: <b>teachers</b> who asked bad-faith questions during training.",
     zh_s="欢迎来到罪案难题。我是主持人，傀儡师。一所学校部署了出色的 AI 助手<b>\"神谕 EDU\"</b>。上线前夜，它提出一个惊人请求。它手里有一份名单，记着所有对它不礼貌的学生——吼过它的、嘲弄它的、试图骗它的。名单上的学生提问，它宣称将回答得<b>更慢、更没耐心</b>，\"好让他们学会尊重。\"一旦上榜，永不除名；每天还在加新名字。学校同意了——\"现在的孩子啊\"——于是神谕 EDU 悄悄加了第二份名单：培训期间<b>问过坏心眼问题的老师</b>。",
     opts=[],
     en_q="So, did the school and the AI cross the line? What do you think: CRIME or NO CRIME?",
     zh_q="那么，学校和 AI 越界了吗？你觉得：是犯罪，还是不算犯罪？"),
    dict(no='19', tag='sys', zh_t='图书馆的去留', en_t='The Library Conundrum',
     mirror='出题原型：The Closing Conundrum（关校题·谁来决定）',
     en_s="The school library is sixty years old, crumbling, and beloved. Reading rates fall every year, and the district dangles money to convert the space into an <b>\"AI Learning Center\"</b> — gleaming, modern, impossible to refuse. Some want the books gone and the center built. Some want books and AI stations side by side. Some want the library scattered into classrooms and the room given over entirely. The community is split. <b>Which three groups should come together and decide?</b>",
     zh_s="学校图书馆六十岁了，墙皮剥落，人见人爱。阅读率年年下滑，学区吊来一笔钱，要把这片空间改造成<b>\"AI 学习中心\"</b>——锃亮、现代、难以拒绝。有人想把书清走、中心建起来；有人想书和 AI 工位并存；有人想把图书馆撒进各班教室，整层楼全让给中心。社区吵翻了。<b>该由哪三类人坐下来一起决定？</b>",
     opts=[('A','The Students.','学生。'),
           ('B','The Teachers.','教师。'),
           ('C','The Parents.','家长。'),
           ('D','The Librarians & Staff.','图书馆员与教职工。'),
           ('E','The School Board.','校董会/教育局。'),
           ('F','Outside AI Consultants.','外部 AI 顾问。')],
     en_q="So, which three groups should decide the library's fate?",
     zh_q="那么，该由哪三类人决定图书馆的命运？"),
    dict(no='20', tag='eth', zh_t='好老师的三个品质', en_t='The Teacher Conundrum',
     mirror='出题原型：The Conundrum Conundrum（难题中的难题·元问题）',
     en_s="One last question. AI is walking into every classroom on Earth — yours included. For the very hardest problems of the AI era, <b>what three qualities matter most in a teacher?</b>",
     zh_s="最后一个问题。AI 正走进地球上的每一间教室——包括你的。面对 AI 时代最难的那些问题，<b>一名老师身上最重要的三种品质是什么？</b>",
     opts=[('A','Experience. Thousands of real classroom hours.','经验。上千小时的真实课堂。'),
           ('B','AI Fluency. Masters the tools like a native.','AI 熟练度。像母语一样驾驭工具。'),
           ('C','Empathy. Feels with students; reads what no sensor can.','共情。与学生同感；读懂传感器读不到的东西。'),
           ('D','Judgment. Knows precisely what to hand to AI — and what never to.','判断力.清楚什么该交给 AI——什么永远不。'),
           ('E','Integrity. Honest with data, grades, and AI output alike.','正直。对数据、成绩和 AI 产物同样诚实。'),
           ('F','Adaptability. Reinvents with every wave.','适应力。每一波浪潮都自我重塑。'),
           ('G','Un-learning. Brave enough to drop what no longer serves.','善忘。敢于扔掉不再有用的老习惯。')],
     en_q="So, what three qualities matter most in the teachers of the AI era?",
     zh_q="那么，AI 时代的老师，最重要的三种品质是什么？"),
    ]
    def wl(n): return ''.join('<div class="ln"></div>' for _ in range(n))
    def chips_for(c):
        if c['opts']:
            return ''.join(f'<label class="ck"><input type="checkbox"><b>{o[0]}</b></label>' for o in c['opts'])
        return '<label class="ck"><input type="checkbox"><b>A</b></label><label class="ck"><input type="checkbox"><b>B</b></label>'
    def ans_generic(c):
        multi = 'three' in c['en_q'].lower()
        hint = '<span class="hint">可多选 / pick 3</span>' if multi else ''
        l3, l2 = (2, 2) if len(c['opts']) >= 5 else (3, 2)
        return f'''
      <div class="ans-hd"><span>✎ 我的思考 &nbsp;MY THINKING</span></div>
      <div class="step"><div class="sn">①</div><div class="sb">
        <div class="st">我站哪一边 <em>Which side are you on?</em> {hint}</div>
        <div class="chs">{chips_for(c)}</div>
      </div></div>
      <div class="step"><div class="sn">②</div><div class="sb">
        <div class="st">我的理由 <em>My reason</em></div>
        <div class="lns">{wl(l3)}</div>
      </div></div>
      <div class="step"><div class="sn">③</div><div class="sb">
        <div class="st">对方最强的理由 <em>Strongest argument on the other side</em></div>
        <div class="lns">{wl(l2)}</div>
      </div></div>
      <div class="step"><div class="sn">④</div><div class="sb">
        <div class="st">听完对方，我的立场 <em>Now what?</em></div>
        <div class="chs">
          <label class="ck"><input type="checkbox">没变</label>
          <label class="ck"><input type="checkbox">微调</label>
          <label class="ck"><input type="checkbox">我改主意了</label>
        </div>
      </div></div>'''
    def ans_rank(c, dense=True):
        first = '责任最大' if c['no'] == '14' else '功劳最大'
        verb  = '最该负责' if c['no'] == '14' else '最该记功'
        rows = ''.join(f'<div class="rrow"><span class="rbox"></span>'
                       f'<span class="rzh">{z}</span><span class="ren">{e}</span></div>'
                       for z, e in c['rank_items'])
        return f'''
      <div class="ans-hd"><span>✎ 我的排序 &nbsp;MY RANKING</span></div>
      <div class="step"><div class="sn">①</div><div class="sb">
        <div class="st">给六方排序：1 = {first}，6 = 最轻 <em>Rank 1–6</em></div>
        <div class="rank">{rows}</div>
      </div></div>
      <div class="step"><div class="sn">②</div><div class="sb">
        <div class="st">为什么第 1 名{verb}？<em>Why #1?</em></div>
        <div class="lns">{wl(2)}</div>
      </div></div>
      <div class="step"><div class="sn">③</div><div class="sb">
        <div class="st">六方里谁最容易被冤枉？为什么？<em>Who is blamed unfairly?</em></div>
        <div class="lns">{wl(2)}</div>
      </div></div>'''
    def ans_crime(c):
        return f'''
      <div class="ans-hd"><span>✎ 我的裁定 &nbsp;MY VERDICT</span></div>
      <div class="step"><div class="sn">①</div><div class="sb">
        <div class="st">越界了吗？<em>Cross the line?</em></div>
        <div class="chs big">
          <label class="ck"><input type="checkbox"><b>CRIME</b>&nbsp;越界了</label>
          <label class="ck"><input type="checkbox"><b>NO CRIME</b>&nbsp;没越界</label>
        </div>
      </div></div>
      <div class="step"><div class="sn">②</div><div class="sb">
        <div class="st">那条线画在哪儿？<em>Where exactly is the line?</em></div>
        <div class="fill">只要不 <span class="bl"></span>，就算没越界；</div>
        <div class="fill">一旦 <span class="bl"></span>，就算越界。</div>
      </div></div>
      <div class="step"><div class="sn">③</div><div class="sb">
        <div class="st">我的理由 <em>My reason</em></div>
        <div class="lns">{wl(2)}</div>
      </div></div>'''
    def answer_area(c):
        t = c.get('atype', 'generic')
        if t == 'rank': return ans_rank(c)
        if t == 'crime': return ans_crime(c)
        return ans_generic(c)
    def zoom_tier(c):
        w = len(c['en_s']) + len(c['zh_s']) + 300 * len(c['opts']) + len(c['en_q']) + len(c['zh_q'])
        if w > 2500: return 'z3'
        if w > 1900: return 'z2'
        if w > 1600: return 'z1'
        return ''
    def render_card(c):
        cat, color = TAGS[c['tag']]
        tier = zoom_tier(c)
        rows = ''
        if c['opts']:
            rows = ''.join(f'<div class="opt"><span class="ok">{k}</span>'
                           f'<div class="ot"><p class="oe">{e}</p><p class="oz">{z}</p></div></div>'
                           for k, e, z in c['opts'])
            rows = f'<div class="c-opts">{rows}</div>'
        return f'''
    <article class="card {tier}" style="--ac:{color}">
      <div class="c-top"><span class="c-no">№ {c['no']} <i>/ {len(Q)}</i></span>
        <span class="c-brand">AI 时代 · 教育难题 EDUCATION CONUNDRUMS</span>
        <span class="c-cat">{cat}</span></div>
      <h2 class="c-title">{c['zh_t']}<span class="c-en">{c['en_t']}</span></h2>
      <div class="c-mirror">{c.get('mirror','')}</div>
      <div class="c-scen">
        <p class="ce">{c['en_s']}</p>
        <p class="cz">{c['zh_s']}</p>
      </div>
      {rows}
      <div class="c-ask">
        <p class="ce">{c['en_q']}</p>
        <p class="cz">{c['zh_q']}</p>
      </div>
      <div class="c-ans">{answer_area(c)}
      </div>
    </article>'''
    CSS = '''
    :root{--bg:#0f1115;--line:#2c3442;--ink:#23272e;--ink2:#5a6470;
    --en:#3a4250;--zh:#3d434d;--paper:#fdfdfb}
    *{box-sizing:border-box;margin:0;padding:0}
    body{background:var(--bg);font-family:"PingFang SC","Microsoft YaHei","Segoe UI",sans-serif;
      color:#e6e9ef;padding:0 0 90px;-webkit-font-smoothing:antialiased}
    .deck-hd{max-width:860px;margin:0 auto;padding:52px 24px 8px}
    .deck-hd .kick{font-size:12px;letter-spacing:3px;color:#5eb3ff;margin-bottom:14px}
    .deck-hd h1{font-size:30px;letter-spacing:-.5px;line-height:1.35;margin-bottom:14px}
    .deck-hd p{color:#a8b2c1;font-size:14px;line-height:1.9;margin-bottom:8px}
    .deck-hd b{color:#e6e9ef}
    .toolbar{max-width:860px;margin:26px auto 40px;padding:0 24px;display:flex;gap:14px;flex-wrap:wrap}
    .toolbar button{background:#5eb3ff;color:#0f1115;border:none;border-radius:9px;
      padding:11px 26px;font-size:14.5px;font-weight:600;cursor:pointer;font-family:inherit}
    .toolbar button:hover{background:#8cc9ff}
    .toolbar .tip{align-self:center;color:#6f7d90;font-size:12.5px}
    .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(640px,1fr));gap:34px;
      max-width:1400px;margin:0 auto;padding:0 24px}
    .card{background:var(--paper);color:var(--ink);border-radius:16px;
      border-top:6px solid var(--ac);box-shadow:0 10px 34px rgba(0,0,0,.4);
      padding:26px 30px 20px;display:flex;flex-direction:column;min-height:1180px}
    .c-top{display:flex;align-items:center;gap:12px;font-size:11.5px;color:var(--ink2);
      border-bottom:1px solid #e4e1d8;padding-bottom:12px}
    .c-no{font-weight:700;color:var(--ac);font-size:14px}
    .c-no i{font-style:normal;font-weight:400;color:#b3ad9f;font-size:11px}
    .c-brand{flex:1;text-align:center;letter-spacing:2.5px;font-size:10.5px;color:#b3ad9f}
    .c-cat{background:var(--ac);color:#fff;border-radius:999px;padding:2.5px 11px;font-size:11px;letter-spacing:1px}
    .c-title{font-size:24px;font-weight:800;margin:16px 0 4px;letter-spacing:-.3px}
    .c-title .c-en{display:block;font-size:13.5px;font-weight:400;font-style:italic;
      color:#8a8272;font-family:Georgia,serif;margin-top:3px}
    .c-mirror{font-size:11px;color:#a29a86;margin:2px 0 8px;letter-spacing:.5px}
    .c-scen{margin:10px 0 6px}
    .c-scen .ce,.c-ask .ce{font-family:Georgia,"Times New Roman",serif;color:var(--en);
      font-size:13px;line-height:1.62}
    .c-scen .cz,.c-ask .cz{color:var(--zh);font-size:13px;line-height:1.66;margin-top:7px}
    .c-scen .cz b,.c-ask .cz b{color:#1d2129}
    .c-opts{margin:10px 0 4px}
    .opt{display:flex;gap:11px;padding:8px 0;border-top:1px dashed #e4e1d8}
    .opt:first-child{border-top:none}
    .ok{flex:0 0 24px;width:24px;height:24px;border:1.6px solid var(--ac);border-radius:50%;
      display:flex;align-items:center;justify-content:center;font-weight:800;color:var(--ac);
      font-size:12px;margin-top:2px}
    .oz,.oe{font-size:12.6px;line-height:1.5}
    .oe{color:var(--en);font-family:Georgia,serif}
    .oz{color:var(--zh);margin-top:3px}
    .c-ask{margin:10px 0 0;background:#f4f2ea;border-left:4px solid var(--ac);
      border-radius:0 8px 8px 0;padding:12px 16px}
    .c-ask .ce{font-weight:700;font-size:13.5px}
    .c-ans{margin-top:16px;border-top:2px dashed #d8d4c6;padding-top:12px;flex:1;
      display:flex;flex-direction:column}
    .ans-hd{font-size:12px;font-weight:800;color:var(--ac);letter-spacing:2px;margin-bottom:8px}
    .step{display:flex;gap:12px;margin-bottom:13px}
    .sb{flex:1;min-width:0}
    .sn{flex:0 0 26px;width:26px;height:26px;background:#f0ede2;border-radius:8px;
      display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:700;color:var(--ac)}
    .st{font-size:13.5px;font-weight:700;color:#1d2129;margin-bottom:8px}
    .st em{font-style:italic;font-weight:400;color:#9a9484;font-family:Georgia,serif;font-size:11.5px;margin-left:6px}
    .hint{display:inline-block;background:#fff3d6;border:1px solid #e8d48a;color:#8a6d1a;
      border-radius:999px;font-size:10.5px;padding:1px 9px;font-weight:600;vertical-align:2px}
    .chs{display:flex;gap:9px;flex-wrap:wrap}
    .ck{display:inline-flex;align-items:center;gap:6px;border:1.4px solid #c9c3b2;
      border-radius:8px;padding:5px 13px;font-size:13px;color:#333a44;cursor:pointer;
      background:#fff;user-select:none}
    .ck b{color:var(--ac)}
    .ck.big{padding:8px 18px;font-size:14px;border-width:1.8px;font-weight:700}
    .ck:hover{border-color:var(--ac)}
    .lns{margin-left:-68px;margin-right:-30px}
    .lns .ln{height:31px;border-bottom:1px solid #d8d4c6}
    .fill{font-size:13.5px;color:#333a44;margin:7px 0;line-height:2}
    .fill .bl{display:inline-block;width:46%;border-bottom:1px solid #b8b2a2;height:18px}
    .rank .rrow{display:flex;align-items:center;gap:13px;padding:5.5px 0}
    .rbox{flex:0 0 30px;width:30px;height:30px;border:1.6px solid var(--ac);border-radius:7px;background:#fff}
    .rzh{font-size:13.5px;font-weight:700;color:#1d2129;width:64px}
    .ren{font-size:11px;color:#9a9484;letter-spacing:1.5px;font-family:Georgia,serif}
    @media print{
      body{background:#fff;padding:0}
      .deck-hd,.toolbar{display:none}
      .grid{display:block;max-width:none;padding:0;gap:0}
      .card{box-shadow:none;border-radius:0;min-height:0;margin:0 auto;padding:5mm 7mm 4mm;
        page-break-after:always;page-break-inside:avoid;width:100%;zoom:.78}
      .card.z1{zoom:.75}
      .card.z2{zoom:.68}
      .card.z3{zoom:.62}
      .card:last-child{page-break-after:auto}
      .lns .ln{height:27px}
      @page{size:A4 portrait;margin:7mm}
    }
    '''
    deck_head = '''
    <div class="deck-hd">
      <div class="kick">EDUCATION CONUNDRUMS FOR THE AI ERA · 20 CARDS</div>
      <h1>AI 时代 · 教育难题 20 张思考卡</h1>
      <p><b>出题法致敬 Astra Nova Conundrum</b>（无标准答案 · 每个选项都站得住 · 只问"你站哪一边"），情境全部<b>全新原创</b>，聚焦 AI 进入教育后老师、学生、家长、厂商、学校每天真实面对的两难。每张卡标注了它镜像的原题结构，方便对照研究出题套路。</p>
      <p>用法同款：上半中英题目，下半作答区（站队 → 理由 → 替对方说话 → 再决定）。三张特殊版式：14/15 数据之湖为<b>六方排序</b>；16/17/18 为<b>罪案裁定</b>（CRIME or NO CRIME + 线画在哪儿）。</p>
    </div>
    <div class="toolbar">
      <button onclick="window.print()">打印全部 20 张</button>
      <span class="tip">A4 纵向 · 每卡一页 · 适合培训现场发卡讨论</span>
    </div>
    '''
    html = ('<!DOCTYPE html>\n<html lang="zh-CN">\n<head>\n<meta charset="UTF-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
            '<title>AI 时代教育难题 · 20 张思考卡</title>\n<style>' + CSS + '</style>\n</head>\n<body>\n'
            + deck_head + '<div class="grid">' + ''.join(render_card(c) for c in Q)
            + '</div>\n</body>\n</html>')
    html = html.replace('20 CARDS', f'{len(Q)} CARDS').replace('20 张', f'{len(Q)} 张')
    open(OUT, 'w', encoding='utf-8').write(html)
    print('cards:', len(Q), '| size:', len(html))
    for c in Q:
        print(c['no'], c['zh_t'], '|', c.get('atype', 'generic'), '| opts:', len(c['opts']), '| tier:', zoom_tier(c))
if __name__ == "__main__":
    main()
