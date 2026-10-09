# -*- coding: utf-8 -*-
import json, math
rings=json.load(open('/tmp/tnrings.json'))
PL={'sivaganga':(9.85,78.48),'kalaiyar':(9.85,78.63),'virupachi':(10.30,77.95),'thiruppathur':(10.12,78.52),'madurai':(9.92,78.12),
    'trichy':(10.80,78.69),'panchal':(8.97,77.93),'mysore':(12.30,76.65),'chennai':(13.08,80.27),'arcot':(12.91,79.33),'palay':(8.72,77.74),'ramnad':(9.37,78.83)}
def make_proj(lon0,lat1,K):
    cx=math.cos(math.radians(10.8))
    return lambda lat,lon:((lon-lon0)*cx*K,(lat1-lat)*K)
def land_path(P):
    return " ".join("M"+" L".join("%.1f,%.1f"%P(y,x) for x,y in r)+"Z" for r in rings)
MARK='<marker id="{i}" markerWidth="9" markerHeight="9" refX="7" refY="4.5" markerUnits="userSpaceOnUse" orient="auto"><path d="M0,0 L9,4.5 L0,9 z" class="{c}"/></marker>'
DEFS='<defs>'+MARK.format(i='a1',c='arrfill')+MARK.format(i='a2',c='arrfill2')+MARK.format(i='a3',c='arrfill3')+MARK.format(i='a4',c='arrfill4')+MARK.format(i='a5',c='arrfill5')+'</defs>'

# ---------- main map ----------
K1,LON0,LAT1=60,76.1,13.7
P1=make_proj(LON0,LAT1,K1)
W1=(80.5-LON0)*math.cos(math.radians(10.8))*K1; H1=(LAT1-7.9)*K1
p1={k:P1(*v) for k,v in PL.items()}
def d1(k,label,dx,dy,cls='',anc='start'):
    x,y=p1[k]; return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.2" class="mdot {cls}"/><text x="{x+dx:.1f}" y="{y+dy:.1f}" text-anchor="{anc}" class="mlabel {cls}">{label}</text>'
sv=p1['sivaganga']; vr=p1['virupachi']; my=p1['mysore']; ar=p1['arcot']; pa=p1['palay']
bx0,by0=P1(10.5,77.6); bx1,by1=P1(9.3,79.3)
main=f'''<svg viewBox="-14 0 {W1+14:.0f} {H1:.0f}" xmlns="http://www.w3.org/2000/svg" class="map">{DEFS}
 <path d="{land_path(P1)}" class="land"/>
 <text x="{W1-4:.0f}" y="{H1*0.40:.0f}" text-anchor="end" class="sea">Bay of Bengal</text>
 <text x="{P1(8.15,78.9)[0]:.0f}" y="{P1(8.15,78.9)[1]:.0f}" class="sea">Indian Ocean</text>
 <rect x="{bx0:.1f}" y="{by0:.1f}" width="{bx1-bx0:.1f}" height="{by1-by0:.1f}" rx="4" class="zoombox"/>
 <path d="M{ar[0]:.1f},{ar[1]+4:.1f} C{ar[0]+25:.1f},{ar[1]+80:.1f} {sv[0]+40:.1f},{sv[1]-90:.1f} {sv[0]+12:.1f},{by0-2:.1f}" class="route foe" marker-end="url(#a4)"/>
 <path d="M{vr[0]-4:.1f},{vr[1]-4:.1f} L{my[0]+6:.1f},{my[1]+8:.1f}" class="route hyder" marker-end="url(#a3)"/>
 <path d="M{pa[0]+2:.1f},{pa[1]-5:.1f} C{pa[0]-10:.1f},{pa[1]-40:.1f} {sv[0]-30:.1f},{sv[1]+50:.1f} {sv[0]-14:.1f},{by1+2:.1f}" class="route ooma" marker-end="url(#a5)"/>
 {d1('mysore','Mysore',-4,-9,'hy')}
 {d1('arcot','Arcot (Nawab)',-6,-4,'foe','end')}
 {d1('chennai','Chennai (British)',-6,-5,'foe','end')}
 {d1('trichy','Tiruchirappalli',7,4)}
 {d1('palay','Palayamkottai',-6,4,'','end')}
 {d1('panchal','Panchalankurichi',-6,4,'','end')}
 <text x="{(bx0+bx1)/2:.1f}" y="{by0-6:.1f}" text-anchor="middle" class="mlabel cap">SIVAGANGA</text>
 <text x="{bx1+3:.1f}" y="{by1+10:.1f}" text-anchor="end" class="mlabel small">zoomed below</text>
</svg>'''

# ---------- inset ----------
K2,L0,LA1=170,77.6,10.5
P2=make_proj(L0,LA1,K2)
W2=(79.3-L0)*math.cos(math.radians(10.8))*K2; H2=(LA1-9.3)*K2
q={k:P2(*v) for k,v in PL.items()}
def d2(k,label,dx,dy,cls='',anc='start'):
    x,y=q[k]; r=5.5 if cls=='cap' else 4
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" class="mdot {cls}"/><text x="{x+dx:.1f}" y="{y+dy:.1f}" text-anchor="{anc}" class="mlabel {cls}">{label}</text>'
S,Kc,V,T=q['sivaganga'],q['kalaiyar'],q['virupachi'],q['thiruppathur']
inset=f'''<svg viewBox="0 0 {W2:.0f} {H2:.0f}" xmlns="http://www.w3.org/2000/svg" class="inset">{DEFS}
 <rect width="{W2:.0f}" height="{H2:.0f}" class="seabg"/>
 <path d="{land_path(P2)}" class="land"/>
 <path d="M{Kc[0]:.1f},{Kc[1]-6:.1f} C{Kc[0]-20:.1f},{Kc[1]-90:.1f} {V[0]+60:.1f},{V[1]-30:.1f} {V[0]+7:.1f},{V[1]-2:.1f}" class="route flee" marker-end="url(#a1)"/>
 <path d="M{V[0]-2:.1f},{V[1]+7:.1f} C{V[0]-10:.1f},{V[1]+90:.1f} {S[0]-60:.1f},{S[1]+30:.1f} {S[0]-7:.1f},{S[1]+3:.1f}" class="route back" marker-end="url(#a2)"/>
 {d2('virupachi','Virupachi',8,3,'star')}
 {d2('madurai','Madurai',-8,-7,'','end')}
 {d2('thiruppathur','Thiruppathur ✝',8,-2,'')}
 {d2('sivaganga','SIVAGANGA',-8,19,'cap','end')}
 {d2('kalaiyar','Kalaiyar Koil',9,14,'')}
 {d2('ramnad','Ramanathapuram',-8,4,'','end')}
 <text x="{W2-6:.0f}" y="{H2-8:.0f}" text-anchor="end" class="sea">Palk Bay</text>
</svg>'''
svg=main
