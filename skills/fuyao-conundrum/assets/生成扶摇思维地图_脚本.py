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
    parser.add_argument('--output', default='扶摇_思维地图_样张.html', help='输出HTML路径，默认当前目录')
    args = parser.parse_args()
    if not Path(args.output).parent.exists():
        parser.error('输出目录不存在，请先选择已有目录。')
    OUT = args.output
    # ============ 数据区（示例：小鲲，12 张卡） ============
    STUDENT = dict(name='小鲲', term='丙午年 · 秋', done=12, total=24)
    # 卡号, 五族(见FAMILY), 中文题名, 所站立场, 立场变化(没变/微调/改主意), 理由字数, 替对方金句(可选)
    CARDS = [
     ('01','eth','唯一的回信','C','没变',14,None),
     ('02','res','方舟 2.0','—','没变',22,'我砍掉的是乌鸦。它聪明，可它离了谁都能活。'),
     ('03','log','造龙先造心','D','没变',18,None),
     ('05','log','会做梦的 R7','D','改主意',31,'「它不知道自己知道」——我原来没想过，我们也不知道自己不知道。'),
     ('06','eth','项圈的第一句话','C','没变',26,None),
     ('09','ip','最后的观星人','B','没变',24,None),
     ('10','ip','火星出生的她','D','微调',29,'两个世界认领一个孩子，不是分裂，是双份的家。'),
     ('12','log','原子级复制品','C','没变',27,None),
     ('14','res','文明的火种','B','微调',33,'知识可以重新长出来，但要知道怎么长——所以学校里要有图书馆员。'),
     ('17','res','山是睡着的巨人','C','没变',35,None),
     ('18','eth','再见，曾祖父','C','微调',38,'回忆不该学会新的句子——可如果是她自己在等这句话呢？'),
     ('20','ip','扶摇','C','没变',41,'麻雀不是错了，它只是不需要九万里的风。'),
    ]
    CLASS = dict(
     name='扶摇阁 · 全班 10 人概览', done_avg=11.4,
     heat=[  # 五族 × (改主意率, 平均理由字数)
       ('归属与传承','ip',0.18,26),('责任与共情','eth',0.22,29),
       ('规则与排序','sys',0.15,24),('取舍与风险','res',0.31,32),('哲学与创造','log',0.27,30)],
     quotes=[  # 全班金句（匿名）
       ('05·会做梦的 R7','它不知道自己知道——我们也不知道自己不知道。'),
       ('02·方舟 2.0','珊瑚没有脚，它逃不了，所以只能靠我们带上船。'),
       ('20·扶摇','我的九万里是：让怕的事变成会做的事。'),
     ])
    # 仅使用去标识课堂记录；输入文字按文本转义，不执行HTML。
    STUDENT = {k: escape(str(v)) if isinstance(v, str) else v for k, v in STUDENT.items()}
    CARDS = [tuple(escape(str(v)) if isinstance(v, str) else v for v in c) for c in CARDS]
    if any(len(c) != 7 or not isinstance(c[5], (int, float)) or c[5] < 0 for c in CARDS):
        parser.error('CARDS每项须有7个字段，理由字数须为非负数。')
    STUDENT['done'] = len(CARDS)
    CLASS['name'] = escape(str(CLASS['name']))
    CLASS['quotes'] = [(escape(str(a)), escape(str(b))) for a, b in CLASS['quotes']]
    CLASS['heat'] = [(escape(str(n)), k, max(0, min(float(r), 1)), max(0, float(w))) for n, k, r, w in CLASS['heat']]
    FAMILY = dict(ip=('归属与传承','#7c5cd6'), eth=('责任与共情','#1e9e6a'),
                  sys=('规则与排序','#d97b29'), res=('取舍与风险','#2b7cc9'),
                  log=('哲学与创造','#d94f70'))
    CHG = {'没变':('·','#b3ad9f'), '微调':('◐','#c98f2b'), '改主意':('↻','#c0392b')}
    def chip(c):
        no, fam, title, stance, chg, words, q = c
        fname, color = FAMILY[fam]
        mark, mcolor = CHG.get(chg, ('·','#b3ad9f'))
        q_html = f'<div class="q">“{q}”</div>' if q else ''
        return f'''<div class="chip" style="--ac:{color}">
      <div class="ch-top"><span class="ch-no">№{no}</span><span class="ch-chg" style="color:{mcolor}">{mark} {chg}</span></div>
      <div class="ch-title">{title}</div>
      <div class="ch-row"><span class="ch-stance">站 {stance}</span><span class="ch-fam">{fname}</span></div>
      <div class="ch-bar"><i style="width:{min(words*2.2,100)}%"></i></div>
      <div class="ch-words">理由 {words} 字</div>
      {q_html}
    </div>'''
    def heat_row(h):
        name, key, rate, words = h
        _, color = FAMILY[key]
        return f'''<div class="hrow" style="--ac:{color}">
      <span class="hname">{name}</span>
      <div class="hbar"><i style="width:{min(rate*100*2.6,100):.0f}%"></i><b>{rate*100:.0f}%</b></div>
      <span class="hwords">均 {words} 字</span>
    </div>'''
    chips = ''.join(chip(c) for c in CARDS)
    q_picks = [c for c in CARDS if c[6]][:3]
    quotes_html = ''.join(f'<div class="pick"><span class="p-no">№{c[0]} · {c[2]}</span><p>“{c[6]}”</p></div>' for c in q_picks)
    heat_html = ''.join(heat_row(h) for h in CLASS['heat'])
    class_quotes = ''.join(f'<div class="pick sm"><span class="p-no">{a}</span><p>“{b}”</p></div>' for a, b in CLASS['quotes'])
    words_series = [c[5] for c in CARDS]
    wmax = max(max(words_series, default=0), 1)
    spark = ''.join(f'<i style="height:{w/wmax*100:.0f}%"></i>' for w in words_series)
    chg_count = sum(1 for c in CARDS if c[4] != '没变')
    CSS = '''
    :root{--ink:#23272e;--ink2:#5a6470;--paper:#fdfdfb;--line:#e4e1d8}
    *{box-sizing:border-box;margin:0;padding:0}
    body{background:#0f1115;font-family:"PingFang SC","Microsoft YaHei",sans-serif;color:var(--ink);padding:24px}
    .page{background:var(--paper);width:210mm;min-height:297mm;margin:0 auto 26px;
      border-radius:14px;padding:14mm 13mm;box-shadow:0 10px 34px rgba(0,0,0,.4)}
    .kick{font-size:10.5px;letter-spacing:3px;color:#b8893a;margin-bottom:8px}
    h1{font-size:25px;letter-spacing:1px}
    .sub{font-size:12px;color:#8a8272;margin-top:4px}
    .hd{display:flex;justify-content:space-between;align-items:flex-end;
      border-bottom:2px solid #1d2129;padding-bottom:10px;margin-bottom:16px}
    .hd-r{text-align:right;font-size:12px;color:var(--ink2);line-height:1.8}
    .hd-r b{color:#1d2129;font-size:15px}
    .sec-t{font-size:13px;font-weight:800;letter-spacing:2px;color:#1d2129;margin:18px 0 10px;
      display:flex;align-items:center;gap:8px}
    .sec-t::after{content:"";flex:1;height:1px;background:var(--line)}
    .chips{display:grid;grid-template-columns:repeat(4,1fr);gap:9px}
    .chip{border:1px solid var(--line);border-top:3.5px solid var(--ac);border-radius:9px;
      padding:8px 10px 7px;background:#fff}
    .ch-top{display:flex;justify-content:space-between;font-size:9.5px;color:#a29a86}
    .ch-chg{font-weight:700}
    .ch-title{font-size:12.5px;font-weight:700;margin:3px 0 4px}
    .ch-row{display:flex;justify-content:space-between;font-size:10px;color:var(--ink2)}
    .ch-stance{color:var(--ac);font-weight:800}
    .ch-fam{font-size:9px;letter-spacing:.5px}
    .ch-bar{height:3.5px;background:#f0ede2;border-radius:2px;margin-top:6px;overflow:hidden}
    .ch-bar i{display:block;height:100%;background:var(--ac)}
    .ch-words{font-size:8.8px;color:#b3ad9f;margin-top:3px}
    .chip .q{font-size:9.5px;color:#6b6353;line-height:1.55;margin-top:6px;
      border-top:1px dashed var(--line);padding-top:5px}
    .row2{display:grid;grid-template-columns:1.15fr 1fr;gap:18px;margin-top:4px}
    .spark{display:flex;align-items:flex-end;gap:5px;height:88px;padding:0 2px}
    .spark i{flex:1;background:linear-gradient(180deg,#b8893a,#e0c089);border-radius:2px 2px 0 0;min-height:4%}
    .spark-lb{display:flex;gap:5px;font-size:8.5px;color:#b3ad9f;margin-top:4px}
    .spark-lb span{flex:1;text-align:center}
    .stat{font-size:11.5px;color:var(--ink2);line-height:2.1}
    .stat b{color:#1d2129;font-size:13px}
    .pick{border-left:3px solid #b8893a;padding:4px 0 4px 12px;margin-bottom:9px}
    .pick .p-no{font-size:9.5px;color:#a29a86;letter-spacing:1px}
    .pick p{font-size:12.5px;line-height:1.7;color:#3d434d;margin-top:2px}
    .pick.sm p{font-size:11.5px}
    .ask{background:#f4f2ea;border-radius:10px;padding:12px 16px}
    .ask li{font-size:12px;color:#3d434d;margin:6px 0 6px 16px;line-height:1.7}
    .note{font-size:9.5px;color:#b3ad9f;margin-top:14px;text-align:center;letter-spacing:1px}
    /* 班级页 */
    .hrow{display:flex;align-items:center;gap:12px;margin-bottom:9px}
    .hname{width:88px;font-size:11.5px;font-weight:700;color:#1d2129}
    .hbar{flex:1;height:14px;background:#f0ede2;border-radius:7px;position:relative;overflow:hidden}
    .hbar i{display:block;height:100%;background:var(--ac);border-radius:7px 0 0 7px}
    .hbar b{position:absolute;right:8px;top:-1px;font-size:10px;color:#1d2129}
    .hwords{font-size:10px;color:#8a8272;width:64px;text-align:right}
    @media print{
      body{background:#fff;padding:0}
      .page{box-shadow:none;border-radius:0;margin:0;width:100%;min-height:0;
        page-break-after:always;page-break-inside:avoid;padding:11mm 12mm;zoom:.88}
      .page:last-child{page-break-after:auto}
      @page{size:A4 portrait;margin:0}
    }
    '''
    page1 = f'''
    <div class="page">
      <p class="note">虚构样张：班级统计为独立示例，未从个人记录推算；请替换为真实、去标识且经核对的数据。只记录当次任务与支持条件，不形成学生画像。</p><div class="kick">FUYAO PAVILION · THINKING MAP</div>
      <div class="hd">
        <div><h1>{STUDENT['name']} 的思维地图</h1>
          <p class="sub">{STUDENT['term']} · 扶摇 · 少年大问题</p></div>
        <div class="hd-r">完成 <b>{STUDENT['done']}</b> / {STUDENT['total']} 张<br>
          立场流动 <b>{chg_count}</b> 次（微调+改主意）</div>
      </div>
      <div class="sec-t">航线 · {len(CARDS)}张卡，按时间排列</div>
      <div class="chips">{chips}</div>
      <p class="sub" style="margin-top:8px">顶色=思维训练五族（紫=归属与传承 绿=责任与共情 橙=规则与排序 蓝=取舍与风险 粉=哲学与创造）· ◐=微调 ↻=改主意 · 条=理由字数</p>
      <div class="row2">
        <div>
          <div class="sec-t">理由 · 越写越长，还是越写越具体</div>
          <div class="spark">{spark}</div>
          <div class="spark-lb">{''.join(f'<span>{c[0]}</span>' for c in CARDS)}</div>
          <p class="sub" style="margin-top:6px">从 {words_series[0] if words_series else '—'} 字到 {words_series[-1] if words_series else '—'} 字。字数不是重点，具体才是——看看最早的理由，再看看最后一条。</p>
        </div>
        <div>
          <div class="sec-t">这一程 · 只看实际记录</div>
          <p class="stat">
          实际记录：<b>{len(CARDS)}</b> 张卡<br>
          记有立场修改：<b>{chg_count}</b> 次（不代表能力高低）<br>
          原话摘录：<b>{len(q_picks)}</b> 条（不自动评选最佳）</p>
        </div>
      </div>
      <div class="sec-t">你的原话 · 摘了三句</div>
      {quotes_html}
      <div class="sec-t">下一叠 · 三个问题（没有答案，只有问题）</div>
      <div class="ask"><ol>
        <li>你在哪一类题上最容易改主意？是理由被说服的，还是听懂对面之后？</li>
        <li>选一张自己保留原看法的卡：当时依据是什么？现在是否还需要补充？没有这样的记录就跳过。</li>
        <li>下一叠卡里，你最想挑战哪一族？（写在这里：＿＿＿＿＿＿＿＿＿＿）</li>
      </ol></div>
      <p class="note">这张地图不是分数，是镜子——它只描述你思维的航迹，不评判你站过的任何一边。</p>
      <p class="note" style="margin-top:4px">扶摇阁 谨制 · 汤幸初出品·首席专家 · 深圳市云端学校</p>
    </div>'''
    page2 = f'''
    <div class="page">
      <p class="note">班级统计与金句均为虚构演示，非学生真实表现或教育效果证据。</p><div class="kick">FUYAO PAVILION · CLASS OVERVIEW</div>
      <div class="hd">
        <div><h1>班级思维总览</h1><p class="sub">{CLASS['name']} · 教师页（学生页人手一份，此页不留档）</p></div>
        <div class="hd-r">人均完成 <b>{CLASS['done_avg']}</b> 张</div>
      </div>
      <div class="sec-t">五族热力 · 谁在哪类题上流动</div>
      <p class="sub">条=该族"改主意率"（微调+改主意 ÷ 该族完成数）。<b>流动不是优点的代名词，不流动也不是缺点</b>——这页只帮你决定下次课从哪族开卡。</p>
      <div style="margin-top:12px">{heat_html}</div>
      <div class="sec-t">全班的金句 · 匿名</div>
      {class_quotes}
      <div class="sec-t">给教师的三句话</div>
      <div class="ask"><ol>
        <li>结合原话和课堂情境选择下次题目；不从改主意率推断学生勇气、能力或性格。</li>
        <li>把全班金句读给学生听（匿名）——供学生比较理由；是否采用由教师判断。</li>
        <li>地图发下去后，只问一句："哪一处你自己都没想到？"</li>
      </ol></div>
      <p class="note">扶摇阁 谨制 · 汤幸初出品·首席专家 · 深圳市云端学校</p>
    </div>'''
    html = ('<!DOCTYPE html>\n<html lang="zh-CN">\n<head>\n<meta charset="UTF-8">\n'
            '<title>扶摇 · 思维地图样张</title>\n<style>' + CSS + '</style>\n</head>\n<body>\n'
            + page1 + page2 + '\n</body>\n</html>')
    open(OUT, 'w', encoding='utf-8').write(html)
    print('OK, size:', len(html))
if __name__ == "__main__":
    main()
