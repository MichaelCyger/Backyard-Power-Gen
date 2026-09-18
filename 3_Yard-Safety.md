# Yard safety

**Chapters:** [1. The Need](1_The-Need.md) · [2. The Idea](2_The-Idea.md) · **3. Yard Safety** · [4. The House](4_The-House.md) · [5. The Vault](5_The-Vault.md) · [6. The Approval](6_The-Approval.md) · [7. The Swap](7_The-Swap.md) · [8. Vault Spec](8_Vault-Spec.md) · [9. The Fuel](9_The-Fuel.md) · [10. The Proofs](10_The-Proofs.md)

← [Previous: 2. The Idea](2_The-Idea.md) · [Start](README.md) · [Whole book as a PDF](Backyard-1.4.pdf) · **Next:** [4. The House](4_The-House.md) →

---

## The claim

The yard stays usable: grass, a walk, a playset. The Backyard Generating Station sits under **ten feet of soil**, inside a lead-lined concrete vault. That cover is the same idea as other tanks American yards already bury (septic tanks, underground propane, heating-oil tanks). Ten feet on the lid is on the deep side of that habit, closer to a large buried fuel tank than to a shallow septic lid.

The extra dose is meant to be **a few mrem a year if a person lived on the grass over the vault, all day, every day**. That is the conservative number: someone camping on that spot for 8,760 hours. Nobody does that. A playset is an hour here and there. At one hour a day for a year, the extra is a **small fraction of one cross-country flight**, not a flight.

That is the design target. The vault does the stopping. The ten feet of dirt is extra. The numbers in this chapter, and in Chapter 8, are written as if that dirt washed off. If the lawn is still safe with a bare lid, it is safe with a playset on ten feet of soil.

![Site section: playset, soil, vault, house](diagrams/01-site-section.svg)

---

## What a few mrem means

Dose is how much radiation energy a body absorbs. The everyday US unit is the **mrem** (millirem: one-thousandth of a rem). People already get a dose every year from the sky, the dirt, and the air in the house. That ordinary background in the United States is on the order of **300 mrem a year**. It is higher in the mountains than at the coast. It changes from house to house.

A few mrem a year on top of that, **for a person who lived on the grass**, is about **one percent of background**, or less. That full-time lawn number is in the same size class as **one cross-country flight**. It is far below the usual public limit for a licensed source, which is **100 mrem a year** from that source.

**A note on the units.** mrem is a yearly kind of number when we talk about a lawn. A survey meter on the grass reads a *rate* (how hard it is right now). Multiply that rate by the hours you actually stand there, and you get the year’s extra. The design uses the hardest case: every hour of the year on that spot. A playset uses a slice of those hours.

One hour a day is 365 hours out of 8,760, about **4% of the year**:

```
a few mrem/year (if you lived there) × (365 / 8,760) ≈ 0.15 to 0.2 mrem/year
```

That is about **one-fifteenth to one-twentieth of one coast-to-coast flight**.

| What | About how much | What that means |
| --- | --- | --- |
| Ordinary US background | ~300 mrem/year | Sky, dirt, and house air. Already happening. |
| Extra if a person *lived* on the grass over the vault, 24/7 | a few mrem/year, if it is measurable at all | The design target. About 1% of background. About one cross-country flight, spread over the whole year. |
| Extra for a child on a playset ~1 hour a day | ~0.15 to 0.2 mrem/year | A fraction of one flight, not a flight. |
| Public limit from a licensed source | 100 mrem/year | A ceiling, not a goal. The vault is built well below it. |
| Cross-country flight | a few mrem | One trip. Same size as the *live-on-the-lawn* number, much larger than the playset number. |

Nothing shields to zero, and the yard already has background. **The vault is built so the lawn does not become a special place.** You should not need a fence or a keep-off sign.

---

## What has to be stopped

The vault holds a small nuclear core. While it is on, two kinds of radiation try to leave: **gammas** (like very hard X-rays) and **neutrons** (heavy, uncharged particles from splitting atoms). After it is shut down, leftover heat fades and the neutron problem fades with it. Gammas from the used fuel stay inside the same vault. Chapter 9 is what those neutrons are doing in the core, and why graphite and boron are in the story.

Gammas are stopped by dense things. Lead and thick concrete are the point of the lining. A few inches of lead and a thick concrete wall cut gammas by a huge factor. Ten feet of dirt on top cut them again.

Neutrons are the harder yard problem. They do not care much about lead. They slow down when they hit light atoms, especially **hydrogen**. That slowing is called moderation. Once they are slow, boron or more hydrogen can catch them. Wet dirt has water, and water is hydrogen. Dry dirt has much less.

So:

- **The vault** (lead, concrete, and a hydrogen-rich layer such as concrete or a boron mix) is the shield that has to work on its own.
- **The soil** is a bonus layer. Wet soil is a better bonus than dry soil, because of that hydrogen.
- **Dry soil is the worse case.** Neutrons travel farther in dry sand or a drought-baked lot than in damp ground. The dose on the grass must still be a few mrem a year in that worse case, and with the lid bare. Wet years and ten feet of cover are then extra margin, not the thing you counted on.

If someone built a thin vault and counted on ten feet of damp dirt to do the real work, a dry summer or a washed-out lid would show it. That is not this design. The vault is sized as if the dirt dried out and then left.

---

## How it sits in the hole

