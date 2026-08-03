# Launch asset system

Every asset has one job. Together they form the release campaign without
turning the Agent into Wall Street theater.

| Asset | Job | Composition | Design restraint |
|---|---|---|---|
| `hero.png` | README first impression and repository identity | Buffett on the right; decision copy on the left | No stock ticker, money, logo, or fabricated quotation |
| `poster.png` | Main launch poster and shareable vertical key art | Monumental archive portrait with a quiet title field | Dignity over celebrity spectacle |
| `social-card.png` | GitHub social preview | 2:1 crop with legible repository identity | Reads at thumbnail size |
| `demo.gif` | Dynamic product demonstration | Question → risk frame → named artifacts → result | Shows method, not simulated model magic |
| `teaser.gif` | Short promotional loop | Agent 002 reveal → anti-quote-bot claim → capability verbs | Campaign energy without guaranteed outcomes |
| `diagrams/01-decision-lens.svg` | Explain the core transformation | Haste and noise pass through four decision lenses | No false certainty |
| `diagrams/02-capability-clusters.svg` | Explain all twelve callable Skills | Four balanced capability families around one human core | Skills remain tools, not personality |
| `diagrams/03-mode-router.svg` | Teach when Skills activate | Four conversation modes with visible Skill limits | Ordinary conversation stays human |
| `diagrams/04-quality-loop.svg` | Explain response governance | Draft → quality gate → revise/release/fallback | One revision, then bounded behavior |
| `diagrams/05-hall-of-fame-network.svg` | Connect the Agent to HoloFame Studio | One Agent joins a governed multi-Agent roundtable | Standalone package does not replace Studio integration |

## Art direction

- Palette: parchment `#E7D8B5`, paper `#F2E9D4`, aged brass `#B99352`,
  oxblood `#7E1F2B`, charcoal `#0B0A09`.
- Typography: editorial serif for durable judgment; compact mono labels for
  evidence, status, and system metadata.
- Motifs: archival folders, compounding curves, margin boundaries, an empty
  partner chair, and owner-level documents.
- Forbidden motifs: cash rain, ticker walls, crystal balls, official Berkshire
  trade dress, unverified quotations, luxury signaling, and victory poses.

## Provenance and rebuilding

`source/hero-master.png` and `source/poster-master.png` were generated with the
built-in OpenAI image generation tool from a local identity reference, then
reviewed for subject, composition, trademarks, text, and campaign fit. They
contain no generated text. Final typography, borders, crops, GIF timing, and
color treatment are deterministic outputs of `scripts/build-media.py`.

Rebuild with Python 3 and Pillow:

```bash
python scripts/build-media.py
```

The artwork is an independent interpretive campaign asset. It is not an
official photograph, endorsement, or Berkshire Hathaway asset.
