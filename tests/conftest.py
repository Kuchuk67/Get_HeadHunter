import pytest


@pytest.fixture
def data_api():
    return [
        {'id': '111404961', 'premium': False, 'name': 'Бухгалтер на торговые операции', 'department': None,
         'has_test': False, 'response_letter_required': False,
         'area': {'id': '66', 'name': 'Нижний Новгород', 'url': 'https://api.hh.ru/areas/66'},
         'salary': {'from': 60000, 'to': 60000, 'currency': 'RUR', 'gross': True},
         'type': {'id': 'open', 'name': 'Открытая'},
         'address': {'city': 'Нижний Новгород', 'street': 'Базарная', 'building': '10', 'lat': 56.351649,
                     'lng': 43.8578, 'description': None, 'raw': 'Нижний Новгород, Базарная, 10',
                     'metro': {'station_name': 'Буревестник', 'line_name': 'Сормовская', 'station_id': '51.292',
                               'line_id': '51', 'lat': 56.333834, 'lng': 43.892799}, 'metro_stations': [
                 {'station_name': 'Буревестник', 'line_name': 'Сормовская', 'station_id': '51.292', 'line_id': '51',
                  'lat': 56.333834, 'lng': 43.892799}], 'id': '120529'}, 'response_url': None,
         'sort_point_distance': None, 'published_at': '2024-11-20T11:33:19+0300',
         'created_at': '2024-11-20T11:33:19+0300', 'archived': False,
         'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=111404961',
         'show_logo_in_search': None, 'insider_interview': None,
         'url': 'https://api.hh.ru/vacancies/111404961?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/111404961',
         'relations': [], 'employer': {'id': '76255', 'name': 'Сормовская кондитерская фабрика,ЗАО',
                                       'url': 'https://api.hh.ru/employers/76255',
                                       'alternate_url': 'https://hh.ru/employer/76255',
                                       'logo_urls': {'240': 'https://img.hhcdn.ru/employer-logo/399676.jpeg',
                                                     'original': 'https://img.hhcdn.ru/employer-logo-original/214962.JPG',
                                                     '90': 'https://img.hhcdn.ru/employer-logo/326819.jpeg'},
                                       'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=76255',
                                       'accredited_it_employer': False, 'trusted': True}, 'snippet': {
            'requirement': 'Знание учетной системы 1С Управление производственным предприятием версия 8.3 и АХАPTA. Опыт работы от 1 года.',
            'responsibility': 'Учет и контроль реализации продукции, акты сверок с контрагентами. - Ввод ИСФ, КСФ, внутренняя управленческая отчетность по Готовой продукции и Дебиторской...'},
         'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [],
         'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
         'professional_roles': [{'id': '18', 'name': 'Бухгалтер'}], 'accept_incomplete_resumes': False,
         'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
         'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False,
         'adv_context': None}]


@pytest.fixture()
def vacansies_data_0():
    return [{'_Vacancy__id_v': '111404961', '_Vacancy__name': 'Бухгалтер на торговые операции',
             '_Vacancy__salary_from': 60000, '_Vacancy__salary_to': 60000, '_Vacancy__currency': 'RUR',
             '_Vacancy__url': 'https://api.hh.ru/vacancies/111404961?host=hh.ru',
             '_Vacancy__date': '2024-11-20T11:33:19+0300', '_Vacancy__additionally': {
            'snippet': 'Знание учетной системы 1С Управление производственным предприятием версия 8.3 и АХАPTA. Опыт работы от 1 года.',
            'schedule': 'Полный день', 'address': 'Нижний Новгород, Базарная'}}]


@pytest.fixture()
def vacansies_data_1():
    return [{'_Vacancy__id_v': '1114049235', '_Vacancy__name': 'Бухгалтер на торговые операции',
             '_Vacancy__salary_from': 60000, '_Vacancy__salary_to': 60000, '_Vacancy__currency': 'RUR',
             '_Vacancy__url': 'https://api.hh.ru/vacancies/111404961?host=hh.ru',
             '_Vacancy__date': '2024-11-20T11:33:19+0300', '_Vacancy__additionally': {
            'snippet': 'Знание учетной системы 1С Управление производственным предприятием версия 8.3 и АХАPTA. Опыт работы от 1 года.',
            'schedule': 'Полный день', 'address': 'Нижний Новгород, Базарная'}}]


