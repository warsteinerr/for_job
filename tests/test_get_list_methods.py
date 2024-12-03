import pytest
import data
import allure


class TestLoginMethod:

    @allure.title('Проверка статус кода')
    def test_status_code_ok(self, get_list_method):
        list_status_code, list_response = get_list_method.get_list_of_users(data.ONLY_TOKEN)
        assert list_status_code == 200

    @allure.title('Проверка формата JSON')
    def test_answer_format(self, get_list_method):
        list_status_code, list_response = get_list_method.get_list_of_users(data.ONLY_TOKEN)
        assert isinstance(list_response, (dict, list))

    @allure.title('Проверка на некоррекнтый токен')
    def test_wrong_token(self, get_list_method):
        list_status_code, list_response = get_list_method.random_token_login()
        assert list_response == []

    @allure.title('Проверка что возвращается xml')
    def test_xml_in_response(self, get_list_method):
        list_status_code, list_response = get_list_method.get_list_in_xml(data.ONLY_TOKEN)
        assert list_response.startswith(data.XML_ANSWER)

    @allure.title('Проверка что возвращается xml mc_test по фильтру')
    def test_get_list_in_xml_base(self, get_list_method):
        list_status_code, list_response, bases = get_list_method.get_list_in_xml_base(data.MC_TEST_FILTER)
        assert all(base == data.MC_TEST_BASE for base in bases)













