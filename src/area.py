import os
import requests
import json
from typing import Any

from pyflakes.checker import counter

from config import PATH_HOME
import re


class Area:
    """ Класс определения id региона"""
    dict_areas = {}

    def __init__(self):
        if not os.path.exists(os.path.join(PATH_HOME, "data")):
            os.mkdir(os.path.join(PATH_HOME, "data"))
        self._path_to_file = os.path.join(PATH_HOME, "data", 'area.json')
        self.__url = 'https://api.hh.ru/areas'
        self.__headers = {'User-Agent': 'HH-User-Agent'}

        if not os.path.exists(os.path.join(PATH_HOME, "data", "area.json")):
            self.load()
            self.save_to_file()





    @classmethod
    def areas(cls, areas):
        """ Рекурсивный метод для парсинга файла регионов"""
        for area in areas:
            name = area['name']
            id_ = area['id']
            areas_ = area['areas']
            Area.dict_areas[name] = id_
            if areas_:
                Area.areas(areas_)




    def load(self):
        """ загружает регионы и создает файл area.json"""

        response = requests.get(self.__url, headers=self.__headers)
        self.status = response.status_code
        if self.status == 200:
            area = response.json()
            Area.areas(area)
            return 'Ok'
        else:
            return f"Ошибка API запроса: {self.status}"

    def save_to_file(self):
        """ Сохраняет файл регионов"""
        try:
             with open(self._path_to_file, 'w', encoding='utf-8') as files:
                 json.dump(Area.dict_areas, fp=files, indent=4, ensure_ascii=False)
        except Exception as er:
             return f"Ошибка записи файла; {er}"
        else:
             # Area.areas(area)
             # print(Area.dict_areas)
             return 'Ok'

    @classmethod
    def id_area(cls, word) -> Any:
        """ определение id региона
        Принимает str название субъекта или города
        Возвращает кортеж (статус, id, наименование объекта)
        """

        if len(Area.dict_areas) == 0:
            file_name = os.path.join(PATH_HOME, "data", 'area.json')
            try:
                with open(file_name, encoding='utf-8') as files:
                    Area.dict_areas = json.load(files)
            except Exception as er:
                return f"Ошибка чтения файла; {er}"


        word_l = word.lower()
        area_reqest = fr'({word_l})\b'
        ares_id: str = ''
        name:str = ""
        status = 'Ok'
        count = 0
        for index, element in Area.dict_areas.items():

            if re.search(area_reqest, index.lower()):
                count += 1
                if ares_id != '':
                    ares_id += ' '
                ares_id += element
                if name != '':
                    name += ','
                name += index
        if count > 10:
            status = 'Слишком большая территория поиска.'
        if ares_id == '':
            status = 'Ничего не найдено'

        return status, ares_id.split(), name