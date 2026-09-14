"""Run in the Atlas repository: python render_observer_lens.py.
Rebuilds the exhibit explanation from reviewed records; never validates a claim.
The versioned conceptual illustration is deliberately art-directed separately.
"""
from pathlib import Path
import json
root=Path(__file__).resolve().parent
data=json.loads((root/'observer-lens-ledger.json').read_text(encoding='utf-8'))
sources={s['key']:s for s in json.loads((root/'observer-lens-source-index.json').read_text(encoding='utf-8'))}
panels=data['panels']
nav=' · '.join(f"[{p['id']} {p['title'].split(':')[0]}](#{p['id'].lower()})" for p in panels)+'\n\n'
body=''
for p in panels:
    body+=f"<a id=\"{p['id'].lower()}\"></a>\n\n### {p['id']} · {p['title']}\n\n**{p['status']}.**\n\n{p['text']}\n\n**What would require revision:** {p['failure']}\n\n**Source:** "
    body+='; '.join(f"[{sources[k]['title']}](https://boundedness-atlas.madmanmuzza.chatgpt.site/papers/{k}/) · PDF "+', '.join(map(str,v)) for k,v in p['sources'].items())+'\n\n'
(root/'OBSERVER_LENS.md').write_text(data['introduction']+nav+body+data['closing'],encoding='utf-8')
print(f"Rendered {len(panels)} reviewed layers, version {data['version']}.")
