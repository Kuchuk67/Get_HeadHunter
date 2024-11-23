import os
import requests
import json
from config import PATH_HOME
import re


class Area:
    dict_areas = {}

    def __init__(self):
        if not os.path.exists(os.path.join(PATH_HOME, "data")):
            os.mkdir(os.path.join(PATH_HOME, "data"))
        self._path_to_file = os.path.join(PATH_HOME, "data", 'area.json')
        self.__url = 'https://api.hh.ru/areas'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        if not os.path.exists(os.path.join(PATH_HOME, "data", "area.json")):
            self.load()


    @classmethod
    def areas(cls, areas):
        for area in areas:
            name = area['name'].lower()
            id_ = area['id']
            areas_ = area['areas']
            Area.dict_areas[name] = id_
            if areas_:
                Area.areas(areas_)




    def load(self):

        response = requests.get(self.__url, headers=self.__headers)
        self.status = response.status_code
        if self.status == 200:
            area = response.json()
            Area.areas(area)
            try:
                with open(self._path_to_file, 'w', encoding='utf-8') as files:
                    json.dump(Area.dict_areas, fp=files, indent=4, ensure_ascii=False)
            except Exception as er:
                return f"Ошибка записи файла; {er}"
            else:
                #Area.areas(area)
                #print(Area.dict_areas)
                return 'Ok'

    @classmethod
    def id_area(cls, word):

        word_l = word.lower()
        area_reqest = fr'({word_l})\b'
        ares_id: str = ''

        for index, element in Area.dict_areas.items():
            # print(area_reqest)
            if re.search(area_reqest, index):
                # print(index.find(area_reqest))
                if ares_id != '':
                    ares_id += ','
                ares_id += element
        return ares_id




