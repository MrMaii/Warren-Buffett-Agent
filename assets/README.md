# Archive Plate and frosted-glass visual system

This release has one reviewed **Archive Plate**. The supplied 1536×1024
artwork is the source of truth: its charcoal stone field, warm bronze editorial
type, right-side portrait window, archival grain, calibration marks, coordinates,
date, and identity labels are already composed into the finished image.

The README presents that primary plate once. The other static PNGs are
distribution slots, not additional editorial content.

| Asset | Role | Format | Constraint |
|---|---|---|---|
| <code>source/hero-master.png</code> | Compatibility source slot | Exact supplied 3:2 plate | Byte-identical to <code>source/poster-master.png</code> |
| <code>source/poster-master.png</code> | Compatibility source slot | Exact supplied 3:2 plate | Byte-identical to <code>source/hero-master.png</code> |
| <code>hero.png</code> | README primary visual | Exact 1536×1024 plate | No crop, redraw, or overlay |
| <code>poster.png</code> | Launch surface | Exact 1536×1024 plate | Same reviewed composition |
| <code>social-card.png</code> | GitHub preview surface | Exact 1536×1024 plate | Same reviewed composition |
| <code>demo.gif</code> | Motion study | 3:2 plate with quiet drift | No generated copy or second layout |
| <code>teaser.gif</code> | Motion study | 3:2 plate with quiet drift | No generated copy or celebrity treatment |

## Shared diagram system

Both Agent repositories use the same six diagram roles, dimensions, framing,
palette, type hierarchy, grain layer, hairline border, and frosted-glass cards.
Only the evidence counts, method language, capability names, and Agent identity
change.

| Slot | Shared purpose |
|---|---|
| <code>01-method-lens.svg</code> | Turn pressure or product noise into the Agent's ordered judgment |
| <code>02-evidence-chain.svg</code> | Show source → observation → claim → runtime → test → behavior |
| <code>03-capability-clusters.svg</code> | Group the twelve Skills around the human core |
| <code>04-mode-router.svg</code> | Show relational, exploratory, task, and high-stakes boundaries |
| <code>05-quality-loop.svg</code> | Show release, violation, upstream repair, and bounded fallback |
| <code>06-studio-network.svg</code> | Show one Agent entering the larger Hall of Fame Studio |

The visual grammar is deliberately quiet and archival:

- charcoal and stone backgrounds, warm bronze edges, parchment cards, and
  muted copper for exceptions;
- editorial serif for identity and judgment, restrained mono for metadata;
- translucent layered panels, inner hairlines, corner calibration marks, and
  a subtle grain filter to create a frosted-glass archive surface;
- no blue or violet AI gradients, automatic focus boxes, generated poster copy,
  ticker walls, cash rain, luxury signaling, keynote spectacle, Berkshire
  Hathaway trade dress, or victory poses.

## Provenance and rebuilding

The master was supplied as a finished external design and reviewed locally.
Typography and composition are locked inside the source plate. The media
builder copies the master unchanged to the three static PNG surfaces and creates
only restrained motion studies. The diagram builder deterministically creates
the six shared SVG roles from this Agent's profile.

<pre><code>npm run media:build
npm run diagrams:build</code></pre>

The artwork is an independent interpretive campaign asset. It is not an
official photograph, endorsement, or Berkshire Hathaway asset.
