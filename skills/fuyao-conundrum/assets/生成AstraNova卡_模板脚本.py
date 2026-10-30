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
    parser.add_argument('--output', default='Astra_Nova_43张思考卡片.html', help='输出HTML路径，默认当前目录')
    parser.add_argument('--source', required=True, help='配套中英逐题对照HTML题库路径（不随包附带）')
    args = parser.parse_args()
    if not Path(args.output).parent.exists():
        parser.error('输出目录不存在，请先选择已有目录。')
    import re
    SRC = args.source
    OUT = args.output
    try:
        src = Path(SRC).read_text(encoding='utf-8-sig')
    except (OSError, UnicodeError) as exc:
        parser.error(f'无法读取题库：{exc}')
    parts = src.split('<div class="q-hd">')[1:]
    if len(parts) != 43:
        parser.error(f'题库格式不匹配：应有43个 q-hd 题块，实际{len(parts)}个；请提供配套中英逐题对照HTML。')
    TAGMAP = {'t-ip': ('功劳归属', '#7c5cd6'), 't-eth': ('科技伦理', '#1e9e6a'),
              't-sys': ('规则与责任', '#d97b29'), 't-res': ('资源与取舍', '#2b7cc9'),
              't-log': ('逻辑与推理', '#d94f70'), 't-cri': ('边界判定', '#d9553d')}
    def grab(pat, s, default=''):
        m = re.search(pat, s, re.S)
        return m.group(1).strip() if m else default
    cards = []
    for p in parts:
        body = p.split('<div class="note">')[0]
        no   = grab(r'class="q-no">(.*?)</span>', body)
        zh_t = grab(r'class="q-t">(.*?)</span>', body)
        en_t = grab(r'class="q-en">(.*?)</span>', body)
        tagc = grab(r'class="tag (t-\w+)">', body)
        i_blk = body.find('<div class="blk">')
        i_ask = body.find('<div class="ask">')
        seg = body[i_blk:i_ask] if i_blk >= 0 and i_ask > i_blk else ''
        en_s = grab(r'<div class="en">(.*?)</div>', seg)
        zh_s = grab(r'<div class="zh">(.*?)</div>', seg)
        ask_seg = body[i_ask:] if i_ask >= 0 else ''
        en_q = grab(r'<div class="ask">\s*<div class="en">(.*?)</div>', ask_seg)
        zh_q = grab(r'<div class="zh">(.*?)</div>', ask_seg)
        opts = []
        mt = re.search(r'<table class="opt">(.*?)</table>', body, re.S)
        if mt:
            for k, e, z in re.findall(
                    r'<tr><td class="k">(.*?)</td><td class="e">(.*?)</td><td class="z">(.*?)</td></tr>',
                    mt.group(1), re.S):
                opts.append((k.strip(), e.strip(), z.strip()))
        cards.append(dict(no=no, zh_t=zh_t, en_t=en_t, tagc=tagc,
                          en_s=en_s, zh_s=zh_s, en_q=en_q, zh_q=zh_q, opts=opts))
    # 题库是外部输入，仅保留必要的内联排版标签，丢弃脚本和事件属性。
    class InlineText(HTMLParser):
        def __init__(self):
            super().__init__(convert_charrefs=True)
            self.out = []
        def handle_starttag(self, tag, attrs):
            if tag in ('b', 'i', 'em', 'strong', 'br'):
                self.out.append('<' + tag + '>')
        def handle_endtag(self, tag):
            if tag in ('b', 'i', 'em', 'strong'):
                self.out.append('</' + tag + '>')
        def handle_data(self, data):
            self.out.append(escape(data))
    def inline(value):
        p = InlineText()
        p.feed(value)
        p.close()
        return ''.join(p.out)
    for c in cards:
        for key in ('zh_t', 'en_t', 'en_s', 'zh_s', 'en_q', 'zh_q'):
            c[key] = inline(c[key])
        c['no'] = escape(re.sub('<[^>]+>', '', c['no']), quote=True)
        c['opts'] = [tuple(inline(t) for t in o) for o in c['opts']]
        if not c['no'] or not c['zh_t'] or not c['zh_q']:
            parser.error('存在缺少编号、中文题名或中文提问的题块，请先修复原题库。')
    # ---------- 作答区 ----------
    RANK_ITEMS = [('企业', 'CORPORATION'), ('科学家', 'SCIENTISTS'), ('傀儡师', 'PUPPETMASTER'),
                  ('媒体', 'MEDIA'), ('政客', 'POLITICIANS'), ('选民', 'VOTERS')]
    META = ''  # 姓名日期栏已按用户要求去掉
    def wl(n):  # 写字横线
        return ''.join('<div class="ln"></div>' for _ in range(n))
    def chips_for(c):
        if c['opts']:
            return ''.join(f'<label class="ck"><input type="checkbox"><b>{o[0]}</b></label>'
                           for o in c['opts'])
        return '<label class="ck"><input type="checkbox"><b>A</b></label><label class="ck"><input type="checkbox"><b>B</b></label>'
    def ans_generic(c, dense=False):
        multi = 'three' in c['en_q'].lower()
        hint = '<span class="hint">可多选 / pick 3</span>' if multi else ''
        if dense:
            l3, l2 = 2, 1
        else:
            l3, l2 = (2, 2) if len(c['opts']) >= 5 else (3, 2)
        return f'''
      <div class="ans-hd"><span>✎ 我的思考 &nbsp;MY THINKING</span></div>
      {META}
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
    def ans_rank(c, dense=False):
        first = '责任最大' if c['no'] == '34' else '功劳最大'
        verb  = '最该负责' if c['no'] == '34' else '最该记功'
        rows = ''.join(f'<div class="rrow"><span class="rbox"></span>'
                       f'<span class="rzh">{z}</span><span class="ren">{e}</span></div>'
                       for z, e in RANK_ITEMS)
        step3 = ('' if dense else '''
      <div class="step"><div class="sn">③</div><div class="sb">
        <div class="st">六方里谁最容易被冤枉？为什么？<em>Who is blamed unfairly?</em></div>
        <div class="lns">{wl2}</div>
      </div></div>''').replace('{wl2}', wl(2))
        return f'''
      <div class="ans-hd"><span>✎ 我的排序 &nbsp;MY RANKING</span></div>
      {META}
      <div class="step"><div class="sn">①</div><div class="sb">
        <div class="st">给六方排序：1 = {first}，6 = 最轻 <em>Rank 1–6</em></div>
        <div class="rank">{rows}</div>
      </div></div>
      <div class="step"><div class="sn">②</div><div class="sb">
        <div class="st">为什么第 1 名{verb}？<em>Why #1?</em></div>
        <div class="lns">{wl(2)}</div>
      </div></div>''' + step3
    def ans_crime(c, dense=False):
        reason_lines = 2 if dense else 3
        return f'''
      <div class="ans-hd"><span>✎ 我的裁定 &nbsp;MY VERDICT</span></div>
      {META}
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
        <div class="lns">{wl(reason_lines)}</div>
      </div></div>'''
    def answer_area(c):
        # 依据内容体量选密度：湖泊系列情境很长，罪案系列文本也长
        heavy_scen = len(c['en_s']) + len(c['zh_s'])
        dense = heavy_scen > 1300 or (int(c['no']) in (34, 35))
        if c['no'] in ('34', '35'):
            return ans_rank(c, dense=True)
        if 37 <= int(c['no']) <= 43:
            return ans_crime(c, dense=(heavy_scen > 1500))
        return ans_generic(c, dense=dense)
    # ---------- 卡片 ----------
    def zoom_tier(c):
        """按内容体量估算打印缩放级别，保证一卡一页 A4。"""
        if c['no'] in ('34', '35'):
            return 'z4'
        w = len(c['en_s']) + len(c['zh_s']) + 300 * len(c['opts']) + len(c['en_q']) + len(c['zh_q'])
        if w > 2500: return 'z3'
        if w > 1900: return 'z2'
        if w > 1600: return 'z1'
        return ''
    def render_card(c):
        cat, color = TAGMAP.get(c['tagc'], ('', '#888'))
        tier = zoom_tier(c)
        opts_html = ''
        if c['opts']:
            rows = ''.join(
                f'<div class="opt"><span class="ok">{k}</span>'
                f'<div class="ot"><p class="oe">{e}</p><p class="oz">{z}</p></div></div>'
                for k, e, z in c['opts'])
            opts_html = f'<div class="c-opts">{rows}</div>'
        return f'''
    <article class="card {tier}" style="--ac:{color}" id="card{c['no']}">
      <div class="c-top"><span class="c-no">№ {c['no']} <i>/ {len(cards)}</i></span>
        <span class="c-brand">ASTRA NOVA · CONUNDRUM 思考卡</span>
        <span class="c-cat">{cat}</span></div>
      <h2 class="c-title">{c['zh_t']}<span class="c-en">{c['en_t']}</span></h2>
      <div class="c-scen">
        <p class="ce">{c['en_s']}</p>
        <p class="cz">{c['zh_s']}</p>
      </div>
      {opts_html}
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
    .c-scen{margin:14px 0 6px}
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
    .c-meta{font-size:11.5px;color:var(--ink2);margin-bottom:12px;display:flex;align-items:center}
    .c-meta .w{display:inline-block;width:88px;border-bottom:1px solid #b8b2a2;margin:0 10px 0 4px}
    .c-meta-note{margin-left:auto;color:#b3ad9f;font-size:10.5px;letter-spacing:1px}
    .step{display:flex;gap:12px;margin-bottom:13px}
    .sb{flex:1;min-width:0}  /* 关键：占满步骤行剩余宽度，否则横线只跟标题文字一样宽 */
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
    .lns{margin-left:-68px;margin-right:-30px}  /* 抵消序号圈38px+卡片左右内边距30px，横线直达卡片边缘 */
    .lns .ln{height:31px;border-bottom:1px solid #d8d4c6}
    .fill{font-size:13.5px;color:#333a44;margin:7px 0;line-height:2}
    .fill .bl{display:inline-block;width:46%;border-bottom:1px solid #b8b2a2;height:18px}
    .rank .rrow{display:flex;align-items:center;gap:13px;padding:5.5px 0}
    .rbox{flex:0 0 30px;width:30px;height:30px;border:1.6px solid var(--ac);border-radius:7px;background:#fff}
    .rzh{font-size:13.5px;font-weight:700;color:#1d2129;width:64px}
    .ren{font-size:11px;color:#9a9484;letter-spacing:1.5px;font-family:Georgia,serif}
    .c-src{font-size:9.8px;color:#b3ad9f;margin-top:auto;padding-top:14px;letter-spacing:.3px}
    @media print{
      body{background:#fff;padding:0}
      .deck-hd,.toolbar{display:none}
      .grid{display:block;max-width:none;padding:0;gap:0}
      .card{box-shadow:none;border-radius:0;min-height:0;margin:0 auto;padding:5mm 7mm 4mm;
        page-break-after:always;page-break-inside:avoid;width:100%;zoom:.78}
      .card.z1{zoom:.75}
      .card.z2{zoom:.68}
      .card.z3{zoom:.62}
      .card.z4{zoom:.53}
      .card:last-child{page-break-after:auto}
      .lns .ln{height:27px}
      @page{size:A4 portrait;margin:7mm}
    }
    '''
    deck_head = '''
    <div class="deck-hd">
      <div class="kick">ASTRA NOVA SCHOOL · CONUNDRUM THINKING CARDS</div>
      <h1>43 张开放难题思考卡</h1>
      <p>每张卡片一题：<b>上半部分</b>是英文原题 + 中文译文（情境、选项、提问，逐段对照）；<b>下半部分</b>是思考作答区——站队、写理由、听反方、再决定。</p>
      <p>卡片按六大主题配色：紫=功劳归属 · 绿=科技伦理 · 橙=规则与责任 · 蓝=资源与取舍 · 粉=逻辑与推理 · 红=边界判定。湖泊系列（34/35）为排序题版式，罪案系列（37–43）为裁定题版式。</p>
    </div>
    <div class="toolbar">
      <button onclick="window.print()">打印全部 43 张</button>
      <span class="tip">打印设置：A4 纵向 · 边距"默认"即可 · 建议双面打印后对折使用</span>
    </div>
    '''
    html = ('<!DOCTYPE html>\n<html lang="zh-CN">\n<head>\n<meta charset="UTF-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
            '<title>Astra Nova · 43 张思考卡（可打印）</title>\n<style>' + CSS + '</style>\n</head>\n<body>\n'
            + deck_head + '<div class="grid">' + ''.join(render_card(c) for c in cards)
            + '</div>\n</body>\n</html>')
    open(OUT, 'w', encoding='utf-8').write(html)
    print('cards:', len(cards), '| size:', len(html))
    for c in cards:
        print(c['no'], c['zh_t'], '| opts:', len(c['opts']), '| ans:',
              'rank' if c['no'] in ('34', '35') else ('crime' if int(c['no']) >= 37 else 'generic'))
if __name__ == "__main__":
    main()
