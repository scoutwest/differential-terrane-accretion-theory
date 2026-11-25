# Differential Terrane Accretion Theory (DTAT): fragments, motion, collision and recession in a young-earth Flood model

**Status:** Draft 1, written 2026-11-25. This is a reorganisation, not new modelling. It merges the DTAT idea from `Noah's Pangea v1` (`Theories.md`; `Model.md` Sections 13.7-13.11) with the clean-room results in `Noah's Pangea v2` (`Model.md` Phases 2, 3, 5 and 6), and adds one new hypothesis from discussion (the fixed-keel crust slip, Section 8). Every carried item is marked **carried**, **recomputed**, **flagged** or **not carried** (Section 11). Nothing here has been re-run from scripts: the v2 numbers are quoted from its logs, the v1 numbers from its text, and the few new numbers are arithmetic done by hand in this draft (marked "hand arithmetic"). No DTAT script exists yet.
**Companion theory:** Cascading Moho Collapse Theory (CMCT), `..\Cascading Moho Collapse Theory (CMCT)\Cascading Moho Collapse Theory (CMCT).md`. CMCT supplies the cause of submergence, the water and the heat constraints. DTAT supplies the sideways motion, the fragments, the collisions and the recession. The interface is in Section 12.
**Nature:** a speculative young-earth creation-science model. Mainstream geoscience rejects its premises. Where a number fails, the failure is stated.

---

## 1. Purpose and scope

**Purpose.** Show one physically possible way that, after a flood caused by submergence (CMCT), today's land, mountains and permanently submerged crust could result from many crustal fragments moving at different speeds, colliding or missing each other, without the runaway-subduction heat of Baumgardner's CPT.

**Core idea (v1 `Theories.md`, kept).** Pangea did not break into a few tidy plates. It broke into hundreds of fragments (terranes and provinces) that moved at different speeds. Fragments that collided while moving fast were pushed up out of the water, as India was pushed into Asia. Fragments that never collided stayed low or submerged, as Zealandia is (about 94% submerged today). The mapped seams between terranes (sutures) are the scars of those collisions.

**What DTAT is for.**
- Fragmentation of the pre-Flood land into provinces and how it moves (kinematics, Sections 6-8).
- Collisions, collision uplift and the ten highest peaks (Section 9).
- Recession as selective, permanent re-emergence (Section 10).
- The slip layer and energy that let crust move (H10) and the origin of the ocean floor left behind (H9) (Sections 7-8).

**What DTAT is not for.**
- It is not the cause of the flood. Submergence is CMCT's (collapse of a layer at the crust base, released water). DTAT's v1 text assumed a keel-loss submergence (CKDT) that CMCT has struck (P9). DTAT now starts from "the land is already submerged, by whatever CMCT supplies."
- It does not supply the water or the heat budget. Those are CMCT's (Section 3).
- It does not cover the post-Flood ice age. That is a separate planned study (CMCT Section 27.5).

---

## 2. Premises and rules

DTAT inherits CMCT's premises unchanged. They are restated here so the file can be read alone; if the two ever differ, CMCT's table is the source.

| ID | Premise or rule |
|----|-----------------|
| P1 | Earth is about 6,000 years old. No radiometric or other deep-time ages are used as inputs, evidence or checks. A number is acceptable only if it is a rate or property from lab or field physics, not an age. **This rules out plate reconstructions built on ages (see Section 11, "not carried").** |
| P2 | Flood at Ussher's AM 1656, about 4,370 years ago. 371 days in total, 150 days of prevailing waters (v1 used a 74-day recession window, Day 150-224). |
| P3 | No "God just did it" steps. Every step needs a physical mechanism and a real-world analogue. |
| P4 | All science must match known data. |
| P5 | Pre-Flood Pangea is low (mountains under 610 m). |
| P6 | Target end state: seven continents, today's ten highest peaks (8,091-8,849 m), isostatic uplift with overshoot and rebound, and a post-Flood ice age (P8). |
| P7 | CPT runaway subduction is rejected. |
| P8 | Leave room for a post-Flood ice age. |
| P9 | **Keel preservation (from CMCT).** No mechanism may conflict with the deep keels (150-250 km) that cratons have today. For DTAT this means: after any motion, each craton must sit over a keel. It does not have to be the keel it started on (Section 8). |
| R1 | Obstacles and failures are written down with their status (Section 14). |
| R2 | Use they/them for anyone whose pronouns are not stated. |
| R3 (DTAT) | Where a v1 and a v2 number disagree, v2 (clean-room) is used unless this file says otherwise. |
| R4 (DTAT) | Illustration is not prediction. A step that animates a known present-day outcome (for example, which provinces are submerged today) must be labelled as such (v1 Section 13.8.5, kept). |

