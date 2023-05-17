from sys import argv


def _display_help() -> None:
    print('Доступные комманды')
    print('  -h | --help | -? : Для вызова меню помощи')
    print('  -l | -less : Для уменьшения вывода')
    print('  -m | -mt | --modificationtime : Для сортировки по дате последнего изменения')
    print('  -n | -name : (по умолчанию) Для сортировки по имени')
    print('  -a | -ascending : Для сортировки по возрастанию')
    print('  -d | -descending : Для сортировки по убыванию')
    print('  -f [паттерн] : Для отбора файлов по определённому паттерну (используется библиотека fnmatch)')
    print('  -s | -search [паттерн] : Для рекурсивного поиска файлов по паттерну (используется библиотека fnmatch)')
    print('  -smr | -set-max-recursion [число] : Для ограничения рекурсивного поиска (по умолчанию 3)')


def check_to_help() -> bool:
    if '-h' in argv or '--help' in argv or '-?' in argv:
        _display_help()
        return True
    return False