@pytest.fixture()
def vacansies_data():
    return [{'_Vacancy__id_v': '111529103', '_Vacancy__name': 'Бухгалтер по расчету заработной платы',
             '_Vacancy__salary_from': 170000, '_Vacancy__salary_to': 190000, '_Vacancy__currency': 'RUR',
             '_Vacancy__url': 'https://api.hh.ru/vacancies/111529103?host=hh.ru',
             '_Vacancy__date': '2024-11-21T16:09:19+0300', '_Vacancy__additionally': {
            'snippet': 'У вас есть опыт работы на данной позиции от 10 х лет. Имеете высшее образование в области бухгалтерского учета/экономики. ',
            'schedule': 'Полный день', 'address': 'Москва, Космодамианская набережная'}},
            {'_Vacancy__id_v': '111499800', '_Vacancy__name': 'Бухгалтер на первичную документацию',
             '_Vacancy__salary_from': 60000, '_Vacancy__salary_to': 60000, '_Vacancy__currency': 'RUR',
             '_Vacancy__url': 'https://api.hh.ru/vacancies/111499800?host=hh.ru',
             '_Vacancy__date': '2024-11-21T11:11:06+0300', '_Vacancy__additionally': {
                'snippet': 'Исполнительность. Внимательность и аккуратность. Опыт работы с первичной документацией от 1 года.',
                'schedule': 'Полный день', 'address': 'Орёл, Машиностроительная улица'}},
            {'_Vacancy__id_v': '111475604', '_Vacancy__name': 'Бухгалтер по расчетам', '_Vacancy__salary_from': 60000,
             '_Vacancy__salary_to': 0, '_Vacancy__currency': 'RUR',
             '_Vacancy__url': 'https://api.hh.ru/vacancies/111475604?host=hh.ru',
             '_Vacancy__date': '2024-08-20T08:39:12+0300', '_Vacancy__additionally': {
                'snippet': 'Опыт работы в программе 1С ЗУП 8.3, 1С Бухгалтерия 8.3. Знание нормативных документов. Уверенное владение ПК...',
                'schedule': 'Полный день', 'address': 'Волгоград, Советская улица'}},
            {'_Vacancy__id_v': '111438577', '_Vacancy__name': 'Бухгалтер по реализации (левый берег)',
             '_Vacancy__salary_from': 0, '_Vacancy__salary_to': 70000, '_Vacancy__currency': 'RUR',
             '_Vacancy__url': 'https://api.hh.ru/vacancies/111438577?host=hh.ru',
             '_Vacancy__date': '2023-11-17T16:24:33+0300', '_Vacancy__additionally': {
                'snippet': 'Высшее образование (среднее специальное). Опыт работы бухгалтером от 2-х лет. Знание 1с и документооборота на предприятии. ',
                'schedule': 'Полный день', 'address': 'Воронеж, Монтажный проезд'}},
            {'_Vacancy__id_v': '111512398', '_Vacancy__name': 'Бухгалтер по расчету заработной платы (Пхукет, Таиланд)',
             '_Vacancy__salary_from': 0, '_Vacancy__salary_to': 0, '_Vacancy__currency': '',
             '_Vacancy__url': 'https://api.hh.ru/vacancies/111512398?host=hh.ru',
             '_Vacancy__date': '2024-09-10T12:40:17+0300', '_Vacancy__additionally': {
                'snippet': 'Опыт работы бухгалтером по заработной плате, Знание 1С, Excel. Понимание законодательства в части расчетов с сотрудниками (НДФЛ, соц. взносы). ',
                'schedule': 'Полный день', 'address': 'город Пхукет, None'}},
            {'_Vacancy__id_v': '111344376', '_Vacancy__name': 'Бухгалтер на первичную документацию',
             '_Vacancy__salary_from': 130000, '_Vacancy__salary_to': 150000, '_Vacancy__currency': 'RUR',
             '_Vacancy__url': 'https://api.hh.ru/vacancies/111344376?host=hh.ru',
             '_Vacancy__date': '2024-05-19T15:46:16+0300', '_Vacancy__additionally': {
                'snippet': 'Высшее образование. Знание требований законодательства в оформлении первичной документации, правил списания ТМЦ. Знание таких программ, как 1С КОРП, ERP...',
                'schedule': 'Полный день', 'address': 'Москва, улица Кржижановского'}},
            {'_Vacancy__id_v': '111422410', '_Vacancy__name': 'Бухгалтер', '_Vacancy__salary_from': 50000,
             '_Vacancy__salary_to': 0, '_Vacancy__currency': 'RUR',
             '_Vacancy__url': 'https://api.hh.ru/vacancies/111422410?host=hh.ru',
             '_Vacancy__date': '2024-07-20T13:52:43+0300', '_Vacancy__additionally': {
                'snippet': 'Образование: среднее-специальное, высшее (бухгалтерский учет, экономика и управление). - Опыт работы от 1 года. - Стрессоустойчивость, умение работать с большим объемом...',
                'schedule': 'Полный день', 'address': 'Омск, улица Маяковского'}},
            {'_Vacancy__id_v': '111429006', '_Vacancy__name': 'Бухгалтер на первичную документацию',
             '_Vacancy__salary_from': 0, '_Vacancy__salary_to': 50000, '_Vacancy__currency': 'RUR',
             '_Vacancy__url': 'https://api.hh.ru/vacancies/111429006?host=hh.ru',
             '_Vacancy__date': '2024-11-20T14:48:19+0300',
             '_Vacancy__additionally': {'snippet': 'Высшее, среднее профессиональное.', 'schedule': 'Полный день',
                                        'address': 'Череповец, Советский проспект'}},
            {'_Vacancy__id_v': '111434899', '_Vacancy__name': 'Бухгалтер', '_Vacancy__salary_from': 0,
             '_Vacancy__salary_to': 0, '_Vacancy__currency': 'RUR',
             '_Vacancy__url': 'https://api.hh.ru/vacancies/111434899?host=hh.ru',
             '_Vacancy__date': '2024-01-04T15:25:17+0300', '_Vacancy__additionally': {
                'snippet': 'Опыт работы от 1 года на аналогичной должности. - Высшее/среднее специальное образование. - Знание бухгалтерского учета и налогового законодательства РФ. - ',
                'schedule': 'Полный день', 'address': 'Пенза, Индустриальная улица'}},
            {'_Vacancy__id_v': '111208995', '_Vacancy__name': 'Бухгалтер на первичную документацию',
             '_Vacancy__salary_from': 75000, '_Vacancy__salary_to': 75000, '_Vacancy__currency': 'RUR',
             '_Vacancy__url': 'https://api.hh.ru/vacancies/111208995?host=hh.ru',
             '_Vacancy__date': '2024-02-21T10:24:58+0300', '_Vacancy__additionally': {
                'snippet': 'Опыт работы бухгалтером коммерческой организации от 1 года. Знание 1С, Excel, СБиС.',
                'schedule': 'Полный день', 'address': 'Барнаул, Балтийская улица'}}]


