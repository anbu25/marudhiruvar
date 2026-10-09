# -*- coding: utf-8 -*-
import os
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)
src=open(os.path.join(HERE,'gen2.py'),encoding='utf-8').read()
exec(compile(src.split("page1=f'''")[0],'g2pre','exec'))
exec(compile(open(os.path.join(HERE,'mapgen.py'),encoding='utf-8').read(),'mapgen','exec'))
svg_main, svg_inset = main, inset
EXTRA3 = '''
    .row2 .mapcard { flex: 1.1; display: flex; flex-direction: column; }
    .mapcard .mainmap { flex: 1.45; min-height: 0; width: 100%; }
    .mapcard .inset { flex: 1; min-height: 0; width: 100%; border: 1.5px solid var(--gold); border-radius: 8px; margin-top: 6px; }
    .seabg { fill: #0f2a3a; } .parchment .seabg { fill: #cfe0dc; }
    .zoombox { fill: none; stroke: #ffd56b; stroke-width: 1.6; stroke-dasharray: 4 2; } .parchment .zoombox { stroke: #8a2418; }
    .mlabel.cap { font-weight: 800; } .mlabel.small { font-size: 7px; font-style: italic; }
    .inset .mlabel { font-size: 11px; } .inset .mlabel.cap { font-size: 13px; }
    .inset .route { stroke-width: 3; }
    .mdot.star { fill: #ffd56b; } .mdot.hy { fill: #7fd0ff; }
    .arrfill4 { fill: #ff4d4d; } .arrfill5 { fill: #6ee7b7; } .parchment .arrfill4 { fill: #b3120a; } .parchment .arrfill5 { fill: #1b7a55; }
    .parchment .arrfill { fill: #c01f12; } .parchment .arrfill2 { fill: #8a2418; }
    .row2 .legend { margin-top: 5px; }
'''
def chapH(num,yr,title,en,ta):
    return f"""<div class="card chapter"><div class="medal"><div class="num">{num}</div><div class="yr">{yr}</div></div>
 <div class="ch-body"><div class="ch-title">{title}</div><div class="ch-en">{en}</div><div class="ch-ta">{ta}</div></div></div>"""
svg_main=svg_main.replace('class="map"','class="map mainmap"')
page1=f'''<div class="poster-container p1">
 {head("MARUDHIRUVAR • TWO BROTHERS, ONE QUEEN, ONE FIGHT FOR FREEDOM","PART I • 1730–1780 • FALL AND RISE")}
 <div class="trio">
  {trio('p','PERIYA MARUTHU','பெரிய மருது','The Commander: a fearless warrior who protects Sivaganga.','வீரமிகு படைத்தளபதி; சிவகங்கையின் காவலர்.')}
  {trio('c','CHINNA MARUTHU','சின்ன மருது','The Strategist: a clever leader who unites the rulers.','அரசர்களை ஒன்றிணைத்த போர்வியூக வல்லுநர்.')}
  {trio('v','QUEEN VELU NACHIYAR','ராணி வேலு நாச்சியார்','The Queen and their ally: refuses to give up her kingdom.','அவர்களின் தலைவி; நாட்டை மீட்கும் உறுதி கொண்ட வீரமங்கை.','object-position:25% top')}
 </div>
 <div class="col">
 {chapH(1,'1730–72','The Heroes Rise','Periya Maruthu, a master of the Valari, and Chinna Maruthu, a sharp strategist, rise as loyal, fearless officers of Sivaganga. Velu Nachiyar, princess of Ramnad, is born in 1730, trains in Silambam, archery and horse riding, and marries King Muthu Vaduganathar of Sivaganga.','வளரி வீரர் பெரிய மருதுவும் போர்வியூக வல்லுநர் சின்ன மருதுவும் சிவகங்கையின் விசுவாசமிக்க, அஞ்சா வீரர்களாக உயர்ந்தனர். 1730-இல் பிறந்த இராமநாதபுர இளவரசி வேலு நாச்சியார் சிலம்பம், வில், குதிரையேற்றம் பயின்று, சிவகங்கை மன்னர் முத்து வடுகநாதரை மணந்தார்.')}
 {chapH(2,'1772','Betrayal at Kalaiyar Koil','The British East India Company joins the Nawab of Arcot and attacks Sivaganga. King Muthu Vaduganathar is killed in battle. Queen Velu Nachiyar escapes with her daughter Vellachi, vowing to win her kingdom back.','கிழக்கிந்தியக் கம்பெனி, ஆர்க்காடு நவாபுடன் கூட்டுச் சேர்ந்து சிவகங்கையைத் தாக்கியது. போரில் மன்னர் வீரமரணம் அடைந்தார். ராணி வேலு நாச்சியார் மகள் வெள்ளச்சியுடன் தப்பி, நாட்டை மீட்க உறுதி ஏற்றார்.')}
{chapH(3,'1772–80','Exile and an Ally','The Maruthu brothers guard the hiding queen and gather loyal supporters across the Sivaganga region. At Virupachi, Hyder Ali of Mysore shelters her and supplies soldiers and arms. For eight years the brothers rally fighters while she builds her army and her alliances.','மருது சகோதரர்கள் காடுகளில் மறைந்த ராணியைக் காத்து, சிவகங்கைப் பகுதியில் விசுவாசிகளைத் திரட்டினர். விருப்பாட்சியில் மைசூர் ஹைதர் அலி அடைக்கலமும் படை, ஆயுத உதவியும் அளித்தார். எட்டு ஆண்டுகள் சகோதரர்கள் வீரர்களைத் திரட்ட, ராணி படையையும் கூட்டணிகளையும் வலுப்படுத்தினார்.')}
{chapH(4,'1780','Sivaganga Is Won Back','The Maruthu brothers fight at the queen’s side as she strikes with Kuyili’s Women’s Army (Udaiyaal Padai). Legend says Kuyili gave her life to destroy the British weapons store. Sivaganga is free, and the brothers become her trusted ministers and commanders.','குயிலியின் "உடையாள் படை"யுடன் ராணி தாக்க, மருது சகோதரர்கள் அவருடன் நின்று போராடினர். ஆயுதக் கிடங்கை அழிக்க குயிலி உயிர்த்தியாகம் செய்ததாகக் கூறப்படுகிறது. சிவகங்கை மீண்டது; சகோதரர்கள் அமைச்சர்களும் தளபதிகளும் ஆனார்கள்.')}
 </div>
 {FOOT}
</div>'''
def node(av,y,e,t):
    imgs=''.join(f'<div class="av"><img src="{IMG[k]}" alt="" style="{"object-position:25% top" if k=="v" else ""}"></div>' for k in av[:1])
    return f'<div class="tl-node">{imgs}<div class="y">{y}</div><div class="e">{e}</div><div class="t">{t}</div></div>'
