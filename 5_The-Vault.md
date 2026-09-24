# The Vault

**Chapters:** [1. The Need](1_The-Need.md) · [2. The Idea](2_The-Idea.md) · [3. Yard Safety](3_Yard-Safety.md) · [4. The House](4_The-House.md) · **5. The Vault** · [6. The Approval](6_The-Approval.md) · [7. The Swap](7_The-Swap.md) · [8. Vault Spec](8_Vault-Spec.md) · [9. The Fuel](9_The-Fuel.md) · [10. The Proofs](10_The-Proofs.md)

← [Previous: 4. The House](4_The-House.md) · [Start](README.md) · [Whole book as a PDF](Backyard-1.5.pdf) · **Next:** [6. The Approval](6_The-Approval.md) →

---

The vault is the sealed box in the hole. Chapter 3 is why the lawn stays a lawn. Chapter 4 is how heat and power leave through the floor. This chapter is what is inside, why it can sit closed for on the order of a century, and why it is furnace-scale rather than a commercial plant. Chapter 9 is the fuel itself: composition, core makeup, how sodium moves, first principles, and how the reaction is meant to stop.

A 1,000 MW plant is a million kilowatts. This vault makes **5 to 10 kWe** of electricity and about **20 to 40 kW of heat**. That is about **1/100,000 to 1/200,000** the electrical size of the plant people picture. It is furnace scale, not campus scale.

---

## What the box is

From the outside the vault is a lead-lined concrete object about the size of a large septic tank, about eight feet across and eight and a half feet tall, under **ten feet of soil**. A crane can lift it. Nobody on the lot opens it. The lid has no hatch for the owner. Pipes and cables leave through the bottom only, into the buried chase that runs to the utility room.

Inside, in layers:

- **A small core** at the center: a beer-keg-to-dishwasher-sized assembly that holds the fuel
- **A hydrogen-rich and boron-bearing layer** that slows and catches neutrons (the particles that do not care much about lead)
- **Lead and thick concrete** that stop gammas (the hard X-ray-like radiation)
- **The sealed outer vault** the crane sees

The dirt above the lid is extra. The vault is sized to do the stopping on its own, including in dry soil and with the lid bare. Chapter 3 is that argument.

![Vault vertical cutaway](diagrams/08-vault-cutaway.svg)

![Radial shield stack](diagrams/02-radial-stack.svg)

---

## How it makes power

The core is a very small nuclear core. Heat comes from splitting atoms in a sealed fuel, at a scale closer to a large home furnace than to a commercial station.

That kit is not invented here. Coated particle fuel (TRISO), heat pipes, and small Stirling engines have been built and tested for space and shop programs. This product would license that class of hardware, or build it from those proven designs. It is not a space reactor placed in a yard, and it is not a new kind of reaction.

That heat does two jobs at the same time. It becomes electricity for the panel. It is also warmth for floors, showers, or a greenhouse. Using both is the design. If the house or a greenhouse uses the warmth, most of what the core makes is used, not thrown away.

A house-scale electrical output of **5 to 10 kWe** (kilowatts of electricity) goes with about **20 to 40 kW of heat** from the core. That is furnace scale. There is no cooling tower. After shutdown, leftover heat drops to about as much as a small space heater, then lower over hours and days. Dirt, concrete, and time can take that.

### From heat in the core to electricity in the house

There is no water flowing through the core, and no steam turbine.

1. **The fuel makes heat.** Tiny coated particles of uranium sit in graphite blocks. About 20% of that uranium is U-235, the isotope that splits easily. The rest is U-238. There are no swimming-pool rods and no open water in the core.
2. **Sealed heat pipes move that heat.** Each pipe is a closed metal tube with a little sodium inside. Sodium is a metal that melts and carries heat very well. When the core is warm, sodium vapor travels to the cool end of the pipe and gives the heat up. It then returns on its own. There is no pump in the vault. The sodium never mixes with house water. If one pipe fails, that tube freezes in place. The others keep working. The core does not “dry out” the way a water reactor can.
3. **A sealed exchanger in the vault floor** hands the heat to a double-wall oil loop. That oil runs through the buried chase to the utility room and back. If the oil leaks, the leak stays in the trench or the utility room. It is a hazardous-fluid cleanup, not an open core.
4. **Stirling engines in the utility room** turn the hot oil and a cool water loop into electricity. A Stirling is a sealed engine with a hot side and a cool side. No flame, no steam, no turbine. Five small units make about 8 kW, with a spare. They last on the order of 10 to 15 years. They live in the utility room on purpose, because a 100-year sealed engine inside the vault has not been shown. Replacing them is a room job, not a yard opening.
5. **Leftover warmth** (about 27 kW on the type unit) goes to house floors, a tank, a greenhouse, or a small outdoor radiator in summer.

