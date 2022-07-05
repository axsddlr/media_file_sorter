import argparse

from util.utils import move_small_files, get_files, get_file_sizes, remove_directories

if __name__ == '__main__':
    # create an argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='the path to search')
    parser.add_argument('--move_small', help='move files to small files directory', action='store_true')
    parser.add_argument('--get_file_sizes', help='get file sizes', action='store_true')
    parser.add_argument('--size', help='the size to move files to', type=int)
    parser.add_argument('--get_files', help='get files', action='store_true')
    parser.add_argument('--remove_all', help='remove small_files and large_files directories', action='store_true')

    args = parser.parse_args()
    # get the path
    path = args.path
    # call the move_small_files function if the --move_small_files argument is passed
    # call move_large function with size argument if the --move_large argument is passed
    if args.move_small:
        if not args.size:
            print('Please provide a size using the --size argument')
            exit(1)
        move_small_files(path, args.size)
    elif args.get_file_sizes:
        if not path:
            print('Please provide a path')
            exit(1)
        get_file_sizes(path)
    elif args.get_files:
        if not path:
            print('Please provide a path')
            exit(1)
        print(get_files(path))
    elif args.remove_all:
        if not path:
            print('Please provide a path')
            exit(1)
        remove_directories(path)
    else:
        print('No arguments passed')
        print('Please use --help for more information')
        print('Exiting...')
        exit()
