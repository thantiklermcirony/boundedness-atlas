"""Elementary identity/fixture checks, not proof of biological application."""
import math, json
from pathlib import Path
from fractions import Fraction as F
root=Path(__file__).resolve().parent
checks=[]
rendered_values=[]
for p in (F(1,5),F(4,5)):
    L=F(3); post=p*L/(1-p+p*L)
    s=2*p-1; e=(L-1)/(L+1)
    assert (s+e)/(1+s*e)==2*post-1
    assert abs(math.atanh(float(2*post-1))-math.atanh(float(s))-.5*math.log(3))<1e-12
    checks.append({'prior':float(p),'posterior':float(post)})
    rendered_values.append(f'{float(post):.6f}')
for n in (1,2,3):
    r=(F(3,2)**(2*n)-1)/(F(3,2)**(2*n)+1)
    value=math.tanh(n*math.log(1.5))**2
    assert abs(float(r*r)-value)<1e-12
    checks.append({'pairs':n,'reflectance':value})
    rendered_values.append(f'{value:.6f}')
def cr(v):
    a,b,c,d=v
    return (a-c)*(b-d)/((a-d)*(b-c))
q=list(map(F,(1,2,3,4))); qp=[(2*x+1)/(x+2) for x in q]
assert cr(q)==cr(qp)
assert (F(1)-1)/(F(1)+1)==(F(10)-10)/(F(10)+10)
data=json.loads((root/'observer-lens-ledger.json').read_text(encoding='utf-8'))
idx={s['key']:s for s in json.loads((root/'observer-lens-source-index.json').read_text(encoding='utf-8'))}
assert len(idx)==41
md=(root/'OBSERVER_LENS.md').read_text(encoding='utf-8')
for value in rendered_values:
    assert value in md, f'Published fixture missing or wrong: {value}'
for p in data['panels']:
    assert f'id="{p["id"].lower()}"' in md
    assert p['failure'] and p['status']
    for key,pages in p['sources'].items():
        assert idx[key]['selected_layers'][p['id']]==pages
print(json.dumps({'identity_checks':'pass','panels':len(data['panels']),'source_records':len(idx),'fixtures':checks},indent=2))
