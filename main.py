import argparse
from util.utils import move_small, move_large


if __name__ == '__main__':
    # create an argument parser
    parser = argparse.ArgumentParser()
    # add an argument for the path
    parser.add_argument('path', help='the path to search')
    # add and argument for move_small function
    parser.add_argument('--move_small', help='move files to small files directory', action='store_true')
    parser.add_argument('--move_large', help='move files to large files directory', action='store_true')
    args = parser.parse_args()
    # get the path
    path = args.path
    # call the move_small_files function if the --move_small_files argument is passed
    if args.move_small:
        move_small(path)
    if args.move_large:
        move_large(path)
