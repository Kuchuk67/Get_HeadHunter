from abc import ABC, abstractmethod
from config import PATH_HOME
import os


class Save_Vacancies(ABC):

    def __init__(self, file_name:str):
        if not os.path.exists(os.path.join(PATH_HOME, "data")):
            os.mkdir(os.path.join(PATH_HOME, "data"))
        self._path_to_file = os.path.join(PATH_HOME, "data", file_name)
        super().__init__()

    @property
    def file_name(self):
        ''' Возвращает абсолютный путь к файлу '''
        return self._path_to_file



    @abstractmethod
    def save(self):
        ''' Добавляет вакансии в файл '''
        pass


    @abstractmethod
    def read(self):
        ''' Читает вакансии из файла '''
        pass


    def remove(self):
        ''' Удаляет файл '''
        os.remove(self.file_name)


