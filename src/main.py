import argparse
from rename import RandomRename

commands = ['enter', 'show']
parser = argparse.ArgumentParser(description='Randomly rename files')
parser.add_argument('-e', '--ext', help='extension type(s) of file(s) that need renaming')
parser.add_argument('-p ', '--pre', help='prefix to give files')

parser.add_argument('-com', '--command', help='command that needs to be evaluated')
parser.add_argument('paths', help='path to search for files')

args = parser.parse_args()
prefixes = None
paths = None
extensions =  None

if args.paths: 
    prefixes = args.pre.split(',')
if args.paths: 
    paths = args.paths.split(',')
if args.ext:
    extensions = args.ext.split(',')


r = RandomRename(paths, prefixes=prefixes, extensions=extensions)
r.rename_files()
        

