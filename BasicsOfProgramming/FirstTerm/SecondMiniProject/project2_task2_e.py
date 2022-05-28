import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("pathh", type=str)

args = parser.parse_args()

path_list = []


try:
    for path in os.listdir(args.pathh):
        full_path = os.path.join(args.pathh, path)
        if os.path.isfile(full_path):
            path_list.append(full_path)

    for fil in path_list:
        os.remove(fil)
    os.rmdir(args.pathh)
except OSError as e:
    print("Error: %s : %s" % (args.pathh, e.strerror))