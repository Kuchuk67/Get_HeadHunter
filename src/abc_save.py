from abc import ABC, abstractmethod
from config import PATH_HOME
import os


class Save_Vacancies(ABC):

    def __init__(self, file_name:str):
        self._path_to_file = os.path.join(PATH_HOME, "data", file_name)

    @property
    def file_name(self):
        ''' Возвращает абсолютный путь к файлу '''
        return self._path_to_file

    @abstractmethod
    def add(self):
        ''' Добавляет вакансии в файл '''
        pass


    @abstractmethod
    def read(self):
        ''' Читает вакансии из файла '''
        pass

    @abstractmethod
    def remove(self):
        ''' Удаляет вакансии из файла '''
        pass


