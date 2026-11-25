"""Test T1 (DTAT Section 8.4): does craton crust sit over a thick keel of about the same outline?

Inputs (read by path, not copied):
  - Afonso et al. (2019, GJI 217, 1602) lithospheric thickness grid, 0.2 deg, metres
    (data/afonso_2019/lithospheric-thickness-griddata.nc, from the EarthByte GPlates portal)
  - Hasterok et al. (2022) craton and province polygons from Noah's Pangea v2/data/hasterok_2022

Measures
  1. Share of each craton's area where lithosphere is at least T km thick (T = 150, 180; P9 range 150-250 km).
  2. Where the thick lithosphere is: under cratons, under other continental/transitional provinces, or elsewhere.
  3. Null: the same craton shapes rigidly moved to random places (a) anywhere on the globe, (b) onto continental or
     transitional provinces only. What share would then sit on thick lithosphere?
  4. Offset: slide each craton outline over the grid (up to +-1,500 km) and find the shift that puts the most of it on
     thick lithosphere. How far from zero is the best shift?

Run from the repo root.  h5py is needed to read the HDF5-based grid; if it is not installed globally, point DTAT_PYLIB at
a folder that holds it.  Output: results/registration_test_log.txt and results/registration_test_cratons.csv
"""
import csv
import os
import sys

if os.environ.get("DTAT_PYLIB"):
    sys.path.insert(0, os.environ["DTAT_PYLIB"])
import h5py
import numpy as np
import shapefile
import shapely
from shapely.geometry import shape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V2 = os.path.normpath(os.path.join(ROOT, "..", "Noah's Pangea v2", "data", "hasterok_2022"))
NC = os.path.join(ROOT, "data", "afonso_2019", "lithospheric-thickness-griddata.nc")
# Thickness model: "afonso" (default) or "litho1" (run scripts/build_litho1_grid.py first). Set with T1_MODEL.
MODEL = os.environ.get("T1_MODEL", "afonso")
SUFFIX = "" if MODEL == "afonso" else "_" + MODEL
os.makedirs(os.path.join(ROOT, "results"), exist_ok=True)
RNG = np.random.default_rng(1656)
R_EARTH = 6371.0
STRIDE = 2           # use every 2nd grid node (0.4 deg) for masks and areas
THRESHOLDS = (150.0, 180.0)
N_DRAWS = 300
MAX_PTS = 3000
SHIFTS_KM = np.arange(-1500, 1501, 100)

out = []


def p(s=""):
    print(s)
    out.append(s)


# ---------------------------------------------------------------- grid
with h5py.File(NC, "r") as f:
    lat_full = np.array(f["lat"], dtype=float)
    lon_full = np.array(f["lon"], dtype=float)
    lab_full = np.array(f["z"], dtype=float) / 1000.0     # km
lab = lab_full[::STRIDE, ::STRIDE]
lat = lat_full[::STRIDE]
lon = lon_full[::STRIDE]
if MODEL == "litho1":
    z = np.load(os.path.join(ROOT, "data", "litho1_0", "litho1_lab_0.4deg.npz"))
    assert STRIDE == 2 and np.allclose(z["lat"], lat) and np.allclose(z["lon"], lon)
    lab = z["lab_km"]
nlat, nlon = lab.shape
LON, LAT = np.meshgrid(lon, lat)
dlat = np.radians(lat[1] - lat[0])
dlon = np.radians(lon[1] - lon[0])
cell_area = (R_EARTH ** 2) * dlat * dlon * np.cos(np.radians(LAT))      # km2 per node
cell_area = np.clip(cell_area, 0, None)
p("T1 REGISTRATION TEST: craton crust against lithosphere thickness")
if MODEL == "litho1":
    p(f"Model: LITHO1.0 (Pasyanos et al. 2014), LID-BOTTOM minus surface, nearest of 40,962 mesh nodes, on a {nlat}x{nlon} grid at 0.4 deg.")
else:
    p(f"Grid: Afonso et al. (2019), {lab_full.shape[0]}x{lab_full.shape[1]} at 0.2 deg, used every {STRIDE}nd node ({nlat}x{nlon}).")
p(f"Lithosphere thickness: min {lab.min():.0f} km, mean {np.average(lab, weights=cell_area):.0f} km, max {lab.max():.0f} km (grid values read as metres).")
p(f"Total area on grid: {cell_area.sum():.3e} km2 (sphere: {4*np.pi*R_EARTH**2:.3e}).")


