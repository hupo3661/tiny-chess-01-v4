import os,json,random,base64
from urllib.request import urlopen,Request
VM=[0,82,337,365,477,1025,0]
VE=[0,94,281,297,512,936,0]
PH=[0,0,1,1,2,4,0]
def _H(s):
 t=[x-64 for x in base64.b64decode(s)];return [t[(j>>3)*4+min(j&7,7-(j&7))] for j in range(64)]
Z=[0]*64
PM=[Z,Z,_H('LDY2NjZAQEA2QEVKNkVFSjZASko2SkpKNkVAQCw2NjY='),Z,Z,_H('IhgYDiIYGA4iGBgOIhgYDiwiIhg2LCwsVFRAQFReSkA=')]
PE=[_H('QEBAQHJycnJZWV5jSkpPWUVFSk9AQEBFQEBAQEBAQEA='),Z,Z,Z,Z,_H('DhgiLCIsNkAiNlReIjZeaCI2XmgiNlReIiJAQA4iIiI=')]
ND=[17,15,-15,-17]
RD=[16,1,-16,-1]
KD=RD+ND
NL=[31,33,14,18,-31,-33,-14,-18]
SQ=[r*16+f for r in range(8) for f in range(8)]
_r=random.Random(20261123)
ZK=[[_r.getrandbits(64) for _ in range(128)] for _ in range(15)]
ZSD=_r.getrandbits(64)
ZCT=[_r.getrandbits(64) for _ in range(16)]
ZEP=[_r.getrandbits(64) for _ in range(128)]
MA=100000
IF=1000000
SV=[0,100,300,300,500,900,10000]
PA=[0,5,10,20,35,60,90,0]
PB=[0,10,20,35,60,100,140,0]
CM=[15]*128
CM[4]=12;CM[7]=14;CM[0]=13;CM[116]=3;CM[119]=11;CM[112]=7
CR={6:(7,5),2:(0,3),118:(119,117),114:(112,115)}
EF=1<<17;CF=1<<18;DF=1<<19
b=[0]*128
s=0;cs=0;ep=-1
kq=[0,0]
sm=0;se=0;ph=0;zk=0;pk=0
H=[];RP=set();PC={}
def pi(p,q):
 r=q>>4;f=q&7
 return (7-r)*8+f if p<8 else r*8+f
def fen(F):
 global b,s,cs,ep,sm,se,ph,zk,pk,H
 b=[0]*128;sm=0;se=0;ph=0;zk=0;pk=0;H=[]
 P=F.split();rows=P[0].split('/')
 for i,row in enumerate(rows):
  r=7-i;f=0
  for ch in row:
   if ch.isdigit(): f+=int(ch)
   else:
    p='pnbrqk'.index(ch.lower())+1+(0 if ch.isupper() else 8);q=r*16+f;b[q]=p
    if p%8==6: kq[0 if p<8 else 1]=q
    t=p%8;j=pi(p,q);sg=1 if p<8 else -1
    sm+=sg*(VM[t]+PM[t-1][j]);se+=sg*(VE[t]+PE[t-1][j]);ph+=PH[t]
    zk^=ZK[p][q]
    if t==1: pk^=ZK[p][q]
    f+=1
 s=0 if len(P)<2 or P[1]=='w' else 1
 if s: zk^=ZSD
 cs=0
 if len(P)>2: cs=sum(1<<i for i,ch in enumerate('KQkq') if ch in P[2])
 zk^=ZCT[cs];ep=-1
 if len(P)>3 and P[3]!='-':
  e=P[3];ep=(int(e[1])-1)*16+(ord(e[0])-97);zk^=ZEP[ep]
def atk(q,by):
 for d in ((-15,-17) if by==0 else (15,17)):
  t=q+d
  if not t&0x88 and b[t]==1+by*8: return True
 n=2+by*8
 for d in NL:
  t=q+d
  if not t&0x88 and b[t]==n: return True
 k=6+by*8
 for d in KD:
  t=q+d
  if not t&0x88 and b[t]==k: return True
 bp=3+by*8;rp=4+by*8;qq=5+by*8
 for d in ND:
  t=q+d
  while not t&0x88:
   p=b[t]
   if p:
    if p==bp or p==qq: return True
    break
   t+=d
 for d in RD:
  t=q+d
  while not t&0x88:
   p=b[t]
   if p:
    if p==rp or p==qq: return True
    break
   t+=d
 return False
