# Version history

High-level log of the Backyard Generating Station book (chapters 1 through 10). Notes files (`100_Notes.md`, `_writing_style.md`) are not part of the compiled book.

**Current version: 1.5**

The compiled reading copy is `Backyard-{version}.pdf` (currently `Backyard-1.4.pdf`). Rebuild it with `python3 build_pdf.py` after you change a chapter. The filename follows `VERSION` in `build_pdf.py`.

When you ship a new version, add a section at the top of the list below. Say what a reader would notice, not every line edit. Bump the number on this page, in `build_pdf.py`, and in `README.md`. The next build writes a new file named for that number.

---

## 1.5 — 24 September 2026

The public entry says what the book is, in a few lines, and what green means.

**What a reader would notice**

- README opens on the house, the vault, and a plain definition of green: carbon-free electricity and heat at the house, and power that does not stop when the sun goes down
- The same definition appears once in Chapter 2, where the solar tax-credit argument already lives
- Walk-away numbers stay on the README: output, dose, cost, and what is still ahead

**Locked product is unchanged.** Chapter 8 numbers are unchanged.

---

## 1.4 — 18 September 2026

Contact is LinkedIn, not an email address.

**What a reader would notice**

- Title page, README, and LICENSE: message on LinkedIn (`linkedin.com/in/cyger`). No email
- GitHub reading guide and chapter jump links from 1.3 are unchanged

**Locked product is unchanged.** Chapter 8 numbers are unchanged.

---

## 1.3 — 17 September 2026

Copyright, license, and a public-facing stamp. Locked engineering is unchanged.

**What a reader would notice**

- Title page and page footers: copyright Michael Cyger, concept design basis. No “Confidential. Not for distribution.”
- Not a DIY build. Not a licensed plant or appliance
- LICENSE: read and share with attribution; no commercial use; no patent grant. Commercial use needs a written license
- README carries the same version number as this file and the PDF

**Locked product is unchanged.** Chapter 8 numbers are unchanged.

---

## 1.2 — 9 September 2026

Chapter 10: an honest proof plan. Closed arithmetic on the page. Handbook bounds that are not a signed result. Open rows that still need codes, tests, or a stamp.

**What a reader would notice**

- New chapter, **10 The Proofs**, after the fuel chapter. Dual audience: house sentence, then the method and the pass number
- Every design claim restated as a proof item: Closed, Bound, or Open
- Closed pieces finished in the open: power, burnup inventory, fission rate, decay-heat fit, pipe count vs 35 kW, oil flow, vault mass vs float, playset ratio, fluence order of magnitude
- Handbook bounds that are not a substitute for transport: tenth-value layers, inverse square, Carnot 47% vs Stirling 25%
- Doppler traced from “hotter means less splitting” to the negative net-power-coefficient rule and DB-11, with no fake coefficient and no invented k-effective
- Outside work named with the spec or test: MCNP/SCALE/ORIGEN, heat-pipe stands, ASME/ASCE, 10 CFR 71 Type B, AGR/HTGR fuel data, glass-dump furnace, licensed cold-critical, UL/IEEE/NFPA, 10 CFR 20/70/73/74, NQA-1
- 10 CFR 53 exists (final rule effective 29 April 2026) as an optional **commercial plant** path, including microreactors. It is not a house-appliance stamp. Chapter 6’s product certificate still does not exist
- Five new drawings (Figures 22 to 26)
- Chapter 8 §16 points at Chapter 10. If they disagree, Chapter 8 still wins for engineering

**Locked product is unchanged.** Chapter 8 numbers are unchanged. This version does not claim the Open rows are green.

---

## 1.1 — 9 September 2026

Chapter 9: the fuel, the core, sodium in the heat pipes, first principles, shutdown, and a short contrast with US water plants and sodium fast reactors.

**What a reader would notice**

- New chapter, **9 The Fuel**, after the spec. Dual audience: homeowner story first, then the mechanism
- Thirteen new drawings (Figures 9 to 21): TRISO particle, particle-to-core, core makeup, heat pipe, fission, neutron life, thermal vs fast, chemistry, shutdown ladder, PWR/BWR/BGS, two sodiums, scale, Doppler
- Type stated in the open: heat-pipe microreactor, TRISO-UCO, graphite moderator, thermal spectrum. Not a fast reactor. Not a water plant
- Sodium is milliliters in 24 sealed pipes, not a pumped pool. TerraPower Natrium (Kemmerer, Wyoming, construction 2026) is the pool: 345 MWe fast, about 40,000 times BGS-8
- Shutdown as a ladder: Doppler, drums, size plus earth, glass dump last
- Honest limit: the stack is the safety case; a 100-year yard life is still a specification
- Chapters 2 to 8, the notes file, and the writing-style order now point at Chapter 9 for fuel physics
- If Chapter 9 and Chapter 8 disagree, Chapter 8 still wins for engineering

**Locked product is unchanged.** Chapter 8 numbers are unchanged. This version is the explanation chapter the spec was missing.

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
