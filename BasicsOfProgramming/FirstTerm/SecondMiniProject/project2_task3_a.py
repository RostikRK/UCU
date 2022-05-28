import os
import argparse
import zipfile
import re
from zipfile import ZipFile


parser = argparse.ArgumentParser()

parser.add_argument("fpater", type=str)
parser.add_argument("pathh1", type=str)
parser.add_argument("pathh2", type=str)


args = parser.parse_args()
try:
    with ZipFile(args.pathh1, 'r') as zipObj:
    # Extract all the contents of zip file in current directory
        zipObj.extractall('temp')

    fileswithpat = []
    curdir = os.getcwd()
    ddir = curdir + "/temp/"
    fileslis = os.listdir(ddir)
    for file in fileslis:
        match = re.search(args.fpater, file)
        if match:
            fileswithpat.append(file)
except FileNotFoundError:
        print('Error: Path file (', args.pathh1 ,', or ', args.patth2,') not found')