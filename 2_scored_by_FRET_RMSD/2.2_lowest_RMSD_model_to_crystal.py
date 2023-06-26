#!/usr/bin/env python3

# Align models with FRET > 0.4 and RMSD < 15 A to crystal structure

cmd.load("models_scored_by_FRET_and_RMSD.pdb")
cmd.load("6n2v_conformer1.pdb")

cmd.align("6n2v_conformer1", "models_scored_by_FRET_and_RMSD")

cmd.cartoon("tube")
cmd.set("cartoon_tube_radius", 1)
cmd.set("cartoon_ring_finder", 2)
cmd.set("cartoon_ring_mode", 1)
cmd.set("cartoon_ring_transparency", 0.5)
cmd.set("cartoon_ring_width", 0.3)
cmd.set_color("myorange", [247, 171, 126])
cmd.set_color("myorange_bright", [238, 203, 186])
cmd.set_color("myviolet", [141, 99, 179])
cmd.set_color("myviolet_bright", [187, 181, 209])

# color models
cmd.color(
    "myviolet",
    "models_scored_by_FRET_and_RMSD and ((chain B and resi 1-16) or (chain A and resi 35-57))",
)
cmd.color(
    "myviolet_bright", "models_scored_by_FRET_and_RMSD and (chain B and resi 17-32)"
)
cmd.color(
    "myorange",
    "models_scored_by_FRET_and_RMSD and ((chain A and resi 1-18) or (chain B and resi 33-48))",
)
cmd.color(
    "myorange_bright", "models_scored_by_FRET_and_RMSD and (chain A and resi 19-34)"
)

# color crystal structure
cmd.color("myorange", "6n2v_conformer1 and ((resi 1-17) or (resi 85-99))")
cmd.color("myorange_bright", "6n2v_conformer1 and (resi 18-35)")
cmd.color("myviolet", "6n2v_conformer1 and (resi 36-73)")
cmd.color("myviolet_bright", "6n2v_conformer1 and (resi 74-84)")


# show the model with the lowest RMSD to the crystal structure (model 21, RMSD = 8.6 A)
cmd.set("state", 21)