def ich(c): return atk(kq[c],1-c)
def ad(p,q,g):
 global sm,se,ph,zk,pk
 t=p%8;j=pi(p,q);cg=g if p<8 else -g
 sm+=cg*(VM[t]+PM[t-1][j]);se+=cg*(VE[t]+PE[t-1][j]);ph+=g*PH[t]
 zk^=ZK[p][q]
 if t==1: pk^=ZK[p][q]
def gm(cap=False):
 ms=[];c=s
 for q in SQ:
  p=b[q]
  if not p or (p<8)!=(c==0): continue
  t=p%8;r=q>>4
  if t==1:
   d=16 if c==0 else -16;pr=7 if c==0 else 0;to=q+d
   if not b[to]:
    if (to>>4)==pr:
     for pt in (5,4,3,2): ms.append(q|(to<<7)|(pt<<14))
    elif not cap:
     ms.append(q|(to<<7))
     if r==(1 if c==0 else 6) and not b[q+2*d]: ms.append(q|((q+2*d)<<7)|DF)
   for dd in ((15,17) if c==0 else (-15,-17)):
    to=q+dd
    if to&0x88: continue
    w=b[to]
    if w and (w<8)!=(c==0):
     if (to>>4)==pr:
      for pt in (5,4,3,2): ms.append(q|(to<<7)|(pt<<14))
     else: ms.append(q|(to<<7))
    elif to==ep: ms.append(q|(to<<7)|EF)
  elif t==2 or t==6:
   for d in (NL if t==2 else KD):
    to=q+d
    if to&0x88: continue
    w=b[to]
    if not w:
     if not cap: ms.append(q|(to<<7))
    elif (w<8)!=(c==0): ms.append(q|(to<<7))
   if t==6 and not cap:
    for bit,rt,em,at,tg in (((1,7,(5,6),(4,5,6),6),(2,0,(1,2,3),(4,3,2),2)) if c==0 else ((4,119,(117,118),(116,117,118),118),(8,112,(113,114,115),(116,115,114),114))):
     if q==(4 if c==0 else 116) and cs&bit and b[rt]==(4 if c==0 else 12) and not any(b[x] for x in em) and not any(atk(x,1-c) for x in at): ms.append(q|(tg<<7)|CF)
  else:
   dirs=ND if t==3 else (RD if t==4 else KD)
   for d in dirs:
    to=q+d
    while not to&0x88:
     w=b[to]
     if not w:
      if not cap: ms.append(q|(to<<7))
     else:
      if (w<8)!=(c==0): ms.append(q|(to<<7))
      break
     to+=d
 return ms
def mk(m):
 global s,cs,ep,zk
 fr=m&127;to=(m>>7)&127;pt=(m>>14)&7;p=b[fr];cap=0
 if m&EF: cap=b[to-16 if s==0 else to+16]
 elif b[to]: cap=b[to]
 H.append((m,cap,cs,ep,zk,pk,sm,se,ph))
 zk^=ZCT[cs]
 if ep>=0: zk^=ZEP[ep]
 ep=-1
 if m&EF:
  cq=to-16 if s==0 else to+16;b[cq]=0;ad(cap,cq,-1)
 elif cap: ad(cap,to,-1)
 ad(p,fr,-1);b[fr]=0
 np=(pt+(8 if p>=8 else 0)) if pt else p
 b[to]=np;ad(np,to,1)
 if p%8==6: kq[0 if p<8 else 1]=to
 if m&CF:
  f2,t2=CR[to];p2=b[f2];b[t2]=p2;b[f2]=0;ad(p2,f2,-1);ad(p2,t2,1)
 if m&DF: ep=fr+(16 if s==0 else -16)
 cs&=CM[fr]&CM[to]
 zk^=ZCT[cs]
 if ep>=0: zk^=ZEP[ep]
 s=1-s;zk^=ZSD
 return cap
