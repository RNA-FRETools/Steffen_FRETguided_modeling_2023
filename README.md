# Steffen et al., Manuscript submitted to *Nucleic Acids Research* 2023

This repository contains structural models of the *de novo* modeling workflow of a manganese(II) sensing riboswitch (PDB 6n2v, the modeling code can be found [here](https://github.com/RNA-FRETools/rosettascripts/blob/master/tutorial/Mn_riboswitch.md)).
The resulting models are organized as follows:

* `1_scored_by_rosetta_energy/` contains the top 10 models scored by the Rosetta energy function from FARFAR2 (Watkins, *Structure* 2020) along with the predicted donor and acceptor accessible-contact volumes (ACV). 
The predicted mean FRET values and Rosetta energy scores are listed in `top10_rosetta_energy_FRET_prediction.csv`

|state|FRET|name        |Rosetta_score|
|-----|----|------------|-------------|
|1    |0.79|S_000292_003|-193.882     |
|2    |0.1 |S_000014_004|-188.55      |
|3    |0.09|S_000290_008|-186.863     |
|4    |0.07|S_000059_012|-185.191     |
|5    |0.19|S_000083_009|-185.004     |
|6    |0.89|S_000355_008|-184.459     |
|7    |0.11|S_000017_003|-184.249     |
|8    |0.19|S_000280_003|-184.198     |
|9    |0.41|S_000175_010|-182.34      |
|10   |0.59|S_000086_004|-182.05      |


* `2_scored_by_FRET_RMSD/` contains models filtered by a FRET treshold >0.4 and a RMSD < 15 A. All models are superimposed and aligned to the crystal structure (PDB 6n2v). The best model (no. 21) has a RMSD of 8.6 A to the crystal structure.
The calculated RMSDs and Rosetta energy scores are listed in `models_scored_by_FRET_and_RMSD.csv`

|state|RMSD       |name        |Rosetta_score|
|-----|-----------|------------|-------------|
|1    |11.70476341|S_000355_008|-184.459     |
|2    |11.52333355|S_000086_010|-175.494     |
|3    |12.03283024|S_000054_007|-173.63      |
|4    |10.88898373|S_000020_003|-171.933     |
|5    |10.44953918|S_000258_005|-169.661     |
|6    |13.49610806|S_000338_007|-168.749     |
|7    |10.57738781|S_000204_011|-168.064     |
|8    |13.25025749|S_000019_004|-167.958     |
|9    |10.83572388|S_000175_000|-166.923     |
|10   |9.577008247|S_000285_011|-165.794     |
|11   |13.53243637|S_000122_000|-164.966     |
|12   |11.17252827|S_000155_013|-164.935     |
|13   |12.80242443|S_000303_003|-164.797     |
|14   |10.9003458 |S_000117_012|-163.64      |
|15   |11.6927042 |S_000110_003|-163.108     |
|16   |13.79495525|S_000340_005|-162.663     |
|17   |12.81744862|S_000108_011|-162.019     |
|18   |10.13959885|S_000160_008|-161.171     |
|19   |9.497522354|S_000049_005|-159.395     |
|20   |11.12359333|S_000284_004|-159.281     |
|21   |8.576731682|S_000273_005|-157.595     |
|22   |12.72814083|S_000195_012|-157.481     |
|23   |13.86498737|S_000051_007|-157.187     |
|24   |11.52849102|S_000140_007|-157.024     |
|25   |11.27006149|S_000219_003|-157.019     |


