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
    parser.add_argument('--output', default='小云版_少年大问题_样卡3张.html', help='输出HTML路径，默认当前目录')
    args = parser.parse_args()
    if not Path(args.output).parent.exists():
        parser.error('输出目录不存在，请先选择已有目录。')
    OUT = args.output
    Q = [
    dict(no='01', fam='eth', label='会替别人想', zh_t='小狗说话了',
     en_line='"Who taught you to wait?"',
     story='豆豆是你养了八年的小狗。科学家发明了一个神奇的项圈，戴上它，小狗的话你就听得懂了。豆豆说的第一句话是："我每天这个时候就开始等你回家，等了好多年啦。"它歪着头，问你："你白天去的那个地方，是什么样的呀？"你想了想，可以做三件事，但只能选一件——',
     opts=[('A','带豆豆去一次你上学的地方，让它亲眼看一看。'),
           ('B','从今天起，每天多陪它玩一个小时，哪儿也不去。'),
           ('C','什么都不做。它等了八年都过得挺好，不用改变。')],
     ask='你选哪一件？为什么？',
     mirror='母题：责任与共情（高层版 №06 项圈的第一句话）'),
    dict(no='02', fam='res', label='会做取舍', zh_t='带谁上船',
     en_line='"Four places, six kinds of life."',
     story='大洪水要来了，你有一条船，只能带四种生物上船，其他都要留下。候选的有六个：蜜蜂、老虎、水稻、鲸、乌鸦、狗。船开走以后，留下的就再也没有了。六个里面，你只能挑四个——',
     opts=[],
     ark_items=['蜜蜂','老虎','水稻','鲸','乌鸦','狗'],
     ask='带上船的是哪四个？留下的是谁？',
     mirror='母题：取舍与风险（高层版 №02 方舟 2.0）'),
    dict(no='03', fam='log', label='会想奇怪的问题', zh_t='还是原来的小熊吗',
     en_line='"Is it still your bear?"',
     story='你从小抱到大的小熊，棉花塌了，眼睛掉了一颗。奶奶把它拆开，换了全新的棉花，缝了颗新眼睛，还洗得干干净净——看起来就像新买的一样。妈妈说："旧的坏成那样，这就是一只新熊啦。"你抱着它，感觉还是原来那只，又说不上来为什么——',
     opts=[('A','还是原来的小熊——我一直抱着的这只就是它。'),
           ('B','不是了——棉花和眼睛都换成新的，它只是长得一样。'),
           ('C','我说不清，但我觉得这个问题很重要。')],
     ask='你觉得呢？',
     mirror='母题：哲学与创造（高层版 №12 原子级复制品·同一个两千年的老问题）'),
    ]
    def card(c):
        fam_colors = dict(eth='#1e9e6a', res='#2b7cc9', log='#d94f70')
        color = fam_colors[c['fam']]
        if c.get('ark_items'):
            body = f'''
        <div class="st">① 把带上船的圈出来（圈四个）</div>
        <div class="arks">{''.join(f'<span class="ark">{a}</span>' for a in c['ark_items'])}</div>
        <div class="st" style="margin-top:14px">② 留下的两个是谁？为什么是它们？</div>
        <div class="lns">{''.join('<div class="ln"></div>' for _ in range(2))}</div>'''
        else:
            body = f'''
        <div class="st">① 圈出你选的</div>
        <div class="chs">{''.join(f'<span class="ck"><b>{k}</b> {t}</span>' for k, t in c['opts'])}</div>
        <div class="st" style="margin-top:14px">② 为什么？写一句，或画出来</div>
        <div class="canvas"><span>写字画画都可以</span></div>'''
        return f'''
    <article class="card" style="--ac:{color}">
      <div class="c-top"><span class="c-no">№ {c['no']}</span>
        <span class="c-brand">小云学堂 · 大问题卡</span>
        <span class="c-cat">{c['label']}</span></div>
      <h2 class="c-title">{c['zh_t']}<span class="c-en">{c['en_line']}</span></h2>
      <div class="c-story">{c['story']}</div>
      <div class="c-ask">{c['ask']}</div>
      <div class="c-ans">{body}
        <div class="st" style="margin-top:14px">③ 如果你的好朋友选了别的，他可能是怎么想的？</div>
        <div class="lns">{''.join('<div class="ln"></div>' for _ in range(1))}</div>
        <div class="st" style="margin-top:14px">④ 听完他的想法，你的选择——</div>
        <div class="chs sm">
          <span class="ck-face">😊 不变</span><span class="ck-face">🤔 有点动摇</span><span class="ck-face">🔄 我换啦</span>
        </div>
      </div>
      <div class="c-mirror">{c['mirror']}</div>
    </article>'''
    COVER = '''
    <article class="card cover">
      <div class="cv-mid">
        <div class="cv-kick">XIAOYUN · THINK BIG · FOR YOUNG MINDS</div>
        <h1>大问题 · 小思考家</h1>
        <p class="cv-sub">每张卡一个问题 · 没有标准答案</p>
        <div class="cv-line"></div>
        <p class="cv-p">小朋友，这三张卡里没有"正确答案"。<b>圈一圈</b>——选出你的想法，选什么都不算错；<b>写一写或画一画</b>——告诉我们为什么；<b>想一想</b>——如果别人和你选得不一样，他为什么会那样选？想完这三个，你想换答案也可以，不换也可以。</p>
        <p class="cv-quote">北方有一条很大的鱼，它变成大鸟，乘着风飞上九万里的天空。<br>——庄子（两千年前，就有个爱想大问题的人）</p>
      </div>
      <div class="cv-foot">
        <div>小云学堂 谨制 · 丙午年 · 与你共勉</div>
        <div class="cv-brand2">汤幸初出品·首席专家 · 深圳市云端学校</div>
      </div>
    </article>'''
    CSS = '''
    :root{--ink:#23272e;--ink2:#5a6470;--paper:#fdfdfb;--line:#e4e1d8}
    *{box-sizing:border-box;margin:0;padding:0}
    body{background:#0f1115;font-family:"PingFang SC","Microsoft YaHei",sans-serif;color:var(--ink);padding:0 0 60px}
    .hd{max-width:760px;margin:0 auto;padding:44px 22px 6px}
    .hd .kick{font-size:11px;letter-spacing:3px;color:#5eb3ff;margin-bottom:12px}
    .hd h1{font-size:26px;color:#e6e9ef}
    .hd p{color:#a8b2c1;font-size:13.5px;line-height:1.9;margin-top:10px}
    .hd b{color:#e6e9ef}
    .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(620px,1fr));gap:30px;
      max-width:1360px;margin:24px auto 0;padding:0 22px}
    .card{background:var(--paper);border-radius:16px;border-top:6px solid var(--ac);
      box-shadow:0 10px 34px rgba(0,0,0,.4);padding:24px 28px 18px;min-height:1150px;
      display:flex;flex-direction:column}
    .c-top{display:flex;align-items:center;gap:10px;font-size:11px;color:var(--ink2);
      border-bottom:1px solid var(--line);padding-bottom:10px}
    .c-no{font-weight:800;color:var(--ac);font-size:14px}
    .c-brand{flex:1;text-align:center;letter-spacing:2.5px;font-size:10px;color:#b3ad9f}
    .c-cat{background:var(--ac);color:#fff;border-radius:999px;padding:3px 11px;font-size:11px}
    .c-title{font-size:26px;font-weight:800;margin:14px 0 2px}
    .c-title .c-en{display:block;font-size:14px;color:#8a8272;font-family:Georgia,serif;
      font-style:italic;font-weight:400;margin-top:4px}
    .c-story{font-size:16.5px;line-height:2.05;color:#3d434d;margin:14px 0 10px;text-align:justify}
    .c-ask{background:#f4f2ea;border-left:4px solid var(--ac);border-radius:0 10px 10px 0;
      padding:12px 16px;font-size:17px;font-weight:800;color:#1d2129;margin-bottom:16px}
    .c-ans{border-top:2px dashed #d8d4c6;padding-top:14px;flex:1}
    .st{font-size:15px;font-weight:800;color:#1d2129;margin-bottom:9px}
    .chs{display:flex;flex-direction:column;gap:10px}
    .ck{border:1.6px solid #c9c3b2;border-radius:12px;padding:10px 14px;font-size:15px;
      color:#333a44;background:#fff;line-height:1.6}
    .ck b{color:var(--ac);margin-right:6px}
    .chs.sm{flex-direction:row;flex-wrap:wrap}
    .ck-face{border:1.6px solid #c9c3b2;border-radius:999px;padding:8px 18px;font-size:14.5px;background:#fff}
    .canvas{height:300px;border:1.6px dashed #c9c3b2;border-radius:14px;position:relative;background:#fff}
    .canvas span{position:absolute;bottom:10px;right:14px;font-size:12px;color:#c5bfae}
    .lns{margin-left:-40px;margin-right:-26px}
    .lns .ln{height:44px;border-bottom:1.5px solid #d8d4c6}
    .arks{display:flex;gap:12px;flex-wrap:wrap}
    .ark{border:1.8px solid #c9c3b2;border-radius:999px;padding:12px 22px;font-size:17px;background:#fff}
    .c-mirror{font-size:11px;color:#b3ad9f;margin-top:auto;padding-top:14px;letter-spacing:.4px}
    .card.cover{border-top-color:#b8893a;--ac:#b8893a;justify-content:space-between}
    .cv-mid{padding-top:120px;text-align:center}
    .cv-kick{font-size:11px;letter-spacing:4px;color:#b8893a;margin-bottom:24px}
    .cv-mid h1{font-size:44px;letter-spacing:4px;font-weight:800}
    .cv-sub{font-size:14px;color:#8a8272;margin-top:12px;letter-spacing:2px}
    .cv-line{width:66px;height:2px;background:#b8893a;margin:30px auto}
    .cv-p{font-size:15.5px;color:#3d434d;line-height:2.2;max-width:540px;margin:0 auto 12px;text-align:left}
    .cv-p b{color:#1d2129}
    .cv-quote{margin-top:36px;font-size:14.5px;color:#8a6d1a;line-height:2.3}
    .cv-foot{text-align:center;font-size:12px;color:#b3ad9f;letter-spacing:3px;padding-bottom:6px}
    .cv-brand2{margin-top:7px;font-size:11px;letter-spacing:1.5px;color:#a29a86}
    @media print{
      body{background:#fff;padding:0}
      .hd{display:none}
      .grid{display:block;max-width:none;padding:0;gap:0}
      .card{box-shadow:none;border-radius:0;min-height:0;margin:0 auto;
        page-break-after:always;page-break-inside:avoid;width:100%;zoom:.74;padding:6mm 8mm 5mm}
      .card:last-child{page-break-after:auto}
      .lns .ln{height:38px}
      @page{size:A4 portrait;margin:7mm}
    }
    '''
    html = ('<!DOCTYPE html>\n<html lang="zh-CN">\n<head>\n<meta charset="UTF-8">\n'
            '<title>小云版 · 少年大问题 · 样卡</title>\n<style>' + CSS + '</style>\n</head>\n<body>\n'
            '<div class="hd"><div class="kick">XIAOYUN EDITION · AGES 9-11 · PROTOTYPE</div>'
            '<h1>小云版样卡（4-5 年级）</h1>'
            '<p>这是"一题三层"的低海拔证明：与扶摇版<b>同一母题、同一封面锚点（庄子）</b>，但情境换成身边事、选项减到 2-3 个、作答改为圈一圈+画写+一句换位思考，英文只留一句点睛。三张样卡分别对应高层版的 №06 项圈 / №02 方舟 / №12 复制品。</p></div>\n'
            '<div class="grid">' + COVER + ''.join(card(c) for c in Q) + '</div>\n</body>\n</html>')
    open(OUT, 'w', encoding='utf-8').write(html)
    print('OK', len(html))
if __name__ == "__main__":
    main()
