import json,re,math
m=json.load(open('/tmp/tnpath.json')); W,H=m['W'],m['H']
LON0,LAT1,K=76.1,13.7,60; cx=math.cos(math.radians(10.8))
def P(lat,lon): return ((lon-LON0)*cx*K,(LAT1-lat)*K)
pl={'ramnad':(9.37,78.83),'sivaganga':(9.85,78.48),'kalaiyar':(9.85,78.63),'virupachi':(10.30,77.95),'thiruppathur':(10.12,78.52),
    'madurai':(9.92,78.12),'trichy':(10.80,78.69),'panchal':(8.97,77.93),'mysore':(12.30,76.65),'chennai':(13.08,80.27),'arcot':(12.91,79.33),'palay':(8.72,77.74)}
pt={k:P(*v) for k,v in pl.items()}
def dot(k,label,dx,dy,cls='',anc='start'):
    x,y=pt[k]; return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.4" class="mdot {cls}"/><text x="{x+dx:.1f}" y="{y+dy:.1f}" text-anchor="{anc}" class="mlabel {cls}">{label}</text>'
sv,kv,vr,my_,pc,tr=[pt[k] for k in ('sivaganga','kalaiyar','virupachi','mysore','panchal','trichy')]
svg=f'''<svg viewBox="-14 0 {W+14:.0f} {H:.0f}" xmlns="http://www.w3.org/2000/svg" class="map">
 <defs><marker id="a1" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" class="arrfill"/></marker>
 <marker id="a2" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" class="arrfill2"/></marker>
 <marker id="a4" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#ff4d4d"/></marker>
 <marker id="a3" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" class="arrfill3"/></marker></defs>
 <path d="{m['path']}" class="land"/>
 <text x="{W-4:.0f}" y="{H*0.40:.0f}" text-anchor="end" class="sea">Bay of Bengal</text>
 <text x="{P(8.15,78.9)[0]:.0f}" y="{P(8.15,78.9)[1]:.0f}" class="sea">Indian Ocean</text>
 <path d="M{kv[0]-3:.1f},{kv[1]-5:.1f} C{kv[0]-30:.1f},{kv[1]-60:.1f} {vr[0]+30:.1f},{vr[1]+45:.1f} {vr[0]+4:.1f},{vr[1]+5:.1f}" class="route flee" marker-end="url(#a1)"/>
 <path d="M{vr[0]-3:.1f},{vr[1]+6:.1f} C{vr[0]-8:.1f},{vr[1]+70:.1f} {sv[0]-45:.1f},{sv[1]-50:.1f} {sv[0]-4:.1f},{sv[1]-6:.1f}" class="route back" marker-end="url(#a2)"/>
 <path d="M{vr[0]-4:.1f},{vr[1]-4:.1f} L{my_[0]+6:.1f},{my_[1]+8:.1f}" class="route hyder" marker-end="url(#a3)"/>
 <path d="M{pc[0]:.1f},{pc[1]-5:.1f} Q{pc[0]+10:.1f},{(pc[1]+sv[1])/2:.1f} {sv[0]+4:.1f},{sv[1]+6:.1f}" class="route ally"/>
 <path d="M{sv[0]+3:.1f},{sv[1]-6:.1f} Q{sv[0]+22:.1f},{(sv[1]+tr[1])/2:.1f} {tr[0]-3:.1f},{tr[1]+5:.1f}" class="route ally"/>
 <path d="M{pt['arcot'][0]:.1f},{pt['arcot'][1]+4:.1f} C{pt['arcot'][0]+30:.1f},{pt['arcot'][1]+90:.1f} {kv[0]+30:.1f},{kv[1]-90:.1f} {kv[0]+2:.1f},{kv[1]-5:.1f}" class="route foe" marker-end="url(#a4)"/>
 <path d="M{pt['palay'][0]:.1f},{pt['palay'][1]-5:.1f} Q{pt['palay'][0]-25:.1f},{(pt['palay'][1]+sv[1])/2:.1f} {sv[0]-3:.1f},{sv[1]+6:.1f}" class="route ooma"/>
 {dot('mysore','Mysore',-4,-8,'hy','start')}
 {dot('trichy','Tiruchirappalli',7,4,'')}
 {dot('virupachi','Virupachi',-7,-5,'star','end')}
 {dot('madurai','Madurai',-7,12,'','end')}
 {dot('thiruppathur','Thiruppathur',7,-3,'')}
 {dot('kalaiyar','Kalaiyar Koil',8,5,'')}
 {dot('sivaganga','SIVAGANGA',-8,16,'cap','end')}
 {dot('ramnad','Ramanathapuram',-6,14,'','end')}
 {dot('panchal','Panchalankurichi',7,4,'')}
 {dot('chennai','Chennai (British)',-6,-6,'','end')}
 {dot('arcot','Arcot (Nawab)',-6,-6,'','end')}
 {dot('palay','Palayamkottai',8,-2,'')}
</svg>'''

