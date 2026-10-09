import json, math
d=json.load(open('/tmp/states.json'))
tn=[f for f in d['features'] if f['properties'].get('NAME_1')=='Tamil Nadu'][0]['geometry']['coordinates']
def dp(pts,eps):
    if len(pts)<3: return pts
    (x1,y1),(x2,y2)=pts[0],pts[-1]
    dx,dy=x2-x1,y2-y1; L=math.hypot(dx,dy) or 1e-12
    md,mi=0,0
    for i in range(1,len(pts)-1):
        dist=abs(dy*(pts[i][0]-x1)-dx*(pts[i][1]-y1))/L
        if dist>md: md,mi=dist,i
    if md>eps: return dp(pts[:mi+1],eps)[:-1]+dp(pts[mi:],eps)
    return [pts[0],pts[-1]]
def area(r): return abs(sum(r[i][0]*r[(i+1)%len(r)][1]-r[(i+1)%len(r)][0]*r[i][1] for i in range(len(r))))/2
rings=[]
for poly in tn:
    r=poly[0]
    if area(r)<0.01: continue
    r=[tuple(p) for p in r]; m=len(r)//2
    rings.append(dp(r[:m+1],0.01)[:-1]+dp(r[m:],0.01))
LON0,LON1,LAT0,LAT1=76.1,80.5,7.9,13.7
K=60; cx=math.cos(math.radians(10.8))
W=(LON1-LON0)*cx*K; H=(LAT1-LAT0)*K
def P(lat,lon): return ((lon-LON0)*cx*K,(LAT1-lat)*K)
path=" ".join("M"+" L".join("%.1f,%.1f"%P(y,x) for x,y in r)+"Z" for r in rings)
json.dump({'W':W,'H':H,'path':path,'n':sum(len(r) for r in rings)},open('/tmp/tnpath.json','w'))
print(W,H,len(path),len(rings))

json.dump([[list(p) for p in r] for r in rings],open('/tmp/tnrings.json','w'))