def um():
 global s,cs,ep,zk,pk,sm,se,ph
 m,cap,oc,oe,oz,op,om,oe2,oph=H.pop()
 s=1-s;fr=m&127;to=(m>>7)&127;pt=(m>>14)&7;p=b[to]
 if pt: p=1+(8 if p>=8 else 0)
 b[fr]=p;b[to]=0
 if p%8==6: kq[0 if p<8 else 1]=fr
 if m&CF:
  f2,t2=CR[to];b[f2]=b[t2];b[t2]=0
 if cap:
  if m&EF:
   cq=to-16 if s==0 else to+16;b[cq]=cap
  else: b[to]=cap
 cs,ep,zk,pk,sm,se,ph=oc,oe,oz,op,om,oe2,oph
def pev():
 v=PC.get(pk)
 if v is not None: return v
 wp=[q for q in SQ if b[q]==1];bp=[q for q in SQ if b[q]==9]
 mg=0;eg=0
 for own,opp,pc,sg in ((wp,bp,9,1),(bp,wp,1,-1)):
  for q in own:
   f=q&7;r=q>>4;rr=r if sg>0 else 7-r
   if all(b[b2]!=pc or (b2&7)<f-1 or (b2&7)>f+1 or ((b2>>4)<=r if sg>0 else (b2>>4)>=r) for b2 in opp): mg+=sg*PA[rr];eg+=sg*PB[rr]
 PC[pk]=(mg,eg)
 return (mg,eg)
def rp(em): return -260 if em>110 else (140 if em<-110 else 0)
tt={};KL={}
LK=set()
nd=[0];ST=[False]
BG=70000
def osc(m,ttm,ply):
 if m==ttm: return 1<<28
 to=(m>>7)&127;vic=b[to];pt=(m>>14)&7
 if vic or pt or (m&EF): return (1<<24)+((pt*16 if pt else 0)+SV[vic%8])*32-SV[b[m&127]%8]
 k=KL.get(ply)
 if k:
  if m==k[0]: return (1<<23)+2
  if len(k)>1 and m==k[1]: return (1<<23)+1
 return 0
def ev():
 pm,pe2=pev();mg=sm+pm;eg=se+pe2
 for q in SQ:
  p=b[q]
  if not p: continue
  t=p%8;c=0 if p<8 else 1
  if t in (3,4,5):
   dirs=ND if t==3 else (RD if t==4 else KD)
   cnt=0
   for d in dirs:
    to=q+d
    while not to&0x88:
     w=b[to]
     if not w: cnt+=1
     else:
      if (w<8)!=(c==0): cnt+=1
      break
     to+=d
   w_=((5,4) if t==3 else ((3,2) if t==4 else (1,1)))
   mg+=(cnt*w_[0] if c==0 else -cnt*w_[0]);eg+=(cnt*w_[1] if c==0 else -cnt*w_[1])
 sc=(mg*ph+eg*(24-ph))//24
 return sc if s==0 else -sc
def evq():
 pm,pe2=pev();mg=sm+pm;eg=se+pe2
 sc=(mg*ph+eg*(24-ph))//24
 return sc if s==0 else -sc
def qs(a,be,ply):
 nd[0]+=1
 if (nd[0]&1023)==0 and nd[0]>=BG: ST[0]=True
 if ST[0]: return evq()
 chk=ich(s)
 if chk:
  if ply>=16: return evq()
  best=-IF
 else:
  e=evq()
  if e>=be: return e
  if e>a: a=e
  best=e
  if ply>=16: return best
 ms=gm(not chk)
 ms.sort(key=lambda m: osc(m,0,0),reverse=True)
 for m in ms:
  mk(m)
  if atk(kq[1-s],s): um();continue
  v=-qs(-be,-a,ply+1);um()
  if v>best:
   best=v
   if v>a: a=v
   if a>=be: break
 return best if best>-IF else -MA+ply