CSS=re.search(r'<style>(.*?)</style>',open('/tmp/plot_tpl.html',encoding='utf-8').read(),re.S).group(1)
# drop single-page specific bits we override
EXTRA='''
    body { flex-direction: column; justify-content: flex-start; align-items: center; gap: 24px; }
    @media print { body { gap: 0; } .poster-container { break-after: page; page-break-after: always; } .poster-container:last-child { break-after: auto; page-break-after: auto; } }
    .part { font-family: 'Cinzel', serif; font-size: 10px; letter-spacing: 3px; color: #ffd56b; margin-top: 3px; }
    .trio { display: flex; gap: 8px; margin-bottom: 8px; }
    .trio .card { flex: 1; display: flex; flex-direction: column; align-items: center; text-align: center; padding: 6px 8px 7px; }
    .trio .pic { width: 70px; height: 88px; margin-bottom: 6px; }
    .p1 .ch-en { font-size: 11.5px; line-height: 1.32; } .p1 .ch-ta { font-size: 11px; line-height: 1.32; } .p1 .play { margin-top: 2px; font-size: 9.5px; } .p1 .trio { margin-bottom: 6px; } .p1 .ch-title { font-size: 13.5px; margin-bottom: 2px; } .p1 .col { gap: 5px; } .p1 .card.chapter { padding: 5px 10px; } .p1 .role { font-size: 10px; } .p1 .role .rta { font-size: 9.5px; } .p1 .role .tag { width: 24px; height: 24px; } .p1 .roles { margin-top: 4px; }
    .p1 .trio .rl { font-size: 11px; } .p1 .trio .rt { font-size: 10.5px; }
    .trio .nm { font-family: 'Cinzel', serif; font-weight: 800; font-size: 12.5px; color: #ffd56b; }
    .trio .nt { font-family: 'Noto Serif Tamil', serif; font-weight: 700; font-size: 11.5px; color: #ffe29a; }
    .trio .rl { font-size: 10.5px; line-height: 1.3; margin-top: 2px; color: #fff8e6; font-weight: 500; }
    .trio .rt { font-family: 'Noto Sans Tamil', sans-serif; font-size: 10px; line-height: 1.3; color: #f3e2c0; }
    .col { display: flex; flex-direction: column; gap: 7px; flex: 1; min-height: 0; }
    .col .chapter { flex: 1 1 auto; min-height: 0; }
    .tags { display: flex; gap: 3px; margin-top: 4px; }
    .tag { width: 24px; height: 24px; border-radius: 50%; overflow: hidden; border: 1.5px solid var(--gold); }
    .tag img { width: 100%; height: 100%; object-fit: cover; object-position: top center; display: block; }
    .scene { flex-shrink: 0; width: 120px; height: 96px; border-radius: 10px; border: 2px solid var(--gold); object-fit: cover; }
    .places { font-size: 10px; line-height: 1.45; color: #f3e2c0; margin-top: 6px; padding: 5px 4px 0; border-top: 1px solid rgba(232,184,74,0.5); }
    .places b { color: #ffd56b; }
    .parchment .places { color: #3a2410; border-color: rgba(138,36,24,0.5); } .parchment .places b { color: #8a2418; }
    .roles { display: flex; gap: 6px; margin-top: 6px; }
    .role { flex: 1; display: flex; gap: 5px; align-items: flex-start; font-size: 10.5px; line-height: 1.28; color: #fff8e6; font-weight: 500; background: rgba(232,184,74,0.08); border: 1px solid rgba(232,184,74,0.35); border-radius: 8px; padding: 4px 5px; }
    .role b { color: #ffd56b; } .role .tag { flex-shrink: 0; width: 26px; height: 26px; }
    .role .rta { font-family: 'Noto Sans Tamil', sans-serif; font-size: 9.5px; color: #f3e2c0; font-weight: 500; }
    .parchment .role { color: #2b1608; background: rgba(138,36,24,0.06); border-color: rgba(138,36,24,0.35); } .parchment .role b { color: #8a2418; } .parchment .role .rta { color: #3a2410; }
    .play { margin-top: 4px; font-size: 10px; font-weight: 700; color: #ffd56b; }
    .play span { font-weight: 500; color: #f3e2c0; font-style: italic; }
    .parchment .play { color: #8a2418; } .parchment .play span { color: #3a2410; }
    .closing { text-align: center; margin-top: 7px; }
    .closing .c-en { font-family: 'Cinzel', serif; font-weight: 800; font-size: 13px; letter-spacing: 1.5px; color: #ffd56b; }
    .closing .c-ta { font-family: 'Noto Serif Tamil', serif; font-weight: 700; font-size: 12px; color: #ffe29a; }
    .row2 { display: flex; gap: 8px; flex: 1; min-height: 0; }
    .row2 .mapcard { flex: 1.15; }
    .row2 .col { flex: 1.35; }
    .mapcard svg { flex: 1; min-height: 0; width: 100%; }
    .route.ally { stroke: #c9a2ff; stroke-dasharray: 1 4; stroke-width: 2.2; }
    .arrfill3 { fill: #7fd0ff; }
    .route.foe { stroke: #ff4d4d; stroke-dasharray: 7 3; stroke-width: 2.2; }
    .route.ooma { stroke: #6ee7b7; stroke-width: 2.2; }
    .legend .l5 i { border-color: #ff4d4d; border-top-style: dashed; } .legend .l6 i { border-color: #6ee7b7; }
    .parchment .route.foe { stroke: #b3120a; } .parchment .route.ooma { stroke: #1b7a55; } .parchment .legend .l5 i { border-color: #b3120a; } .parchment .legend .l6 i { border-color: #1b7a55; }
    .legend .l4 i { border-color: #c9a2ff; border-top-style: dotted; }
    .tl-node .av { width: 28px; height: 28px; border-radius: 50%; overflow: hidden; border: 2px solid var(--gold); margin: -2px auto 3px; position: relative; z-index: 1; background: #2a0507; }
    .tl-node .av img { width: 100%; height: 100%; object-fit: cover; object-position: top center; display: block; }
    .tl::before { top: 12px; }
    .parchment .tag, .parchment .tl-node .av, .parchment .scene { border-color: #8a2418; }
    .parchment .part, .parchment .trio .nm, .parchment .closing .c-en { color: #8a2418; }
    .parchment .trio .nt, .parchment .closing .c-ta { color: #7a1e12; }
    .parchment .trio .rl { color: #2b1608; } .parchment .trio .rt { color: #3a2410; }
    .parchment .route.ally { stroke: #6a3d9a; } .parchment .arrfill3 { fill: #1d5f8a; }
    .parchment .legend .l1 i { border-color: #c01f12; } .parchment .legend .l2 i { border-color: #8a2418; } .parchment .legend .l3 i { border-color: #1d5f8a; } .parchment .legend .l4 i { border-color: #6a3d9a; }
    .parchment .route.flee { stroke: #c01f12; }
    @media print { .parchment .trio .card { box-shadow: inset 0 0 0 3px #f8eed3, inset 0 0 0 4px rgba(201,138,18,0.55); } }
'''
IMG={'p':'assets/images/periya_maruthu.jpeg','c':'assets/images/chinna_maruthu.jpeg','v':'assets/images/velu_nachiyar.jpeg'}
def tags(s):
    if len(s)==3: return ''
    n={'p':'Periya Maruthu','c':'Chinna Maruthu','v':'Velu Nachiyar'}
    pos={'v':'object-position:25% top'}
    return '<div class="tags">'+''.join(f'<span class="tag" title="{n[k]}"><img src="{IMG[k]}" alt="{n[k]}" style="{pos.get(k,"")}"></span>' for k in s)+'</div>'
