"""Draw the DTAT illustration set into ../images (PNG + SVG, numbered 01-08).

Numbers come from 'Differential Terrane Accretion Theory (DTAT).md' (sections cited per figure).
Schematic panels are NOT to scale. Run from the repo root: python scripts/draw_images.py
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Polygon, FancyBboxPatch

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "images")
os.makedirs(OUT, exist_ok=True)

LAND, SEA, KEEL, CRUST, SLIP, MANTLE, INK = "#c9a66b", "#5b8fb9", "#6f5a86", "#b9b4a8", "#d9693b", "#e9dfd0", "#222222"
GOOD, BAD, WARN = "#3b7d4f", "#b03a2e", "#c8902c"


def save(fig, name):
    for ext in ("png", "svg"):
        fig.savefig(os.path.join(OUT, f"{name}.{ext}"), dpi=130, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def title(fig, t, sub=None, ysub=0.905):
    fig.suptitle(t, fontsize=17, fontweight="bold", color=INK, y=1.0)
    if sub:
        fig.text(0.5, ysub, sub, ha="center", fontsize=11, color="#555555")


def blank(ax, xl, yl):
    ax.set_xlim(*xl)
    ax.set_ylim(*yl)
    ax.axis("off")


def arrow(ax, p, q, color=INK, lw=2.2, style="-|>"):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle=style, mutation_scale=16, lw=lw, color=color))


# ---------------------------------------------------------------- 01
def fig01():
    fig, axs = plt.subplots(1, 3, figsize=(15, 5.8))
    title(fig, "01  The core idea: many fragments, only some collide",
          "Schematic, not to scale. Sections 1 and 6.3. Every fragment is crust; the land is already submerged (cause: CMCT).")
    fig.subplots_adjust(top=0.78)
    rects = [(0.2, 2.2, 1.6, 1.4), (1.9, 2.4, 1.5, 1.2), (3.5, 2.2, 1.3, 1.4),
             (0.2, 0.7, 1.2, 1.4), (1.5, 0.5, 1.7, 1.5), (3.3, 0.6, 1.5, 1.3)]
    for ax in axs:
        blank(ax, (-0.2, 6.4), (0, 4.4))
    axs[0].set_title("Before: Pangea broken into fragments", fontsize=12)
    for (x, y, w, h) in rects:
        axs[0].add_patch(Rectangle((x, y), w, h, fc=LAND, ec=INK, lw=1.4))
    axs[1].set_title("During: different speeds and directions", fontsize=12)
    moves = [(-0.1, 0.3), (0.3, 0.5), (0.9, 0.1), (-0.1, -0.3), (0.5, -0.2), (1.0, -0.1)]
    for (x, y, w, h), (dx, dy) in zip(rects, moves):
        axs[1].add_patch(Rectangle((x + dx * 0.9, y + dy * 0.9), w, h, fc=LAND, ec=INK, lw=1.4, alpha=0.9))
        arrow(axs[1], (x + w / 2, y + h / 2), (x + w / 2 + dx * 1.2, y + h / 2 + dy * 1.2), color=SLIP, lw=2)
    axs[2].set_title("After: collided rise, the rest stay submerged", fontsize=12)
    axs[2].add_patch(Rectangle((-0.1, 0.1), 5.2, 4.1, fc="#cfe0ee", ec="none"))
    axs[2].add_patch(Rectangle((0.2, 2.2), 1.4, 1.4, fc=SEA, ec=INK, lw=1.2, alpha=0.85))
    axs[2].add_patch(Rectangle((0.3, 0.6), 1.1, 1.3, fc=SEA, ec=INK, lw=1.2, alpha=0.85))
    axs[2].add_patch(Rectangle((1.8, 1.5), 1.7, 1.7, fc=LAND, ec=INK, lw=2))
    axs[2].add_patch(Polygon([[1.8, 3.2], [2.65, 4.0], [3.5, 3.2]], fc="#a9814a", ec=INK, lw=1.5))
    axs[2].text(2.65, 2.3, "collided:\nland +\nmountains", ha="center", va="center", fontsize=10)
    axs[2].add_patch(Rectangle((3.9, 0.8), 1.0, 1.1, fc=SEA, ec=INK, lw=1.2, alpha=0.85))
    axs[2].text(4.4, 0.65, "missed:\nsubmerged", ha="center", va="top", fontsize=9)
    axs[2].text(0.9, 2.9, "submerged", ha="center", fontsize=9, color="white")
    save(fig, "01_core_idea")


# ---------------------------------------------------------------- 02
def fig02():
    fig, (a, b) = plt.subplots(1, 2, figsize=(14, 5.8), gridspec_kw={"width_ratios": [1, 1.15]})
    title(fig, "02  The fragments are real provinces, and a third of the crust is already under water",
          "Hasterok et al. (2022) provinces; ETOPO 2022 bedrock (v2 Phases 2 and 5). Sections 4 and 6.1.")
    fig.subplots_adjust(top=0.80, wspace=0.25)
    names = ["Continental\n(647 provinces)", "Transitional\n(136 provinces)"]
    area = [1.73, 0.38]
    bars = a.bar(names, area, color=[LAND, SEA], ec=INK)
    a.set_ylabel("Area (10$^8$ km$^2$)")
    a.set_ylim(0, 2.1)
    for r, v in zip(bars, area):
        a.text(r.get_x() + r.get_width() / 2, v + 0.04, f"{v:.2f}", ha="center", fontsize=12)
    a.set_title("Fragment layer: 2.10×10$^8$ km$^2$ (41.3% of the Earth)", fontsize=11)
    a.spines[["top", "right"]].set_visible(False)
    cats = ["Continental", "Transitional", "Together"]
    below = [20.2, 92.6, 33.3]
    b.bar([-0.27, 0.73, 2.0], below, 0.27, color=SEA, ec=INK, label="below sea level")
    b.bar([0, 1], [9.6, 69.3], 0.27, color="#3f6f94", ec=INK, label="below −200 m")
    b.bar([0.27, 1.27], [3.2, 49.5], 0.27, color="#27496a", ec=INK, label="below −1,000 m")
    for i, (xp, v) in enumerate(zip([-0.27, 0.73, 2.0], below)):
        b.text(xp, v + 1.5, f"{v}%", ha="center", fontsize=11, fontweight="bold" if i == 2 else None)
    b.set_xticks(range(3))
    b.set_xticklabels(cats)
    b.set_ylim(0, 112)
    b.set_ylabel("Share of area (%)")
    b.legend(frameon=False, loc="upper left", bbox_to_anchor=(0.0, 0.88))
    b.set_title("Submerged today: 33.3% = 7.0×10$^7$ km$^2$", fontsize=11)
    b.spines[["top", "right"]].set_visible(False)
    b.annotate("v1 quoted '18% submerged'. That was the transitional\nshare of area, not the share below sea level.",
               (2.0, 42), (1.25, 100), fontsize=9.5, color=BAD, arrowprops=dict(arrowstyle="->", color=BAD))
    save(fig, "02_fragments_and_submergence")


# ---------------------------------------------------------------- 03
def fig03():
    fig, ax = plt.subplots(figsize=(12, 6))
    title(fig, "03  Fragments can cross their own width in days at the mean breakup speed",
          "Closure time = √area ÷ 0.30 m/s (25.9 km/day); hand arithmetic from v2 speed and v1 size range. Section 7.4.")
    fig.subplots_adjust(top=0.80)
    pts = [("smallest province\n669 km$^2$", 26), ("average of 1,000\nfragments", 385), ("average of 500", 544),
           ("average of 100", 1217), ("largest province\n1.84×10$^6$ km$^2$", 1357)]
    v = 25.92
    names = [p[0] for p in pts]
    days = [p[1] / v for p in pts]
    bars = ax.barh(names, days, color=LAND, ec=INK)
    for r, d, p in zip(bars, days, pts):
        ax.text(d + 1, r.get_y() + r.get_height() / 2, f"{d:.1f} days", va="center", fontsize=11)
    ax.axvline(74, color=WARN, lw=2, ls="--")
    ax.text(74.8, -0.55, "74-day recession window (v1)", color=WARN, fontsize=10, va="bottom")
    ax.axvline(150, color=BAD, lw=2, ls="--")
    ax.text(150.8, -0.55, "150 days of\nprevailing waters", color=BAD, fontsize=10, va="bottom")
    ax.set_xlim(0, 185)
    ax.set_ylim(4.6, -0.9)
    ax.set_xlabel("Days to cross the fragment's own diameter")
    ax.spines[["top", "right"]].set_visible(False)
    ax.text(0.78, 0.5, "Says nothing about whether a path\nleads to a collision partner (open, D5).",
            transform=ax.transAxes, ha="right", fontsize=10, color="#555555")
    save(fig, "03_closure_times")


# ---------------------------------------------------------------- 04
def fig04():
    fig, axs = plt.subplots(3, 1, figsize=(13, 10.8))
    title(fig, "04  The new hypothesis: crust slips at the Moho over fixed keels",
          "Cross-section schematic, not to scale; idea from 2026-11-25, untested. Section 8.", ysub=0.95)
    fig.subplots_adjust(top=0.86, hspace=0.3, bottom=0.07)
    keels = [(0.6, 3.6, "keel A"), (8.4, 11.4, "keel B")]
    for ax in axs:
        blank(ax, (-0.3, 12.3), (-0.2, 3.3))
        ax.add_patch(Rectangle((0, 0), 12, 1.0, fc=MANTLE, ec=INK, lw=0.8))
        for (x0, x1, n) in keels:
            ax.add_patch(Polygon([[x0, 1.0], [x1, 1.0], [x1 - 0.3, 0.0], [x0 + 0.3, 0.0]], fc=KEEL, ec=INK, lw=1.2))
            ax.text((x0 + x1) / 2, 0.4, n + " (fixed)", ha="center", color="white", fontsize=10)
        ax.add_patch(Rectangle((0, 1.0), 12, 0.12, fc=SLIP, ec="none"))

    def crust(ax, x0, x1, label, fc=CRUST):
        ax.add_patch(Rectangle((x0, 1.12), x1 - x0, 0.9, fc=fc, ec=INK, lw=1.4))
        ax.text((x0 + x1) / 2, 1.57, label, ha="center", va="center", fontsize=10)

    axs[0].set_title("Before: the crust fragment sits over keel A", fontsize=12, loc="left")
    crust(axs[0], 0.4, 3.8, "crust fragment")
    axs[1].set_title("During: it shears off at the Moho and slides; the slip layer is the only place that heats", fontsize=12, loc="left")
    crust(axs[1], 4.2, 7.6, "crust fragment (sliding)", fc="#d9cdb0")
    arrow(axs[1], (4.4, 2.45), (7.4, 2.45), color=SLIP)
    axs[1].text(9.0, 2.6, "dissipation only in the thin\nslip layer at ~35 km", fontsize=10, color=SLIP, ha="center")
    axs[2].set_title("After: it has swapped keel A for keel B; the vacated ground is bare or needs new crust (H9)", fontsize=12, loc="left")
    crust(axs[2], 8.0, 11.8, "crust fragment on keel B")
    axs[2].add_patch(Rectangle((0.6, 1.12), 3.0, 0.9, fc="none", ec=BAD, lw=1.6, ls="--"))
    axs[2].text(2.1, 1.57, "keel A: new crust\nor bare mantle?", ha="center", va="center", fontsize=9.5, color=BAD)
    axs[2].text(5.8, 2.5, "P9 / H11 met: every craton sits on a keel,\nbut not the keel it started on", fontsize=10, color=GOOD, ha="center")
    handles = [Rectangle((0, 0), 1, 1, fc=KEEL), Rectangle((0, 0), 1, 1, fc=SLIP), Rectangle((0, 0), 1, 1, fc=CRUST)]
    fig.legend(handles, ["keel (stays put)", "slip layer at the Moho", "crust (moves)"],
               loc="lower center", ncol=3, frameon=False, fontsize=11)
    save(fig, "04_fixed_keel_crust_slip")


# ---------------------------------------------------------------- 05
def fig05():
    fig, ax = plt.subplots(figsize=(11.5, 6.8))
    title(fig, "05  Slip-zone heating depends on stress, distance and zone thickness, not on speed",
          "ΔT = τ·d / (ρc·h), ρc = 2.7×10$^6$ J/m$^3$/K; no latent heat or conduction; hand arithmetic. Section 8.2.")
    fig.subplots_adjust(top=0.86)
    d = [i * 50 for i in range(0, 80)]
    cases = [(0.2, 3, "#3b7d4f", "0.2 MPa, 3 km zone"), (0.2, 1, "#8ab17d", "0.2 MPa, 1 km zone"),
             (1.0, 3, "#c8902c", "1 MPa, 3 km zone"), (1.0, 1, "#b03a2e", "1 MPa, 1 km zone")]
    for tau, h, c, lab in cases:
        ax.plot(d, [tau * 1e6 * x * 1e3 / (2.7e6 * h * 1e3) for x in d], color=c, lw=2.6, label=lab)
    for x, lab in [(500, "500 km"), (931, "931 km\nmedian misfit"), (1900, "1,900 km\nhalf the opening"),
                   (3841, "3,841 km\nmean path")]:
        ax.axvline(x, color="#999", lw=1, ls=":")
        ax.text(x, 1540, lab, fontsize=9, ha="center", va="top", color="#444")
    ax.set_xlim(0, 3950)
    ax.set_ylim(0, 1560)
    ax.set_xlabel("Distance slid over the fixed keel (km)")
    ax.set_ylabel("Temperature rise of the slip zone (K)")
    ax.legend(frameon=False, loc="upper left", bbox_to_anchor=(0.01, 0.80), fontsize=11)
    ax.spines[["top", "right"]].set_visible(False)
    ax.text(0.99, 0.43, "For comparison, v2: shearing the asthenosphere at\n0.30 m/s needs 37-951 MPa and heats the layer\n180-9,200 K (350-8,900 × budget B). Ruled out.",
            transform=ax.transAxes, ha="right", fontsize=10, color=BAD)
    ax.text(0.01, 0.50, "The real stress of a Moho slip layer\nis not known (test T2).",
            transform=ax.transAxes, ha="left", fontsize=10, color="#555")
    save(fig, "05_slip_zone_heating")


# ---------------------------------------------------------------- 06
def fig06():
    fig, axs = plt.subplots(1, 3, figsize=(15, 5.8))
    title(fig, "06  The hardest test: does craton crust sit over a keel of the same outline?",
          "Map-view schematic, not to scale. Section 8.3 (item 1) and test T1. T1 result (Section 8.5): 67-70% of craton area on lithosphere ≥ 150 km, against 36-42% for random landing (two models).")
    fig.subplots_adjust(top=0.78)
    for ax in axs:
        blank(ax, (0, 10), (-0.6, 7.6))

    def keel(ax, x, y, w, h):
        ax.add_patch(Rectangle((x, y), w, h, fc=KEEL, ec=INK, alpha=0.45, lw=1.2))

    def cr(ax, x, y, w, h, ec=INK, ls="-"):
        ax.add_patch(Rectangle((x, y), w, h, fc="none", ec=ec, lw=2.5, ls=ls))

    axs[0].set_title("Today: craton crust broadly over thick lithosphere (67-70%)", fontsize=11)
    keel(axs[0], 1, 2, 3.6, 3)
    cr(axs[0], 1.1, 2.1, 3.4, 2.8)
    keel(axs[0], 5.8, 1.5, 3, 3.8)
    cr(axs[0], 5.9, 1.6, 2.8, 3.6)
    axs[0].text(5, 0.5, "purple = keel,  outline = crust", ha="center", fontsize=10)
    axs[1].set_title("If crust slid over fixed keels: it must stop on one", fontsize=11)
    keel(axs[1], 1, 2, 3.6, 3)
    keel(axs[1], 5.8, 1.5, 3, 3.8)
    cr(axs[1], 1.1, 2.1, 3.4, 2.8, ec=SLIP, ls="--")
    cr(axs[1], 5.9, 1.6, 2.8, 3.6, ec=GOOD)
    arrow(axs[1], (2.8, 5.7), (7.2, 5.7), color=SLIP)
    axs[1].text(5, 6.3, "crust slides", ha="center", fontsize=11, color=SLIP)
    axs[1].text(2.8, 1.3, "start", ha="center", fontsize=10, color=SLIP)
    axs[1].text(7.3, 0.7, "lands on keel B: match", ha="center", fontsize=10, color=GOOD)
    axs[2].set_title("What the test can find: mis-registered outlines", fontsize=11)
    keel(axs[2], 1, 2, 3.6, 3)
    keel(axs[2], 5.8, 1.5, 3, 3.8)
    cr(axs[2], 2.6, 0.7, 3.4, 2.8, ec=BAD)
    cr(axs[2], 6.6, 3.0, 2.8, 3.4, ec=BAD)
    axs[2].text(5, 7.1, "crust offset from keel by hundreds of km", ha="center", fontsize=10, color=BAD)
    axs[2].text(5, -0.4, "T1: 114 craton polygons compared with Afonso (2019) and LITHO1.0\nthickness models: loose match in both",
                ha="center", fontsize=10)
    save(fig, "06_registration_test")


# ---------------------------------------------------------------- 07
def fig07():
    fig, (a, b) = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={"width_ratios": [1, 1.2]})
    title(fig, "07  What sliding does not fix: the floor left behind (H9) and the force needed (H10)",
          "v2 Phase 6 (clean-room). Sections 7.2 and 8.3.")
    fig.subplots_adjust(top=0.82, wspace=0.55)
    labels = ["Need: ocean floor on\ncontinent-bearing plates", "C1: uncovered if carried\nfloor goes back to Pangea",
              "Transitional provinces\n(stranded continent)"]
    vals = [1.64, 1.08, 0.38]
    a.barh(labels, vals, color=["#9aa7b3", BAD, SEA], ec=INK)
    for i, v in enumerate(vals):
        a.text(v + 0.03, i, f"{v:.2f}×10$^8$ km$^2$", va="center", fontsize=11)
    a.set_xlim(0, 2.5)
    a.invert_yaxis()
    a.set_xlabel("Area (10$^8$ km$^2$)")
    a.spines[["top", "right"]].set_visible(False)
    a.set_title("New floor: 66% of the need is uncovered\n(302 × the H1 area limit)", fontsize=11)
    a.text(1.25, 2.75, "Exhumed mantle (C2) covers 21-85% at assumed\nwidths of 100-400 km. Sliding over fixed keels\nleaves these figures unchanged.",
           fontsize=9.5, color="#444", ha="center", va="top")
    a.set_ylim(3.6, -0.5)
    labs = ["Wet, 1,650 K", "Wet, 1,500 K", "Dry"]
    lo = [350, 1060, 2100]
    hi = [430, 1300, 8900]
    b.barh(labs, hi, color="#e0b0a8", ec=INK)
    b.barh(labs, lo, color=BAD, ec=INK)
    b.set_xscale("log")
    b.set_xlim(100, 6e4)
    b.invert_yaxis()
    b.axvline(1, color=GOOD)
    for i, (l, h) in enumerate(zip(lo, hi)):
        b.text(h * 1.1, i, f"{l:,}-{h:,} × B", va="center", fontsize=10.5)
    b.set_xlabel("Energy in 150 days, as multiples of the heat budget B (log scale)")
    b.set_title("Shearing the asthenosphere (H10): at least 350 × B", fontsize=11)
    b.spines[["top", "right"]].set_visible(False)
    fig.text(0.62, -0.03, "B = 1.4×10$^{26}$ J. A thin Moho slip layer, not the asthenosphere,\nis the untested alternative (Section 8).",
             ha="center", fontsize=10, color="#444")
    save(fig, "07_what_sliding_does_not_fix")


# ---------------------------------------------------------------- 08
def fig08():
    fig, ax = plt.subplots(figsize=(14, 8.4))
    title(fig, "08  DTAT and CMCT: who supplies what, and what is still open",
          "Interface from DTAT Section 12 and CMCT Section 23. Green = computed in v2, amber = hypothesis or flagged number, red = open or failing.")
    fig.subplots_adjust(top=0.9)
    blank(ax, (0, 14), (0, 8.2))

    def box(x, y, w, h, text, c, fs=10.5):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.04,rounding_size=0.15", fc=c, ec=INK, lw=1.4))
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs)

    ax.text(3.0, 7.7, "CMCT (vertical)", ha="center", fontsize=14, fontweight="bold", color=KEEL)
    ax.text(11.0, 7.7, "DTAT (sideways)", ha="center", fontsize=14, fontweight="bold", color=SLIP)
    box(0.4, 6.2, 5.2, 1.0, "Cause of submergence:\ncollapse of a crust-base layer + released water", "#f3d7d3")
    box(0.4, 4.9, 5.2, 1.0, "Constraints: heat budget B (1.4×10$^{26}$ J),\nwater budget H6, H1-H5, H9-H11", "#d6ead9")
    box(0.4, 3.6, 5.2, 1.0, "Candidate slip layer:\nserpentinite layer at the crust base", "#f6e6c4")
    box(0.4, 2.3, 5.2, 1.0, "Vent cracks along province boundaries\n(geometry only)", "#f6e6c4")
    box(8.4, 6.2, 5.2, 1.0, "Fragments: 647 + 136 provinces; nine-block fit\n(631 of 647 fit)", "#d6ead9")
    box(8.4, 4.9, 5.2, 1.0, "Motion: 3,841 km mean, 0.30 m/s in 150 d;\nasthenosphere drag fails (≥ 350 × B)", "#f3d7d3")
    box(8.4, 3.6, 5.2, 1.0, "Fixed-keel crust slip over the Moho\n(T1: match real but loose, 67-70% vs 36-42%)", "#f6e6c4")
    box(8.4, 2.3, 5.2, 1.0, "Collisions, uplift (ratio borrowed, P1), ten peaks;\nrecession: 33.3% stays submerged", "#f6e6c4")
    arrow(ax, (5.7, 6.7), (8.3, 6.7), color=KEEL, lw=2.4)
    ax.text(7.0, 6.85, "submerged land", ha="center", fontsize=9.5)
    arrow(ax, (5.7, 5.4), (8.3, 5.4), color=KEEL, lw=2.4)
    ax.text(7.0, 5.55, "limits", ha="center", fontsize=9.5)
    arrow(ax, (5.7, 4.1), (8.3, 4.1), color=KEEL, lw=2.4, style="<|-|>")
    ax.text(7.0, 4.25, "which side slips?", ha="center", fontsize=9.5)
    arrow(ax, (8.3, 2.8), (5.7, 2.8), color=SLIP, lw=2.4)
    ax.text(7.0, 2.95, "do collisions\nclose vents?", ha="center", fontsize=9.5)
    box(0.4, 0.4, 13.2, 1.3, "Shared and open:  H9 new floor (1.08×10$^8$ km$^2$ uncovered)  ·  H10 force and energy  ·  "
        "registration of crust over keels\norder of events (slide, collapse, collisions)  ·  lasting uplift after collision  ·  fragment paths",
        "#f3d7d3", fs=11)
    save(fig, "08_dtat_cmct_interface_and_open_problems")


for f in (fig01, fig02, fig03, fig04, fig05, fig06, fig07, fig08):
    f()
print("done")
