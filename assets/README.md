# Unified Archive Plate media system

This release uses one approved **Archive Plate** for every static campaign
surface. The supplied 1536×1024 artwork is the visual source of truth: its
charcoal stone field, warm bronze editorial typography, right-side portrait
window, corner marks, crosshair, coordinates, date, grain, and identity labels
are already part of the finished image.

| Asset | Job | Format and composition | Constraint |
|---|---|---|---|
| `source/hero-master.png` | Compatibility source slot | Exact supplied 3:2 Archive Plate | Must equal `source/poster-master.png` byte-for-byte |
| `source/poster-master.png` | Compatibility source slot | Exact supplied 3:2 Archive Plate | Must equal `source/hero-master.png` byte-for-byte |
| `hero.png` | README first impression | Exact 3:2 Archive Plate | No crop, redraw, or overlay |
| `poster.png` | Main launch poster | Exact 3:2 Archive Plate | The supplied typography remains locked |
| `social-card.png` | GitHub social preview | Exact 3:2 Archive Plate | Same composition as the main poster |
| `demo.gif` | Motion study | 3:2 plate with subtle archival drift | No added title, box, focus window, or claim |
| `teaser.gif` | Short motion study | 3:2 plate with subtler archival drift | No generated copy or celebrity treatment |
| `diagrams/*.svg` | Explain the Agent and Studio relationship | Operational diagrams | Unchanged by the visual plate update |

## Shared visual grammar

- Ratio: `3:2`; static master and static outputs are `1536×1024`.
- Field: dark charcoal/stone with warm bronze and parchment type.
- Composition: large identity field on the left; narrow vertical portrait window
  on the right; archival metadata and calibration marks around the plate.
- Typography: editorial serif for identity; restrained mono for metadata.
- Excluded: new focus rectangles, automatic title cards, generated quotations,
  logo imitation, ticker walls, cash rain, luxury signaling, Berkshire
  Hathaway trade dress, and victory poses.

## Provenance and rebuilding

The master was supplied as a finished external design and reviewed locally.
Unlike the earlier experimental selective-focus workflow, it contains locked
typography and composition. `scripts/build-media.py` validates that the two
legacy source slots are identical, copies the master unchanged to the three
static PNG surfaces, and creates only quiet 3:2 motion studies for the GIFs.

Rebuild with Python 3 and Pillow:

```bash
npm run media:build
# or: python scripts/build-media.py
```

The artwork is an independent interpretive campaign asset. It is not an
official photograph, endorsement, or Berkshire Hathaway asset.