def roles(items):
    out=''
    for k,en,ta in items:
        nm={'p':'Periya','v':'Velu Nachiyar','c':'Chinna'}[k]
        pos='object-position:25% top' if k=='v' else ''
        out+=f'<div class="role"><span class="tag"><img src="{IMG[k]}" alt="" style="{pos}"></span><div><b>{nm}:</b> {en}<div class="rta">{ta}</div></div></div>'
    return '<div class="roles">'+out+'</div>'
def chap(num,yr,title,en,ta,play,scene):
    rl=f'<div class="play">🎭 In the play: <span>{play}</span></div>'
    who=''
    sc=f'<img class="scene" src="assets/scenes/{scene}.jpg" alt="" onerror="this.remove()">'
    return f'''<div class="card chapter"><div class="medal"><div class="num">{num}</div><div class="yr">{yr}</div></div>
 <div class="ch-body"><div class="ch-title">{title}</div><div class="ch-en">{en}</div><div class="ch-ta">{ta}</div>{tags(who)}{rl}</div>{sc}</div>'''
def trio(k,name,ta,role,rta,pos=''):
    return f'''<div class="card"><div class="pic"><img src="{IMG[k]}" alt="{name}" style="{pos}"></div><div class="nm">{name}</div><div class="nt">{ta}</div><div class="rl">{role}</div><div class="rt">{rta}</div></div>'''
