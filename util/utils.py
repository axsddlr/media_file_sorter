import shutil
from pathlib import Path

import cv2

video_extensions = [
    ".mp4",
    ".avi",
    ".mkv",
    ".mov",
    ".wmv",
    ".flv",
    ".mpeg",
    ".mpg",
    ".m4v",
    ".3gp",
    ".3g2",
    ".mts",
    ".ts",
    ".webm",
]


def move_files(path, size=None, duration=None, target=None):
    path = Path(path)

    for file in path.glob("**/*"):
        if file.suffix.lower() in video_extensions and file.is_file():
            video = cv2.VideoCapture(str(file))
            file_duration = video.get(cv2.CAP_PROP_POS_MSEC) / 1000

            should_move = False
            if size is not None:
                should_move = file.stat().st_size <= size
            elif duration is not None:
                should_move = file_duration <= duration

            if should_move:
                dest_dir = file.parent / target
                dest_dir.mkdir(exist_ok=True)
                shutil.move(file, dest_dir / file.name)


def move_small_files(path, size_mb):
    size_bytes = size_mb * 1024 * 1024
    move_files(path, size=size_bytes, target="small_files")


def move_short_duration_files(path, duration_sec):
    move_files(path, duration=duration_sec, target="short_duration_files")


def move_long_duration_files(path, duration_sec):
    move_files(path, duration=duration_sec, target="long_duration_files")


def get_file_sizes(path):
    path = Path(path)

    for file in path.glob("**/*"):
        if file.suffix.lower() in video_extensions and file.is_file():
            print(f"{file.name}: {file.stat().st_size} bytes")


def get_video_duration(path):
    path = Path(path)

    for file in path.glob("**/*"):
        if file.suffix.lower() in video_extensions and file.is_file():
            video = cv2.VideoCapture(str(file))
            duration_sec = video.get(cv2.CAP_PROP_POS_MSEC) / 1000
            print(f"{file.name}: {duration_sec} seconds")


import os
import shutil
from pathlib import Path

import cv2

video_extensions = [
    ".mp4",
    ".avi",
    ".mkv",
    ".mov",
    ".wmv",
    ".flv",
    ".mpeg",
    ".mpg",
    ".m4v",
    ".3gp",
    ".3g2",
    ".mts",
    ".ts",
    ".webm",
]


def move_files(path, size=None, duration=None, target=None):
    path = Path(path)

    for file in path.glob("**/*"):
        if file.suffix.lower() in video_extensions and file.is_file():
            video = cv2.VideoCapture(str(file))
            file_duration = video.get(cv2.CAP_PROP_POS_MSEC) / 1000

            should_move = False
            if size is not None:
                should_move = file.stat().st_size <= size
            elif duration is not None:
                should_move = file_duration <= duration

            if should_move:
                dest_dir = file.parent / target
                dest_dir.mkdir(exist_ok=True)
                shutil.move(file, dest_dir / file.name)


def get_files(path):
    path = Path(path)
    files_list = []

    for file in path.glob("**/*"):
        if file.suffix.lower() in video_extensions and file.is_file():
            files_list.append(str(file))

    return files_list


def move_small_files(path, size_mb):
    size_bytes = size_mb * 1024 * 1024
    move_files(path, size=size_bytes, target="small_files")


def move_short_duration_files(path, duration_sec):
    move_files(path, duration=duration_sec, target="short_duration_files")


def move_long_duration_files(path, duration_sec):
    move_files(path, duration=duration_sec, target="long_duration_files")


def get_file_sizes(path):
    path = Path(path)

    for file in path.glob("**/*"):
        if file.suffix.lower() in video_extensions and file.is_file():
            print(f"{file.name}: {file.stat().st_size} bytes")


def get_video_duration(path):
    path = Path(path)

    for file in path.glob("**/*"):
        if file.suffix.lower() in video_extensions and file.is_file():
            video = cv2.VideoCapture(str(file))
            duration_sec = video.get(cv2.CAP_PROP_POS_MSEC) / 1000
            print(f"{file.name}: {duration_sec} seconds")


def remove_short_duration_files(path, duration_sec):
    path = Path(path)

    for file in path.glob("**/*"):
        if file.suffix.lower() in video_extensions and file.is_file():
            video = cv2.VideoCapture(str(file))
            file_duration = video.get(cv2.CAP_PROP_POS_MSEC) / 1000

            if file_duration <= duration_sec:
                os.remove(file)
