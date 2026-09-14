"""Build the public observer figure and its relationship-level honesty record."""
from pathlib import Path
import json
from html import escape

HERE=Path(__file__).resolve().parent

def build():
    data=json.loads((HERE/'observer-map.json').read_text(encoding='utf-8'))
    records={r['id']:r for r in data['relationships']}
    assert len(records)==15 and all(r['sources'] and r['logic'] and r['conditions'] and r['failure'] for r in records.values())
    sources=json.loads((HERE/'observer-sources.json').read_text(encoding='utf-8'))
    assert all(s in sources for r in records.values() for s in r['sources'])
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1560" height="1760" viewBox="0 0 1560 1760" role="img" aria-labelledby="title description">',
        '<title id="title">The observer in the world — the Murray Research Programme</title>',
        '<desc id="description">A scoped physical loop connects a system, accessible signals, retained record, estimated state, prediction, decision and action. Measurements can be selected at a cost. Identifiability, predictive sufficiency and attainable action value are separate gates. Biological self-maintenance and subjective experience remain extensions or open questions. A separate human-reviewed evidence loop revises the map. Every relationship E01 to E15 is explained with sources and limits in HONESTY.md.</desc>',
        '<defs><linearGradient id="bg" x2="1" y2="1"><stop stop-color="#071723"/><stop offset="1" stop-color="#102d35"/></linearGradient><pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#b0d0d8" stroke-opacity=".04"/></pattern><marker id="arrow" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0 0L9 4.5L0 9" fill="#71d4ca"/></marker><marker id="amber" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0 0L9 4.5L0 9" fill="#ecc58b"/></marker></defs>',
        '<rect width="1560" height="1760" fill="url(#bg)"/><rect width="1560" height="1760" fill="url(#grid)"/>',
        '<style>text{font-family:Arial,Helvetica,sans-serif;fill:#e6f1ef} .label{font-size:24px;fill:#aac6ca}.id{font-family:monospace;font-size:24px;fill:#71d4ca}.path{fill:none;stroke:#71d4ca;stroke-width:3;marker-end:url(#arrow)}.open{fill:none;stroke:#ecc58b;stroke-width:2;stroke-dasharray:7 7}</style>']
    def text(x,y,body,size=28,fill=None,extra=''):
        color=f' style="fill:{fill}"' if fill else ''
        svg.append(f'<text x="{x}" y="{y}" font-size="{size}"{color} {extra}>{escape(body)}</text>')
    text(75,65,'DANIEL JOHN MURRAY / THE MURRAY RESEARCH PROGRAMME',24,'#a5c8c9')
    text(70,136,data['title'],58)
    text(75,182,data['subtitle'],27,'#b9d6d4')
    svg.append('<rect x="50" y="226" width="1460" height="800" rx="18" fill="#0b202a" stroke="#32505a"/>')
    text(80,267,'ONE PHYSICAL WORLD · DECLARE THE DOMAIN, DO NOT ASSUME COMPLETENESS',22,'#a5c8c9')
    svg.append('<path d="M540 290H1440V913H85V607H540Z" fill="#72cdb8" fill-opacity=".035" stroke="#557e79" stroke-dasharray="6 7"/>')
    text(565,308,'OBSERVER DESCRIPTION',22,'#b0d9cb')
    for node in data['nodes']:
        x,y,w,h=[node[k] for k in ['x','y','w','h']]
        svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#102e38" stroke="#4b737a"/>')
        text(x+18,y+27,node['tag'],17,'#8ac6be')
        text(x+18,y+66,node['title'],31)
        for i,line in enumerate(node['lines']):text(x+18,y+103+29*i,line,21,'#bed0d1')
    paths=[('E01','M445 388H590',466,363),('E02','M920 388H1060',950,363),
           ('E03','M1225 472V680',1242,552),('E04','M1060 756H920',952,736),
           ('E05','M590 756H455',485,736),('E06','M290 680V472',306,545),
           ('E07','M755 680V472',770,520)]
    for rid,d,x,y in paths:
        svg.append(f'<path d="{d}" class="path"/><text x="{x}" y="{y}" class="id">{rid}</text>')
    text(320,577,'intervene',20,'#a8c7c7')
    text(783,550,'choose a reading',21,'#a8c7c7')
    text(105,882,'E09  Physical self-maintenance: a biological model still to earn.',24,'#ecc58b')
    text(100,971,'E08  BOUNDS + COMPOSITION',25,'#71d4ca')
    text(550,971,'Conservation · resources · units · order · calibrated operations',24,'#c2d7d8')
    text(78,1084,'THREE TESTS BETWEEN A PLAUSIBLE PICTURE AND A USEFUL MODEL',25,'#b0d0d0')
    cards=[(80,'E13','CAN WE TELL THEM APART?',['Distinct states can produce','the same accessible record.']),
           (570,'E14','DOES THE FUTURE DIFFER?',['Retain a distinction when it','changes a declared prediction.']),
           (1060,'E15','CAN AN ACTION HELP?',['Perfect information still has','an attainable decision ceiling.'])]
    for x,rid,title,lines in cards:
        svg.append(f'<path d="M{x} 1114H{x+420}" stroke="#71d4ca" stroke-width="3"/>')
        text(x,1158,rid,24,'#71d4ca');text(x,1197,title,23)
        for i,line in enumerate(lines):text(x,1235+31*i,line,24,'#b4ced0')
    text(80,1335,'A SECOND LOOP: REVISE OUR KNOWLEDGE OF THE FIRST',25,'#b0d0d0')
    for x,title,sub in [(80,'Results + counterexamples','Retain successes and failures'),(580,'Review the evidence','Check premises and scope'),(1080,'Version the shared map','Update affected relationships')]:
        svg.append(f'<rect x="{x}" y="1364" width="390" height="106" rx="8" fill="#152e36" stroke="#5a7578"/>')
        text(x+17,1405,title,27);text(x+17,1442,sub,22,'#b4ced0')
    svg.append('<path d="M470 1415H580M970 1415H1080" class="path"/>')
    text(497,1389,'E11',22,'#71d4ca');text(996,1389,'E12',22,'#71d4ca')
    svg.append('<path d="M1275 1470V1494H275V1470" class="path"/>')
    text(585,1489,'E12 · next discriminating test',18,'#71d4ca')
    text(80,1535,'Human-reviewed revisions · source-bound connections · no automatic promotion to scientific law',24,'#b4ced0')
    svg.append('<path d="M80 1558H1480" stroke="#3b5a60"/>')
    text(80,1594,'E10  SUBJECTIVE EXPERIENCE REMAINS AN OPEN QUESTION',25,'#ecc58b')
    text(80,1635,'No loop shape, simulation or associative algebra establishes consciousness.',25,'#c3cece')
    text(80,1698,'EVERY E-NUMBER → HONESTY: DERIVATION · SOURCE · ASSUMPTIONS · FAILURE',23,'#71d4ca')
    text(80,1737,'Version '+data['version']+'  /  Conceptual research map; current implementation is a local finite-model prototype.',20,'#9cbdc0')
    svg.append('</svg>')
    (HERE/'observer-world-loop.svg').write_text('\n'.join(svg)+'\n',encoding='utf-8')
    md=['# Honesty: what each connection is allowed to claim','',
        '**The figure is an evidence-indexed research map, not a proof of the whole programme.** Each E-number below identifies a relationship, its derivation or source, its assumptions and what could invalidate its use.','',
        '[View the full diagram](observer-world-loop.svg) · [Programme direction](PROGRAMME_DIRECTION.md) · [41 manuscript records](https://boundedness-atlas.madmanmuzza.chatgpt.site/papers/)','',
        '## How to read the map','',
        'Read the physical loop from system to signal, record, estimated state, future/decision, action and back to the system. The observer is part of that physical world. The lower evidence loop describes how researchers revise the account; it is not another physical law or an autonomous discovery service. The three middle gates separately ask whether a distinction is observable, predictive and useful for control.','',
        'The solid arrows show declared mathematical/model relationships, not blanket empirical certification. The outlined observer description is a modelling boundary. Physical self-maintenance is a required biological extension; subjective experience remains open. Nothing here identifies a sensory record, a Bayesian belief or a diagram with conscious experience.','',
        '## Present implementation and publication boundary','',
        'A local finite enzyme-model prototype now exercises noisy observation, joint uncertainty over state/mechanism/calibration, future prediction, paid measurement and terminal action. Tests distinguish sensor ambiguity from missing predictive state and from limited control opportunity. A form-specific observation can improve identification and prediction while adding little decision value. Exact conditional information ceilings now check whether a proposed improvement target is attainable before further policy search.','',
        'Those are scoped local model results. This page releases the conceptual relationships and the elementary decision-ceiling derivation, not the private experiment code, unpublished mechanisms, clinical evidence or a public reproducibility package. The numerical research is not presented here as independently published validation. Manuscript citations below identify the author’s programme sources and their stated premises; they are not independent replications.','',
        '## Relationship index','',
        '| ID | Relationship | Evidence type |','|---|---|---|']
    for r in records.values():md.append(f"| [{r['id']}](#{r['id'].lower()}) | {r['title']} | {r['kind']} |")
    for r in records.values():
        md += ['',f"<a id=\"{r['id'].lower()}\"></a>",f"## {r['id']} · {r['title']}",'',
               '**Status:** '+r['kind']+'.','',r['logic'],'','**Required conditions:** '+r['conditions'],'',
               '**Failure or limit:** '+r['failure'],'','**Sources:** '+ '; '.join(f"[{sources[s]['title']}]({sources[s]['url']}) — {sources[s]['location']}" for s in r['sources'])+'.']
    md += ['', '## How the centrepiece evolves', '',
        'The editable source is [observer-map.json](observer-map.json), with citations in [observer-sources.json](observer-sources.json). Run `python build_observer_map.py` to generate the image and this page together. This regeneration does not verify the science. A human reviews any change in claims, source scope or evidence class before publication.','',
        'Keep relationship IDs stable. New laboratory cases attach to an existing relationship when its assumptions fit; otherwise introduce a scoped new relation with an explicit bridge. Record what result prompted a revision and which downstream claims depend on it. Preserve old versions and failed tests. Split a node when the current representation merges a distinction needed by an admitted future or action; merge nodes only after a sufficiency test. An additional line on the figure is not itself a discovery.','',
        'A Möbius strip would identify points with a specific twist and non-orientable surface structure. The current directed information/action graph establishes none of that. It therefore remains a directed loop with a distinct evidence-revision cycle. If a later mathematical model requires a different topology, that change needs its own definition, derivation and evidence; a visual resemblance is insufficient.','',
        'The next biological bridge should specify real measurements, physical internal resources and feasible actions. It should check attainable improvement before optimizing a sensor or controller, then test whether a costly distinction can be acquired while the relevant action is still available. The system should earn this extension through results, not expand merely to fill a diagram.','',
        'No single Lean score can certify this map. A proof assistant can check a formal implication under formal assumptions. Numerical checks, model adequacy, empirical calibration, causal identification and novelty require their own evidence.','',
        '## Version record','',f"- {data['version']}: replaced the small organising illustration with a large relationship-indexed observer map; added distinct identifiability, predictive-sufficiency and decision-ceiling gates; retained biological self-maintenance and experience as explicitly unfinished questions."]
    (HERE/'HONESTY.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
    print('Built 6 nodes, 15 indexed relationships; SVG and Honesty page share one ledger.')

if __name__=='__main__':build()
