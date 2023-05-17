from check_to_help import check_to_help
from search import check_to_search
from file_interaction.file_filter_sifting import filter_sifting
from file_interaction.files_displayer import Displayer
from file_interaction.files_giver import get_files
from file_interaction.files_parser import parse_files
from file_interaction.files_sort import sort_files


def main() -> None:
    if check_to_help():
        return
    if check_to_search():
        return
    files_names = get_files()
    files_names = filter_sifting(files_names)
    if len(files_names) == 0:
        return
    files = parse_files(files_names)
    sort_files(files)
    Displayer().display_files(files)


if __name__ == '__main__':
    main()
