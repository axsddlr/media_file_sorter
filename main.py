import argparse
from util.utils import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="the path to search")
    parser.add_argument(
        "--move_small", help="move files to small files directory", action="store_true"
    )
    parser.add_argument("--get_file_sizes", help="get file sizes", action="store_true")
    parser.add_argument("--size", help="the size to move files to", type=int)
    parser.add_argument("--duration", help="get video duration", type=int)
    parser.add_argument("--get_files", help="get files", action="store_true")
    parser.add_argument(
        "--remove_empty",
        help="remove small_files and large_files directories",
        action="store_true",
    )
    parser.add_argument(
        "--remove_small",
        help="remove small_files and large_files directories",
        action="store_true",
    )
    parser.add_argument(
        "--get_video_duration", help="get video duration", action="store_true"
    )
    parser.add_argument(
        "--get_short_video",
        help="get short video duration (in minutes)",
        action="store_true",
    )
    parser.add_argument(
        "--get_long_video",
        help="get long video duration (in minutes)",
        action="store_true",
    )

    args = parser.parse_args()
    path = args.path

    if not path:
        print("Please provide a path")
        exit(1)

    if args.move_small:
        if not args.size:
            print("Please provide a size using the --size argument")
            exit(1)
        move_small_files(path, args.size)
    elif args.get_file_sizes:
        get_file_sizes(path)
    elif args.get_files:
        print(get_files(path))
    elif args.remove_empty:
        remove_directories(path)
    elif args.remove_small:
        remove_small_files(path)
    elif args.get_video_duration:
        get_video_duration(path)
    elif args.get_short_video:
        if not args.duration:
            print("Please provide a duration using the --duration argument")
            exit(1)
        move_short_duration_files(path, args.duration)
    elif args.get_long_video:
        if not args.duration:
            print("Please provide a duration using the --duration argument")
            exit(1)
        move_long_duration_files(path, args.duration)
    else:
        print("No arguments passed")
        print("Please use --help for more information")
        print("Exiting...")
        exit()
