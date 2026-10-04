"""Eigenes Wort-RNN mit vollständigen Dialogen und Antwortgewichtung."""
from pathlib import Path
import argparse,json,re
import numpy as np
p=argparse.ArgumentParser();p.add_argument('--steps',type=int,default=16000);a=p.parse_args()
root=Path(__file__).parent; text=(root/'training.txt').read_text()
def tokenize(s):return re.findall(r'\n|[^\W_]+|[^\s\w]',s,flags=re.UNICODE)
tokens=['<unk>']+sorted(set(tokenize(text))); ids={s:i for i,s in enumerate(tokens)}
dialogs=[]
for d in text.split('§'):
 if d.strip():
  seq=tokenize('§\n'+d.strip()+'\n');dialogs.append(np.array([ids[t] for t in seq]))
H=96;V=len(tokens);rng=np.random.default_rng(27)
W=rng.normal(0,.07,(H,V));U=np.linalg.qr(rng.normal(size=(H,H)))[0]*.85;O=rng.normal(0,.04,(V,H));b=np.zeros((H,1));c=np.zeros((V,1))
params=[W,U,O,b,c];cache=[np.zeros_like(v) for v in params];smooth=0
for step in range(a.steps):
 seq=dialogs[int(rng.integers(len(dialogs)))];xs=seq[:-1].copy();ys=seq[1:];L=len(xs)
 split=next((i for i in range(L-1) if tokens[xs[i]]=='KI' and tokens[xs[i+1]]==':'),L)
 if step%5==0:
  for t in range(2,max(2,split-1)):
   if tokens[xs[t]] not in ['Mensch',':','\n'] and rng.random()<.025:xs[t]=0
 hs=np.zeros((H,L+1));D=np.zeros((V,L));loss=0;total=0
 for t,(x,y) in enumerate(zip(xs,ys)):
  hs[:,t+1]=np.tanh(W[:,x]+U@hs[:,t]+b[:,0]);z=O@hs[:,t+1]+c[:,0];z-=z.max();pr=np.exp(z);pr/=pr.sum()
  weight=1. if t>=split+1 else .15
  loss-=weight*np.log(max(float(pr[y]),1e-12));total+=weight;pr[y]-=1;D[:,t]=weight*pr
 R=np.zeros((H,L));dh=np.zeros(H)
 for t in reversed(range(L)):
  R[:,t]=(O.T@D[:,t]+dh)*(1-hs[:,t+1]**2);dh=U.T@R[:,t]
 dW=np.zeros_like(W)
 for t,x in enumerate(xs):dW[:,x]+=R[:,t]
 grads=[dW,R@hs[:,:L].T,D@hs[:,1:].T,R.sum(axis=1,keepdims=True),D.sum(axis=1,keepdims=True)]
 for v,g,m in zip(params,grads,cache):
  np.clip(g,-3,3,out=g);m+=g*g;v-=.035*g/np.sqrt(m+1e-8)
 value=loss/total;smooth=value if not step else .99*smooth+.01*value
 if step%1000==0:print(step,round(smooth,3),flush=True)
model={'tokens':tokens,'kind':'word-rnn','hidden':H,'W':W.tolist(),'U':U.tolist(),'O':O.tolist(),'b':b[:,0].tolist(),'c':c[:,0].tolist(),'steps':a.steps,'loss':smooth,'training_chars':len(text),'training_dialogues':len(dialogs)}
(root/'model.json').write_text(json.dumps(model,ensure_ascii=False));print('Wortmodell gespeichert',V,'Wörter und Zeichen')