**Ten feet down** means **ten feet of soil above the lid**, not ten feet to the middle of the core. The vault is about eight and a half feet tall, about the size of a large septic tank. The hole is deeper than that: vault plus ten feet of cover, on the order of eighteen feet to the pad. Towns already permit deep buried tanks. The grass still only sees a **10 by 10 foot** patch. How far that patch sits from the house is a local permit question, the same as a septic tank or a buried propane tank.

The vault is the object the crane sets. It is sealed. Nobody on the lot opens it. Heat and power leave through pipes and cables, not through a hatch in the lid.

Those pipes and cables do not come out the top, under the playset. They leave through the **bottom** of the vault, then turn and run sideways in a buried **chase** toward the house. A chase is just that buried run: two heat pipes and a few wires in a trench, the same idea as a sewer lateral or a buried propane line.

That path is a design choice, for these reasons:

- Radiation that finds a hole prefers a straight line. A hole in the lid would point at the grass. A hole in the floor points at more earth.
- Earth is a thick, cheap dump. What goes down is swallowed by dirt and water in the soil.
- The chase then bends (down, over, then toward the house) so there is no straight shot back up to the lawn.
- The house still gets heat and power. The connections are at the house end of the chase, in the utility room, where a plumber and an electrician already work.

A particle can bounce. The underside chase makes the easy path point into the ground, and it keeps holes out of the lid. Frost, wet soil, and a path a crew can service at the house end are ordinary buried-line problems. They do not put a hole under a child’s feet.

---

## Why a playset is the right test

A playset is hours, not minutes, and it is children, and it is right on the grass. If that is acceptable, a walk across the yard is not a special event.

The dose target is a yearly number on the grass **as if someone lived there**. A child on a playset is a few feet higher than the grass. Air does not shield much, so each hour on the set is about the same as an hour on the lawn, maybe a little less because they are farther from the lid.

They are not living on the set. One hour a day is about 4% of the live-there number. If living on the grass is a few mrem a year (about one flight), the playset year is a **fraction of that flight**. The rest of their year (the house, the car, an actual flight, a town at a different altitude) already moves the number by more than the playset does.

Two practical rules sit next to the physics:

- **Do not pin the playset to the vault.** The swing set sits on the ten feet of soil, on shallow footings or a pad, the way it would over a buried tank. Do not drive long posts down until they hit the concrete lid. The lid is not a footing.
- **Do not make the dirt do the real work.** Ten feet of cover is the story you tell. The vault still has to meet the lawn number if a flood washes that dirt off.

The playset is allowed because the number on the grass is small, the vault does not depend on the swing set being somewhere else, and the pipe openings are aimed at dirt, not at the slide.

---

## If the top two feet go away

Yards get dug. Yards flood. Two feet of soil can leave.

With ten feet above the lid, two feet gone still leaves eight feet of dirt, plus the whole vault. Losing a couple of feet of soil might make the lawn number a few times higher (dirt cuts dose in layers; take away a layer and more gets through). A few times a number that was already “a few mrem, if anything” is still a small add to background, **if the vault was the real shield**.

If the vault was thin and the dirt was doing the work, two feet gone is a different story. That is why dry soil and a bare lid are design cases, not surprises.

Flood water itself is extra shield. The risk in a flood is **scour**: dirt washed off the lid. The vault should still meet the lawn target with the lid bare, sitting in a washed-out hole. Then a playset after a storm is a mud cleanup. The dose target still holds.

If a machine hits the concrete, that person is on the box, not on the lawn. That contact number is a crew-and-design number. It is not the playset number. A vault built to stand alone stays low there too. A vault that needed the dirt would not.

Soil right against the vault can pick up a little short-lived activity if neutrons leak, which is why the vault’s own neutron layer exists. The top two feet of lawn are not that layer. Washing them off does not bring “the hot dirt” to the swing, unless the scour goes all the way to the wall.

---

## What you would measure

On an intact yard, a meter on the grass should read like the rest of the lot, or a faint bump over the lid that is still in the noise of background. Background already wiggles from day to day.

You would not design for a special fence, a keep-off sign, or a rule that the kids play on the other side of the driveway. If those were required, the vault is too thin.

Startup happens after the hole is backfilled and the chase is closed. Until then the core is locked off and is not making this kind of dose. At the end of life the locks go back in before the crane comes. The lawn number is a *running, buried* number.

---

## What this chapter covered

This is the yard chapter: ten feet of soil above the lid, the vault as the shield, wet dirt better than dry dirt, pipes out the bottom through a buried chase, and a playset as the test. The claim is a few mrem a year extra **if a person lived on the grass**, which is about one cross-country flight; a playset hour a day is a fraction of that flight. Later chapters can put a real shield stack on a drawing. If children cannot play on the grass, the vault is not thick enough.

---

You have finished chapter 3 of 10.

**Next chapter:** [4. The House](4_The-House.md)

← [Previous: 2. The Idea](2_The-Idea.md) · [Start](README.md) · [Whole book as a PDF](Backyard-1.4.pdf) · **Next:** [4. The House](4_The-House.md) →

**Chapters:** [1. The Need](1_The-Need.md) · [2. The Idea](2_The-Idea.md) · **3. Yard Safety** · [4. The House](4_The-House.md) · [5. The Vault](5_The-Vault.md) · [6. The Approval](6_The-Approval.md) · [7. The Swap](7_The-Swap.md) · [8. Vault Spec](8_Vault-Spec.md) · [9. The Fuel](9_The-Fuel.md) · [10. The Proofs](10_The-Proofs.md)

