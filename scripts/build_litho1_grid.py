"""Turn LITHO1.0 (Pasyanos et al. 2014) node files into a lithosphere-thickness grid on the same 0.4 deg lat/lon nodes
that registration_test.py uses for the Afonso et al. (2019) grid.

Reads data/litho1_0/extracted/LITHO1.0/litho_model (the author's native files, unpacked from litho1.0.tar.gz).
Each node file lists layer boundaries; the LID-BOTTOM line gives the lithosphere-asthenosphere boundary as a depth in metres
below sea level, and the last line gives the model's top surface (negative = land above sea level). Thickness is
LID-BOTTOM depth minus top depth. Nodes are the 40,962 vertices of a level-7 icosahedral mesh (about 110 km apart);
each grid node takes the value of the nearest mesh node.  Output: data/litho1_0/litho1_lab_0.4deg.npz (lat, lon, lab_km).
Run from the repo root (needs h5py only to read the Afonso grid for its lat/lon axes; set DTAT_PYLIB if needed).
"""
import os
import sys

if os.environ.get("DTAT_PYLIB"):
    sys.path.insert(0, os.environ["DTAT_PYLIB"])
import h5py
import numpy as np
from scipy.spatial import cKDTree

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M = os.path.join(ROOT, "data", "litho1_0", "extracted", "LITHO1.0", "litho_model")
NC = os.path.join(ROOT, "data", "afonso_2019", "lithospheric-thickness-griddata.nc")

coords = np.loadtxt(os.path.join(M, "Icosahedron_Level7_LatLon_mod.txt"))      # columns: geocentric lat, geographic lat, lon
n = len(coords)
lab = np.full(n, np.nan)
top = np.full(n, np.nan)
for k in range(1, n + 1):
    lid = None
    last = None
    with open(os.path.join(M, f"node{k}.model"), encoding="ascii", errors="replace") as fh:
        for line in fh:
            parts = line.split()
            if len(parts) < 10:
                continue
            last = parts
            if parts[-1] == "LID-BOTTOM" and lid is None:
                lid = float(parts[0])
    if lid is not None and last is not None and last[-1].endswith("-TOP"):
        lab[k - 1] = lid
        top[k - 1] = float(last[0])
thick_km = (lab - top) / 1000.0
ok = np.isfinite(thick_km)
print(f"nodes {n}; usable {ok.sum()}; thickness km: min {np.nanmin(thick_km):.0f}, mean {np.nanmean(thick_km):.0f}, max {np.nanmax(thick_km):.0f}")

with h5py.File(NC, "r") as f:
    lat = np.array(f["lat"], dtype=float)[::2]
    lon = np.array(f["lon"], dtype=float)[::2]


def unit(la, lo):
    la, lo = np.radians(la), np.radians(lo)
    return np.stack([np.cos(la) * np.cos(lo), np.cos(la) * np.sin(lo), np.sin(la)], -1)


tree = cKDTree(unit(coords[ok, 1], coords[ok, 2]))
LON, LAT = np.meshgrid(lon, lat)
d, idx = tree.query(unit(LAT.ravel(), LON.ravel()))
grid = thick_km[ok][idx].reshape(LAT.shape)
print(f"grid {grid.shape}; max distance to a mesh node {np.degrees(2*np.arcsin(d.max()/2))*111.195:.0f} km")
np.savez(os.path.join(ROOT, "data", "litho1_0", "litho1_lab_0.4deg.npz"), lat=lat, lon=lon, lab_km=grid)
print("saved")