@pytest.fixture()
def files():
    return [{'_Vacancy__id_v': '111404961', '_Vacancy__name': 'Бухгалтер на торговые операции',
             '_Vacancy__salary_from': 60000, '_Vacancy__salary_to': 60000, '_Vacancy__salary_average': 60000,
             '_Vacancy__url': 'https://api.hh.ru/vacancies/111404961?host=hh.ru', '_Vacancy__currency': 'RUR',
             '_Vacancy__date': '2024-11-20T11:33:19+0300', '_Vacancy__additionally': {
            'snippet': 'Знание учетной системы 1С Управление производственным предприятием версия 8.3 и АХАPTA. Опыт работы от 1 года.',
            'schedule': 'Полный день', 'address': 'Нижний Новгород, Базарная'}
             },
            {'_Vacancy__id_v': '1114049235', '_Vacancy__name': 'Бухгалтер на торговые операции',
             '_Vacancy__salary_from': 60000, '_Vacancy__salary_to': 60000, '_Vacancy__salary_average': 60000,
             '_Vacancy__url': 'https://api.hh.ru/vacancies/111404961?host=hh.ru', '_Vacancy__currency': 'RUR',
             '_Vacancy__date': '2024-11-20T11:33:19+0300', '_Vacancy__additionally': {
                'snippet': 'Знание учетной системы 1С Управление производственным предприятием версия 8.3 и АХАPTA. Опыт работы от 1 года.',
                'schedule': 'Полный день', 'address': 'Нижний Новгород, Базарная'}
             }]



