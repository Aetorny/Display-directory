import os
from time import ctime
from typing import List, Tuple, Optional

from directory_information import DISPLAY_DIRECTORY
from file_interaction.file_class import File, Files
from config import less

__translates_month = {
    'Jan': 'Январь',
    'Feb': 'Февраль',
    'Mar': 'Март',
    'Apr': 'Апрель',
    'May': 'Май',
    'Jun': 'Июнь',
    'Jul': 'Июль',
    'Aug': 'Август',
    'Sep': 'Сентябрь',
    'Oct': 'Октябрь',
    'Nov': 'Ноябрь',
    'Dec': 'Декабрь'
}


def date_translate(date: str) -> str:
    # Translates dates kind 'Fri Apr 21 17:55:56 2023'
    # It translates it to   'ПЯТ АПР 21 17:55:56 2023'
    _day_of_week, month, date = date[:3], date[4:7], date[8:]

    month = __translates_month[month]

    date = month + ' ' + date
    return date


def parse_name(name: str) -> Tuple[str, str]:
    delimiter_idx = name.rfind('{')
    if delimiter_idx == -1:
        return name, ''
    name_eng, name_rus = name[:delimiter_idx-1], name[delimiter_idx+1:-1]
    return name_eng, name_rus


def parse_files(files_names: List[str], directories_of_folders: Optional[List[str]] = None) -> Files:
    files = Files()
    directory = DISPLAY_DIRECTORY

    files.files = []
    for idx, file_name in enumerate(files_names):
        if directories_of_folders:
            directory = directories_of_folders[idx]
        
        extension_delimiter = file_name.rfind('.')
        if extension_delimiter > 0:
            name, extension = file_name[:extension_delimiter], file_name[extension_delimiter+1:]
        else:
            name, extension = file_name[:], ''

        name_eng, name_rus = parse_name(name)

        if os.path.isdir(f'{directory}\\{file_name}'):
            file_type = '<DIR>'
        else:
            file_type = ''

        modification_date_secounds = int(
            os.path.getmtime(f'{directory}\\{file_name}'))
        if not less:
            modification_date = ctime(modification_date_secounds)
            modification_date = date_translate(modification_date)
        else:
            modification_date = ''

        file = File()
        file.name_eng = name_eng
        file.name_rus = name_rus
        file.extension = extension
        file.type = file_type  # type: ignore
        file.modification_date = modification_date
        file.modification_date_secounds = modification_date_secounds

        files.files.append(file)

    return files
