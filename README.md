# Get_HeadHunter
* запуск проекта get_headhunter\main.py

Работа с вакансиями загруженными с HeadHunter по API
Создание списка вакансий. Сортировка по дате и зарплате.
Итерирование списка. Удаление ненужных вакансий.
Сохрание и чтение файла со списком в формате JSON

## Структура проекта

### модуль get_headhunter
Модуль пользовательской оболочки для работы с программой
### модуль src
Классы работы  с данными
### модуль tests
Тесты классов
### каталог data
Каталог хранения данных пользователя и кодов регионов
### файл config.py
[Дополнительные настройки](#config) программы и API запросов 

## Содержание

* [class Vacancies()](#Vacancies) vacancies.py
* [class IterVacancies](#IterVacancies) vacancies.py
* [class Vacancy](#Vacancy) vacancy.py
* [class CompareVacancies](#CompareVacancies) vacancy.py
* [class GetAPI(ABC)](#GetAPI) get_api.py
* [class ListVacansies(GetAPI)](#ListVacansies) list_vacancies.py
* [class Files_Vacancies(ABC)](#Files_Vacancies)  file_vacancies.py
* [class FilesJSON(Files_Vacancies)](#FilesJSON)  file_json.py
* [class Area](#Area)  area.py

## Описание классов

# Vacancies
Формирует из данных полученных по API  список с объектами вакансий,
добавляет объекты, сортирует список, удаляет объекты из списка.

```x =   Vacancies()```

### метод vacancies
Возвращает список экземпляров вакансия Vacancу
Добавляет в список экземпляров вакансию Vacancу

```lists = x.vacancies```

Удаляет все вакансии
```del x.vacancies```

### метод  vacancy_del
Удаляет одну вакансию. Принимает id вакансии

```x.vacancy_del(123213)```

### метод  created
Отдает список объектов с вакансиями

```x.created(vacansies_data)```

### метод  sort_date
Сортирует список вакансий по дате 

```x.data.sort_date()```

### метод sort_salary
Сортирует список вакансий по зарплате

```x.sort_salary()```

---

# IterVacancies
Возвращает следующее объект Вакансию Vacancy.
Returns: int: Следующая вакансии.
Raises: StopIteration: Если достигнута верхняя граница диапазона.

```
f = IterVacancies(x.vacancies)
    while True:
        print(next(f)) 
>>> Бухгалтер, зарплата: 85250, Полный день, адрес: Хабаровск
```
        

---

# Vacancy
Позволяет создать объект, который содержит данные по одной конкретной вакансии

``` 
a = Vacancy(1, 'Дворник', 12000, 13000, 'RU', 'http://#', '2024-02-16T14:58:28+0300', {'snippet': 'Чисто подметать двор', 'schedule': 'Полный день', 'address': 'Москва, Космодамианская набережная'} 
```

атрибуты — приватные:
- id вакансии
- название вакансии
- зарплата от
- зарплата до
- валюта зарплаты
- url
- дата
- словарь пользовательский данных
  * адрес офиса
  * краткое описание или требования
  * график работы

средняя по вилке зарплаты - высчитывается CompareVacancies.average

### staticmethod метод valid(data)
Проверка на положительные целые числа
при отрицательных возвращает ноль

### метод  id_v

``` result = a.id_v ```

возвращает id вакансии
### метод name

``` result = a.name ```

возвращает имя вакансии
### метод salary_from

``` result = a.salary_from ```

возвращает зарплату 'от' вакансии
### метод salary_to

``` result = a.salary_to ```

возвращает зарплату 'до' вакансии
### метод salary_average

``` result = a.salary_average ```

возвращает среднюю зарплату вакансии
### метод currency

``` result = a.currency ```

возвращает валюту зарплаты  вакансии
### метод url

``` result = a.url ```

возвращает урл вакансии
### метод additionally

``` result = a.additionally ```

возвращает словарь пользовательских данных вакансии
### метод date

``` result = a.date ```

возвращает дату вакансии

# CompareVacancies
Класс создает функцию сравнения вакансий по зарплате
на вход принимает зкземпляр вакансии 
Возвращает TRUE если проверяемая вакансия больше по зарплате

``` 
a = первая вакансия
b = вторая вакансия
compare = CompareVacancies(a)
if compare(b):
    pass
 ```

### метод average
статический метод подсчета средней зарплаты по вилке зарплат
```
salary = CompareVacancies.average(a.salary_from, a.salary_to)
```

# GetAPI
отправляет запрос для получения данных API
создаст объект: список словарей с данными

### метод area
параметр area для API запроса
и изменение параметра area для API запроса

``` 
result = a.area
a.area = '113'
 ```


### метод salary
параметр salary для API запроса
и изменение параметра salary для API запроса
``` 
result = a.salary
a.salary = '60000'
 ```

### abstractmethod to_dict
```pass```

### метод connect
делает API запрас, 
сохраняет статус-код запроса.
если статус 200 возвращает словарь с JSON данными

```
api = ListVacansies('Бухгалтер')
status = api.connect()
if status == 200:
   print("Данные API загружены")
   vacansies_data = api.to_dict()
```

### метод  data
метод выводит полученные по API вакансии

---
# ListVacansies
### метод  to_dict
Формирует из данных полученных по API  список словарей 
Выбирает только нужные поля данных вакансий
Если данные отсутствуют заменяет их нулями или пробелами

```
api = ListVacansies('Бухгалтер')
status = api.connect()
if status == 200:
   print("Данные API загружены")
   vacansies_data = api.to_dict()
```

---

# Files_Vacancies
абстрактный класс работы  с файлами
Принимает имя файла
Определяет путь и имя файла

### метод  file_name
Возвращает абсолютный путь к файлу 

---

# FilesJSON
класс работы  с файлами JSON
принимает имя файла без расширения


```
f = FilesJSON('имя файла без расширения')

```

### метод data_json_created
принимает списка объектов Vacansy
Создает из списка объектов Vacansy список словарей для JSON файла
Если есть файл загружает вакансии
Добавляет к ним новый список
Одинаковые вакансии не добавляются

``` list_data_to_file = f.data_json_created(x.vacancies) ```

### метод  save
Добавляет подготовленный список вакансии в файл *.json
Возвращает Ок или ошибку

```
list_data_to_file = f.data_json_created(x.vacancies)
status = f.save(list_data_to_file)

```

### метод read
Читает вакансии из файла 
Возвращает список словарей с вакансиями
или пустой список при ошибке

```
data_from_file = f.read()
x.created(data_from_file)
```

### метод remove
Удаляет файл *.json

``` f.remove() ```

--- 
# Area
Класс определения id региона area.json
При инициализации если нет файла с регионами
вызывает метод load и метод save_to_file

``` Area() ```

### метод load
загружает регионы и создает файл area.json

``` ```

### метод save_to_file
Сохраняет файл регионов

### метод id_area
#### @classmethod
определение id региона
Принимает str название субъекта или города
Возвращает кортеж (статус(Ok), id, наименование объекта)

``` id_area = Area.id_area('Мочква')```


# config
Файл настроек config.py
API запросы

* Количество ваканий на загружаемой странице

```PER_PAGE = 100```

* Количество загружаемых страниц

```PAGE = 5```

* Регион поиска по умолчанию

```AREA = '113'```

* Файл для сохранения данных по умолчанию

```FILE_NAME = 'data'```






