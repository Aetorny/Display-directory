import os
from typing import List

from directory_information import DISPLAY_DIRECTORY


def get_files() -> List[str]:
    files = os.listdir(DISPLAY_DIRECTORY)
    if '.mypy_cache' in files:
        files.remove('.mypy_cache')
    if '__pycache__' in files:
        files.remove('__pycache__')
    return files
