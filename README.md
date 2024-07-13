# FRET-guided modeling of nucleic acids
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10963197.svg)](https://doi.org/10.5281/zenodo.10963197)

> [!NOTE]
> Please cite: Fabio D Steffen, Richard A Cunha, Roland K O Sigel, Richard Börner, FRET-guided modeling of nucleic acids, *Nucleic Acids Research*, **2024**, https://doi.org/10.1093/nar/gkae496

This repository contains structural models of the proof-of-concept *de novo* modeling trial of a **manganese(II) sensing riboswitch** (PDB 6n2v). The modeling code can be found [here](https://github.com/RNA-FRETools/rosettascripts/blob/master/tutorial/Mn_riboswitch.md).

The resulting models are organized as follows:

* `1_scored_by_rosetta_energy/` contains the top 10 models **scored by the Rosetta energy function from FARFAR2** (Watkins, *Structure* 2020) was well as  donor and acceptor accessible-contact volumes (ACV). 
The predicted mean FRET values computed by [*FRETraj*](https://github.com/RNA-FRETools/fretraj/) and the Rosetta energy scores are listed in `top10_rosetta_energy_FRET_prediction.csv`

|state|FRET|name        |Rosetta_score|
|-----|----|------------|-------------|
|1    |0.79|S_000292_003|-193.882     |
|2    |0.1 |S_000014_004|-188.55      |
|3    |0.09|S_000290_008|-186.863     |
|4    |0.07|S_000059_012|-185.191     |
|5    |0.19|S_000083_009|-185.004     |
|... |

Visualize the ACVs on the structural models by running the following Python script from the **PyMOL command line**
```
run top10_rosetta_energy.py
```

---

* `2_scored_by_FRET_RMSD/` contains models **filtered by a FRET treshold >0.4 and a RMSD < 15 A**. All models are superimposed and aligned to the crystal structure (PDB 6n2v). The best model (no. 21) has a RMSD of 8.6 A to the crystal structure.
The calculated RMSDs and Rosetta energy scores are listed in `models_scored_by_FRET_and_RMSD.csv`

|state|RMSD       |name        |Rosetta_score|
|-----|-----------|------------|-------------|
|1    |11.70476341|S_000355_008|-184.459     |
|2    |11.52333355|S_000086_010|-175.494     |
|3    |12.03283024|S_000054_007|-173.63      |
|... |
|**21**   |8.576731682|S_000273_005|-157.595     |
|... |

Visualize the overlay of the low RMSD models
```
run 2.1_lowest_RMSD_model_overlay.py
```

Compare the individual models to the crystal structure
```
run 2.2_lowest_RMSD_model_to_crystal.py
```

