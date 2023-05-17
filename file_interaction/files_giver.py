import os
from typing import List

from directory_information import DISPLAY_DIRECTORY


def get_files() -> List[str]:
    files = os.listdir(DISPLAY_DIRECTORY)
    return files
