import os
from sys import argv

_cur_dir = os.getcwd()
if len(argv) > 1 and not argv[1].startswith('-'):
    _cur_dir = os.path.join(_cur_dir, argv[1].strip('"'))
    if argv[1].startswith('C:'):
        _cur_dir = argv[1].strip('"')

DISPLAY_DIRECTORY = os.path.realpath(_cur_dir)

if not os.path.exists(DISPLAY_DIRECTORY):
    raise FileNotFoundError(
        f'Этот путь ведёт не до папки или содержит ошибки: {DISPLAY_DIRECTORY}')

print('\tТекущая директория:', DISPLAY_DIRECTORY, end='  ')
