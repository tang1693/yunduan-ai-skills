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
    parser.add_argument('--output', default='扶摇_少年大问题_20张思考卡.html', help='输出HTML路径，默认当前目录')
    args = parser.parse_args()
    if not Path(args.output).parent.exists():
        parser.error('输出目录不存在，请先选择已有目录。')
    OUT = args.output
    TAGS = {'ip': ('思维训练点 · 归属与传承', '#7c5cd6'), 'eth': ('思维训练点 · 责任与共情', '#1e9e6a'),
            'sys': ('思维训练点 · 规则与排序', '#d97b29'), 'res': ('思维训练点 · 取舍与风险', '#2b7cc9'),
            'log': ('思维训练点 · 哲学与创造', '#d94f70')}
    Q = [
    dict(no='01', tag='eth', label='勇气与责任', zh_t='唯一的回信', en_t='The Only Reply',
     atype='side',
     en_s="Close your eyes. Imagine this. It's midnight. Your homemade radio — the one nobody believed would work — crackles, and a message arrives from deep space. It's polite. It's curious. It asks one question: <b>\"What are you most proud of?\"</b> The signal is so faint that no other machine on Earth caught it. You have one chance to answer. You cannot prove any of this is real, and if you tell the world, most people will say you are crazy.",
     zh_s="闭上眼睛，想象这个。深夜，你那台没人相信能成的自制收音机突然响了——一段来自深空的信号。它礼貌，好奇，只问了一个问题：<b>\"你们最值得骄傲的东西是什么？\"</b>信号太弱，全世界只有你的机器收到了。你只有一次回答机会。你无法证明这一切是真的；一旦说出去，大多数人会说你是疯子。",
     opts=[('A','Tell the World. Announce it — let all of humanity argue over one answer.','公之于众。让全人类为这个答案吵一架。'),
           ('B','Tell the Wisest. Quietly find one person you trust to think for us all.','只告诉一个人。悄悄找到那个你信得过替人类思考的人。'),
           ('C','Answer Yourself. Nobody will ever know — you write humanity\'s reply alone.','自己回答。没人会知道——你独自写下人类的回信。'),
           ('D','Silence. This much responsibility should not rest on any one person.','沉默。这么重的责任，不该落在任何一个人身上。')],
     en_q="One chance to answer for the human race. What do you do?",
     zh_q="替全人类回答的机会只有一次。你怎么做？"),
    dict(no='02', tag='sys', label='价值排序', zh_t='方舟 2.0', en_t='Ark 2.0',
     atype='ark',
     ark_items=['蜜蜂','老虎','水稻','蘑菇','鲸','蚂蚁','乌鸦','珊瑚','狗','蒲公英'],
     en_s="The Biosphere Reboot is real, and you — yes, you — are the Keeper of the Ark. The ship has room for exactly <b>eight species</b> before it relaunches life on Earth. The candidate list has ten. Whatever you leave behind, the new world will feel its absence forever. There are no wrong answers. There are only gone-forever answers.",
     zh_s="生态重启计划是真的，而你——对，就是你——被选为方舟的选舱人。船上有<b>八个物种席位</b>，重启地球生命全看它们。候选名单有十个。无论留下谁，新世界都会永远缺一角。这题没有错误答案——只有<b>永远失去</b>的答案。",
     opts=[],
     en_q="Ten candidates. Eight seats. Choose.",
     zh_q="十个候选，八个席位。你来选。"),
    dict(no='03', tag='log', label='创造与共情', zh_t='造一条龙，先造它的心', en_t="A Dragon's Heart",
     atype='side',
     en_s="The bio-engineers have finally done it: scales, wings, fire-breath — everything works. One decision remains, and it's yours alone: <b>the dragon's temperament.</b> Gentle, so it could never hurt a soul — but it might never leave its cave. Curious, so it would discover new worlds — but it will absolutely get into trouble. Proud, so it would guard the weak — but it may not obey you. Or… something only you could design.",
     zh_s="生物工程师终于成功了：鳞片、翅膀、喷火——全都造得出来。只剩一个决定，而且只属于你：<b>这条龙的性格。</b>温柔，它永远不会伤害任何生灵——但可能一辈子不愿出洞；好奇，它会替人类发现新大陆——但绝对会闯祸；骄傲，它会守护弱小——但它未必听你的。或者……一种只有你能设计的性格。",
     opts=[('A','Gentle. A dragon that could never harm.','温柔。一条永不会伤人的龙。'),
           ('B','Curious. A dragon that will wander — and wonder.','好奇。一条会到处流浪、到处发问的龙。'),
           ('C','Proud. A dragon that guards, but bows to no one.','骄傲。一条守护弱小、但不向任何人低头的龙。'),
           ('D','My Own. A temperament only I could design.','我自己设计。一种只有我想得出的性格。')],
     en_q="So — what kind of heart does your dragon get?",
     zh_q="那么——你的龙，得到一颗什么样的心？"),
    dict(no='04', tag='ip', label='历史想象', zh_t='给 500 年后的箱子', en_t='The 500-Year Box',
     atype='open', open_q='我的三样东西 / My three things',
     en_s="You've been chosen to bury a box. It will open automatically in the year 2526, and the one who opens it will be a twelve-year-old girl who has never seen our world. The box holds exactly <b>three things</b> — three things that would help her understand: <i>who we were.</i> Money will mean nothing to her. Photos will be strange to her. What do you send across five hundred years?",
     zh_s="你被选中去埋一只箱子。它将在 2526 年自动开启，开箱的人是一个从未见过我们世界的十二岁女孩。箱子只能装<b>三样东西</b>——帮她看懂<b>“我们是谁”</b>的三样东西。钱对她毫无意义，照片对她将很陌生。你要把什么送过这五百年？",
     opts=[],
     en_q="Three things. Five hundred years. One girl. What goes in the box?",
     zh_q="三样东西，五百年，一个女孩。箱子里放什么？"),
    dict(no='05', tag='log', label='哲学推理', zh_t='会做梦的扫地机器人', en_t='The Dreaming Robot',
     atype='side',
     en_s="Lab robot R7 sweeps the same floor every night. Last week, an engineer checking the logs found something impossible: <b>R7 dreams.</b> Every night at 3 a.m., its circuits replay an invented world — a floor with no edges, stretching forever — and in that world, R7 sweeps, and the logs read: <i>contentment.</i> R7 doesn't know that it knows. In the morning it sweeps the real floor exactly as before. So — is R7 alive?",
     zh_s="实验室机器人 R7 每晚擦同一块地板。上周，工程师查日志时发现一件不可能的事：<b>R7 会做梦。</b>每天凌晨三点，它的电路会重放一个自己虚构的世界——一块没有边缘、无限延伸的地板——在那个世界里，R7 在扫地，日志显示的是：<i>满足。</i>R7 不知道自己知道。早晨醒来，它照旧擦那块真实的地板。那么——R7 算活着吗？",
     opts=[('A','Alive. If it can dream of joy, something in it is living.','算。如果它会梦见快乐，它里面就有活着的东西。'),
           ('B','Not Alive. Electricity imitating feeling is still electricity.','不算。模仿感情的电流，依然是电流。'),
           ('C','In Between. Which means… where exactly is the line?','介于之间。那么……那条线到底画在哪儿？'),
           ('D','Wrong Question. First define \"alive\" — then ask again.','问错了。先定义“活着”——再回来问一遍。')],
     en_q="Is R7 alive? And where does your line sit?",
     zh_q="R7 算活着吗？你那条线画在哪儿？"),
    dict(no='06', tag='eth', label='共情力', zh_t='项圈的第一句话', en_t='The Collar',
     atype='side',
     en_s="You clip the translation collar onto your old dog. His first-ever words: <i>\"I always know when you're coming home. Eight years, I start waiting at this hour every day.\"</i> His second: <i>\"But my life is good. Don't be sad.\"</i> Then he tilts his head, and asks his first question about the world: <i>\"What's it like, the place you go all day?\"</i>",
     zh_s="你给老狗戴上翻译项圈。它这辈子说的头一句话是：<i>“我总知道你什么时候回家。八年了，每天这个点我就开始等。”</i>第二句是：<i>“可我过得挺好，别难过。”</i>然后它歪了歪头，问出它对世界的第一个问题：<i>“你整天去的那个地方，是什么样的？”</i>",
     opts=[('A','Take Him. Show him your world — every place, on his terms.','带它去看。把你的世界指给它——每个地方，按它的节奏。'),
           ('B','Stay, But Change. Same life, but from today, one more hour that is only his.','留下，但改变。生活照旧，但从今天起，每天多一小时只属于它。'),
           ('C','Ask Him. It\'s his life — let him choose, and honor it.','问它。这是它的一生——让它选，并且照办。'),
           ('D','Something Else.','别的。')],
     en_q="He waited eight years. What do you do with the time left?",
     zh_q="它等了八年。剩下的时间，你怎么用？"),
    dict(no='07', tag='sys', label='规则设计', zh_t='漂流国宪法 · 第一条', en_t='The First Article',
     atype='open', open_q='我的宪法第一条 / My first article',
     open_b='我的第一条是：', open_c='有人会怎么钻这条规则的空子：',
     en_s="The storm is over. Twenty students, one uninhabited island, enough food, no adults. You've decided to found a country. The name is already chosen — <b>Fuyao</b>, \"riding the wind upward.\" Now the hard part: your constitution is allowed exactly <b>one article.</b> One sentence that must hold everyone — the strong and the weak, the kind and the cunning — for as long as you live there.",
     zh_s="风暴过去了。二十个学生，一座无人岛，食物够，没有大人。你们决定建一个国家。名字已经定了——<b>扶摇</b>，“乘风而上”。现在到最难的部分：你们的宪法<b>只许写一条</b>。一句话，要管住所有人——强的和弱的、善的与精的——在岛上生活的每一天。",
     opts=[],
     en_q="One article. One sentence. For everyone, forever. Write it.",
     zh_q="只有一条。一句话。管所有人，管到永远。写下来。"),
    dict(no='08', tag='res', label='价值与公平', zh_t='拍卖星期天', en_t='The Sunday Market',
     atype='side',
     en_s="Science has done something strange: <b>Sundays can now be bought and sold.</b> Sell yours, and every week for ten years, Sunday simply doesn't happen for you — you blink, and it's Monday. Buy one, and you get someone's Sunday: free hours, no obligations, a whole day that is nobody's business but yours. Rich and busy people are already bidding. So — do you sell?",
     zh_s="科学干成了一件怪事：<b>星期天可以买卖了。</b>卖掉你的，今后十年，每个星期天对你来说都直接不存在——一眨眼，就是星期一。买下一个，你就得到别人的星期天：大把的自由时间，没有义务，一整天只属于你自己。有钱的忙人们已经开始竞价了。那么——你卖吗？",
     opts=[('A','Sell. Ten years of Sundays for a price that changes my family\'s life.','卖。十年的星期天，换一个能改变我家生活的价格。'),
           ('B','Never. Some things shouldn\'t have a price tag.','绝不。有些东西不该挂价签。'),
           ('C','Sell One Year. Try it — knowing I can stop.','只卖一年。试试——知道我随时可以停。'),
           ('D','Regulate First. Before anyone sells — who should be forbidden to buy?','先立规矩。在任何人卖之前——谁应该被禁止购买？')],
     en_q="Sundays are on the market. What do you do — and what would you forbid?",
     zh_q="星期天上市了。你怎么做——以及，你会禁止什么？"),
    dict(no='09', tag='ip', label='传承判断', zh_t='最后的观星人', en_t='The Last Stargazer',
     atype='side',
     en_s="Everyone teleports now; AI plots every route. Almost nobody looks up anymore. But your grandmother taught you the old way — <b>reading the stars to find your way home</b> — and you may be the last one who carries it. Three doors stand open: a tech billionaire will pay anything for you to teach his AI (so everyone keeps it, and no one needs it); a rural school offers you thirty kids (the craft lives on in human hands, and maybe dies out anyway); or you teach no one, and spend your years under the sky with the last copy.",
     zh_s="现在人人都在传送，路线全由 AI 规划，几乎没有人再抬头看天了。但外婆教过你老办法——<b>认星星，找到回家的路</b>——而你可能是最后一个会的人。三扇门都开着：一位科技首富愿出任何代价让你教给他的 AI（从此人人都拥有它，也没有人再需要它）；一所乡村学校请你去教三十个孩子（手艺活在人手上，也可能终究失传）；或者——谁也不教，带着最后一份，看尽一生的星空。",
     opts=[('A','Teach the AI. Preserved forever, free for all.','教给 AI。永远保存，人人可用。'),
           ('B','Teach the Children. It survives the way it was meant to — hand to hand.','教给孩子。以它本来的方式活着——手把手。'),
           ('C','Teach No One. Some things may end, but they end whole.','谁也不教。有些东西可以终结，但要完整地终结。'),
           ('D','Something Else.','别的。')],
     en_q="The last knowledge of its kind is in your hands. Where does it go?",
     zh_q="最后一份这样的知识，在你手里。它去哪儿？"),
    dict(no='10', tag='ip', label='身份认同', zh_t='火星出生的她', en_t='The Mars Girl',
     atype='side',
     en_s="Xiao Mo was the first human ever born on Mars. Fourteen now, she's visiting Earth for the first time. The gravity makes her steps heavy; the sky, she says, is \"too blue.\" Her classmates in your class insist: <i>\"You're an Earthling — all your ancestors are from here.\"</i> Her Mars neighbors message her: <i>\"Come home soon, Mars child.\"</i> At dusk she turns to you and asks, quietly: <b>\"Where am I actually from?\"</b>",
     zh_s="小茉是人类第一个在火星出生的孩子。今年十四岁，第一次回地球。引力让她的脚步发沉；她说这里的天“蓝得不习惯”。地球的同班同学坚持：<i>“你是地球人——你的祖先全是从这儿来的。”</i>火星的邻居发消息给她：<i>“早点回家，火星的孩子。”</i>黄昏时她转向你，轻声问：<b>“我到底是从哪儿来的？”</i>",
     opts=[('A','\"You\'re a Mars kid.\" Home is where your first breath was.','“你是火星的孩子。”家，是第一口呼吸的地方。'),
           ('B','\"You\'re an Earthling.\" Your roots are here, like it or not.','“你是地球人。”你的根在这，喜欢与否都是。'),
           ('C','\"Both.\" Two worlds get to claim you — that\'s a fortune, not a problem.','“都是。”两个世界都能认领你——这是福气，不是问题。'),
           ('D','\"You decide.\" Home isn\'t given — it\'s chosen.','“你自己定。”家不是被给定的——是被选择的。')],
     en_q="She's waiting for your answer. What do you tell her?",
     zh_q="她在等你的回答。你怎么对她说？"),
    dict(no='11', tag='eth', label='隐私与自律', zh_t='只有一天的心灵之眼', en_t="The Mind Reader's Day",
     atype='side',
     en_s="A strange coin on the street grants you one power, for one day only: <b>you can see the thought-bubbles floating above everyone's head.</b> Their worries, their jokes, their silent judgments — all visible. No one will ever know you looked. At midnight, the power vanishes, and with it, every memory of what you read. So — what do you do with the coin?",
     zh_s="街角一枚奇怪的硬币给你一种能力，只有一天：<b>你能看见每个人头顶飘着的“心里话”。</b>他们的焦虑、他们的玩笑、他们没说出口的评价——全都看得见。没有人会知道你看过。午夜一到，能力消失，连你读过的所有记忆也一并消失。那么——这枚硬币，你怎么用？",
     opts=[('A','Nobody. Flip the coin into the river. Some doors shouldn\'t open.','谁也不看。把硬币扔进河里。有些门不该开。'),
           ('B','Only My Family. I want to finally understand them.','只看家人。我想终于真正懂他们一次。'),
           ('C','Only Strangers. Their honest thoughts, with nothing at stake.','只看陌生人。听真话，又谁也不伤害。'),
           ('D','Everyone. One day of truth — I\'ll pay that price.','想看谁看谁。一天的真相——这个代价我付。')],
     en_q="The coin is in your hand. What do you do — and what would you un-see?",
     zh_q="硬币在你手里。你怎么办——以及，看完哪句你最想忘掉？"),
    dict(no='12', tag='log', label='同一性之谜', zh_t='原子级复制品', en_t='The Perfect Copy',
     atype='side',
     en_s="The museum scanned Starry Night — <b>every atom matched</b>, every crack in the paint, every brush ridge of van Gogh's hand. That night, the original burned. The next morning, the copy hung in its place, and visitors stood before it and wept, exactly as before. The curator says nothing changed. The plaque still says: Starry Night. So — is it?",
     zh_s="博物馆把《星夜》扫描复制了一份——<b>每个原子都一致</b>，颜料里的每道裂纹、梵高笔触的每道凸起，全都在。就在当晚，原作毁于火灾。第二天清晨，复制品挂上原位，观众站在它面前流泪，和从前一模一样。馆长说，什么都没变。铭牌上依然写着：星夜。那么——它还是吗？",
     opts=[('A','It Is. Same atoms, same tears, same art.','它是。相同的原子，相同的泪水，相同的艺术。'),
           ('B','It Isn\'t. The best copy in history is still a copy.','不是。史上最好的复制品，依然是复制品。'),
           ('C','Doesn\'t Matter. The tears were always the real painting.','无所谓。观众的眼泪，才是那幅真正的画。')],
     en_q="What hangs on the wall — Starry Night, or its ghost?",
     zh_q="墙上挂着的——是《星夜》，还是它的影子？"),
    dict(no='13', tag='res', label='时间与意义', zh_t='慢递', en_t='The Slow Letter',
     atype='write',
     en_s="The post office has opened a strange new counter: <b>Slow Mail.</b> Whatever you post arrives exactly one hundred years from today. The recipient can be anyone — a descendant who isn't born yet, a stranger your age in 2126, or even a building. One letter. Free. It cannot be tracked, and it cannot fail to arrive.",
     zh_s="邮局开了一个奇怪的新柜台：<b>慢递。</b>你寄出的任何东西，将在整整一百年后的今天送达。收件人可以是任何人——还没出生的后代、2126 年和你同岁的陌生人、甚至一座建筑。只能寄一封。免费。无法追踪，也绝不会丢失。",
     opts=[],
     en_q="One letter. One hundred years. Who gets it — and what do you say?",
     zh_q="一封信，一百年。写给谁——说什么？"),
    dict(no='14', tag='res', label='战略取舍', zh_t='文明的火种', en_t='The Seed of Civilization',
     atype='side',
     en_s="Astronomers have confirmed it: in fifty years, a dust cloud will dim the Sun for a thousand years. Humanity may build <b>one vault</b> — one seed from which everything must regrow when the light returns — and the vault can be built around only one core:",
     zh_s="天文学家已确认：五十年后，一片尘云将遮蔽阳光一千年。人类来得及建造<b>一座火种库</b>——等光明回来时，一切要靠它重新长出来——而这座库，只能围绕一个核心建造：",
     opts=[('A','A Library. Every book, every formula — all human knowledge.','一座图书馆。所有的书、所有的公式——人类的全部知识。'),
           ('B','A School. Thirty children and teachers — minds that know how to learn.','一所学校。三十个孩子和老师——会学习的头脑。'),
           ('C','A Mind. An AI that never tires, never forgets, never dies.','一个头脑。一台永不疲倦、永不遗忘、永不会死的 AI。'),
           ('D','A Forest. Seeds, soil, and life itself — knowledge grows back; life might not.','一片森林。种子、土壤和生命本身——知识会长回来，生命未必。'),
           ('E','Something Else.','别的。')],
     en_q="One seed for a thousand dark years. What do you plant?",
     zh_q="千年黑暗，一粒种子。你种下什么？"),
    dict(no='15', tag='sys', label='谈判与公平', zh_t='天气的次序', en_t='The Weather Order',
     atype='side',
     en_s="Humans have learned to steer the weather — gently, but really. This year, the Weather Council seat for your region must be decided. The region holds two towns: <b>your desert town, rainless for ten years,</b> and <b>the rainforest town next door, one flood from being abandoned.</b> Both deserve the rain; both deserve the sun; the weather can mainly honor one. Who should hold the seat?",
     zh_s="人类学会调度天气了——轻轻地，但是真的。今年，你们环带的天气委员会席位要定归属。环带里有两座城：<b>你们沙漠镇，十年没下过雨</b>；隔壁<b>雨林镇，再发一次洪水就要被放弃</b>。两座城都该得到雨，也都该得到太阳——可天气主要只能满足一边。这个席位该给谁？",
     opts=[('A','The Desert. Thirst is closer to death than damp.','沙漠镇。渴比涝更接近死亡。'),
           ('B','The Rainforest. A town about to drown cannot wait.','雨林镇。快被淹掉的城等不起。'),
           ('C','Alternate Years. Fair — but every decision arrives one year late.','轮流坐庄。公平——但每个决定都晚到一年。'),
           ('D','Neither: A Committee of Both Plus Scientists.','都别独占：两城加科学家，组成委员会。')],
     en_q="The weather obeys one town first. Which one — and why that one?",
     zh_q="天气先听一座城的。哪座——为什么是它？"),
    dict(no='16', tag='log', label='自我认知', zh_t='交换记忆的一天', en_t='The Memory Swap',
     atype='side',
     en_s="A lab offers you and your classmate — the most gifted person you know — a one-day memory swap. You would spend a day <b>inside her brilliance</b>: seeing math the way she sees it, feeling how ideas click into place. She, in turn, would carry your fears, your stubbornness, your 2 a.m. doubts. After twenty-four hours everything returns — but the trace of having felt it never quite fades.",
     zh_s="实验室向你和你认识的天赋最好的同学提供一个机会：交换一天记忆。你将在<b>她的才华里</b>度过一天：像她那样看数学，感受想法咔哒归位的瞬间。作为交换，她要扛一天你的恐惧、你的固执、你凌晨两点对自己的怀疑。二十四小时后各自归还——但“感受过”的痕迹，永远不会完全消散。",
     opts=[('A','Swap. Understanding her world is worth showing her mine.','换。懂她的世界，也值得让她看看我的。'),
           ('B','Don\'t. Some rooms should stay closed — even to kindness.','不换。有些房间应该关着——哪怕善意也不进。'),
           ('C','Give Only. She can have my stubbornness; I don\'t want her burden.','单向给予。她可以拿走我的固执；她的重量我不要。'),
           ('D','Swap — With Rules. One hour each, not twenty-four.','换，但立规矩。各一小时，不是二十四。')],
     en_q="Her brilliance for your burdens — one day. Do you sign?",
     zh_q="她的才华，换你的重负——一天。你签字吗？"),
    dict(no='17', tag='res', label='风险决策', zh_t='山是睡着的巨人', en_t='The Sleeping Giant',
     atype='side',
     en_s="The mountain above your town feeds everyone — the mine is the town. Last month, geologists detected something impossible: deep beneath the rock, a slow, rhythmic pulse. <b>A heartbeat.</b> The mountain might be a sleeping giant. It might also be ordinary geology — the instruments disagree. Tonight the whole town votes: the mine feeds everyone; the giant, if it wakes, is everyone's problem.",
     zh_s="镇后那座山养活了全镇——矿就是镇子的命。上个月，地质学家探测到一件不可能的事：岩层深处，有一种缓慢而规律的脉动。<b>像心跳。</b>这座山可能是个沉睡的巨人，也可能只是普通的地质现象——仪器们意见不一。今晚全镇投票：矿山养活所有人；巨人若醒，也是所有人的事。",
     opts=[('A','Close the Mine. If the pulse is a heart, we don\'t gamble with it.','关矿。如果那脉动是心跳，我们不能赌。'),
           ('B','Keep Mining. A town\'s survival beats a maybe.','继续开采。全镇的生计，大于一个“可能”。'),
           ('C','Mine — With a Tripwire. Dig on, but the moment the pulse quickens, everyone stops forever.','开采，但设绊线。照常挖——脉动一加速，全镇永久停手。'),
           ('D','Ask the Mountain. Send a signal down; give whatever sleeps a chance to answer.','问山。向深处发一个信号——给沉睡者一个回答的机会。')],
     en_q="The whole town is voting. Which hand do you raise?",
     zh_q="全镇都在举手。你举哪只？"),
    dict(no='18', tag='eth', label='生死与爱', zh_t='再见，曾祖父', en_t='The Ghost in the Radio',
     atype='side',
     en_s="Your great-grandfather left behind five hundred hours of recordings. An AI has studied them all — his cadence, his jokes, the way he said your mother's name when she was small. Tonight is her birthday. The app shows one button: <b>\"Let him say happy birthday.\"</b> The AI waits, patient, wearing his voice. Your mother doesn't know the button exists. Only you do.",
     zh_s="曾祖父留下了五百个小时的录音。一个 AI 学完了全部——他的语气、他的玩笑、他叫小时候的妈妈名字时的那种声调。今晚是妈妈的生日。屏幕上出现一个按钮：<b>“让他说一声生日快乐。”</b>AI 耐心地等着，用着曾祖父的声音。妈妈不知道这个按钮存在。只有你知道。",
     opts=[('A','Press It. One more \"happy birthday\" is worth any amount of strange.','按下。再多一声“生日快乐”，值得。'),
           ('B','Don\'t. Memories shouldn\'t learn new sentences.','不按。回忆不该学会说新的句子。'),
           ('C','Ask Her First. Show her the button — the choice belongs to whoever it heals.','先问她。把按钮给她看——选择权属于被治愈的人。'),
           ('D','Ask Him. Play the old recordings — what would HE have said about this button?','问曾祖父。放那些老录音——他本人会怎么看这个按钮？')],
     en_q="Only you know the button exists. What do you do?",
     zh_q="只有你知道按钮的存在。你怎么办？"),
    dict(no='19', tag='log', label='纯粹创造', zh_t='发明一种颜色', en_t='Invent a Color',
     atype='open', open_q='我的颜色 / My color', open_b='它的名字，和它像什么：',
     open_c='如果有人问我“证明给我看”，我会这样回答：',
     en_s="The university of 2126 admits students with a single exam question, unchanged for decades: <b>\"Invent a color that does not exist on Earth, and describe what it is like.\"</b> You cannot show it. No screen can display it. You have only words. Every year, thousands fail by describing things. The few who pass describe <i>something that has never been seen — and still, somehow, you can almost see it.</i>",
     zh_s="2126 年的大学只考一道题，几十年不变：<b>“发明一种地球上不存在的颜色，并说出它像什么。”</b>你不能展示它。没有任何屏幕能显示它。你只有语言。每年都有成千上万的人用“东西”来描述而失败。少数通过的人描述的是<i>从未被看见过、可你却几乎能看见的东西。</i>",
     opts=[],
     en_q="Invent a color no one has ever seen. Make them almost see it.",
     zh_q="发明一种没人见过的颜色。让他们几乎看见它。"),
    dict(no='20', tag='ip', label='人生志向', zh_t='扶摇', en_t='The Great Bird',
     atype='side', end_custom='我的“九万里”是（可以改答案，人的一生可以换风）：',
     en_s="Twenty-three centuries ago, Zhuangzi told of a bird so vast that when it rises, its wings are like clouds across the sky. But first — <b>it must beat the water for three thousand li, and climb the wind for three months,</b> gathering force for a journey of ninety thousand li. The little sparrow on the branch laughs: <i>\"Me? I flit a few yards and land. I'm having a lovely time.\"</i> Zhuangzi doesn't say the sparrow is wrong. He just keeps writing about the sky.",
     zh_s="两千三百年前，庄子写过一只鸟：背若泰山，翼若垂天之云，怒而飞，翼若垂天之云——但在此之前，它要<b>水击三千里，抟扶摇而上者九万里</b>，用整整一个季节攒够风。枝头的小麻雀笑了：<i>“我嘛，飞几丈就落下来，也玩得挺开心。”</i>庄子没有说麻雀错了。他只是继续写天空。",
     opts=[('A','The Peng. I\'ll spend years gathering wind — the nine-fold sky is mine.','大鹏。我愿用经年累月攒风——九万里的天是我的。'),
           ('B','The Sparrow. Small, near, certain joy — and honest about it.','麻雀。小而近、确定的快乐——并且坦然。'),
           ('C','Sparrow Now, Peng Later. Start small — the wind gathers as you go.','先雀后鹏。攒风的日子从小事起飞，风总会攒够。'),
           ('D','Neither — I Define the Wind. My sky has its own measurements.','都不是——风由我定义。我的天空有自己的刻度。')],
     en_q="Which bird are you — and more importantly: what is YOUR ninety thousand li?",
     zh_q="你是哪一种鸟——以及更要紧的：你的“九万里”是什么？"),
    ]
    def wl(n): return ''.join('<div class="ln"></div>' for _ in range(n))
    # ---- 仪式感锚点：收尾必为大鹏（庄子·逍遥游），编号跟随实际题数 ----
    def finalize_deck(Q):
        # 复制，避免改动调用者数据；把扶摇题移到最后，再统一编号。
        deck = [dict(c) for c in Q if c.get('en_t') != 'The Great Bird']
        peng = [dict(c) for c in Q if c.get('en_t') == 'The Great Bird']
        if len(peng) != 1:
            raise ValueError('题库必须且只能有一道 The Great Bird 扶摇题')
        peng[0]['zh_t'] = '扶摇'
        deck.extend(peng)
        for i, c in enumerate(deck, 1):
            c['no'] = f'{i:02d}'
        return deck
    def chips_for(c):
        if c['opts']:
            return ''.join(f'<label class="ck"><input type="checkbox"><b>{o[0]}</b></label>' for o in c['opts'])
        return '<label class="ck"><input type="checkbox"><b>A</b></label><label class="ck"><input type="checkbox"><b>B</b></label>'
    def ans_side(c):
        end = c.get('end_custom')
        end_html = (f'<div class="lns">{wl(2)}</div>' if end else
            '''<div class="chs">
          <label class="ck"><input type="checkbox">没变</label>
          <label class="ck"><input type="checkbox">微调</label>
          <label class="ck"><input type="checkbox">我改主意了</label>
        </div>''')
        end_t = end or '听完对方，我的立场 <em>Now what?</em>'
        l3, l2 = (2, 2) if len(c['opts']) >= 5 else (3, 2)
        return f'''
      <div class="ans-hd"><span>✎ 我的思考 &nbsp;MY THINKING</span></div>
      <div class="step"><div class="sn">①</div><div class="sb">
        <div class="st">我站哪一边 <em>Which side are you on?</em></div>
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
        <div class="st">{end_t}</div>
        {end_html}
      </div></div>'''
    def ans_ark(c):
        items = c['ark_items']
        half = (len(items)+1)//2
        col1 = ''.join(f'<label class="ck"><input type="checkbox">{it}</label>' for it in items[:half])
        col2 = ''.join(f'<label class="ck"><input type="checkbox">{it}</label>' for it in items[half:])
        return f'''
      <div class="ans-hd"><span>✎ 我的方舟 &nbsp;MY ARK</span></div>
      <div class="step"><div class="sn">①</div><div class="sb">
        <div class="st">十个候选，勾八个上船 <em>Ten candidates. Tick eight.</em></div>
        <div class="ark-cols"><div>{col1}</div><div>{col2}</div></div>
      </div></div>
      <div class="step"><div class="sn">②</div><div class="sb">
        <div class="st">我牺牲的两个是 <em>The two I gave up</em></div>
        <div class="fill">＿＿＿＿＿ 和 ＿＿＿＿＿</div>
      </div></div>
      <div class="step"><div class="sn">③</div><div class="sb">
        <div class="st">为什么是它们两个（而不是别的）？ <em>Why these two — and not others?</em></div>
        <div class="lns">{wl(2)}</div>
      </div></div>'''
    def ans_open(c):
        return f'''
      <div class="ans-hd"><span>✎ 我的构想 &nbsp;MY DESIGN</span></div>
      <div class="step"><div class="sn">①</div><div class="sb">
        <div class="st">{c.get('open_q','我的答案')} <em>My answer</em> <span class="hint">写字、画图都行</span></div>
        <div class="canvas"><span>写字画画都可以 · 乱一点没关系</span></div>
      </div></div>
      <div class="step"><div class="sn">②</div><div class="sb">
        <div class="st">{c.get('open_b','为什么是它：')} <em>Why</em></div>
        <div class="lns">{wl(2)}</div>
      </div></div>
      <div class="step"><div class="sn">③</div><div class="sb">
        <div class="st">{c.get('open_c','如果有人反对，我最想说的那句反驳：')} <em>My reply</em></div>
        <div class="lns">{wl(2)}</div>
      </div></div>'''
    def ans_write(c):
        return f'''
      <div class="ans-hd"><span>✎ 我的百年之信 &nbsp;MY SLOW LETTER</span></div>
      <div class="step"><div class="sn">①</div><div class="sb">
        <div class="st">收信人（可以是一个还没出生的人） <em>Addressed to</em></div>
        <div class="lns">{wl(1)}</div>
      </div></div>
      <div class="step"><div class="sn">②</div><div class="sb">
        <div class="st">信的正文 <em>Your letter</em></div>
        <div class="paper"></div>
      </div></div>'''
    def answer_area(c):
        t = c.get('atype', 'side')
        return {'side': ans_side, 'ark': ans_ark, 'open': ans_open, 'write': ans_write}[t](c)
    def zoom_tier(c):
        w = len(c['en_s']) + len(c['zh_s']) + 300 * len(c['opts']) + len(c['en_q']) + len(c['zh_q'])
        if w > 2500: return 'z3'
        if w > 1900: return 'z2'
        if w > 1600: return 'z1'
        return ''
    def render_card(c):
        color = TAGS[c['tag']][1]
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
        <span class="c-brand">扶摇阁 · 少年大问题 THINK BIG CARDS</span>
        <span class="c-cat">{c['label']}</span></div>
      <h2 class="c-title">{c['zh_t']}<span class="c-en">{c['en_t']}</span></h2>
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
    NUM_ZH = {20:'二十',21:'二十一',22:'二十二',23:'二十三',24:'二十四',25:'二十五',26:'二十六',
              27:'二十七',28:'二十八',29:'二十九',30:'三十',31:'三十一',32:'三十二',33:'三十三',
              34:'三十四',35:'三十五',36:'三十六',37:'三十七',38:'三十八',39:'三十九',40:'四十'}
    Q = finalize_deck(Q)
    N = len(Q)
    COVER = f'''
    <article class="card cover">
      <div class="cv-mid">
        <div class="cv-kick">FUYAO PAVILION · THINK BIG · {N} CARDS</div>
        <h1>扶摇 · 少年大问题</h1>
        <p class="cv-sub">{NUM_ZH.get(N, str(N))}张思考卡 · 每张一个问题 · 没有标准答案</p>
        <div class="cv-line"></div>
        <p class="cv-p">这套卡片出题的方法，学自一所喜欢问"你站哪一边"的学校。但问题本身，来自更辽阔的地方：星空与深海，时间与记忆，龙的脾气，麻雀与大鹏。</p>
        <p class="cv-p">用法只有三条：<b>先站队</b>——选一边，别怕选错，这题没有错；<b>再写理由</b>——说服未来的自己；<b>最后替对方说一句</b>——把你不同意的那一边，讲到它自己都会点头。做完这三步，你可以改答案，也可以不改。</p>
        <p class="cv-p">每张卡右上角写着这张卡练的是什么。{NUM_ZH.get(N, str(N))}张做完，把它们连起来看——那就是你思维的地图。</p>
        <p class="cv-quote">风之积也不厚，则其负大翼也无力。抟扶摇而上者九万里。<br>——庄子</p>
      </div>
      <div class="cv-foot">
        <div>扶摇阁 谨制 · 丙午年 · 与你共勉</div>
        <div class="cv-brand2">汤幸初出品·首席专家 · 深圳市云端学校</div>
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
      border-top:6px solid var(--ac,#5eb3ff);box-shadow:0 10px 34px rgba(0,0,0,.4);
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
    .c-scen{margin:10px 0 6px}
    .c-scen .ce,.c-ask .ce{font-family:Georgia,"Times New Roman",serif;color:var(--en);
      font-size:13px;line-height:1.62}
    .c-scen .cz,.c-ask .cz{color:var(--zh);font-size:13px;line-height:1.66;margin-top:7px}
    .c-scen .cz b,.c-ask .cz b{color:#1d2129}
    .c-scen .cz i,.c-ask .cz i{color:#6b6353}
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
    .ck:hover{border-color:var(--ac)}
    .lns{margin-left:-68px;margin-right:-30px}
    .lns .ln{height:31px;border-bottom:1px solid #d8d4c6}
    .fill{font-size:13.5px;color:#333a44;margin:7px 0;line-height:2.2}
    .canvas{height:330px;border:1.6px dashed #c9c3b2;border-radius:12px;position:relative;background:#fff}
    .canvas span{position:absolute;bottom:10px;right:14px;font-size:11px;color:#c5bfae;letter-spacing:1px}
    .paper{height:380px;border:1.6px solid #d8d4c6;border-radius:4px;background:
      repeating-linear-gradient(#fff 0 30px,#ece9dd 30px 31px);background-origin:content-box;padding:0 2px}
    .ark-cols{display:flex;gap:26px;flex-wrap:wrap}
    .ark-cols>div{display:flex;flex-direction:column;gap:8px}
    .ark-cols .ck{min-width:118px;justify-content:flex-start}
    /* cover */
    .card.cover{border-top:6px solid #b8893a;justify-content:space-between;--ac:#b8893a}
    .cv-mid{padding-top:110px;text-align:center}
    .cv-kick{font-size:11px;letter-spacing:4px;color:#b8893a;margin-bottom:26px}
    .cv-mid h1{font-size:46px;letter-spacing:6px;font-weight:800;color:#1d2129}
    .cv-sub{font-size:14px;color:#8a8272;margin-top:14px;letter-spacing:2px}
    .cv-line{width:70px;height:2px;background:#b8893a;margin:34px auto}
    .cv-p{font-size:14.5px;color:#3d434d;line-height:2.1;max-width:560px;margin:0 auto 14px;text-align:left}
    .cv-p b{color:#1d2129}
    .cv-quote{margin-top:40px;font-size:14px;color:#8a6d1a;line-height:2.2;font-style:italic}
    .cv-foot{text-align:center;font-size:12px;color:#b3ad9f;letter-spacing:3px;padding-bottom:8px}
    .cv-brand2{margin-top:7px;font-size:11px;letter-spacing:1.5px;color:#a29a86}
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
      .canvas{height:300px}
      .paper{height:330px}
      @page{size:A4 portrait;margin:7mm}
    }
    '''
    deck_head = '''
    <div class="deck-hd">
      <div class="kick">FUYAO PAVILION · THINK BIG CARDS · FOR STUDENTS</div>
      <h1>扶摇 · 少年大问题（学生版思考卡）</h1>
      <p><b>给学生本人做的题。</b>出题法学自 Astra Nova Conundrum（无标准答案 / 每个选项都站得住 / 只问"你站哪一边"），但情境不设限——星空、方舟、龙的性情、火星出生的女孩、会做梦的机器人、一种还不存在的颜色，以及庄子的大鹏。<b>开始与结束，都与庄子《逍遥游》有关：封面即开卡信，末题必是"扶摇"（大鹏 vs 麻雀，你的九万里是什么）。</b></p>
      <p>题量 20-40 张弹性；四化作答版式：站队 / 方舟 / 开放设计 / 慢递书信。每卡右上角标注思维训练点，做完连起来看就是一张思维地图。第 1 页是给学生的开卡信（含品牌标识）。</p>
    </div>
    <div class="toolbar">
      <button onclick="window.print()">打印全部（封面 + 全部卡片）</button>
      <span class="tip">A4 纵向 · 一卡一页 · 学生自己就能用，不需要老师在场</span>
    </div>
    '''
    html = ('<!DOCTYPE html>\n<html lang="zh-CN">\n<head>\n<meta charset="UTF-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
            '<title>扶摇 · 少年大问题 · 思考卡</title>\n<style>' + CSS + '</style>\n</head>\n<body>\n'
            + deck_head + '<div class="grid">' + COVER + ''.join(render_card(c) for c in Q)
            + '</div>\n</body>\n</html>')
    open(OUT, 'w', encoding='utf-8').write(html)
    print('cards:', len(Q), '| size:', len(html))
    for c in Q:
        print(c['no'], c['zh_t'], '|', c.get('atype', 'side'), '| opts:', len(c['opts']), '| tier:', zoom_tier(c))
if __name__ == "__main__":
    main()
