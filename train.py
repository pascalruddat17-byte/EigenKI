"""Eigenes Zeichen-RNN: zufällige Gewichte, BPTT und Adagrad, keine API."""
import argparse, json
from pathlib import Path
import numpy as np

p=argparse.ArgumentParser()
p.add_argument('--steps',type=int,default=2500)
a=p.parse_args()
root=Path(__file__).parent
text=(root/'training.txt').read_text()
chars=sorted(set(text)); ids={c:i for i,c in enumerate(chars)}
data=np.array([ids[c] for c in text]); V=len(chars); H=48
rng=np.random.default_rng(7)
W=rng.normal(0,.04,(H,V)); U=rng.normal(0,.04,(H,H)); O=rng.normal(0,.04,(V,H))
b=np.zeros((H,1)); c=np.zeros((V,1))
params=[W,U,O,b,c]; cache=[np.zeros_like(v) for v in params]
pos=0; h=np.zeros((H,1)); smooth=np.log(V)
for step in range(a.steps):
    if pos+65>=len(data): pos=0; h=np.zeros_like(h)
    xs=data[pos:pos+64]; ys=data[pos+1:pos+65]; pos+=64
    states=[h]; probs=[]; loss=0.
    for x,y in zip(xs,ys):
        h=np.tanh(W[:,x:x+1]+U@h+b); states.append(h)
        z=O@h+c; z-=z.max(); pr=np.exp(z); pr/=pr.sum()
        probs.append(pr); loss-=np.log(max(float(pr[y,0]),1e-12))
    grads=[np.zeros_like(v) for v in params]; dW,dU,dO,db,dc=grads
    dh=np.zeros_like(h)
    for t in reversed(range(len(xs))):
        dy=probs[t].copy(); dy[ys[t]]-=1
        dO+=dy@states[t+1].T; dc+=dy
        raw=(O.T@dy+dh)*(1-states[t+1]**2)
        db+=raw; dW[:,xs[t]:xs[t]+1]+=raw; dU+=raw@states[t].T; dh=U.T@raw
    for v,g,m in zip(params,grads,cache):
        np.clip(g,-5,5,out=g); m+=g*g; v-=.07*g/np.sqrt(m+1e-8)
    smooth=.99*smooth+.01*loss/len(xs)
    if step%250==0: print(step,round(smooth,3),flush=True)
model={'chars':chars,'hidden':H,'W':W.tolist(),'U':U.tolist(),'O':O.tolist(),'b':b[:,0].tolist(),'c':c[:,0].tolist(),'steps':a.steps,'loss':smooth}
(root/'model.json').write_text(json.dumps(model,ensure_ascii=False))
print('Gespeichert: model.json')
