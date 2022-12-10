import argparse
from util.utils import *

if __name__ == '__main__':
    # create an argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='the path to search')
    parser.add_argument('--move_small', help='move files to small files directory', action='store_true')
    parser.add_argument('--get_file_sizes', help='get file sizes', action='store_true')
    parser.add_argument('--size', help='the size to move files to', type=int)
    parser.add_argument('--duration', help='get video duration', type=int)
    parser.add_argument('--get_files', help='get files', action='store_true')
    parser.add_argument('--remove_empty', help='remove small_files and large_files directories', action='store_true')
    parser.add_argument('--remove_small', help='remove small_files and large_files directories', action='store_true')
    parser.add_argument('--get_video_duration', help='get video duration', action='store_true')
    parser.add_argument('--get_short_video', help='get short video duration (in minutes)', action='store_true')
    parser.add_argument('--get_long_video', help='get long video duration (in minutes)', action='store_true')

    args = parser.parse_args()
    # get the path
    path = args.path

    # define a dictionary of functions, where the keys are the names of the arguments
    # and the values are the functions to call
    functions = {
        'move_small': lambda: move_small_files(path, args.size),
        'get_file_sizes': lambda: get_file_sizes(path),
        'get_files': lambda: print(get_files(path)),
        'remove_empty': lambda: remove_directories(path),
        'remove_small': lambda: remove_small_files(path),
        'get_video_duration': lambda: get_video_duration(path),
        'get_short_video': lambda: move_short_duration_files(path, args.duration),
        'get_long_video': lambda: move_long_duration_files(path, args.duration),
    }

    # get the key of the first argument passed to the script, and use it to retrieve the
    # corresponding function from the functions dictionary
    # if no argument is passed, print an error message and exit
    arg = next(iter(args.keys()), None)
    func = functions.get(arg)
    if func:
        func()
    else:
        print('No arguments passed')
        print('Please use --help for more information')
        print('Exiting...')
        exit()