def lookup(latd, lond):
    i = np.clip(np.rint((latd - lat[0]) / (lat[1] - lat[0])).astype(int), 0, nlat - 1)
    j = np.clip(np.rint((((lond + 180.0) % 360.0) - 180.0 - lon[0]) / (lon[1] - lon[0])).astype(int), 0, nlon - 1)
    return lab[i, j]


def rasterize(geom):
    minx, miny, maxx, maxy = geom.bounds
    i0 = max(0, int(np.floor((miny - lat[0]) / (lat[1] - lat[0]))))
    i1 = min(nlat, int(np.ceil((maxy - lat[0]) / (lat[1] - lat[0]))) + 1)
    j0 = max(0, int(np.floor((minx - lon[0]) / (lon[1] - lon[0]))))
    j1 = min(nlon, int(np.ceil((maxx - lon[0]) / (lon[1] - lon[0]))) + 1)
    m = np.zeros((nlat, nlon), bool)
    if i1 <= i0 or j1 <= j0:
        return m
    sub = shapely.contains_xy(geom, LON[i0:i1, j0:j1], LAT[i0:i1, j0:j1])
    m[i0:i1, j0:j1] = sub
    return m


# ---------------------------------------------------------------- polygons
def load(name):
    r = shapefile.Reader(os.path.join(V2, name), encoding="utf-8", encodingErrors="replace")
    return [(rec.as_dict(), shape(s.__geo_interface__)) for rec, s in zip(r.records(), r.shapes())]


cratons = load("cratons")
provs = load("global_gprv")
p(f"Cratons: {len(cratons)} polygons. Provinces: {len(provs)}.")

crat_masks = []
for rec, g in cratons:
    m = rasterize(g)
    if m.sum() == 0:     # polygon smaller than one node: use a representative point
        pt = g.representative_point()
        i = int(np.rint((pt.y - lat[0]) / (lat[1] - lat[0])))
        j = int(np.rint((pt.x - lon[0]) / (lon[1] - lon[0])))
        m[min(max(i, 0), nlat - 1), min(max(j, 0), nlon - 1)] = True
    crat_masks.append(m)
crat_union = np.any(crat_masks, axis=0)

cont_union = np.zeros((nlat, nlon), bool)
for rec, g in provs:
    if rec.get("crust_type") in ("continental", "transitional"):
        cont_union |= rasterize(g)
noncraton_cont = cont_union & ~crat_union

# ---------------------------------------------------------------- 1. per-craton thick-share
area_c = np.array([cell_area[m].sum() for m in crat_masks])
p(f"\nCraton area on this grid: {area_c.sum():.3e} km2 (Section 4 of the DTAT document gives 4.08e7 km2 from polygon geometry).")
rows = []
for T in THRESHOLDS:
    fr = np.array([cell_area[m & (lab >= T)].sum() / cell_area[m].sum() for m in crat_masks])
    rows.append(fr)
frac150, frac180 = rows
agg150 = (frac150 * area_c).sum() / area_c.sum()
agg180 = (frac180 * area_c).sum() / area_c.sum()
mean_lab_c = np.array([np.average(lab[m], weights=cell_area[m]) for m in crat_masks])
agg_mean = np.average(mean_lab_c, weights=area_c)
p("\n1. HOW MUCH OF EACH CRATON SITS ON THICK LITHOSPHERE (observed, zero offset)")
p(f"   Area-weighted mean lithosphere thickness under cratons: {agg_mean:.0f} km")
p(f"   Share of craton area with lithosphere >= 150 km: {agg150*100:.0f}%   (>= 180 km: {agg180*100:.0f}%)")
for T, fr in zip(THRESHOLDS, rows):
    p(f"   Cratons (count of {len(fr)}) with at least 50% of their area >= {T:.0f} km: {int((fr >= 0.5).sum())}; "
      f"at least 80%: {int((fr >= 0.8).sum())}; under 20%: {int((fr < 0.2).sum())}")
order = np.argsort(frac150)
p("   Thinnest-keel cratons (share >= 150 km, area km2), the cases that look decoupled:")
for k in order[:10]:
    p(f"     {cratons[k][0]['prov_name'][:34]:34s} {cratons[k][0]['continent'][:14]:14s} {frac150[k]*100:5.0f}%  mean {mean_lab_c[k]:4.0f} km  area {area_c[k]:.2e}")

# ---------------------------------------------------------------- 2. where is the thick lithosphere
p("\n2. WHERE THE THICK LITHOSPHERE IS (global)")
for T in THRESHOLDS:
    thick = lab >= T
    tot = cell_area[thick].sum()
    a = cell_area[thick & crat_union].sum() / tot
    b = cell_area[thick & noncraton_cont].sum() / tot
    c = cell_area[thick & ~cont_union].sum() / tot
    p(f"   Lithosphere >= {T:.0f} km covers {tot:.3e} km2 ({tot/cell_area.sum()*100:.1f}% of the Earth): "
      f"{a*100:.0f}% under cratons, {b*100:.0f}% under other continental/transitional provinces, {c*100:.0f}% outside all provinces (ocean or unmapped).")