If the oil pump or the Stirling units stop, heat has nowhere to go except the vault and the dirt. Temperature at the heat-pipe ends rises. Control drums spring shut, without a phone or a motor that has to stay on. Leftover heat then soaks into the 42-ton box and the earth.

The core is run **cold and slow**: a trickle of heat in a lot of mass. That is how a sealed life on the order of a century is even thinkable. The neutron battering that ages metal in a big plant is much gentler here because the power in each liter of core is small.

---

## The paint-can of fuel

Fuel use at this output, over a century, is measured in kilograms, not tons. Chapter 8 works the inventory: about **30 kilograms (about 66 pounds) at first start**, still a paint-can of heavy metal inside the core, inside the vault. By the end of life, on the order of **15 to 25 kilograms has been used up**. Chapter 9 is what that paint-can is made of (coated particles, graphite, about 20% U-235) and why it is not a water-plant fuel rod. The vault is almost all shield and box. The crane is for the box.

Material mixed into the fuel is used up as the fuel is used up, so the output stays even. There is no refueling truck. There is no hatch. At the end, what cannot be recycled is still in that paint-can size class at a licensed site (Chapter 7).

The fuel is assembled in the factory, in a shutdown state, and never handled on the lot.

---

## Why it stays put

A commercial plant needs staff, pumps, and a tower because leftover heat after shutdown is enormous. Here leftover heat is a space heater. The earth is the sink. The vault does not rely on a pump staying on.

If power is pulled faster or slower, the battery and the inverter in the utility room take the jump. The core is not asked to follow the dryer. It makes a steady trickle.

If the core ever tries to run away (a sudden rise in splitting), the fuel and the geometry are chosen so heat itself slows the reaction: hotter means less splitting, in milliseconds, without a person or a motor. That is a materials fact, not a software mode. That passive slowing is the ordinary protection. Chapter 9 is the Doppler picture, the drum springs, and the cases that do and do not shut the core down. It is why the last-ditch glass layer below is not expected to run.

If the vault ever got far hotter than it should anyway, a passive layer above the core is meant to melt, flow, and set into a glass-like mass that stills the reaction and locks the insides in place. The whole vault stays one object. That is last-ditch only. The fuel and the drums are designed so the vault does not get there.

---

## Off on the truck, on in the hole

Fresh fuel has never been used, so it is not already hot. In the factory the core is assembled with **locks and control elements in the shutdown position**. The vault is sealed around that. What leaves the plant is a heavy, closed object that is not producing electricity and not producing heat.

It is trucked as permitted heavy freight. A crane sets it. Chapter 4’s crew connects the utility room. Inspectors sign.

Only after it is buried and the chase is closed does a **licensed startup** happen. The shutdown locks are released in a controlled procedure. That is the first time the core makes heat. Until that step the vault is cold. At the end of life the same locks go back in before the crane returns. The vault that rides out is shut down on purpose, the same way it rode in.

The owner does not hold the key to those locks. A phone app, if there is one, does not move them. Chapter 2’s app is a status screen only.

---

## What the vault is not

There is no cooling tower, no staff gate, and no refueling floor.

The owner does not open it to service it. There is no filter, hatch, or oil change in the yard.

It is not safe because the dirt is deep. It is safe because the box is thick, the pipes leave through the floor, the power is furnace-scale, and the locks stay in until a licensed person releases them. Ten feet of soil is the yard you see. The vault still has to meet the lawn dose target if that soil leaves.

It is a 20 to 40 kW heat source in a factory-sealed vault, about 1/100,000 the electrical size of a 1,000 MW plant. That size is the approval argument (Chapter 6).

---

## What this chapter covered

This is the vault: layers, furnace-scale heat, two products (electricity and warmth), heat pipes to an oil chase to Stirling engines in the utility room, a paint-can of fuel, no pumps you service in the yard, a glass dump that is not expected to run, and a truck that carries a locked box. Chapter 3 is the grass. Chapter 4 is the utility room. Chapter 6 is the stamp. Chapter 9 is the fuel and the first principles. Chapter 10 is the proof plan. The machine is designed so the yard never needs a hatch.

---

You have finished chapter 5 of 10.

**Next chapter:** [6. The Approval](6_The-Approval.md)

← [Previous: 4. The House](4_The-House.md) · [Start](README.md) · [Whole book as a PDF](Backyard-1.5.pdf) · **Next:** [6. The Approval](6_The-Approval.md) →

**Chapters:** [1. The Need](1_The-Need.md) · [2. The Idea](2_The-Idea.md) · [3. Yard Safety](3_Yard-Safety.md) · [4. The House](4_The-House.md) · **5. The Vault** · [6. The Approval](6_The-Approval.md) · [7. The Swap](7_The-Swap.md) · [8. Vault Spec](8_Vault-Spec.md) · [9. The Fuel](9_The-Fuel.md) · [10. The Proofs](10_The-Proofs.md)

