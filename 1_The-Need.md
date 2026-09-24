# The need

**Chapters:** **1. The Need** · [2. The Idea](2_The-Idea.md) · [3. Yard Safety](3_Yard-Safety.md) · [4. The House](4_The-House.md) · [5. The Vault](5_The-Vault.md) · [6. The Approval](6_The-Approval.md) · [7. The Swap](7_The-Swap.md) · [8. Vault Spec](8_Vault-Spec.md) · [9. The Fuel](9_The-Fuel.md) · [10. The Proofs](10_The-Proofs.md)

[Start](README.md) · [Whole book as a PDF](Backyard-1.6.pdf) · **Next:** [2. The Idea](2_The-Idea.md) →

---

The United States is asking the grid to do two jobs at once, and it is falling behind on both.

It must make a lot more electricity: data centers, factories, electric cars, and houses switching from gas heat to electric heat. Demand that sat almost flat for twenty years is now pointed up. One recent national forecast puts use on the order of **20% higher by 2030** and **about 40% higher by the mid-2030s** ([ICF, 2026](https://www.icf.com/news/2026/06/icf-report-rising-us-electricity-demand-press-release)). Spare generating capacity above what planners already need is already thin, a few percent of the fleet. Some of the biggest regional grids have little or no extra room.

It must also keep the lights on with wires, poles, and buried cables that were treated as permanent and are not. In 2024 the average US customer sat through about **11 hours** without power, nearly twice the yearly average of the decade before. Major weather did most of that damage. Even in ordinary years, with the big storms stripped out, the average customer still loses about **two hours** ([US Energy Information Administration](https://www.eia.gov/todayinenergy/detail.php?id=66744)).

Those two facts meet at the house. The bill is rising because new plants and new wires cost money. The outages are rising because the old plant and the old wires are failing, or because the utility turns the power off on purpose when wind and dry brush make a live line a fire starter. A house that can keep its own power on is how you stay cool in a heat wave, warm in a freeze, and alive if the machine in the bedroom needs a wall outlet.

The Backyard Generating Station is one answer to that need: power made at the house, compared at the same meter to rooftop solar. This chapter is the need, not the machine.

---

## The country is short of new power

For a long stretch, US electricity use barely grew. Efficiency hid new gadgets. That stretch is over.

The new load is lumpy and fast. A single data-center campus can ask for as much power as a small city. Car chargers and heat pumps add house by house. Seattle City Light, to take one utility that has said this publicly, expects electrical demand in its territory to **double in about twenty years**, and it is already shopping for new wind, solar, and geothermal because the old hydro will not cover it ([Seattle Times, Aug. 16, 2026](https://www.seattletimes.com/seattle-news/politics/fixing-seattles-power-outages-continues-a-1960s-class-divide/)). That utility also needs new substations at a couple hundred million dollars each, and a multi-billion-dollar dam upgrade. The pattern is national: more load, long lead times, and towns that do not want a 1,000 MW plant next door.

When load grows faster than plants and transmission, two household results follow. Rates go up to pay for what does get built. Reserve margin goes down, so a hot afternoon or a cold week has less slack. Chapter 2 puts numbers on the bill. The need underneath those numbers is simple: the country is trying to electrify more of life on a grid that was not sized for that, and that is not being rebuilt at the same pace.

---

## The wires are old, in many cities at once

Outages are not only hurricanes. They are also 1960s cable that was buried as if it would last forever.

Seattle is a clean example because the paper trail is public. More than **300 miles** of underground cable are decades past useful life. Replacing them is pegged at more than **$2 billion** over at least 15 years. Average restoration time went from **78 minutes in 2014** to **145 minutes in 2024**, even with big weather events taken out, which put that utility in the worst quarter of the country for getting the lights back on. Neighborhoods that buried lines in the 1960s and 1970s for looks now lose power over and over. One Queen Anne household logged more than 20 outages after 2021, including six in the first half of a single year. A “run to failure” habit (keep rates low, fix it when it breaks) is what a former utility chief called the worst reliability she had seen in her career. The cables were never a permanent object. There was no fund waiting when the bill came due ([Seattle Times](https://www.seattletimes.com/seattle-news/politics/fixing-seattles-power-outages-continues-a-1960s-class-divide/)).

That is one city. The same aging-and-weather pattern shows up across the map:

- **Texas, February 2021.** A winter storm and a grid that could not keep generation online left millions of homes dark in a freeze. The state later counted **246** storm-related deaths. Most were hypothermia. Others were carbon monoxide from grills and generators, house fires from space heaters, and people whose oxygen, dialysis, or other electric medical gear stopped ([Texas DSHS](https://www.dshs.texas.gov/sites/default/files/news/updates/SMOC_FebWinterStorm_MortalitySurvReport_12-30-21.pdf); [Texas Tribune](https://www.texastribune.org/2021/03/25/texas-deaths-winter-storm/)).
- **Houston and the Gulf, July 2024.** Hurricane Beryl knocked out more than **2.1 million** CenterPoint customers, about three-quarters of that territory. Restoration ran about **11 days** ([CenterPoint after-action](https://www.centerpointenergy.com/en-us/Documents/GHRI%20Tracker/CenterPoint_Beryl_After_Action_Final_Report.pdf)). EIA’s national 2024 spike is, in large part, Beryl plus Helene plus Milton ([EIA](https://www.eia.gov/todayinenergy/detail.php?id=66744)).
- **Carolinas and Florida, 2024.** Helene and Milton took down transmission, distribution, and substations. South Carolina’s average customer lost on the order of **50 hours** that year, an outlier that is still a real year in a real state ([EIA](https://www.eia.gov/todayinenergy/detail.php?id=66744)).
- **California, on purpose.** Utilities turn lines off when wind and dry fuel make a spark into a fire. A Public Safety Power Shutoff can run a day or two, sometimes longer, across many counties at once. Oregon, Colorado, Idaho, and Hawaii have copied the tool ([CPUC on PSPS](https://www.cpuc.ca.gov/psps/)). The wire is aging and the climate is drier. The tool they use is a planned blackout.
- **Portland metro, January 2024.** Ice and wind took out hundreds of thousands of customers. Some sat in the cold for about a week. At least ten deaths were tied to that week: hypothermia, trees, lines, fires ([KGW](https://www.kgw.com/article/news/local/the-story/pge-rate-hike-power-outage-winter-storm-january-2024/283-93f2ccf9-c4ff-4e4d-942d-80cd83976788)).

The national scoreboard is the EIA reliability tables: with major events included, the average customer’s yearly minutes without power jumped from **342 in 2023** to **611 in 2024**. Strip the major events and you still have about **two hours** a year of ordinary failure, the everyday signature of trees, old cable, and deferred maintenance ([EIA Table 11.3](https://www.eia.gov/electricity/annual/html/epa_11_03.html)).

The same aging-cable problem is not limited to Seattle. It is what “run to failure” looks like when the failure arrives in a lot of cities in the same decade.

---

## The same story, elsewhere

Aging plants and thin reserve are not only an American problem.

**Spain and Portugal, April 28, 2025.** A voltage collapse took down most of the Iberian grid, the worst European blackout in about twenty years. Portugal’s transmission was back in about 12 hours. Spain’s took about 16. Elevators, trains, and hospitals ran on whatever backup they had. The official investigation is public ([ENTSO-E expert panel](https://eepublicdownloads.blob.core.windows.net/public-cdn-container/clean-documents/Publications/2025/iberian-blackout/Final%20Report%20on%20the%20Grid%20Incident%20in%20Spain%20and%20Portugal%20on%2028%20April%202025.pdf)).

**South Africa, years on end.** Eskom’s aging coal fleet could not meet load, so the country lived on scheduled “load shedding”: hours a day, by neighborhood, for years. When the plants run better, the blackouts ease. When they do not, the schedule returns. That is what a generation shortfall looks like as an everyday schedule, not a one-week storm ([Eskom system updates](https://www.eskom.co.za/eskoms-winter-2025-power-system-outlook-loadshedding-is-expected-to-be-avoided-provided-unplanned-maintenance-remains-below-13gw/)).

**Puerto Rico.** After Hurricane Maria and through the years after, an old, storm-hit grid left households on diesel and long dark stretches. It is a US territory living the end state of deferred rebuild.

The point for a US house is that a rich country is not exempt. If the plants are late and the wires are past their life, outages become ordinary. Seattle’s 15-year cable program and South Africa’s load-shedding calendar are the same problem at different speeds: not enough working infrastructure for the load that is already there.

---

## How uptime saves lives

Electricity is no longer only lights and television. For a growing share of households it is a medical device, a climate-control system, and the pump that keeps water clean. When it stays on, people are less likely to die from what follows the outage: a dark house in a heat wave, a freeze, or a medical device that stops.

**Heat.** Air conditioning is life-safety equipment in a heat wave. Older adults, infants, and people on certain medicines cannot dump heat. A multi-day outage in July is not an inconvenience. It is a medical event in the living room. The house that keeps 8 kW on through that week is a house that keeps people out of the ER.

**Cold.** Texas 2021 is the large, counted case: hundreds of deaths, most from the house going as cold as the street. Portland 2024 is the smaller cousin. Space heaters and ovens used as furnaces start fires. The deaths are hypothermia and the fire, not “the storm” in the abstract.

**Home medical gear.** HHS tracks Medicare beneficiaries who live at home on electricity-dependent equipment: oxygen concentrators, ventilators, BiPAP, home dialysis, infusion pumps, powered beds and chairs, implanted heart-assist devices. That electricity-dependent group is **over 3 million** people. Count those plus people who need dialysis, tank oxygen, home health, or hospice and the at-risk total is **over 4.6 million**, in every state, down to the ZIP code ([HHS emPOWER](https://empowerprogram.hhs.gov/empowermap)). That list is Medicare only. It misses children (the Queen Anne household whose son’s air purifier dies in the night), working-age adults on a CPAP or a fridge full of insulin, and anyone whose pharmacy cold-chain sits in a kitchen refrigerator. Hours without power is enough. Days is a hospital trip or worse.

**The generator that kills.** When the grid dies, people drag out gasoline generators, run cars in garages, and light grills indoors. Texas counted **19** carbon monoxide deaths in that one freeze. Uptime at the panel is how those people never start the motor.

**Water and waste.** City pumps, well pumps, and lift stations run on electricity. After a long outage you get boil-water notices, dead sewage pumps, and a house that cannot flush. Infection and dehydration follow the dark, especially for the same people already on medical gear.

**The rest of the street.** Traffic lights, cell sites, and 911 answering all have hours of battery or diesel, not weeks. A house that stays up does not restore the city. It keeps the people in that house off the overwhelmed hospital list while the city is down.

Seattle’s story already has the small version: a toddler who coughs when the purifier stops, a parent who cannot keep the house warm, a remote class that assumes the wall outlet works. Scale that by 4.6 million Medicare households and by every heat wave and ice storm, and keeping power on is a public-health issue.

---

## What this means at one house

A typical house uses about 10,000 to 12,000 kWh a year. A high-use house can run $400 to $600 a month. Chapter 2 does the bill math, including rates that are already climbing.

The need under that math is uptime and capacity in the same object.

Rooftop solar at that house makes power when the sun is out. In a heat wave that can help in the afternoon. At night, in an ice storm, in a week of coastal weather, or during a Public Safety Power Shutoff, the array is a cold roof. A battery helps for hours, not for a Texas week, unless something is still filling it.

The Backyard Generating Station is sized to keep filling that battery in the dark: 5 to 10 kWe, plus heat the house can use. It does not replace a national rebuild of 300 miles of Seattle cable or a new 1,000 MW plant. It is how one family stays on while that rebuild is 15 years out, and how that family adds a slice of supply the country is short of, at the place the load already is.

If the country is heading into a decade or two of tight reserve and old wires, the house that can run through an outage is the house that does not add a hypothermia death, a heat stroke, a silent oxygen concentrator, or a generator in the garage to the tally.

---

## What this chapter covered

This is the need: more electricity, older wires, longer dark hours, and a medical dependence on the outlet that did not exist at this scale when the 1960s cable went in. The examples are Seattle, Texas, Houston, the Carolinas, California, Portland, and the same failure mode abroad. The life-safety case is heat, cold, home medical gear, carbon monoxide, and water. Chapter 2 is the product and the payback.

---

You have finished chapter 1 of 10.

**Next chapter:** [2. The Idea](2_The-Idea.md)

[Start](README.md) · [Whole book as a PDF](Backyard-1.6.pdf) · **Next:** [2. The Idea](2_The-Idea.md) →

**Chapters:** **1. The Need** · [2. The Idea](2_The-Idea.md) · [3. Yard Safety](3_Yard-Safety.md) · [4. The House](4_The-House.md) · [5. The Vault](5_The-Vault.md) · [6. The Approval](6_The-Approval.md) · [7. The Swap](7_The-Swap.md) · [8. Vault Spec](8_Vault-Spec.md) · [9. The Fuel](9_The-Fuel.md) · [10. The Proofs](10_The-Proofs.md)

