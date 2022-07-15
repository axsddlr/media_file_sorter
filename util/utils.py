import os
import shutil

import cv2

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
    # get the files in the path
    files = os.listdir(path)
    # if the files list is empty, delete the directory
    if not files:
        os.rmdir(path)
    # if the files list is not empty, loop through the files
    else:
        for f in files:
            # if the file is a directory, call the function again
            if os.path.isdir(os.path.join(path, f)):
                remove_directories(os.path.join(path, f))


def remove_small_files(path):
    """
    This function will delete the small_files directory.

    :param path: the path to the directory you want to delete the small_files directory from
    """
    # if the small_files directory exists, delete it
    if os.path.exists(os.path.join(path, "small_files")):
        shutil.rmtree(os.path.join(path, "small_files"))


def move_small_files(path, size: int):
    """
    It will move all files that are less than 50MB in size to a
    directory called "small_files" in the same directory as the file.

    :param path: This is the path to the directory that you want to move the files from
    :param size: This is the size of the file in MB
    :type size: int
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

                    # if small_files directory is empty, delete it
                    if not os.listdir(dest_dir):
                        os.rmdir(dest_dir)


def move_short_duration_files(path, duration: float):
    """
    It will move all files that are less than 50MB in size to a
    directory called "small_files" in the same directory as the file.

    :param path: This is the path to the directory that you want to move the files from
    :param duration: This is the duration of the video in seconds
    :type duration: int
    """
    # Looping through the path, subdirectories, and files.
    for path, subdirs, files in os.walk(path):
        # Looping through the files in the path.
        for filename in files:
            # if the file extension is in the video_extensions list, add it to the list
            if os.path.splitext(filename)[1] in video_extensions:
                # if path is windows, replace backslashes with forward slashes
                if os.name == 'nt':
                    path = path.replace('\\', '/')
                else:
                    path = path
                # get the file size
                dur = get_dur(os.path.join(path, filename))
                dest_dir = path.rsplit("/", 1)[0] + "/small_files"
                # print the file size
                # print(filename + ": " + dur)
                # if the duration is less than the duration argument, move the file to the small_files directory
                if dur < duration:
                    # Checking to see if the destination directory exists. If it does not exist, it creates the
                    # directory.
                    if not os.path.exists(dest_dir):
                        os.makedirs(dest_dir)
                    if os.path.exists(os.path.join(dest_dir, filename)) and os.path.exists(dest_dir):
                        continue
                    else:
                        # Moving the file from the path to the destination directory.
                        shutil.move(os.path.join(path, filename), dest_dir)


def move_long_duration_files(path, duration: float):
    """
    If the file is a video file, get the duration of the file. If the
    duration is greater than the duration argument, move the file to the large_files directory.

    :param path: The path to the directory you want to move files from
    :param duration: The duration of the video in seconds
    :type duration: float
    """
    # Looping through the path, subdirectories, and files.
    for path, subdirs, files in os.walk(path):
        # Looping through the files in the path.
        for filename in files:
            # if the file extension is in the video_extensions list, add it to the list
            if os.path.splitext(filename)[1] in video_extensions:
                # if path is windows, replace backslashes with forward slashes
                if os.name == 'nt':
                    path = path.replace('\\', '/')
                else:
                    path = path
                # get the file size
                dur = get_dur(os.path.join(path, filename))
                dest_dir = path.rsplit("/", 1)[0] + "/large_files"
                # print the file size
                # print(filename + ": " + dur)
                # if the duration is less than the duration argument, move the file to the small_files directory
                if dur > duration:
                    # Checking to see if the file exists in the destination directory. If it does, it will continue
                    # to the next file.
                    if not os.path.exists(dest_dir):
                        os.makedirs(dest_dir)
                    if os.path.exists(os.path.join(dest_dir, filename)) and os.path.exists(dest_dir):
                        continue
                    else:
                        # Moving the file from the path to the destination directory.
                        shutil.move(os.path.join(path, filename), dest_dir)


def get_video_duration(path):
    """
    For each file in the directory, if the file extension is in the video_extensions list, get the file size and print the
    file name and size

    :param path: the path to the directory you want to search
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
                dur = get_dur(os.path.join(path, filename))
                # print the file size
                print(filename + ": " + dur)


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
    It takes a number of bytes and returns a string with the number and the unit of measurement

    :param num: The number of bytes to convert
    :return: the size of the file in bytes, KB, MB, GB, or TB.
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def get_dur(filename):
    """
    It takes a video file as input and returns the duration of the video in minutes

    :param filename: The name of the video file
    :return: the duration of the video in minutes.
    """
    video = cv2.VideoCapture(filename)
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
    seconds = frame_count / fps
    minutes = int(seconds / 60)
    rem_sec = int(seconds % 60)
    # return f"{minutes}:{rem_sec}"
    return minutes