nc_share = cell_area[noncraton_cont & (lab >= 150)].sum() / cell_area[noncraton_cont].sum()
p(f"   For comparison, {nc_share*100:.0f}% of non-craton continental/transitional area is >= 150 km thick "
  f"(craton: {agg150*100:.0f}%).")

# ---------------------------------------------------------------- 3. null: rigid random placement
def unit(latd, lond):
    la, lo = np.radians(latd), np.radians(lond)
    return np.stack([np.cos(la) * np.cos(lo), np.cos(la) * np.sin(lo), np.sin(la)], -1)


def to_latlon(v):
    return np.degrees(np.arcsin(np.clip(v[..., 2], -1, 1))), np.degrees(np.arctan2(v[..., 1], v[..., 0]))


def rot_axis(axis, ang):
    axis = axis / np.linalg.norm(axis)
    K = np.array([[0, -axis[2], axis[1]], [axis[2], 0, -axis[0]], [-axis[1], axis[0], 0]])
    return np.eye(3) + np.sin(ang) * K + (1 - np.cos(ang)) * (K @ K)


def rot_c_to_t(c, t):
    ax = np.cross(c, t)
    n = np.linalg.norm(ax)
    if n < 1e-12:
        return np.eye(3)
    return rot_axis(ax, np.arccos(np.clip(np.dot(c, t), -1, 1)))


# subsample points per craton (area weighted by construction: cells are equal-weight after cos(lat) sampling)
pts = []
for m in crat_masks:
    ii, jj = np.nonzero(m)
    w = cell_area[ii, jj]
    if len(ii) > MAX_PTS:
        sel = RNG.choice(len(ii), MAX_PTS, replace=False, p=w / w.sum())
        ii, jj = ii[sel], jj[sel]
    pts.append((LAT[ii, jj], LON[ii, jj]))
cont_cells = np.nonzero(cont_union)
cont_w = cell_area[cont_union]
cont_w = cont_w / cont_w.sum()

null_a = {T: [] for T in THRESHOLDS}
null_b = {T: [] for T in THRESHOLDS}
cen = []
for (la, lo) in pts:
    v = unit(la, lo)
    c = v.mean(0)
    cen.append(c / np.linalg.norm(c))
for d in range(N_DRAWS):
    acc = {("a", T): 0.0 for T in THRESHOLDS}
    acc.update({("b", T): 0.0 for T in THRESHOLDS})
    for k, (la, lo) in enumerate(pts):
        v = unit(la, lo)
        for mode in ("a", "b"):
            if mode == "a":
                t = RNG.normal(size=3)
                t /= np.linalg.norm(t)
            else:
                idx = RNG.choice(len(cont_w), p=cont_w)
                t = unit(LAT[cont_cells[0][idx], cont_cells[1][idx]], LON[cont_cells[0][idx], cont_cells[1][idx]])
            R = rot_axis(t, RNG.uniform(0, 2 * np.pi)) @ rot_c_to_t(cen[k], t)
            la2, lo2 = to_latlon(v @ R.T)
            labv = lookup(la2, lo2)
            for T in THRESHOLDS:
                acc[(mode, T)] += area_c[k] * np.mean(labv >= T)
    for T in THRESHOLDS:
        null_a[T].append(acc[("a", T)] / area_c.sum())
        null_b[T].append(acc[("b", T)] / area_c.sum())
p(f"\n3. NULL: the same {len(cratons)} craton shapes moved rigidly to random places ({N_DRAWS} draws, each craton independent)")
for T, obs in zip(THRESHOLDS, (agg150, agg180)):
    for lbl, nul in (("anywhere on the globe", null_a[T]), ("only onto continental/transitional provinces", null_b[T])):
        lo_, hi_ = np.percentile(nul, [2.5, 97.5])
        p(f"   >= {T:.0f} km, placed {lbl}: mean {np.mean(nul)*100:.0f}% (95% range {lo_*100:.0f}-{hi_*100:.0f}%); observed {obs*100:.0f}%")

