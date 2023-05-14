try:
    from colorama import Fore, init
    is_colorama_installed = True
except ModuleNotFoundError:
    is_colorama_installed = False

from file_interaction.file_class import Files
import os


class Displayer:
    def _colorize_string(self, s: str) -> str:
        if not is_colorama_installed:
            return s

        if self.file_type == '<DIR>':
            s = Fore.YELLOW + s + Fore.RESET
        if self.file_extension == 'py':
            s = Fore.CYAN + s + Fore.RESET

        return s

    def _create_end_string(self) -> str:
        s = f'{self.idx:{self.max_idx}}  {self.name_rus:{self.max_file_name_rus}}  '
        name = self.name_eng
        if self.max_file_name_eng == 0:
            return s
        for i in range(0, len(name), self.max_file_name_eng):
            if i != 0:
                s += '\n'
                s += f'{" ":{self.max_idx}}  {" ":{self.max_file_name_rus}} '
            name_part = name[i:i+self.max_file_name_eng]
            s += f'{name_part:{self.max_file_name_eng+1}}'
            if i == 0:
                s += f'  {self.file_extension:{self.max_file_extension}}  {self.modification_date:{self.max_modification_date}}  {self.file_type}'
        s = self._colorize_string(s.strip('\n'))
        return s

    def display_files(self, files: Files) -> None:
        init()
        columns = os.get_terminal_size().columns
        self.max_idx = len(str(len(files.files)))
        self.max_file_name_eng = max(
            len(x.name_eng) for x in files.files
        )
        self.max_file_name_rus = max(len(x.name_rus) for x in files.files)
        self.max_file_extension = max(len(x.extension) for x in files.files)
        self.max_modification_date = max(
            len(x.modification_date) for x in files.files)
        self.max_file_name_eng = min(self.max_file_name_eng, columns-16-self.max_idx-self.max_file_name_rus-self.max_file_extension-self.max_modification_date)
        for idx, file in enumerate(files.files):
            self.idx = idx+1
            self.name_eng = file.name_eng
            self.name_rus = file.name_rus
            self.file_extension = file.extension
            self.modification_date = file.modification_date
            self.file_type = file.type
            to_print = self._create_end_string()
            print(to_print)