page2=f'''<div class="poster-container">
 {head("MARUDHIRUVAR • TWO BROTHERS, ONE QUEEN, ONE FIGHT FOR FREEDOM","PART II • 1780–1801 • GUARDIANS OF A KINGDOM")}
 <div class="row2">
  <div class="card mapcard"><div class="card-title">THE MAP OF THE STRUGGLE</div><div class="card-title-ta">போராட்டத்தின் வரைபடம்</div>
   {svg_main}
   <div class="legend"><span class="l5"><i></i>Nawab + British</span><span class="l3"><i></i>Help from Mysore</span><span class="l6"><i></i>Oomaithurai 1801</span></div>
   {svg_inset}
   <div class="legend"><span class="l1"><i></i>Escape 1772</span><span class="l2"><i></i>Return 1780</span></div>
   <div class="note">Tamil Nadu, simplified outline. Distances approximate.</div></div>
  <div class="col">
   {chapH(5,'1780–96','Guardians of Sivaganga','Periya Maruthu leads the army and Chinna Maruthu guides the government, building forts, temples and tanks. After the queen passes in 1796, they keep guarding Sivaganga with her daughter Vellachi and stand with Veerapandiya Kattabomman against the British.','பெரிய மருது படையையும் சின்ன மருது ஆட்சியையும் வழிநடத்தி, கோட்டை, கோயில், குளங்களை அமைத்தனர். 1796-இல் ராணி மறைந்த பின்னும் மகள் வெள்ளச்சியுடன் சிவகங்கையைக் காத்து, வீரபாண்டிய கட்டபொம்மனுடன் ஆங்கிலேயரை எதிர்த்தனர்.')}
   {chapH(6,'1799–1801','Refuge and Rebellion','After Kattabomman is hanged in 1799, his brother Oomaithurai escapes from prison in 1801 and finds refuge in Sivaganga. The brothers refuse to give him up and issue the Jambudvipa Proclamation, calling all to unite against the British. War follows.','1799-இல் கட்டபொம்மன் தூக்கிலிடப்பட்ட பின், அவர் தம்பி ஊமைத்துரை 1801-இல் சிறையிலிருந்து தப்பி சிவகங்கையில் அடைக்கலம் பெற்றார். அவரை ஒப்படைக்க மறுத்த சகோதரர்கள் அனைவரும் ஒன்றுபட "ஜம்புத் தீவு பிரகடனம்" வெளியிட்டனர். போர் மூண்டது.')}
   {chapH(7,'Oct 1801','The Last Stand','Fighting on from the forests of Kalaiyar Koil against a far larger force, the brothers are captured. For sheltering Oomaithurai and defying the British, they are hanged at Thiruppathur with many followers. Their sacrifice still inspires Tamil Nadu.','காளையார்கோவில் காடுகளிலிருந்து மிகப் பெரிய படையை எதிர்த்துப் போராடிய சகோதரர்கள் பிடிபட்டனர். ஊமைத்துரைக்கு அடைக்கலம் அளித்து ஆங்கிலேயரை எதிர்த்ததற்காக, பலருடன் திருப்பத்தூரில் தூக்கிலிடப்பட்டனர். அவர்களின் தியாகம் இன்றும் தமிழகத்துக்கு ஊக்கமளிக்கிறது.')}
  </div>
 </div>
 <div class="card timeline"><div class="card-title">TIMELINE OF COURAGE</div>
  <div class="tl">
   {node('v','1730','Velu Nachiyar born; later weds the King','வேலு நாச்சியார் பிறப்பு; மணம்')}
   {node('v','1772','King killed at Kalaiyar Koil; queen escapes','காளையார்கோவில் போர்')}
   {node('c','1772–80','Exile; Hyder Ali shelters the queen','விருப்பாட்சி அடைக்கலம்')}
   {node('v','1780','Sivaganga won back with Kuyili’s army','சிவகங்கை மீட்பு')}
   {node('p','1796','Queen passes; brothers guard Sivaganga','ராணி மறைவு')}
   {node('c','1799','Kattabomman hanged','கட்டபொம்மன் தியாகம்')}
   {node('c','1801','Oomaithurai’s refuge; Proclamation','ஊமைத்துரை; பிரகடனம்')}
   {node('p','Oct 1801','Brothers hanged at Thiruppathur','மருது சகோதரர்களின் தியாகம்')}
  </div></div>
 <div class="closing"><div class="c-en">TWO BROTHERS. ONE QUEEN. ONE DREAM OF FREEDOM.</div><div class="c-ta">இரு சகோதரர்கள்; ஒரு ராணி; ஒரே சுதந்திரக் கனவு.</div></div>
 <div class="qrbar"><img src="assets/qr.svg" alt="QR code"><div><div class="q-en">SCAN TO READ ONLINE</div><div class="q-ta">இணையத்தில் படிக்க ஸ்கேன் செய்யுங்கள்</div></div></div>
 {FOOT}
</div>'''
CSS_LOCAL=re.sub(r"@import url\('https://fonts.googleapis.com[^']*'\);","@import url('assets/fonts/fonts.css');",CSS)
QRCSS='''
    .trio .card:nth-child(1), .trio .card:nth-child(2) { flex: 1.2; } .trio .card:nth-child(3) { flex: 0.9; }
    /* Print fixes (must come last: earlier print rules lost to later base rules of equal specificity) */
    @media print {
      .poster-container { box-shadow: none !important; }
      .parchment .card, .parchment .hero-card { box-shadow: inset 0 0 0 3px #f8eed3, inset 0 0 0 4px rgba(201,138,18,0.55) !important; }
      body:not(.parchment) .card, body:not(.parchment) .hero-card, body:not(.parchment) .medal, body:not(.parchment) .pic, body:not(.parchment) .portrait-box, body:not(.parchment) .icon { box-shadow: none !important; }
      .parchment .pic, .parchment .portrait-box { box-shadow: 0 0 0 2px #f8eed3, 0 0 0 3px #c98a12 !important; }
      .parchment .medal, .parchment .tl-node b { box-shadow: none !important; }
    }

    .qrbar { display: flex; justify-content: center; align-items: center; gap: 10px; margin-top: 5px; }
    .qrbar img { width: 15mm; height: 15mm; background: #fff; padding: 1mm; border-radius: 2mm; }
    .qrbar .q-en { font-family: 'Cinzel', serif; font-weight: 800; font-size: 10px; letter-spacing: 1px; color: #ffd56b; }
    .qrbar .q-ta { font-family: 'Noto Serif Tamil', serif; font-weight: 700; font-size: 10.5px; color: #ffe29a; }
    .parchment .qrbar .q-en { color: #8a2418; } .parchment .qrbar .q-ta { color: #7a1e12; }
'''
html=f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Marudhiruvar - The Story, in history order (2 pages)</title>
<style>{CSS_LOCAL}{EXTRA}{EXTRA3}{QRCSS}</style>
<link rel="stylesheet" href="assets/mobile.css" media="screen and (max-width: 820px)">
</head>
<body>
{page1}
{page2}
<script src="assets/theme.js"></script>
</body></html>'''
open(os.path.join(ROOT,'story.html'),'w',encoding='utf-8').write(html)
