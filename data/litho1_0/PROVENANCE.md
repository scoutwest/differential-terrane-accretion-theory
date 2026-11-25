# Provenance
Downloaded 2026-11-25 from the model authors' site: https://igppweb.ucsd.edu/~gabi/litho1/litho1.0.tar.gz (12.4 MB; the file is kept unmodified in this folder). Unpacked into `extracted/` (not tracked by git; re-create with `tar -xzf litho1.0.tar.gz -C extracted`). Only the data files are used; the C++ reader in `extracted/LITHO1.0/progs/` was not compiled or run.
Citation: Pasyanos, M.E., Masters, T.G., Laske, G., Ma, Z. (2014), "LITHO1.0: An updated crust and lithospheric model of the Earth", Journal of Geophysical Research 119, 2153-2173, doi:10.1002/2013JB010626.
Licence and terms of reuse were not checked.
`litho1_lab_0.4deg.npz` is derived (by `scripts/build_litho1_grid.py`): lithosphere thickness in km = depth of the LID-BOTTOM boundary minus the model's top surface, taking the nearest of the 40,962 icosahedral mesh nodes for each 0.4 degree grid node (largest distance to a node 75 km). Thickness on the grid: min 6, mean 107, max 323 km.
Used by `scripts/registration_test.py` with `T1_MODEL=litho1` (DTAT Section 8.5).
