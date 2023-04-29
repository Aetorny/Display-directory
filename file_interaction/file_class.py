from typing import List, Literal, Tuple


class File:
    name_eng: str
    name_rus: str
    extension: str
    type: Literal['<DIR>', '']
    modification_date: str
    modification_date_secounds: int


class Files:
    files: List[File]

    def sort(
        self, sort_by: Tuple[
            Literal['modification_date', 'name'],
            Literal['ascending', 'descending']]
    ) -> None:
        if sort_by[0] == 'modification_date':
            if sort_by[1] == 'ascending':
                self.files.sort(
                    key=lambda x: self.__sort_by_creation_date_ascending(x))
            else:
                self.files.sort(
                    key=lambda x: self.__sort_by_creation_date_descending(x))
        else:
            if sort_by[1] == 'ascending':
                self.files.sort(key=lambda x: self.__sort_by_name_ascending(x))
            else:
                self.files.sort(
                    key=lambda x: self.__sort_by_name_descending(x))

    def __sort_by_creation_date_ascending(self, file: File) -> int:
        add = 0
        if file.type == '<DIR>':
            add = 10**9
        return file.modification_date_secounds + add

    def __sort_by_creation_date_descending(self, file: File) -> int:
        add = 0
        if file.type == '<DIR>':
            add = 10**9
        return -file.modification_date_secounds + add

    def __sort_by_name_ascending(self, file: File) -> str:
        if file.name_rus != '':
            s = file.name_rus
        else:
            s = 'я'*10 + file.name_eng
        if file.type == '<DIR>':
            s = '!'*10 + s
        return s

    def __sort_by_name_descending(self, file: File) -> str:
        if file.name_rus != '':
            s = file.name_rus[::-1]
        else:
            s = 'zzz'*10 + file.name_eng[::-1]
        if file.type == '<DIR>':
            s = '!'*10 + s
        return s