def head(sub_en,part):
    return f'''<div class="header"><div class="title-banner"><div class="title-main">THE STORY</div></div>
 <div class="title-sub-ta">மூவரின் வீரக் காவியம்</div><div class="title-sub-en">{sub_en}</div><div class="part">{part}</div><div class="divider"></div></div>'''
FOOT='<div class="footer">HONORING THE VALOR OF SIVAGANGA • TAMIL NADU HISTORY</div>'

page1=f'''<div class="poster-container p1">
 {head("THREE HEROES • ONE FIGHT FOR FREEDOM","PART I • 1730–1780 • FALL AND RISE")}
 <div class="trio">
  {trio('p','PERIYA MARUTHU','பெரிய மருது','The Commander: a fearless warrior who protects Sivaganga.','வீரமிகு படைத்தளபதி; சிவகங்கையின் காவலர்.')}
  {trio('v','QUEEN VELU NACHIYAR','ராணி வேலு நாச்சியார்','The Queen: a fighter who refuses to give up her kingdom.','நாட்டை மீட்கும் உறுதி கொண்ட வீரமங்கை.','object-position:25% top')}
  {trio('c','CHINNA MARUTHU','சின்ன மருது','The Strategist: a clever leader who unites the rulers.','அரசர்களை ஒன்றிணைத்த போர்வியூக வல்லுநர்.')}
 </div>
 <div class="col">
 {chap(1,'1730–72','Three Heroes Rise','Velu Nachiyar, princess of Ramnad, trains in Silambam, archery and horse riding, then marries King Muthu Vaduganathar of Sivaganga. Nearby, Periya Maruthu, a master of the Valari, and Chinna Maruthu, a sharp strategist, win fame as fearless warriors.','இராமநாதபுர இளவரசி வேலு நாச்சியார் சிலம்பம், வில், குதிரையேற்றம் பயின்று, சிவகங்கை மன்னர் முத்து வடுகநாதரை மணந்தார். அருகில், வளரி வீரர் பெரிய மருதுவும் கூர்மையான போர்வியூக வல்லுநர் சின்ன மருதுவும் அஞ்சா வீரர்களாகப் புகழ் பெற்றனர்.','Velu Nachiyar intro • Marudhu brothers intro • “Veeram” • “Sara Sara”','ch1')}
 {chap(2,'1772','Betrayal at Kalaiyar Koil','The British East India Company joins the Nawab of Arcot and attacks Sivaganga. King Muthu Vaduganathar is killed in battle. Queen Velu Nachiyar escapes with her daughter Vellachi, vowing to win her kingdom back.','கிழக்கிந்தியக் கம்பெனி, ஆர்க்காடு நவாபுடன் கூட்டுச் சேர்ந்து சிவகங்கையைத் தாக்கியது. போரில் மன்னர் வீரமரணம் அடைந்தார். ராணி வேலு நாச்சியார் மகள் வெள்ளச்சியுடன் தப்பி, நாட்டை மீட்க உறுதி ஏற்றார்.','Nawab of Arcot • Wedding • Killing of the King, Lament & Oath • The Escape','ch2')}
 {chap(3,'1772','Three Heroes Unite','As the play tells it, the queen in hiding meets the Maruthu brothers. Periya Maruthu offers his sword, Chinna Maruthu his strategy, and the three pledge to win Sivaganga back.','நாடகத்தில் காட்டப்படுவது போல், தலைமறைவான ராணி மருது சகோதரர்களைச் சந்தித்தார். பெரிய மருது தம் வாளையும் சின்ன மருது தம் போர்த்திட்டத்தையும் அளிக்க, மூவரும் சிவகங்கையை மீட்க உறுதி ஏற்றனர்.','The hunt • Velu Nachiyar meets Marudhu Iruvar','ch3')}
 {chap(4,'1772–80','An Ally in Exile','At Virupachi, Hyder Ali of Mysore shelters the queen and supports her with soldiers and arms. For eight years she builds her army, while the brothers gather fighters and loyal supporters in Sivaganga.','விருப்பாட்சியில் மைசூர் ஹைதர் அலி ராணிக்கு அடைக்கலமும் படை, ஆயுத உதவியும் அளித்தார். எட்டு ஆண்டுகள் ராணி படை திரட்ட, மருது சகோதரர்கள் சிவகங்கையில் வீரர்களையும் ஆதரவாளர்களையும் திரட்டினர்.','Hyder Ali scene','ch4')}
 {chap(5,'1780','Sivaganga Is Won Back','The queen strikes with Kuyili’s Women’s Army (Udaiyaal Padai), the brothers fighting at her side. Legend says Kuyili gave her life to destroy the British weapons store. Sivaganga is free, and the brothers become her trusted ministers and commanders.','குயிலியின் "உடையாள் படை"யுடனும், அவருடன் நின்று போராடிய மருது சகோதரர்களுடனும் ராணி தாக்கினார். ஆயுதக் கிடங்கை அழிக்க குயிலி உயிர்த்தியாகம் செய்ததாகக் கூறப்படுகிறது. சிவகங்கை மீண்டது; சகோதரர்கள் அமைச்சர்களும் தளபதிகளும் ஆனார்கள்.','Village attack • Back to the palace','ch5')}
 </div>
 {FOOT}
</div>'''