---

## 3. Constraints taken from CMCT and the heat analysis

Not re-derived here. Numbers are from CMCT Section 3 and v2 Phase 1.

- **H1 (area).** Fresh hot oceanic lithosphere exposed to seawater ≲ 3.6×10¹¹ m².
- **H2 (rate).** Heat into the ocean ≲ 4.4×10¹⁸ W averaged.
- **H3 (location).** Heat released deeper than about 10 km does not count against H1 and H2. (Conduction time through 10 km is about 3×10⁶ years.)
- **H4 (no fresh seafloor shortcut).** Today's ocean floor was not freshly made in the Flood.
- **H9 (new floor).** Say how the 1.64×10⁸ km² of ocean floor on continent-bearing plates arose within H1-H3.
- **H10 (motion).** Name the energy and the weak layer that move blocks about 3,800 km in 150 days, with dissipation staying deep and below melting.
- **H11 (keel preservation, from P9).** After the Flood each craton has a keel of 150-250 km. A mechanism must state what it leaves.
- **Budget B** = 1.4×10²⁶ J (ocean limited to 40 °C bulk). B and the 40 °C cap are unverified (CMCT O9).

---

## 4. The fragment layer (data)

All from v2 (clean-room), which re-downloaded the data from the publisher. v1 used the same dataset.

