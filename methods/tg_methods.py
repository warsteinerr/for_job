import requests
import data
import allure


class TgMethods:

    @allure.step('Получение ссылки для регистрации')
    def get_telegram_link(self, connection_params, body):
        response = requests.post(data.BASE_URL, params=connection_params, json=body)
        return response.status_code, response.json()


    @allure.step('Удаление связки')
    def delete_knot(self, delete_id, body):
        delete_response = requests.delete(data.BASE_URL, params=f'id={delete_id}', json=body)
        return delete_response.status_code, delete_response.json()

    @allure.step('Удаление подряд два раза одной и той же связки')
    def double_delete_knot(self):
        status_code, create_response = self.get_telegram_link(data.ADMIN_MCTEST, data.ONLY_TOKEN)
        user_id = create_response["id"]
        self.delete_knot(user_id, data.ONLY_TOKEN)
        status_code, answer_response = self.delete_knot(user_id, data.ONLY_TOKEN)
        return status_code, answer_response


    @allure.step('Удаление связку после создания')
    def delete_telegram_knot(self, connection_params, body):
        status_code, create_response = self.get_telegram_link(connection_params, body)
        user_id = create_response["id"]
        delete_knot_status_code, delete_knot_response = self.delete_knot(user_id, body)
        return delete_knot_status_code, delete_knot_response, user_id


