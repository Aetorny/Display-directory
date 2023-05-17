import os
from sys import argv
from typing import List, Tuple, Optional
from directory_information import DISPLAY_DIRECTORY
from fnmatch import fnmatch
from file_interaction.files_parser import parse_files
from file_interaction.files_displayer import Displayer
from file_interaction.file_class import Files
from config import less


def check_to_search() -> bool:
    filename_idx = -1
    if '-s' in argv:
        filename_idx = argv.index('-s')
    elif '-search' in argv:
        filename_idx = argv.index('-search')

    max_recursion_idx = -1
    if '-smr' in argv:
        max_recursion_idx = argv.index('-smr')
    elif '-set-max-recursion' in argv:
        max_recursion_idx = argv.index('-set-max-recursion')

    max_recursion: Optional[str] = None
    if max_recursion_idx != -1 and max_recursion_idx <= len(argv) - 2:
        max_recursion = argv[max_recursion_idx+1]
        if not max_recursion.isdigit():
            max_recursion = None

    if filename_idx != -1 and filename_idx <= len(argv) - 2:
        if max_recursion:
            search(argv[filename_idx+1], int(max_recursion))
        else:
            search(argv[filename_idx+1])
        return True
    return False


finded_elements: List[Tuple[str, str]] = []


def search(filename: str, max_recursion: int = 3) -> None:
    global finded_elements
    finded_elements = []
    current_dir = DISPLAY_DIRECTORY
    _recursive_search(current_dir, filename, max_recursion=max_recursion)
    if len(finded_elements) == 0:
        return
    only_filenames: List[str] = []
    only_directories: List[str] = []
    for directory, filename in finded_elements:
        only_filenames.append(filename)
        only_directories.append(directory)


    files: Files = parse_files(only_filenames, only_directories)
    for file in files.files:
        if file.name_rus:
            file.name_eng = file.name_eng + ' {' + file.name_rus + '}' + '.' + file.extension
            name_idx = only_filenames.index(file.name_eng)
            file.name_rus = finded_elements[name_idx][0]
        else:
            name_idx = only_filenames.index(file.name_eng + '.' + file.extension)
            file.name_rus = finded_elements[name_idx][0]
        if less:
            path = file.name_rus
            tail, head_1 = os.path.split(path)
            _tail, head_2 = os.path.split(tail)
            file.name_rus = '...\\' + head_2 + '\\' + head_1
    Displayer().display_files(files)


def _recursive_search(
        current_dir: str,
        search_filename: str,
        current_recursion: int = 0,
        max_recursion: int = 3
    ) -> None:
    global finded_elements
    if current_recursion >= max_recursion:
        return
    files = os.listdir(current_dir)
    for filename in files:
        if fnmatch(filename, search_filename):
            finded_elements.append((current_dir, filename))
        if os.path.isdir(current_dir+'\\'+filename):
            _recursive_search(current_dir+'\\'+filename, search_filename, current_recursion+1, max_recursion)