**Source.** Hasterok, Halpin, Hand, Collins, Kreemer, Gard & Glorie (2022), *Earth-Science Reviews*, "New maps of global geologic provinces and tectonic plates"; the authors' repository `github.com/dhasterok/global_tectonics` (GPL-3.0). It has 914 provinces. Filtered to continental and transitional crust: **647 continental provinces and 136 transitional provinces**, 2.105×10⁸ km² together (41.3% of the Earth).
- v2 holds the unmodified download in `Noah's Pangea v2\data\hasterok_2022\` (with `PROVENANCE.md`). This file does not copy it. Use it by path.
- **Area correction (v2 obstacle 5).** The shapefile `area` field is wrong for four provinces (Lhasa Terrane and Gangdese Arc share a value; Karakoram and Ladakh differ by 25-35% from their geometry). v2 recomputed all areas from the polygon geometry. v1 used the shapefile field, so v1's size range (669 to 1,840,575 km²) has not been re-checked against the corrected areas. **Flagged.**
- **Size spread.** Three-plus orders of magnitude (v1), from about 700 km² to about 1.8×10⁶ km².
- **Fragment boundaries.** Province polygons exist in the dataset; v1's simplified copy (`province_polygons.json`) is not carried.

**Craton polygons.** 114 cratons cover 4.08×10⁷ km² (8% of the Earth, 24% of continental-province area) (v2 5.5).

---

## 5. Pangea as nine rigid blocks, and which provinces do not fit (v2 Phase 3)

**Carried (clean-room, no ages).** Provinces went to the plate polygon that holds them, giving nine rigid blocks: Africa 90 provinces (with Somali), Eurasia 271, North America 187 (with Caribbean), South America 50 (with Scotia), Antarctica 55, Australia 68, Arabia 17, India 32, Zealandia/Pacific 13. Africa was held fixed; each other block was rotated about an Euler pole to minimise overlap and the gap between facing margins, with a soft pull on 36 conjugate-pair provinces (pairs from the dataset's own `conjugate1`/`conjugate2` fields), in two passes (v2 3.2).

| Result of the fit | Value |
|-------------------|-------|
| Total overlap | 6×10⁵ km², 0.3% of the crust area |
| South America closes on Africa by | 53.9° |
| Conjugate pairs ending closer than today | 30 of 30 cross-block pairs (median 5,448 → 1,712 km). **Not independent**, because the pairs are part of the fit. In the geometry-only fit, 19 of 30 were closer. |
| Continental provinces fitting (under 25% overlap) | **631 of 647 (97.5%)** |
| Transitional provinces fitting | 120 of 136 |
| Weakest block | India: 21 of 32 provinces fit, 16% area-weighted overlap |

**The 16 continental misfits** (9 in eastern Africa and Madagascar, 5 in India, Buller Terrane, Zagros Foreland Basin) are the natural first candidates for independent motion (Section 7.3).

**Limits (v2 3.5).** The fit is one good packing among many (the best four local minima differed by under 1% in cost). It tests overlap only, not gaps. It has no paleomagnetic or kinematic check, which would need ages (rejected, P1). The conjugate pairs come from mainstream reconstructions, so they carry mainstream geometric inference even though no ages are used. **The fitted Pangea is a best packing, not proof of the pre-Flood arrangement.**

---

## 6. What is submerged today, and the recession claim (v2 Phase 5; corrects v1)

### 6.1 Submerged crust today (ETOPO 2022 bedrock, 0.25° sampling)
| Crust type | Area | Below sea level | Below −200 m | Below −1,000 m |
|------------|------|-----------------|--------------|----------------|
| Continental (647) | 1.73×10⁸ km² | 20.2% | 9.6% | 3.2% |
| Transitional (136) | 3.8×10⁷ km² | **92.6%** | 69.3% | 49.5% |
| Together | 2.10×10⁸ km² | **33.3% (7.0×10⁷ km²)** | | |

226 provinces (95 continental, 131 transitional) have more than half their area below sea level, 6.6×10⁷ km² in all.

**Correction to v1.** v1 states that "about 18% of continental plus transitional crust today is permanently submerged." That 18% is the **share of area that is classed transitional** (3.8×10⁷ of 2.1×10⁸ km²), not the share below sea level. The share below sea level is **33.3%** (v2). It includes continental shelves and flooded interiors. Any recession mechanism has to leave about a third of the crust under water, which is more than v1 assumed.

### 6.2 Named submerged fragments (v2 5.2-5.3, carried)
- **Zealandia** (Mortimer et al. 2017, GSA Today): 4.9×10⁶ km², about 94% submerged, a thinned and stretched continent straddling the Pacific-Australian plate boundary. In the dataset: 26 provinces, 6.27×10⁶ km² (it includes back-arc basins and ridges), 95.1% below sea level. The North/South split in v2 is v2's own (by plate polygon), not the literature's (North 4.63×10⁶ km², 96.1% submerged; South 1.64×10⁶ km², 92.4%).
- Others (area, share below sea level): Kerguelen Plateau south part 2.0×10⁵ km² (100%); Exmouth Plateau 5.2×10⁵ (100%); Sunda Shelf 7.3×10⁵ (99%); Alpha Mendeleev Ridge 1.1×10⁶ (100%); Lord Howe Rise 8.6×10⁵ (mean −1,803 m); Campbell Plateau 5.4×10⁵ (−881 m); Mauritius, Seychelles and Chagos remnants (95-98%); Blake Plateau and Bahama Platform (95-100%); Iberian Rifted Margin (96%); and others in v2 5.3.
- **Stretching** is a note in CMCT (Section 4.5), not part of the flood. The transitional provinces' mean elevation of −1,360 m and 92.6% submergence is read there as stretched crust (β about 1.5). DTAT uses this only as a description of what the submerged fragments are, not as a flood source.

### 6.3 Recession (the DTAT reframe, kept)
"Recession" does not need global sea level to fall. If most submerged crust stays submerged and only collided fragments rise, land re-emerges locally. This replaces a global recession mechanism by selective re-emergence, with Zealandia and the 33.3% below sea level today as the precedent. **Open (Section 13):** whether the uncollided share and the 33.3% line up, and the water budget that decides which crust is above water (CMCT H6).

---

## 7. Kinematics: how far, how fast, with what energy (v2 Phase 6)

### 7.1 How far and how fast
Rotating each block back from today to the fitted Pangea gives the path. Motions are relative to Africa (no absolute frame exists in this model).

| Block | Mean travel (km) | Mean speed in 150 days (m/s) |
|-------|------------------|------------------------------|
| South America | 5,248 | 0.41 |
| Antarctica | 4,378 | 0.34 |
| India | 4,750 | 0.37 |
| Australia | 3,645 | 0.28 |
| Zealandia/Pacific | 6,752 | 0.52 |
| Eurasia | 3,126 | 0.24 |
| North America | 4,094 | 0.32 |
| Arabia | 147 | 0.01 |

Area-weighted mean **3,841 km, 0.30 m/s in 150 days** (371 days: 0.12 m/s; spread over the 4,370 years since the Flood it needs 17,600 times the present rate, with the present rate assumed at 5 cm/yr). Speed itself is not a physical limit; the cost is dissipation.

### 7.2 Basal drag in the asthenosphere fails (H10, v2 6.1)
If the layer that shears is the asthenosphere (uniform shear over 100 or 200 km at 0.30 m/s, moving area 3.4×10¹⁴ m² including carried floor, olivine flow laws from Hirth and Kohlstedt):

| Layer | Stress needed | Energy in 150 d | × budget B | Heating of the sheared layer |
|-------|---------------|-----------------|-----------|-------------------------------|
| Wet, 1,650 K | 37-46 MPa | 4.9-6.0×10²⁸ J | 350-430 | 180-440 K |
| Wet, 1,500 K | 113-138 MPa | 1.5-1.8×10²⁹ J | 1,060-1,300 | 550-1,340 K |
| Dry | 222-951 MPa | 2.9×10²⁹-1.3×10³⁰ J | 2,100-8,900 | 1,100-9,200 K |

**A 150-day breakup of the whole Pangea layout by basal drag is not supported.** The dissipation is deep (H3 passes in location) but at least 350 times B, and it heats the layer by 180 K or more, which probably melts it (solidus not checked). Slab pull over a 4,000 km plate gives only about 8 MPa (from memory). No energy source named so far reaches 5×10²⁸ J (keel drips 0.9-8×10²⁶ J; runaway subduction, rejected, 1×10²⁸ J). This is the origin of H10.

v2 left three ways forward open (v2 "Questions before Phase 7"): (a) a thin weak lubricating layer that cuts the drag; (b) a shorter distance, with part of the opening done before the Flood; (c) carry H10 as an open problem. **Section 8 is route (a).**

### 7.3 The 16 misfit provinces as independent fragments (v2 6.3, carried)
Each of the 16 gets its own extra rotation (up to 35°) on top of its block's, chosen to remove overlap while touching other crust. All 16 reach under 10% overlap; median extra motion **931 km**, maximum 2,284 km (Antananarivo Block). At 150 days that is a median 0.07 m/s, up to 0.18 m/s. **Only 9 of 16 end within 100 km of their own block**; 7 end 110-255 km away and would have to drift on their own. Caution (v2): touching other crust is easy to satisfy, so a fit shows space exists, not that it is the true place. Fragments were moved one at a time with a random search (seed 1656), and the path is not checked.

### 7.4 Closure times, recomputed at 0.30 m/s (hand arithmetic)
v1's table (closure of 0.16-8.2 days for all 647 provinces) used a peak speed of 1.9 m/s from v1's old plate-speed curve, whose derivation I have not re-checked. **That speed is not carried.** At the v2 mean of 0.30 m/s (25.9 km/day), closure time is the fragment's diameter (√area) divided by speed:

| Fragment | Area (km²) | Diameter (km) | Closure time at 0.30 m/s |
|----------|-----------|---------------|---------------------------|
| Smallest province (v1 figure) | 669 | 26 | 1.0 day |
| Average of 1,000 fragments | 148,000 | 385 | 14.8 days |
| Average of 500 | 296,000 | 544 | 21 days |
| Average of 100 | 1,480,000 | 1,217 | 47 days |
| Largest province (v1 figure) | 1,840,575 | 1,357 | 52 days |

All are inside the 74-day window of v1 and inside the 150 days of prevailing waters. "Closure" here is only the time to cross one's own diameter. It says nothing about whether a fragment's path leads to a partner. That is still open.

---

## 8. New hypothesis: the crust slips over fixed keels (from discussion, 2026-11-25)

**Not in v1 or v2.** Idea from the user: the layer below the Moho and above the deep mantle (the keel layer) stayed undisturbed and acted as the plate on which the crust slipped, shearing off at the Moho. West Africa then "traded one keel for another": the crust moved, the keel did not. DTAT's fragments are then crust fragments, "subsurface bumper cars", sliding on a Moho-level detachment.

### 8.1 What it would fix
- **P9/H11 is satisfied.** After the slip every craton sits on a keel. It need not be the keel it started on.
- **H10's deep-dissipation branch (Section 7.2) is avoided.** Nothing moves below the Moho, so dissipation is in one thin zone at about 35 km, insulated by the crust above (conduction through 10 km takes 3×10⁶ years). The mass that moves is crust only.
- **Convergence may not need subduction.** Where moving crust meets other crust it can thicken or overthrust, which is DTAT's collision-uplift picture. This could build the Himalaya-Karakoram without CPT's heat. Untested.
- **A candidate slip layer.** The serpentinite layer of CMCT Section 21 is a wet, low-friction candidate (CMCT 27.1 notes hydrous minerals are the only workable water store). **Open:** whether that layer is on the moving side (the lowest crust) or the fixed side (the uppermost keel mantle). It changes where the collapse happens.

### 8.2 The slip-zone heat, by hand arithmetic
The heat in the slip zone depends on the shear stress and the distance, not on speed. Temperature rise of a zone of thickness h: ΔT = τ·d / (ρ·c·h), with ρc = 2.7×10⁶ J/m³/K, no latent heat, no dehydration, no conduction out. (CMCT Section 25 shows the Moho is already at 400-600 °C under cratons, and the serpentinite limit is about 570-620 °C, so a rise of a few hundred K can trigger dehydration.)

| Slide distance d | τ = 0.2 MPa, h = 3 km | τ = 0.2 MPa, h = 1 km | τ = 1 MPa, h = 3 km | τ = 1 MPa, h = 1 km |
|------------------|----------------------|----------------------|--------------------|--------------------|
| 500 km | 12 K | 37 K | 62 K | 185 K |
| 931 km (v2 median misfit motion) | 23 K | 69 K | 115 K | 345 K |
| 1,900 km (3,841 km split between two crusts) | 47 K | 141 K | 235 K | 704 K |
| 3,841 km (v2 mean) | 95 K | 285 K | 474 K | 1,423 K |

**Reading.** DTAT's short slides (hundreds of km) are far gentler than one 3,800 km slide. If two facing crusts both slide over fixed keels, each moves about half the opening distance. A slip zone near 0.2 MPa heats by tens of K; one near 1 MPa and 1 km thick approaches melting at full distance. If all the heat reached the ocean, 1 MPa over the mean 3,841 km for the whole Pangea area (2.105×10¹⁴ m²) is 8×10²⁶ J, about 6 B. At 1,900 km, B is reached at about 0.35 MPa. Heat at 35 km depth does not reach the ocean quickly, so the real limit is melting and dehydration in the zone, not B. **What the stress of a real Moho slip layer is has not been found.** v2's drag at 37-138 MPa is for ductile asthenosphere and does not apply to a thin weak layer.

### 8.3 What it breaks, or does not fix
1. **Registration (the biggest test).** Cratonic crust today sits over a thick keel of about the same outline. If crust slid thousands of km over fixed keels, it had to land on a keel and stop. DTAT softens this, since most fragments end up submerged or elsewhere and only the survivors are "land," so the match would be statistical. But "stuck over a keel" needs a reason. The North China craton (crust without its original keel) is a mainstream counter-example that shows the match is not perfect. Non-age checks exist (keel edges against surface craton edges; seismic fabrics against surface structure). **Test T1 below.**
2. **H9 is not solved.** Wherever crust pulls apart (Atlantic, Indian Ocean), bare mantle with no keel is exposed. v2 6.2: if the continent-bearing plates' carried floor goes back to its Pangea position and the Pacific-side floor stays fixed, **1.08×10⁸ km² is uncovered** (66% of the 1.64×10⁸ km², 302 times the H1 area limit, 301 B at 3.9×10¹⁴ J/m²). Exhumed mantle between stretched margins (C2) covers 21-85% at assumed widths of 100-400 km (needs 321 km on every margin, 468 km on passive ones). Intact new floor passes the heat cap (C3) only if heat extraction stays above about 300 m. The 136 transitional provinces (3.8×10⁷ km²) are about a quarter of the 1.64×10⁸ km², and most Atlantic and Indian floor is oceanic crust, not stranded continent. **A slide over fixed keels does not change these figures.**
3. **A slip layer that weak is runaway.** At 0.2 MPa or less a tiny contrast in elevation or crustal thickness drives the motion. Stopping it in the right place is the registration problem again.
4. **Isostasy (an open opportunity, not a result).** If keels are net dense (CMCT 14.2; v2 5.5: a purely thermal excess of about 2.3%, chemical lightness uncertain), crust that slides onto a keel sinks and crust that slides off rises. That might lower the land that arrives on keels and so help the flood, but real cratons sit at ordinary elevations, so the effect may be cancelled. Unchecked.
5. **Sequence.** Whether the slide, the collapse (CMCT) and the collisions are one event, or follow each other, is not decided (Section 12).

### 8.4 Tests for this hypothesis (none run)
- **T1 Registration.** Compare the 114 craton polygons (Hasterok) with a lithosphere-thickness map such as LITHO1.0 (not yet obtained). Measure how often craton crust sits over a thick keel and how far the outlines are offset. This could end the idea cheaply.
- **T2 Slip-stress budget.** For a Moho slip zone of 1-3 km: the largest stress that avoids melting, and whether serpentinite friction with near-lithostatic pore pressure is that low (friction data not yet sourced).
- **T3 Gap and H9.** Whether any version closes the 1.08×10⁸ km² gap without making new floor hot.
- **T4 Isostatic effect of landing on a keel,** with the net-density sign from CMCT 14.2.

---

## 9. Collisions, uplift and the ten highest peaks

### 9.1 What was carried
- **The ten highest peaks** lie in the Himalayan Orogenic Belt (nine) and the Karakoram Province (K2), inside the Eurasian plate's Tibet and Pamir deformation zones (v2 `phase2b_peaks_provinces.txt`). That is where India meets Eurasia in the fit. DTAT's collision uplift has a concrete target: **8,091-8,849 m from a pre-Flood relief below 610 m.**
- **India is the weak block in the fit** (Section 5): 16% area-weighted overlap, "partly physical" since its northern edge is crushed into Eurasia today.
- **Collision-driven uplift (v1 13.7-13.8, flagged).** v1 converts convergence into surface uplift at 1-2% of the convergence distance. For 500, 1,000 and 2,000 km this gives 1,111-2,222, 2,222-4,444 and 4,444-8,889 m, v1 compared this with its own 1,000-6,000 m keel-loss subsidence target, which is withdrawn with CKDT. The uplift now required is set by the peaks (about 7.5-8.2 km above a pre-Flood relief of under 610 m) and by the recession water budget. v1 also computed that the project's own tracked India-Asia convergence over a 74-day window (39 km) gives only about 130 m, which is local and too small. **Flagged:** the 1-2% ratio came from Himalaya-Tibet mainstream convergence totals, which depend on deep-time reconstructions (P1). The factor from thickening to surface uplift (about 1/4.5 in v1's numbers) was not re-derived. Treat the ratio as a borrowed, unverified number.

### 9.2 What is still open (carried from v1, unresolved)
- Why a collision gives **lasting** uplift rather than a transient bump that isostasy relaxes. No relaxation dynamics are modelled.
- Whether specific fragments follow paths that actually collide (v2 6.3: 7 of 16 misfits end up away from their block), rather than "enough of them, fast enough" being true on average.
- The overshoot-and-ring shape. v1 reused a damped oscillator (ζ = 0.15) from its Phase 4, but its own search found real glacial-isostatic literature to be monotonic. The oscillator is a stylistic choice, **not carried into any verdict.** Overshoot and rebound remain a P6 target.

### 9.3 Contacts and the suture budget (v2 6.4 and 5.4, carried)
- No global suture-zone dataset was found. Three proxies from the Hasterok data: collision-zone plate boundaries (118 segments, 83,400 km; for example Rocky Mountain Frontal Thrust 3,863 km, Himalayan Main Boundary Thrust 3,259 km, Zagros Mountain Front Fault 2,409 km); 18 ophiolite complexes (2.55×10⁶ km²); and craton-to-belt contacts (222 contacts, **129,300 km**, 92% against orogenic belts; Asia 26,800 km, North America 26,400, Africa 24,600, Australia 15,100, South America 14,800, Europe 9,600, Antarctica 8,900, India and Middle East 3,100).
- Five named sutures are in v2 `data\named_sutures.csv`. A named global list was not found (Furnes et al. 2014 was behind a login).
- In the fitted Pangea layout, **149,900 km** of crust of different blocks touches, against **77,500 km today**. Four pairs that touch today but are not among Pangea's top ten (Eurasia-India 11,600 km, Africa-Eurasia 8,100, Arabia-Eurasia 7,200, Africa-Arabia 6,900) are the ones that **closed on each other**: 33,900 km, about 40% of the 83,400 km of collision-zone boundary. Eurasia-North America touches in both layouts (5,200 km in Pangea, 23,700 km now), so it did not open and close cleanly. These are lattice estimates that include overlap, not a test against named sutures.

---

## 10. Water level with independent fragment elevations (v1 13.9, tool only)

v1 built a hypsometric volume-conservation solver (area against elevation, bisection for the sea level that holds a given water volume) using a 2° ETOPO1 grid. **The tool is carried; its results are not.**
- **Validation (carried):** today's bathymetry and the 1,335,000,000 km³ ocean volume return a sea level of **+2.37 m** (against ~0 m). Grid statistics agree with NOAA's published values (ocean area 70.8% against 71.0%, mean ocean depth 3,695 m against 3,686 m, volume within 0.06%).
- **Not carried:** the +3.68 m shift from wiring in 35 pairs (built on the oscillator and on Merdith 250 Ma positions); the wiring itself covered only 5.5% of grid cells.
- **Next use:** v2's ETOPO 2022 grid is finer (0.25°, bedrock). A rebuild on that grid, with CMCT's water budget (H6), would test the recession claim in Section 6.3.

---

## 11. What was carried from v1 and v2, and what was not

| Item | Source | Status | Why |
|------|--------|--------|-----|
| DTAT concept (fragments, differential collision, recession as selective re-emergence) | v1 `Theories.md`, 13.8 | **Carried** | The user's idea; restated in Section 1 |
| 647 continental + 136 transitional provinces | v1 13.8.1; v2 Phase 2 | **Carried (v2)** | Same data; v2 corrected four areas |
| v1 size range 669-1,840,575 km² | v1 | **Flagged** | Used the faulty shapefile area field |
| "18% permanently submerged" | v1 | **Corrected** | It is the transitional share. The share below sea level is 33.3% (v2 5.1) |
| Nine-block Pangea fit, province check (631/647) | v2 Phase 3 | **Carried** | Clean-room, no ages |
| Submerged provinces, Zealandia, sutures proxies | v2 Phase 5 | **Carried** | Computed from ETOPO 2022 and Hasterok |
| Kinematics (3,841 km, 0.30 m/s), basal drag (H10), H9 routes C1-C3, 16 misfits, contacts | v2 Phase 6 | **Carried** | Clean-room |
| Closure time table at 1.9 m/s (0.16-8.2 days) | v1 13.8 | **Recomputed** at 0.30 m/s: 1-52 days (hand arithmetic, Section 7.4) | 1.9 m/s peak speed has no re-checked derivation |
| Collision-uplift ratio (1-2%) | v1 13.7 | **Flagged** | Derived from mainstream Himalaya convergence totals (P1); thickening-to-uplift factor not re-derived |
| 35 conjugate pairs and their 250 Ma positions, "100% closer at 250 Ma, median 20%" | v1 13.8.2-13.8.3 | **Pairing carried (already in the v2 fit); 250 Ma positions and the cross-validation not carried** | Positions come from Merdith et al. (2021) via GPlates, a reconstruction built on dated data (P1). The cross-validation is not independent of mainstream reconstruction |
| 647-fragment "shared per-plate rotation" layout (13.10-13.11), Day-0 polygons | v1 | **Not carried** | Each fragment's rotation is a Merdith 250 Ma plate rotation (P1). v2's own fit replaces it |
| v1 hole/overlap numbers (955 / 2,276 sq-deg) | v1 13.11 | **Not carried** | Raw degrees with no latitude correction (v1 found this bias itself), and from the P1-conflicted layout |
| Lost-continent candidates (Argoland, Greater Adria, Balkanatolia, Gulden Draak Knoll, Batavia Knoll; Mauritia already in the dataset as Mauritius Remnant) | v1 prompt 14; 13.11.3 | **Names only, unplaced** | Real literature candidates, but v1 placed them using Merdith rotations; areas of the last two (15,000 km² each) are v1 illustrative guesses |
| Hypsometric water-level solver | v1 13.9 | **Tool carried, results not** | Section 10 |
| Damped-oscillator uplift curve | v1 13.8.6, Phase 4 | **Not carried into verdicts** | Stylistic; real GIA is monotonic (v1's own finding) |
| Keel-loss subsidence (CKDT) as DTAT's starting point | v1 | **Not carried** | Struck in CMCT under P9 |
| v1 plate-motion animation, globe, renders, UI work, 110 regression tests | v1 Phases 3-10, 13.10 | **Not carried** | Presentation layer built on the 7-plate and 647-fragment layouts. Still in `Noah's Pangea v1` |
| Fixed-keel crust slip | discussion 2026-11-25 | **New, untested** | Section 8 |

