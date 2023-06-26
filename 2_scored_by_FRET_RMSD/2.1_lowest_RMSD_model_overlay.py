#!/usr/bin/env python3

# Overlay models with FRET > 0.4 and RMSD < 15 A to crystal structure

cmd.load("models_scored_by_FRET_and_RMSD.pdb")

cmd.set("all_states", "on")

cmd.cartoon("tube")
cmd.set("cartoon_tube_radius", 0.5)
cmd.set("cartoon_ring_finder", 0)
cmd.set("cartoon_ladder_mode", 0)
cmd.hide("sticks")
cmd.set_color("myorange", [247, 171, 126])
cmd.set_color("myorange_bright", [238, 203, 186])
cmd.set_color("myviolet", [141, 99, 179])
cmd.set_color("myviolet_bright", [187, 181, 209])
cmd.color("myviolet", "(chain B and resi 1-16) or (chain A and resi 35-57)")
cmd.color("myviolet_bright", "(chain B and resi 17-32)")
cmd.color("myorange", "(chain A and resi 1-18) or (chain B and resi 33-48)")
cmd.color("myorange_bright", "(chain A and resi 19-34)")
