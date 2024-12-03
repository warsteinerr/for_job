import requests
import data
import allure
import uuid
import re
class GetListMethods:

    @allure.step('Получение списка юзеров')
    def get_list_of_users(self, connection_params):
        response = requests.get(data.BASE_URL, params=connection_params)
        return response.status_code, response.json()

    @allure.step('Рандомный токен')
    def generate_token_dict(self):
        random_token = str(uuid.uuid4())
        return {"token": random_token}

    @allure.step('Получение списка с рандомным токеном')
    def random_token_login(self):
        random_token = self.generate_token_dict()
        response = requests.get(data.BASE_URL, params=random_token)
        return response.status_code, response.json()

    @allure.step('Получение списка в xml')
    def get_list_in_xml(self, connection_params):
        response = requests.get(f'{data.BASE_URL}{data.XML_URL}', params=connection_params)
        return response.status_code, response.text

    @allure.step('Получение списка в xml от конкретной базы')
    def get_list_in_xml_base(self, connection_params):
        response = requests.get(f'{data.BASE_URL}{data.XML_URL}', params=connection_params)
        db_names = re.findall(r'<DbName>(.*?)</DbName>', response.text)
        return response.status_code, response.text, db_names











