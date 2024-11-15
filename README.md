# Get_HeadHunter
запуск проекта get_headhunter\main.py

# Структура проекта

## 1. get_api.py
## class GetAPI(ABC) 
абстрактный класс для работы с API сервиса с вакансиями.
создаст объект: список словарей с данными
атрибуты:
- status: ответ сервера 200 - OK
- vacancies(приватный): список словарей с вакансиями   

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

### vacancies
абстрактный метод который будет выводить список объектов вакансии 



## 2. vacancies.py
## class Vacancy()

атрибуты — приватные:
- название вакансии
- ссылка на вакансию
- зарплата
- краткое описание или требования

валидировать данные, которыми инициализируются его атрибуты.

методы:
- сравнения вакансий между собой по зарплате


## class Vacancies(GetAPI)

GetFileVacancies наследующийся от абстрактного класса, для работы с платформой hh.ru.
Класс должен уметь подключаться к API и получать вакансии.

### vacancies
метод который возвращает список с объектами вакансии
список создается на основе метода vacancies_data родительского класса.
Если в атрибуте vacancies список отсутствует, он создается автоматически
на основе метода vacancies_data родительского класса


### делитер vacancies  
удалеет список вакансий.
ВНИМАНИЕ! При следующем запуске метода vacancies новый список создается автоматически
на основе метода vacancies_data родительского класса




4. абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл, получения данных из файла по указанным критериям и удаления информации о вакансиях.


5. Создать класс для сохранения информации о вакансиях в JSON-файл.

6.* реализовать классы для работы с другими форматами, например с CSV- или Excel-файлом, с TXT-файлом.

7.Создать функцию для взаимодействия с пользователем.
 Возможности этой функции должны быть следующими:
ввести поисковый запрос для запроса вакансий из hh.ru;
получить топ N вакансий по зарплате (N запрашивать у пользователя);
получить вакансии с ключевым словом в описании.
