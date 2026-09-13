# The Boundedness Atlas

[![Enter the Boundedness Atlas](dist/assets/entrance.jpg)](https://boundedness-atlas.madmanmuzza.chatgpt.site)

## [Enter the Atlas →](https://boundedness-atlas.madmanmuzza.chatgpt.site)

Daniel John Murray’s research programme, presented by connected ideas: bounded composition, predictive state, temporal action, biological capacity, useful intervention and evidence.

- **41 manuscript records**, with abstracts and closing sections reviewed.
- **8 connected contributions**, each with a statement of evidence and scope.
- **41 research families + 41 original numbered items**, overlapping rather than independent discoveries.
- A source index across **471 prediction-bearing main-text pages**, with manuscript hashes and page addresses.
- A focused **biology conservatory**, beginning with the difference between apparent recovery and recoverable capacity.

The site distinguishes conditional mathematics, simulations, secondary analyses and prospective hypotheses. It does not certify global novelty, independent proof verification or universal predictive accuracy. Historical claims and corrections remain visible.

## Rebuild

Python 3, standard library only:

```sh
python build_site.py
python -m http.server 4173 --directory dist
```

Reviewed content lives in `content/atlas.json`; authored assets live in `dist/assets`, `dist/style.css` and `dist/app.js`. `build_site.py` regenerates pages and the public data download. No API keys or hosted AI calls are required. Source receipts refer to the supplied local manuscript revisions; online SSRN parity is not certified.

The previous [Empirical Observatory](https://github.com/thantiklermcirony/empirical-observatory) and [programme architecture](https://github.com/thantiklermcirony/empirical-architecture) remain preserved. Private research has not been included.

Artwork: three original AI-generated botanical illustrations. Exact prompts are recorded in `IMAGE_PROMPTS.json`. They are creative illustrations, not scientific data.

No new blanket license is applied to the author’s manuscripts or pre-existing work. Consult their individual source terms; the Atlas grants no rights over cited third-party material.
