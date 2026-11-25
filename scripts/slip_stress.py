"""Test T2 (DTAT Section 8.4): how weak must a Moho slip layer be, and how weak can real friction make it?

Two sides of the same number, the shear stress tau on the slip surface:
  (A) What friction gives:  tau = mu * (sigma_n - P_f) = mu * sigma_n * (1 - lambda),  lambda = P_f / sigma_n.
  (B) What heating allows:  the slip zone of thickness h heats by dT = tau * d / (rho_c * h) over a slide of d, so
      tau_max = dT_allowed * rho_c * h / d.
dT_allowed is the room between the craton Moho temperature (CKDT Section 25) and the antigorite limit (595 C, middle of the
570-620 C bracket, CKDT Section 21.2), beyond which the serpentinite layer dehydrates.

No ages. Inputs are listed below; friction values are from the literature search of 2026-11-25 (see DTAT Section 8.6).
Run from the repo root: python scripts/slip_stress.py   Output: results/slip_stress_log.txt
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.makedirs(os.path.join(ROOT, "results"), exist_ok=True)
out = []


def p(s=""):
    print(s)
    out.append(s)


G = 9.8
RHO_CRUST = 2800.0          # kg/m3, as in CKDT Section 27
RHO_C = 2.7e6               # J/m3/K, as in DTAT Section 8.2
DEPTHS_KM = (35.0, 39.0, 46.0)   # craton Moho depths: median 39 km, 35-46 km spread (CKDT Sections 19, 25)
SIGMA = {z: RHO_CRUST * G * z * 1e3 for z in DEPTHS_KM}
Z0 = 39.0
S0 = SIGMA[Z0]

p("T2 SLIP-STRESS TEST: Moho slip layer")
p(f"Normal stress at the Moho (rho {RHO_CRUST:.0f} kg/m3, g {G}): " +
  ", ".join(f"{z:.0f} km: {SIGMA[z]/1e9:.2f} GPa" for z in DEPTHS_KM))

# ---------------------------------------------------------------- A
p("\nA. SHEAR STRESS FROM FRICTION AT 39 km (MPa): tau = mu * sigma_n * (1 - lambda)")
mus = (0.1, 0.2, 0.3, 0.5, 0.7)
lams = (0.0, 0.40, 0.90, 0.95, 0.99, 0.995, 0.999, 0.9995)
p("   lambda =  " + "  ".join(f"{l:>7}" for l in lams))
for mu in mus:
    p(f"   mu {mu:.1f}:  " + "  ".join(f"{mu*S0*(1-l)/1e6:7.2f}" for l in lams))
p("   (lambda 0.40 is roughly hydrostatic pore pressure at this depth; 1.0 is fluid pressure equal to the rock load, the most a rock can hold.)")

# ---------------------------------------------------------------- A2
p("\n   Fluid-pressure ratio lambda needed to bring tau down to a target, by friction coefficient (39 km):")
targets = (0.1, 0.2, 0.5, 1.0, 2.0, 5.0)
p("   target tau (MPa) " + "  ".join(f"mu {mu:.1f}  " for mu in mus))
for t in targets:
    p(f"   {t:>6.1f}           " + "  ".join(f"{1 - t*1e6/(mu*S0):7.4f}" for mu in mus))

# ---------------------------------------------------------------- B
p("\nB. STRESS CAP FROM HEATING: tau_max = dT * rho_c * h / d  (MPa)")
p("   Room dT before the antigorite limit (595 C), from the craton Moho temperature at a given surface heat flow (CKDT Section 25.1):")
moho = {28: 363, 32: 421, 36: 478, 40: 535, 44: 592}
for hf, T in moho.items():
    p(f"     {hf} mW/m2: Moho {T} C, room {595 - T} K")
dists = (500, 931, 1900, 3841)
for dT in (230, 117, 60):
    label = {230: "230 K (28 mW/m2 craton)", 117: "117 K (36 mW/m2)", 60: "60 K (40 mW/m2, the Archean mean)"}[dT]
    p(f"   dT allowed = {label}")
    p("     slide d (km)       " + "  ".join(f"{d:>7}" for d in dists))
    for h in (1.0, 3.0):
        p(f"     zone h = {h:.0f} km        " + "  ".join(f"{dT*RHO_C*h*1e3/(d*1e3)/1e6:7.3f}" for d in dists))
p("   Heat absorbed by the dehydration itself would raise these caps; its size was not sourced (Wicks and Whittaker 1965 was not readable).")
p("   Each 100 kJ per kg of reacting rock absorbed is worth about 100 K of heating at c = 1,000 J/kg/K.")

# ---------------------------------------------------------------- C
p("\nC. WHAT FRICTION ACTUALLY ALLOWS (lab values; sources in DTAT Section 8.6)")
cases = [
    ("lizardite, water-saturated gouge, room T", 0.15, 0.35),
    ("end-member lizardite / fibrous serpentine, to 170 C (Tesei et al. 2018)", 0.15, 0.19),
    ("antigorite, room T (Reinen)", 0.5, 0.85),
    ("antigorite + quartz at 500 C (2024 study)", 0.22, 0.22),
    ("serpentinite bare surface at seismic slip rate (Proctor et al. 2014)", 0.1, 0.1),
    ("serpentinite gouge at 1 m/s, 4-22 MPa (Proctor et al. 2014)", 0.39, 0.51),
]
for name, lo, hi in cases:
    lam_hi = [1 - 1e6 / (m * S0) for m in (lo, hi)]
    lam_02 = [1 - 0.2e6 / (m * S0) for m in (lo, hi)]
    p(f"   {name}: mu {lo:g}-{hi:g}. For tau <= 1 MPa need lambda >= {max(lam_hi):.4f}; for tau <= 0.2 MPa need >= {max(lam_02):.4f} (at the stronger value).")
p("   Stress at hydrostatic-like pore pressure (lambda 0.4) with the weakest quoted mu (0.1): "
  f"{0.1*S0*0.6/1e6:.0f} MPa; with mu 0.2: {0.2*S0*0.6/1e6:.0f} MPa.")
p("   Lab normal stresses in these tests are 4-120 MPa, against about 1,070 MPa here; slip distances are metres, against 900-3,800 km.")

# ---------------------------------------------------------------- D
p("\nD. READING")
p("   1. To stay under the heating cap (about 0.04-1.0 MPa for a 40 mW/m2 craton, 0.16-3.7 MPa for a cool 28 mW/m2 craton),")
p("      the slip surface needs lambda of about 0.997-0.9998 at mu 0.1-0.3. That is pore fluid held within 0.02-0.3% of the rock load.")
p("   2. Friction alone, with any lab mu from 0.1 to 0.85, gives tens to hundreds of MPa at lambda 0.9 and still about 1-10 MPa at 0.99.")
p("      So the slip layer works only if it is almost fully fluid-supported.")
p("   3. Fluid at the rock load is what a dehydrating layer can produce, and shear heating drives dehydration, so a self-lubricating")
p("      feedback is physically conceivable. It has not been modelled: it needs fluid trapped for 150 days (very low permeability),")
p("      continuous supply from the reaction, and the layer must not drain by hydrofracture first.")
p("   4. At 0.3 m/s the slip rate is in the range where laboratory friction weakens further (flash heating, melt, thermal pressurisation),")
p("      but those tests are at 1-2 orders of magnitude lower normal stress and metres of slip.")
p("   5. Lizardite, the weakest serpentine in the tests, is the low-temperature phase (it gives way to antigorite above roughly 300 C, from memory,")
p("      not checked), so the weak values may not apply at craton Moho temperatures of 360-590 C, where antigorite (mu 0.5-0.85 at room T, about 0.2 at 500 C in a mixture) is expected.")
p("   6. The antigorite limit leaves little room: 3-60 K for Moho temperatures of 535-592 C. Cooler cratons (28-32 mW/m2) leave 170-230 K")
p("      but are far from the limit, which CKDT Section 25 already found.")

p("\nLIMITS")
p("   Friction values are from a single search pass of abstracts and summaries, not read from the papers. Hydrostatic-like lambda 0.4 is an")
p("   assumption. Uniform shear in a zone of 1 or 3 km; no conduction out of the zone (a few km in 150 days would be ~3.6 m, so it is negligible);")
p("   no latent heat; heating all in the zone. The melting limit of the crust base was not sourced; wet crust solidus is believed to be above")
p("   the antigorite limit, so the dehydration limit is used as the tighter one (from memory). Normal stress is lithostatic with a constant density.")

open(os.path.join(ROOT, "results", "slip_stress_log.txt"), "w", encoding="utf-8").write("\n".join(out) + "\n")
