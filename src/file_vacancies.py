
from abc import ABC, abstractmethod
from config import PATH_HOME
import os


class FilesVacancies(ABC):
    """ абстрактный класс работы  с файлами
    Принимает имя файла
    Определяет путь и имя файла """

    def __init__(self, file_name:str) -> None:
        if not os.path.exists(os.path.join(PATH_HOME, "data")):
            os.mkdir(os.path.join(PATH_HOME, "data"))
        self.__path_to_file = os.path.join(PATH_HOME, "data", file_name)
        super().__init__()

    @property
    def file_name(self) -> str:
        """ Возвращает абсолютный путь к файлу """
        return self.__path_to_file



    @abstractmethod
    def save(self,dict_object) -> str:
        """ Добавляет вакансии в файл """
        pass


    @abstractmethod
    def read(self) -> str:
        """ Читает вакансии из файла """
        pass


    def remove(self) -> None:
        """ Удаляет файл """
        pass