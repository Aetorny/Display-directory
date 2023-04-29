from sys import argv


def _display_help() -> None:
    print('Доступные комманды')
    print('-h | --help | -? : Для вызова меню помощи')
    print('-m | -mt | --modificationtime : Для сортировки по дате последнего изменения')
    print('-n | --name : (по умолчанию) Для сортировки по имени')
    print('-a | --ascending : Для сортировки по возрастанию')
    print('-d | --descending : Для сортировки по убыванию')
    print('-f [паттерн] : Для отбора файлов по определённому паттерну (используется библиотека fnmatch)')


def check_to_help() -> bool:
    if '-h' in argv or '--help' in argv or '-?' in argv:
        _display_help()
        return True
    return False
