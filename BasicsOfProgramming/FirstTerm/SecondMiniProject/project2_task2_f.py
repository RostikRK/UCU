import argparse
import re
import os

parser = argparse.ArgumentParser()

parser.add_argument('freg', type=str)
parser.add_argument('fpater', type=str)
parser.add_argument('--show_lines', action='store_true')
parser.add_argument('--only_show_counts', action='store_true')

args = parser.parse_args()

path_list = os.listdir()
fileswithpat = []
count = 0

for file in path_list:
    match = re.search(args.fpater, file)
    if match:
        fileswithpat.append(file)

try:
    if args.only_show_counts:
        for fil in fileswithpat:
            with open(fil, 'rt') as f:
                for line in f:
                    if line.__contains__('love'):
                        count += 1
        print(count)
    else:
        if args.show_lines:
            for fil in fileswithpat:
                with open(fil, 'rt') as f:
                    dataLog =[]
                    for num, line in enumerate(f, 1):
                        if line.__contains__('love'):
                            newlin = str(num) + ":" + line
                            dataLog.append(newlin)
                    if len(dataLog)>=1:
                        print(fil)
                        print("".join(dataLog))
                    dataLog = []
        else:
            for fil in fileswithpat:
                with open(fil, 'rt') as f:
                    dataLog =[]
                    for line in f:
                        if line.__contains__(args.freg):
                            dataLog.append(line)
                    if len(dataLog)>=1:
                        print(fil)
                        print("".join(dataLog))
                    dataLog = []
except:
    None