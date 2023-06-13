from io import TextIOWrapper
from kaitai_lithtech_dat_struct import LithtechDat
from os.path import splitext, basename

# import pymeshlab


def write_header(f: TextIOWrapper):
    f.write("# ***************************\n")
    f.write("# LT Dat converted by dat2obj\n")
    f.write("# ***************************\n")
    return


def write_body(f: TextIOWrapper, dat: LithtechDat):
    rd = dat.render_data
    wt = dat.world_tree
    wm: LithtechDat.WorldModel = [
        *filter(lambda x: x.world_name.data == "PhysicsBSP", wt.world_models)
    ][0]

    f.write("# All points\n")
    for p in wm.points:
        f.write(f"v {p.x * 0.01} {p.y * 0.01} {p.z * -0.01}\n")  # corrected for x z y
        continue
    f.write("# All polygons\n")
    for poly in wm.polygons:
        f.write(f"f {' '.join(str(i + 1) for i in poly.vertices_indices)}\n")
        continue
    return


def create_mtlib(f: TextIOWrapper):
    return


def convert_dat_to_obj(in_file):
    dat = LithtechDat.from_file(in_file)
    out_file = ".\\out\\" + basename(splitext(in_file)[0]) + ".obj"
    with open(out_file, "w") as f:
        write_header(f)
        write_body(f, dat)
        pass
    return out_file


# def fix_obj():
#     ms = pymeshlab.MeshSet()
#     ms.load_new_mesh(out_file)
#     ms.meshing_remove_duplicate_faces()
#     return
