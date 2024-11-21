from src.list_vacancies import ListVacansies


def test_list_vacancies(data_api, vacansies_data_0) -> None:
    result = ListVacansies.tp_dict(data_api)
    #print(result)



    assert vacansies_data_0 == result



