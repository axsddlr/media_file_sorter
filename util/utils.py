import os

# create a list of video file extensions
import shutil

video_extensions = ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.mpeg', '.mpg', '.m4v', '.3gp', '.3g2', '.mts',
                    '.ts', '.webm']


def get_files(source_dir):
    """
    It takes a directory as an argument and returns a list of all the files in that directory and all of its subdirectories

    :param source_dir: the directory to get the files from
    :return: A list of all the files in the source directory and its subdirectories.
    """
    # get the files in the source directory
    files = os.listdir(source_dir)
    # create a list to store the files
    file_list = []
    # loop through the files
    for file in files:
        # get the file name
        file_name = os.path.join(source_dir, file)
        # if the file is a directory
        if os.path.isdir(file_name):
            # get the files in the subdirectory
            sub_files = get_files(file_name)
            # add the files to the list
            file_list.extend(sub_files)
        # if the file is a file
        else:
            # add the file to the list
            file_list.append(file)
    # return the list
    return file_list


# create function to delete empty directories
def remove_directories(path):
    if not os.listdir(path):
        os.rmdir(path)


# create function to delete small_files directory
def remove_small_files(path):
    if os.path.exists(path):
        shutil.rmtree(path)
        print("Removed small_files directory")
    else:
        print("Small_files directory does not exist")


# use get_files to move files to a directory called small_files
def move_small_files(path, size):
    """
    If the file extension is in the video_extensions list, get the file size and if the file size is less than 50MB, move
    the file to the small_files directory.

    :param path: the path to the directory you want to search
    """
    # Looping through the path, subdirectories, and files.
    for path, subdirs, files in os.walk(path):
        # Looping through the files in the path.
        for filename in files:
            # if the file extension is in the video_extensions list, add it to the list
            if os.path.splitext(filename)[1] in video_extensions:
                # This is checking to see if the operating system is Windows. If it is, it is replacing the backslashes
                # with forward slashes.
                if os.name == 'nt':
                    path = path.replace('\\', '/')
                else:
                    path = path

                # Splitting the path at the last forward slash and taking the first part of the split. Then it is adding
                # "/small_files" to the end of the path.
                dest_dir = path.rsplit("/", 1)[0] + "/small_files"
                # print(dest_dir)

                # Checking to see if the destination directory exists. If it does not exist, it creates the directory.
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)
                # Getting the file size of the file.
                file_size = os.path.getsize(os.path.join(path, filename))
                file_size_mb = file_size / 1000000
                # Checking to see if the file size is less than 50MB.
                if file_size_mb < size:
                    # Checking to see if the file exists in the destination directory. If it does, it will continue
                    # to the next file.
                    if os.path.exists(os.path.join(dest_dir, filename)):
                        continue
                    else:
                        # Moving the file from the path to the destination directory.
                        shutil.move(os.path.join(path, filename), dest_dir)


def get_file_sizes(path):
    """
    For each file in the path, if the file extension is in the video_extensions list, replace backslashes with forward
    slashes, get the file size, and print the file size.

    :param path: the path to the directory you want to get the file sizes from
    """
    for path, subdirs, files in os.walk(path):
        for filename in files:
            # if the file extension is in the video_extensions list, add it to the list
            if os.path.splitext(filename)[1] in video_extensions:
                # if path is windows, replace backslashes with forward slashes
                if os.name == 'nt':
                    path = path.replace('\\', '/')
                else:
                    path = path
                # get the file size
                file_size = os.path.getsize(os.path.join(path, filename))
                # print the file size
                print(filename + ": " + convert_bytes(file_size))


def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0
