from fnmatch import fnmatch
from sys import argv
from typing import List


def filter_sifting(files_names: List[str]) -> List[str]:
    condition = '*'
    for idx, arg in enumerate(argv):
        if arg == '-f':
            if idx+1 < len(argv):
                condition = argv[idx+1].lower()
            else:
                break
    files_names = [x for x in files_names if fnmatch(x.lower(), condition)]
    if condition != '*':
        print('Условие отбора:', condition)
    else:
        print()
    return files_names
