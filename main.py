import argparse
from util.utils import *

if __name__ == '__main__':

    # Creating an argument parser, adding arguments, parsing the arguments, and then calling the functions based on the
    # arguments.
    # create an argument parser
    parser = argparse.ArgumentParser()
    # add an argument
    parser.add_argument('path', help='path to the directory')
    # add and argument for get_files function
    parser.add_argument('--get_files', action='store_true')
    # add and argument for get_file_sizes function
    parser.add_argument('--get_sizes', action='store_true')
    # add and argument for move_files function
    parser.add_argument('--move_files', action='store_true')
    # add and argument for move_small_files function
    parser.add_argument('--only_small', action='store_true')
    # add and argument for move_large_files function
    parser.add_argument('--only_large', action='store_true')
    # add and argument for remove_small_files function
    parser.add_argument('--remove_small', action='store_true')
    # add and argument for remove_large_files function
    parser.add_argument('--remove_large', action='store_true')
    # parse the arguments
    args = parser.parse_args()
    # get the path
    path = args.path
    # call the move_small_files function if the --move_small_files argument is passed
    if args.only_small:
        move_small_files(path)
    # call the move_large_files function if the --move_large_files argument is passed
    if args.only_large:
        move_large_files(path)
    # call the remove_small_files function if the remove_small_files argument is True
    if args.remove_small:
        remove_small_files(path)
    # call the remove_large_files function if the remove_small_files argument is True
    if args.remove_large:
        remove_large_files(path)
    # call the move_files function if the --move_files argument is passed
    if args.move_files:
        move_files(path)
    # call the get_file_sizes function if the --get_file_sizes argument is passed
    if args.get_sizes:
        print(get_file_sizes(path))
    # call the get_files function if the --get_files argument is passed
    if args.get_files:
        print(get_files(path))