**Files left in place.** No code or data was copied from v1 or v2 into this folder. v2's `model\phase3b_fit.py`, `phase3e_province_check.py`, `phase5a_submerged.py` and `phase6a-c` and its `data\hasterok_2022\` are the inputs to reuse by path. v1's `model\phase13_water_level.py` and `fetch_global_hypsometry.py` are the only v1 code worth looking at again.

---

## 12. Interface with CMCT

CMCT Section 23 holds the same table from the other side. Each file states what it takes; neither restates the other's results.

| Direction | Item | Status |
|-----------|------|--------|
| CMCT gives DTAT | The cause of submergence (collapse of a layer at the crust base, released water) in place of the struck keel-loss version | Unresolved; CMCT's verdicts are open |
| CMCT gives DTAT | Heat budget B, constraints H1-H5, H9, H10, H11, and the water budget H6 | Stated in CMCT Section 3; DTAT cites, does not copy |
| CMCT gives DTAT | A possible slip layer: the serpentinite layer (CMCT 21); the Moho temperature of cratons (CMCT 24-25) | Candidate only; whether the layer is on the moving or fixed side is open |
| CMCT gives DTAT | Crack lines along province boundaries that could vent water (CMCT 22) | Geometry only |
| DTAT gives CMCT | Whether fragmented, sliding crust behaves as the venting model needs, and whether collisions close or re-open vents | Not examined |
| DTAT gives CMCT | The slip-zone heat and the order of events (slide, collapse, collision) | Section 8.2 gives the first numbers; sequence undecided |
| DTAT gives CMCT | Recession of the flood and the submerged share (33.3%) | Section 6; CMCT does not address recession |
| Shared | The registration test, H9 and H10 | Section 8.4; both files list them |

