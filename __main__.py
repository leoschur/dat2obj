from dat2obj import convert_dat_to_obj  # , fix_obj
import sys
from os import getcwd
from os.path import isfile, isdir, curdir

dat = sys.argv[1]
if not isfile(dat):
    print(f"File: {dat} does not exist or is not a file.")
    exit(-1)

if __name__ == "__main__":
    print("Starting conversion...\n")
    out_file = convert_dat_to_obj(dat)
    print(f"Finished conversion. File saved to {getcwd()}\\.out\\{out_file}\n")
    # print("Removing duplicates\n")
    # fix_obj()
    # print("Done.")
    pass
