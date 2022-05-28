import os
import argparse
import zipfile

parser = argparse.ArgumentParser()

parser.add_argument("src", type=str)
parser.add_argument("dst", type=str)

args = parser.parse_args()


path_list = []
try:
    if os.path.isdir(args.src) == True:
        for path in os.listdir(args.src):
            full_path = os.path.join(args.src, path)
            if os.path.isfile(full_path):
                path_list.append(full_path)
    else:
        path_list.append(args.src)

    with zipfile.ZipFile(args.dst, 'w') as new_zip:
        for name in path_list:
            new_zip.write(name)
except FileNotFoundError:
        print('Error: Path file (', args.src ,') not found')