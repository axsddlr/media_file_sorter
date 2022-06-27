import os
import shutil

# A dictionary that contains a list of video extensions.
SUBDIRS = {
    "VIDEOS": ['.mov', '.avi', '.mp4', '.m4v', '.ogv', '.webm', '.wmv']
}


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


def get_file_sizes(dir_name):
    """
    It loops through the subdirectories and extensions, and then loops through the files in the directory, and if the file
    has the extension, it gets the file size and converts it to megabytes, and then adds it to the list

    :param dir_name: the name of the directory to search
    :return: A list of file sizes in megabytes.
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
                    # get the file size
                    size = os.path.getsize(file)
                    # convert the size to megabytes
                    size = size / 1000000
                    # add the file size to the list
                    files.append(size)
    # return the list
    return files


def move_files(dir_name):
    """
    It takes a directory name as an argument, gets the files in that directory, creates two new directories, and moves the
    files to the new directories based on their size

    :param dir_name: the name of the directory that contains the files you want to move
    """
    # get the files
    files = get_files(dir_name)

    # create a new directory
    if not os.path.exists('large_files'):
        os.makedirs('large_files')
    if not os.path.exists('small_files'):
        os.makedirs('small_files')

    # loop through the files and move them to the new directory if they are less than 100mb
    for file in files:
        # get the file size
        size = os.path.getsize(file)

        # if the file is less than 100mb
        if size > 100000000:
            # move the file to the new directory
            os.rename(file, 'large_files/' + file)
        elif size < 100000000:
            # move the file to the new directory
            os.rename(file, 'small_files/' + file)


def move_large_files(dir_name):
    """
    "Move all files in a directory that are larger than 100mb to a new directory called large_files."

    Now, let's break down the function into its parts

    :param dir_name: the name of the directory that contains the files you want to move
    """
    # get the files
    files = get_files(dir_name)

    # create a new directory
    if not os.path.exists('large_files'):
        os.makedirs('large_files')

    # loop through the files and move them to the new directory if they are less than 100mb
    for file in files:
        # get the file size
        size = os.path.getsize(file)

        # if the file is less than 100mb
        if size > 100000000:
            # move the file to the new directory
            os.rename(file, 'large_files/' + file)


def move_small_files(dir_name):
    """
    "Move all files less than 100mb from the given directory to a new directory called 'small_files'."

    Now, let's look at the function line by line

    :param dir_name: the name of the directory that contains the files you want to move
    """
    # get the files
    files = get_files(dir_name)

    # create a new directory
    if not os.path.exists('small_files'):
        os.makedirs('small_files')

    # loop through the files and move them to the new directory if they are less than 100mb
    for file in files:
        # get the file size
        size = os.path.getsize(file)

        # if the file is less than 100mb
        if size < 100000000:
            # move the file to the new directory
            os.rename(file, 'small_files/' + file)


def remove_small_files(dir_name):
    """
    It removes the small_files directory if it exists, and then creates a new small_files directory.

    :param dir_name: the name of the directory that contains the files to be split
    """
    # remove the small_files directory
    if os.path.exists('small_files'):
        shutil.rmtree('small_files', ignore_errors=True)


def remove_large_files(dir_name):
    """
    It removes the `large_files` directory if it exists, and then creates a new `large_files` directory

    :param dir_name: the directory where the files are located
    """
    # remove the small_files directory
    if os.path.exists('large_files'):
        shutil.rmtree('large_files', ignore_errors=True)