# ---------------------------------------------------------------- 4. offset search
p("\n4. BEST OFFSET: slide each craton outline up to +-1,500 km; find the shift that puts most of it on >= 150 km lithosphere")
KM_PER_DEG = 111.195
best_off = []
profile = []   # per craton: mean score by offset radius
RBINS = [0, 100, 200, 300, 500, 800, 1100, 1600]
zero_sc = []
best_sc = []
for k, (la, lo) in enumerate(pts):
    lat_c = np.degrees(np.arcsin(cen[k][2]))
    best = (-1, None)
    scores = {}
    for dn in SHIFTS_KM:
        for de in SHIFTS_KM:
            la2 = np.clip(la + dn / KM_PER_DEG, -89.9, 89.9)
            lo2 = lo + de / (KM_PER_DEG * max(np.cos(np.radians(lat_c)), 0.05))
            s = np.mean(lookup(la2, lo2) >= 150.0)
            scores[(dn, de)] = s
    smax = max(scores.values())
    rad = np.array([np.hypot(dn, de) for (dn, de) in scores])
    val = np.array(list(scores.values()))
    profile.append([val[(rad >= RBINS[b]) & (rad < RBINS[b + 1])].mean() if b > 0 else val[rad == 0].mean()
                    for b in range(len(RBINS) - 1)])
    cands = [(np.hypot(dn, de), (dn, de)) for (dn, de), s in scores.items() if s >= smax - 0.01]
    off = min(cands)[0]
    best_off.append(off)
    zero_sc.append(scores[(0, 0)])
    best_sc.append(smax)
best_off = np.array(best_off)
zero_sc = np.array(zero_sc)
best_sc = np.array(best_sc)
p(f"   Median offset of the best placement: {np.median(best_off):.0f} km (zero offset means the observed outline is already best).")
p(f"   Cratons whose observed position is within 1 point of the best placement found: {int((zero_sc >= best_sc - 0.01).sum())} of {len(cratons)}; "
  f"within 10 points: {int((zero_sc >= best_sc - 0.10).sum())}")
p(f"   Offsets at or under 100 km: {int((best_off <= 100).sum())}; 100-500 km: {int(((best_off > 100) & (best_off <= 500)).sum())}; "
  f"over 500 km: {int((best_off > 500).sum())}")
p(f"   Area-weighted mean share >= 150 km at zero offset: {np.average(zero_sc, weights=area_c)*100:.0f}%; at the best offset: {np.average(best_sc, weights=area_c)*100:.0f}% "
  f"(a search over {len(SHIFTS_KM)**2} shifts always finds something at least as good, so the second figure is an upper bound).")

profile = np.array(profile)
p("\n   How the share >= 150 km falls off as the craton outline is moved away from where it is (area-weighted mean over cratons and directions):")
labels = ["0 km (observed)", "1-100 km", "100-200 km", "200-300 km", "300-500 km", "500-800 km", "800-1,100 km"]
for b, lab_ in enumerate(labels):
    p(f"     {lab_:18s} {np.average(profile[:, b], weights=area_c)*100:5.1f}%")
p("   (offset bins are measured on a 100 km shift grid, so the 1-100 km bin holds shifts of 100 km only; 1,100-1,500 km shifts are in the search but not binned.)")

# ---------------------------------------------------------------- reading
p("\nLIMITS")
p("   The thickness grid is a model (Afonso et al. 2019: joint inversion of seismic, gravity, elevation, heat-flow and petrological data).")
p("   Some of its structure may follow the surface geology it was constrained by, so the match may be partly built in; a second, independent")
p("   model (for example LITHO1.0) has not been run. No ages are used (P1). Grid stride 0.4 deg; sampled up to 3,000 points per craton;")
p("   the offset search is a flat-earth shift, adequate to a few degrees but not at high latitude; the null moves each craton as a rigid shape.")
p("   'Thick keel' thresholds follow P9's 150-250 km; the mapping from lithosphere thickness to keel is the model's, not a measurement of a chemical keel.")

open(os.path.join(ROOT, "results", f"registration_test_log{SUFFIX}.txt"), "w", encoding="utf-8").write("\n".join(out) + "\n")
with open(os.path.join(ROOT, "results", f"registration_test_cratons{SUFFIX}.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["craton", "continent", "area_km2_grid", "mean_lab_km", "share_ge150", "share_ge180", "zero_offset_ge150",
                "best_offset_ge150", "best_offset_km"])
    for k, (rec, g) in enumerate(cratons):
        w.writerow([rec["prov_name"], rec["continent"], f"{area_c[k]:.0f}", f"{mean_lab_c[k]:.1f}", f"{frac150[k]:.3f}",
                    f"{frac180[k]:.3f}", f"{zero_sc[k]:.3f}", f"{best_sc[k]:.3f}", f"{best_off[k]:.0f}"])
