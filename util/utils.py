import os
import shutil

SUBDIRS = {
    "VIDEOS": ['.mov', '.avi', '.mp4', '.m4v', '.ogv', '.webm', '.wmv']
}


# create a function that lists all the files in a directory based on SUBDIRS
def get_files(dir_name):
    """
    It loops through the SUBDIRS dictionary, and for each subdirectory, it loops through the extensions, and for each
    extension, it loops through the files in the directory, and if the file has the extension, it adds it to the list.

    :param dir_name: the directory to search for files
    :return: A list of files
    """
    # create a list to store the files
    files = []
    # loop through the SUBDIRS
    for subdir, extensions in SUBDIRS.items():
        # loop through the extensions
        for extension in extensions:
            # get the files in the path
            for file in os.listdir(dir_name):
                # if the file has the extension
                if file.endswith(extension):
                    # add the file to the list
                    files.append(file)
    # return the list
    return files


def move_small(source_dir):
    """
    Move all files in the source directory that are less than 100 megabytes to the destination directory

    :param source_dir: the directory where the files are currently located
    """
    # get current working directory and create dest_dir named small_files
    cwd = os.getcwd()
    dest_dir = os.path.join(cwd, 'small_files')
    # create a list to store the file sizes

    # get the files in the source directory
    files = get_files(source_dir)
    # loop through the files
    for file in files:
        # get the file size
        file_size = os.path.getsize(os.path.join(source_dir, file))
        # if the file size is greater than 100 megabytes
        if file_size < 100000000:
            # create a directory if it doesn't exist
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            # move the file to the destination directory
            shutil.move(os.path.join(source_dir, file), dest_dir)   # move the file to the destination directory


def move_large(source_dir):
    """
    Move all files in the source directory that are less than 100 megabytes to the destination directory

    :param source_dir: the directory where the files are currently located
    """
    # get current working directory and create dest_dir named small_files
    cwd = os.getcwd()
    dest_dir = os.path.join(cwd, 'small_files')
    # create a list to store the file sizes

    # get the files in the source directory
    files = get_files(source_dir)
    # loop through the files
    for file in files:
        # get the file size
        file_size = os.path.getsize(os.path.join(source_dir, file))
        # if the file size is greater than 100 megabytes
        if file_size > 100000000:
            # create a directory if it doesn't exist
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            # move the file to the destination directory
            shutil.move(os.path.join(source_dir, file), dest_dir)   # move the file to the destination directory


