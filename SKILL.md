---
name: qdq-logo
description: Generate professional SVG logos and logo showcase presentations. Use when the user wants to: (1) Create a logo for their product/brand, (2) Generate multiple logo design concepts, (3) Create interactive logo showcase webpages, (4) Export logos in SVG format. Supports geometric patterns, dot matrix designs, line systems, and mixed compositions. Generates clean, minimal, high-end logo designs following modern design principles.
---

# QDQ Logo Generator

Generate professional SVG logos and interactive showcase presentations for products and brands.

## Workflow

### Phase 1: Information Gathering

Collect essential information from the user:

1. **Product/Brand Name** (required)
2. **Industry/Category** (e.g., AI, fintech, design tools)
3. **Core Concept** (e.g., connection, flow, security, simplicity)
4. **Design Preferences** (optional):
   - Style: minimal/complex, geometric/organic
   - Color preference: monochrome/specific colors
   - Mood: cold/warm, professional/friendly

Ask concise questions to gather this information.

### Phase 2: Generate Logo Variants

Based on gathered information, generate **at least 6 design variants** following these principles:

**Design Principles (Critical):**
- **Extreme Simplicity**: 1-2 core elements maximum
- **Generous Negative Space**: At least 40-50% of canvas empty
- **Precise Proportions**: Line weights 2.5-4px (in viewBox 0 0 100 100)
- **Visual Tension**: Use intentional asymmetry
- **Restraint**: Pure forms, no unnecessary decoration
- **Single Focal Point**: Clear visual hierarchy
- **Structural Stability**: Dense lines or thick strokes

**Variant Allocation (ensure diversity):**
1. **Pure geometric** (1): Clean shapes, no dots/lines
2. **Dot matrix** (1): Circle/rounded rect/capsule/hexagon dots
3. **Line system** (1): Lines, curves, or waves
4. **Mixed: dots + geometry** (1): Dots filling/forming shapes
5. **Mixed: lines + geometry** (1): Lines accenting geometric forms
6. **Node network or layered** (1): Multi-element composition

### Phase 3: Create Interactive Showcase

Generate an HTML showcase page using the template in `assets/showcase_template.html`:

1. Replace `{{PRODUCT_NAME}}` with the brand name
2. Replace `{{TAGLINE}}` with a relevant tagline
3. Replace `{{LOGO_COMPONENTS}}` with React SVG components
4. Replace `{{LOGO_DATA}}` with logo metadata array
5. Replace `{{SHOWCASE_SECTION}}` (optional) with showcase images
6. Replace `{{YEAR}}` with current year

### Phase 4: Export and Deliver

1. Save showcase HTML to workspace
2. Start local HTTP server: `python3 -m http.server <port>`
3. Take screenshot using Playwright
4. Send PNG image to user via Discord/message tool
5. Provide SVG code for selected designs if requested

## SVG Best Practices

- Use `viewBox="0 0 100 100"`
- Center around `(50, 50)`
- Leave 10-15 units padding from edges
- Use `currentColor` for fills/strokes
- Group related elements with `<g>`
- Use `<defs>` and `<use>` for repeated elements

## Design Patterns Reference

See `references/design_patterns.md` for detailed:
- Dot matrix systems (concentric rings, grids, capsules, hexagons)
- Geometric shapes (circles, arcs, boolean operations, polygons)
- Line systems (horizontal fills, waves, spirals)
- Node networks
- Combination strategies
- Letter/symbol integration

## Example Usage

**User**: "Design a logo for 'AI Pioneer'"

**Process**:
1. Acknowledge request (AI industry, pioneering/exploration concept)
2. Read `references/design_patterns.md` for inspiration
3. Generate 6 variants:
   - Pioneer Compass (geometric)
   - Neural Constellation (dot matrix)
   - Horizon Lines (line system)
   - Pioneer Path (mixed)
   - Converge (mixed)
   - Pulse Rings (layered)
4. Create showcase HTML using `assets/showcase_template.html`
5. Screenshot and send PNG to user

## Output Format

Deliver:
- PNG showcase image (Discord-friendly)
- HTML file (for interactive viewing)
- Individual SVG files (if requested)