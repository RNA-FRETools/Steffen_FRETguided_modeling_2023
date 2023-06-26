#!/usr/bin/env python3
from pymol import cmd


@cmd.extend
def smooth_map_from_xyz(
    name,
    selection,
    contour_level,
    grid_spacing,
    bfactor=100,
    gaussRes=2,
    grid_buffer=2,
    state=0,
):
    """Creates a map object from a selection with xyz coordinates (e.g. a PDB or XYZ object)
    and draws a smooth isosurface at the specified contour level.
    """
    name_surf = name + "_isosurf"
    name_map = name + "_map"
    bfactor_str = "b={:d}".format(int(bfactor))
    cmd.alter(selection, bfactor_str)
    cmd.alter(selection, bfactor_str)
    gaussRes_default = cmd.get("gaussian_resolution")
    cmd.set("gaussian_resolution", gaussRes)
    cmd.map_new(name_map, "gaussian", grid_spacing, selection, state=state)
    cmd.isosurface(name_surf, name_map, contour_level, selection, buffer=grid_buffer)
    cmd.set("gaussian_resolution", gaussRes_default)
    cmd.disable(selection)


cmd.load("top10_models_scored_by_rosetta_energy.pdb")

cmd.cartoon("tube")
cmd.set("cartoon_tube_radius", 1)

cmd.load("top10_rosetta_energy_acv_D.pdb", discrete=1)
cmd.load("top10_rosetta_energy_acv_A.pdb", discrete=1)

smooth_map_from_xyz("Cy3", "top10_rosetta_energy_acv_D", 0, 1)
smooth_map_from_xyz("Cy5", "top10_rosetta_energy_acv_A", 0, 1)
smooth_map_from_xyz("Cy3_CV", "top10_rosetta_energy_acv_D and resn CV", 0.7, 1)
smooth_map_from_xyz("Cy5_CV", "top10_rosetta_energy_acv_A and resn CV", 0.7, 1)

cmd.set_color("mygreen", [108, 179, 129])
cmd.set_color("myred", [194, 84, 73])
cmd.set_color("myorange", [247, 171, 126])
cmd.set_color("myorange_bright", [238, 203, 186])
cmd.set_color("myviolet", [141, 99, 179])
cmd.set_color("myviolet_bright", [187, 181, 209])
cmd.color("mygreen", "Cy3_isosurf")
cmd.color("myred", "Cy5_isosurf")
cmd.color("mygreen", "Cy3_CV_isosurf")
cmd.color("myred", "Cy5_CV_isosurf")
cmd.set("transparency", 0.4, "Cy3_isosurf")
cmd.set("transparency", 0.4, "Cy5_isosurf")
cmd.color("myviolet", "(chain B and resi 1-16) or (chain A and resi 35-57)")
cmd.color("myviolet_bright", "(chain B and resi 17-32)")
cmd.color("myorange", "(chain A and resi 1-18) or (chain B and resi 33-48)")
cmd.color("myorange_bright", "(chain A and resi 19-34)")
