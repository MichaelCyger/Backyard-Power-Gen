# Version history

High-level log of the Backyard Generating Station book (chapters 1 through 8). Notes files (`100_Notes.md`, `_writing_style.md`) are not part of the compiled book.

**Current version: 1.0**

The compiled reading copy is `Backyard-{version}.pdf` (currently `Backyard-1.0.pdf`). Rebuild it with `python3 build_pdf.py` after you change a chapter. The filename follows `VERSION` in `build_pdf.py`.

When you ship a new version, add a section at the top of the list below. Say what a reader would notice, not every line edit. Bump the number on this page and in `build_pdf.py`. The next build writes a new file named for that number.

---

## 1.0 — 23 August 2026

First complete book. Confidential. Not for distribution. Not patent pending.

**What 1.0 is**

- Chapters 1 to 7: the homeowner story (need, idea, yard safety, house, vault, approval, swap)
- Chapter 8: the engineering design basis for type unit BGS-8
- Eight diagrams in `diagrams/`
- A compiled PDF of those eight chapters: `Backyard-1.0.pdf`

**What a reader would notice**

- Title page: Version, then date, then the product line, then author and email. Equal space from the date to the description and from the description to the author. Confidential. Not for distribution.
- Footer on every page: Confidential. Not for distribution. · Version 1.0 · date · author
- Stirling set is its own first-cost line (five 2 kWe units in the utility room). Factory-scale all-in after a 30% credit is **$50,000 to $90,000**. Decade engine swaps are called out and are not in simple payback.
- Soil above the lid is a fixed **10 ft (3.0 m)**. Dose is still designed with the lid bare. Compared to other buried yard tanks
- Grass footprint of the vault: about **10 by 10 feet**. Setbacks left to local permitting
- House-side gear is the **utility room** (in the house or a small shed)
- App is status only. No storm toggle
- A **chase** is defined: the buried pipe run from the underside of the vault to the utility room
- Heat path is written in order: core, sealed sodium heat pipes, oil chase, Stirling engines in the utility room. No turbine. No water in the core
- Playset sits on the soil, not on posts into the lid
- Swap: an existing house stays on the utility while the crew digs. Homeowner dark window is hours. New-build install can take days
- Size contrast: 5 to 10 kWe is about **1/100,000 to 1/200,000** the electrical size of a 1,000 MW plant
- Fuel language: **at first start** / **consumed by end of life**
- Chapter closers named **What this chapter covered**
- Chapter 8 keeps the spec tables and adds short plain-language leads. BGS-8 is named as the 8 kWe first type unit. MCNP is defined on first use
- Prose is factual. Clever closers were rewritten so a layman does not have to decode them

**Locked product in this version**

- Name: Backyard Generating Station. Buried object: the vault.
- One house, one meter, compared to a complete rooftop solar-plus-battery job
- Family 5 to 10 kWe. Type unit BGS-8: 8 kWe electricity, 35 kW of heat
- Heat and electricity are two products
- Heavy metal about 30 kg (66 lb) at first start. Paint-can leftover at end of life
- Lawn target: a few mrem a year if someone lived on the grass all day. Vault is the shield. Dirt is bonus
- Factory sealed, never opened on the lot, about a 100-year life, crane-out swap
- Pipes leave through the floor only. Convertor wear lives in the utility room
- Approval ask: size-based manufactured appliance. That stamp does not exist yet

**How the chapters settled**

- Chapter 1 states the public need (short grid, old wires, outages) with inline links
- Chapter 2 sizes the appliance against a typical and a high-use house bill, including rising rates
- Chapter 3 makes the playset-and-grass dose argument
- Chapter 4 connects the vault to the panel, battery, gateway, and heat loop
- Chapter 5 is the vault in plain language
- Chapter 6 is the approval path
- Chapter 7 is the swap and take-back
- Chapter 8 is the closed-arithmetic spec. If Chapter 5 and Chapter 8 disagree, Chapter 8 wins for engineering
