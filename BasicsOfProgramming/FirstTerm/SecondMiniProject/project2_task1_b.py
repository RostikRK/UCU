import argparse

parser = argparse.ArgumentParser()

parser.add_argument('str1', type=str)
parser.add_argument('str2', type=str)
parser.add_argument('pathh', type=str)
parser.add_argument('--inplace', action='store_true')

args = parser.parse_args()


try:
    if args.inplace:
        with open(args.pathh, 'r') as file:
            olddat = file.read()
        newdat = olddat.replace(args.str1, args.str2)
        with open(args.pathh, 'w') as file:
            file.write(newdat)
    else:
        file = open(args.pathh,'r')
        olddat = file.read()
        file.close()
        print(olddat.replace(args.str1, args.str2))
except FileNotFoundError:
        print('Error: Path file (', args.pathh ,') not found')