def node(av,y,e,t):
    imgs=''.join(f'<div class="av"><img src="{IMG[k]}" alt="" style="{"object-position:25% top" if k=="v" else ""}"></div>' for k in av[:1])
    return f'<div class="tl-node">{imgs}<div class="y">{y}</div><div class="e">{e}</div><div class="t">{t}</div></div>'
page2=f'''<div class="poster-container">
 {head("THREE HEROES • ONE FIGHT FOR FREEDOM","PART II • 1780–1801 • GUARDIANS OF A KINGDOM")}
 <div class="row2">
  <div class="card mapcard"><div class="card-title">THE MAP OF THE STRUGGLE</div><div class="card-title-ta">போராட்டத்தின் வரைபடம்</div>
   {svg}
   <div class="legend"><span class="l1"><i></i>Escape 1772</span><span class="l2"><i></i>Return 1780</span><span class="l3"><i></i>Help from Mysore</span><span class="l4"><i></i>Southern alliance</span><span class="l5"><i></i>Nawab + British advance</span><span class="l6"><i></i>Oomaithurai’s flight 1801</span></div>
   <div class="note">Tamil Nadu, simplified outline. Distances approximate.</div>
   <div class="places">
    <div><b>Sivaganga</b> the kingdom • சிவகங்கை</div>
    <div><b>Kalaiyar Koil</b> 1772 battle; brothers' last stand • காளையார்கோவில்</div>
    <div><b>Virupachi</b> the queen's refuge • விருப்பாட்சி</div>
    <div><b>Panchalankurichi</b> Kattabomman's fort • பாஞ்சாலங்குறிச்சி</div>
    <div><b>Thiruppathur</b> where the brothers were hanged • திருப்பத்தூர்</div>
   </div></div>
  <div class="col">
   {chap(6,'1780–99','Guardians of Sivaganga','Periya Maruthu leads the army and Chinna Maruthu guides the government, building forts, temples and tanks. After the queen passes in 1796, they keep guarding Sivaganga with her daughter Vellachi, and stand with Veerapandiya Kattabomman against the British.','பெரிய மருது படையையும் சின்ன மருது ஆட்சியையும் வழிநடத்தி, கோட்டை, கோயில், குளங்களை அமைத்தனர். 1796-இல் ராணி மறைந்த பின்னும் மகள் வெள்ளச்சியுடன் சிவகங்கையைக் காத்து, வீரபாண்டிய கட்டபொம்மனுடன் ஆங்கிலேயரை எதிர்த்தனர்.','Nawab and the British soldiers','ch6')}
   {chap(7,'1801','Refuge and Rebellion','Kattabomman’s brother Oomaithurai escapes from prison and finds refuge in Sivaganga. The brothers refuse to give him up and issue the Jambudvipa Proclamation, calling all to unite against the British. War follows.','கட்டபொம்மனின் தம்பி ஊமைத்துரை சிறையிலிருந்து தப்பி சிவகங்கையில் அடைக்கலம் பெற்றார். அவரை ஒப்படைக்க மறுத்த மருது சகோதரர்கள், அனைவரும் ஒன்றுபட "ஜம்புத் தீவு பிரகடனம்" வெளியிட்டனர். போர் மூண்டது.','Veera Sudandiram • War • Umaithurai','ch7')}
   {chap(8,'Oct 1801','The Last Stand','Fighting on from the forests of Kalaiyar Koil against a far larger force, the brothers are captured. For sheltering Oomaithurai and defying the British, they are hanged at Thiruppathur with many followers. Their sacrifice still inspires Tamil Nadu.','காளையார்கோவில் காடுகளிலிருந்து மிகப் பெரிய படையை எதிர்த்துப் போராடிய சகோதரர்கள் பிடிபட்டனர். ஊமைத்துரைக்கு அடைக்கலம் அளித்து ஆங்கிலேயரை எதிர்த்ததற்காக, பலருடன் திருப்பத்தூரில் தூக்கிலிடப்பட்டனர். அவர்களின் தியாகம் இன்றும் தமிழகத்துக்கு ஊக்கமளிக்கிறது.','Hanging of Marudhu Iruvar • “Veera Velanja Mannil” • Mangalam','ch8')}
  </div>
 </div>
 <div class="card timeline"><div class="card-title">TIMELINE OF COURAGE</div>
  <div class="tl">
   {node('v','1730','Velu Nachiyar is born','வேலு நாச்சியார் பிறப்பு')}
   {node('v','1772','King killed at Kalaiyar Koil; queen escapes','காளையார்கோவில் போர்')}
   {node('p','1780','Sivaganga won back; brothers rise as leaders','சிவகங்கை மீட்பு')}
   {node('v','1796','Queen Velu Nachiyar passes away','ராணி மறைவு')}
   {node('c','1801','Oomaithurai finds refuge; Jambudvipa Proclamation','ஊமைத்துரைக்கு அடைக்கலம்; பிரகடனம்')}
   {node('p','1801','Oct: Maruthu brothers hanged at Thiruppathur','மருது சகோதரர்களின் தியாகம்')}
  </div></div>
 <div class="closing"><div class="c-en">THREE HEROES. ONE DREAM OF FREEDOM.</div><div class="c-ta">மூன்று வீரர்கள்; ஒரே சுதந்திரக் கனவு.</div></div>
 {FOOT}
</div>'''
html=f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Marudhiruvar - The Story (2 pages)</title>
<style>{CSS}{EXTRA}</style></head>
<body>
{page1}
{page2}
<script>if (new URLSearchParams(location.search).get('theme') === 'parchment') document.body.classList.add('parchment');</script>
</body></html>'''
open('/Users/a.venkatachalam/PersonalProjects/Maruthiruvar/plot2.html','w',encoding='utf-8').write(html)