**Rule for this file.** No DTAT verdict rests on a CMCT result that CMCT marks open, and (CMCT's rule, kept) no CMCT verdict rests on DTAT.

---

## 13. Open problems register

| ID | Problem | Status |
|----|---------|--------|
| D1 | **H10:** a weak layer and energy source for crust moving hundreds to thousands of km in 150 days | Asthenospheric drag fails by 350× (7.2). Moho slip layer untested (8.4 T2) |
| D2 | **H9:** 1.08×10⁸ km² of new floor | Not solved (8.3, v2 6.2) |
| D3 | **Registration** of craton crust over keels after sliding | Test T1 not run |
| D4 | Lasting collision uplift, not a transient bump | Not modelled |
| D5 | Fragment paths: do the specific provinces actually collide where today's belts are, and not where there are none | Not tested beyond 16 misfits (7 of which end away from their block) |
| D6 | Whether the 33.3% submerged crust matches the uncollided fraction | Not tested |
| D7 | The 1-2% convergence-to-uplift ratio is a borrowed mainstream number (P1) | Needs a physical derivation or replacement |
| D8 | A named global suture list | Not found; proxies only |
| D9 | The faulty shapefile areas (four provinces) in v1's figures | v2 corrected; v1 figures not re-run |
| D10 | Sequence: slide, collapse, collisions | Undecided |
| D11 | No pre-Flood kinematic or paleomagnetic check is possible without ages | Accepted limit of P1 |

---

## 14. Obstacle and decision log

| # | Item | Resolution |
|---|------|------------|
| 1 | v1 and v2 differ: v1 used Merdith 250 Ma reconstructions; v2 is clean-room | R3: v2 used; v1 reconstruction-based items not carried (Section 11) |
| 2 | v1's "18% submerged" mixed up area class with elevation | Corrected to 33.3% below sea level (Section 6.1) |
| 3 | v1's 1.9 m/s closure speed has no re-checked source | Recomputed at v2's 0.30 m/s (Section 7.4) |
| 4 | Fixed-keel slip would change which fragments carry keels, and P9 | Section 8; registration test T1 first |
| 5 | The DTAT text in v1 `Theories.md` still assumes keel-loss submergence | Superseded by Section 1 of this file. The v1 file is left unchanged as an archive |
| 6 | Folder and file naming (the instruction's quoting was ambiguous) | Folder and file are named `Differential Terrane Accretion Theory (DTAT)`, matching CMCT's convention |
| D-A | Decision (user, 2026-11-25): give DTAT its own folder and document, separate from CMCT | Done in this draft |
| D-B | Decision (user, 2026-11-25): crust slip over fixed keels is a candidate to explore in DTAT, not yet in CMCT | Section 8 |

---

## 15. Plan (nothing started)

1. **Phase A: re-verify carried numbers** as CMCT's Section 14 did: area correction (D9), the v2 logs against their scripts, the 1,111-8,889 m uplift grid.
2. **Phase B1: registration test T1** (needs a lithosphere-thickness grid).
3. **Phase B2: Moho slip-zone stress budget T2** with sourced serpentinite friction.
4. **Phase B3: fragment paths and collisions** from v2's fitted layout at 0.30 m/s: which provinces collide, where, in what order, against today's belts and the 33,900 km of closed contacts.
5. **Phase B4: H9** (shared with CMCT).
6. **Phase B5: lasting collision uplift** and the ten peaks.
7. **Phase B6: recession and water level** on the 0.25° ETOPO 2022 grid with CMCT's water budget.

---

## 16. Sources

Primary (via v2, `Noah's Pangea v2\sources\README.md`): S09 Hasterok et al. (2022) and repository; S13 ETOPO 2022 (NOAA); S14 Mortimer et al. (2017), GSA Today 27(3); S15 Pearson et al. (2021), Nature 596 (abstract and snippets only); S16 Hirth and Kohlstedt (olivine flow laws); S19-S23 secondary pages on sutures and ophiolites (Wikipedia, summarised).
From v1 (not re-verified): Merdith et al. (2021) *Earth-Science Reviews* (reconstruction, **not used**); Eakins and Sharman (2010/2012) NOAA hypsometry; Advokaat and van Hinsbergen (2024) *Gondwana Research* 128 (Argoland); van Hinsbergen et al. (2019) *Gondwana Research* (Greater Adria); Licht et al. (2022) *Earth-Science Reviews* (Balkanatolia); Gibbons, Whittaker and Müller (2013) and Gibbons et al. (2016) *Gondwana Research* (Gulden Draak and Batavia knolls); Torsvik et al. (2013) and Ashwal et al. (2017) (Mauritia).
CMCT sections used: 3 (constraints), 4.5, 14.2, 21, 22, 24, 25, 27.5.
