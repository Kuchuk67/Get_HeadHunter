# Get_HeadHunter
запуск проекта get_headhunter\main.py

Класс работы с вакансиями загруженными с HeadHunter по API
    Создание списка вакансий. Сортировка по дате и зарплате.
    Итерирование списка. Удаление ненужных вакансий.
    Сохрание и чтение файла со списком в формате JSON



### Структура проекта



# class GetAPI(ABC) 
#### abc_get_api.py
абстрактный класс для работы с API сервиса с вакансиями.
создаст объект: список словарей с данными
атрибуты:
- status: ответ сервера 200 - OK
- vacancies_data:  список словарей с вакансиями
- vacancies(приватный):  список элементов класса Vacancy  

### load_vacancies
метод получения данных -  отправляет запрос на API hh.ru для получения данных о вакансиях по ключевому слову.
Добавляет полученные данные к существующим. 
Для нового запроса предварительно воспользуйтесь делитером.
принимает: параметр — ключевое слово для поиска вакансий.
вернуть: собирает данные ответа в формате списка словарей из ключа item статус-код ответа.

### vacancies_data
возвращает приватный атрибут vacancies - полученные по API вакансии 

### делиттер vacancies_data
Удаляет загруженные вакансии 




# class ListVacancies(GetAPI) 
#### list_vacancies.py
Формирует из данных полученных по API  список с объектами вакансий, 
добавляет объекты, сортирует список, удаляет объекты из списка

### vacancies
метод который возвращает список с объектами вакансии
список создается на основе метода vacancies_data родительского класса.
Если в атрибуте vacancies список отсутствует, он создается автоматически
на основе метода vacancies_data родительского класса

### сеттер vacancies
Добавляет указанную вакансию в список

### делитер vacancies  
удалеет список вакансий.
ВНИМАНИЕ! При следующем запуске метода vacancies новый список создается автоматически
из данных, которые были полученны по API.

### sort_date
Сортирует список вакансий по дате

### sort_salary
Сортирует список вакансий по зарплате

# class Vacancy
#### vacancy.py
Позволяет создать объект, который содержит данные по одной конкретной вакансии

атрибуты — приватные:
- название вакансии
- зарплата от
- зарплата до
- средняя по вилке зарплаты
- валюта зарплаты
- адрес офиса
- ссылка на вакансию
- краткое описание или требования
- график работы
- дата


###  staticmethod average
имея вилку зарплат находит среднюю зарплату

### compare_vacancies
метод сравнения вакансий между собой по средней в вилке зарплаты
a.compare_vacancies(b)
True - если зарплата объекта 'a' больше чем 'y'



# class Save_Vacancies(ABC)
#### abc_save.py
абстрактный класс для работы с файлами.
Иcпользуется для создания классов обслуживающих ввод-вывод в разные типы файлов
Создает папку data для хранения файлов

атрибут:
- имя файла

### метод file_name
Возвращает абсолютный путь к файлу

### remove
Удаляет файл

# class SaveJSON(Save_Vacancies)
#### save_json.py
класс для работы с файлами JSON

### save 
Добавляет вакансии в файл из списка vacancies
### read
Читает вакансии из файла и записывает в список vacancies




2. vacancies.py
# class Vacancies(SaveJSON, ListVacancies)
Класс  подключатся к API и получать вакансии, читать вакансии из файла и сохранять их в файл














4. абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл, получения данных из файла по указанным критериям и удаления информации о вакансиях.


5. Создать класс для сохранения информации о вакансиях в JSON-файл.

6.* реализовать классы для работы с другими форматами, например с CSV- или Excel-файлом, с TXT-файлом.

7.Создать функцию для взаимодействия с пользователем.
 Возможности этой функции должны быть следующими:
ввести поисковый запрос для запроса вакансий из hh.ru;
получить топ N вакансий по зарплате (N запрашивать у пользователя);
получить вакансии с ключевым словом в описании.