def sr(dep,a,be,ply):
 if dep<=0: return qs(a,be,ply)
 if (nd[0]&2047)==0 and nd[0]>=BG: ST[0]=True
 if ST[0]: return ev()
 nd[0]+=1
 chk=ich(s)
 ent=tt.get(zk);ttm=0
 if ent:
  ed,ef,es,em=ent;ttm=em
  if ed>=dep and ply>0:
   if ef==0: return es
   if ef==1 and es>=be: return es
   if ef==2 and es<=a: return es
 ms=gm()
 if not ms: return -MA+ply if chk else 0
 ms.sort(key=lambda m: osc(m,ttm,min(ply,127)),reverse=True)
 a0=a;best=-IF;bm=0;i=0;lc=0
 for m in ms:
  gchk=False
  cp0=b[(m>>7)&127]
  mk(m)
  if atk(kq[1-s],s): um();continue
  if zk in LK:
   v=rp(-ev())
  else:
   if not chk: gchk=ich(s)
   LK.add(zk)
   rd=dep-1+gchk
   if i>=3 and dep>=3 and not chk and not gchk and not cp0 and not (m>>14)&7 and not m&EF: rd-=1
   if i==0: v=-sr(rd,-be,-a,ply+1)
   else:
    v=-sr(rd,-a-1,-a,ply+1)
    if v>a:
     if rd<dep-1+gchk: v=-sr(dep-1+gchk,-a-1,-a,ply+1)
     if v>a and v<be: v=-sr(dep-1+gchk,-be,-a,ply+1)
   LK.discard(zk)
  um()
  if ST[0]: return best if best>-IF else ev()
  lc+=1
  if v>best:
   best=v;bm=m
   if v>a:
    a=v
   if a>=be:
    if not b[(m>>7)&127] and not (m>>14)&7 and not m&EF:
     kk=KL.setdefault(ply,[])
     if m in kk: kk.remove(m)
     kk.insert(0,m);del kk[2:]
    break
  i+=1
 if lc==0: return -MA+ply if chk else 0
 fl=0 if a0<best<be else (2 if best<=a0 else 1)
 tt[zk]=(dep,fl,best,bm)
 return best
def root():
 global LK
 LK=set(RP);LK.add(zk)
 nd[0]=0;ST[0]=False
 legal=gm()
 if not legal: return None
 bm=legal[0];order=legal[:]
 for dep in range(1,64):
  order.sort(key=lambda m: m==bm,reverse=True)
  a=-IF;best=-IF;nbm=bm;aborted=False
  for i,m in enumerate(order):
   mk(m)
   if atk(kq[1-s],s): um();continue
   if zk in LK:
    v=rp(-ev())
   else:
    LK.add(zk)
    if i==0: v=-sr(dep-1,-IF,-a,1)
    else:
     v=-sr(dep-1,-a-1,-a,1)
     if v>a: v=-sr(dep-1,-IF,-a,1)
    LK.discard(zk)
   um()
   if ST[0]: aborted=True;break
   if v>best: best=v;nbm=m
   if v>a: a=v
  if aborted: break
  bm=nbm;order=legal[:]
  if nd[0]>=BG: break
 return bm
def sn(q): return 'abcdefgh'[q&7]+str((q>>4)+1)
def tu(m):
 u=sn(m&127)+sn((m>>7)&127);pt=(m>>14)&7
 if pt: u+='nbrq'[pt-2]
 return u
def fm(u):
 for m in gm():
  if tu(m)==u: return m
 return None
URL=os.environ.get('MAKEFUN_ENV_URL','')
def po(path,body):
 data=json.dumps(body).encode()
 rq=Request(URL+path,data=data,headers={'Content-Type':'application/json'})
 try:
  with urlopen(rq,timeout=30) as r: return json.loads(r.read().decode())
 except Exception: return {}
def su(st):
 global RP
 RP=set()
 fen(st.get('start_fen') or 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
 RP.add(zk)
 for u in st.get('moves') or []:
  m=fm(u)
  if m is None: break
  mk(m);RP.add(zk)
def play():
 st=po('/game',{})
 while st:
  if st.get('status')!='your_move': break
  su(st)
  m=root()
  if m is None: break
  st=po('/move',{'game':st.get('game'),'move':tu(m)})
  if st.get('status')!='your_move':
   ng=st.get('next_game')
   if ng: st=po('/game',{'game':ng})
   else: break
if __name__=='__main__':
 play()
