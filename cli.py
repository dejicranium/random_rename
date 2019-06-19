import argparse
from rename import RandomRename

import logging

def main():
    parser = argparse.ArgumentParser(description='Randomly rename files')
    parser.add_argument('-e', '--ext', help='extension type(s) of file(s) that need renaming')
    parser.add_argument('-p ', '--pre', help='prefix to add to each filename')
    parser.add_argument('paths', help='paths to search for files')

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

    query = True

    while query:
        reply = input('\nAre you really sure you wish to rename file(s). Action is irreversible. [Y/N]: \n')
        reply = reply.lower()
        valid = ['y', 'yes', 'no', 'n']
        if reply in valid:
            query = False
            if reply in valid[::2]:
                r = RandomRename(paths, prefixes=prefixes, extensions=extensions)
                r.rename_files()
            else:
                print('Aborted')
                pass
        else:
            print('\nYou can only choose either Yes(Y) or No(N)\n')
                
main()