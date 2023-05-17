from sys import argv

from file_interaction.file_class import Files


def sort_files(files: Files) -> None:
    if '-m' in argv or '-mt' in argv or '-modificationtime' in argv:
        if '-d' in argv or '-descending' in argv:
            files.sort(('modification_date', 'descending'))
        else:
            files.sort(('modification_date', 'ascending'))
        return
    if '-d' in argv or '-descending' in argv:
        files.sort(('name', 'descending'))
    else:
        files.sort(('name', 'ascending'))
