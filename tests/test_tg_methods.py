import pytest
import data
import allure


class TestTgMethods:

    @allure.title('Проверка что получаем id')
    def test_telegram_link_id(self, tg_method):
        status_code, answer_respone = tg_method.get_telegram_link(data.ADMIN_MCTEST, data.ONLY_TOKEN)
        assert data.ANSWER_TG_LINK_ID in answer_respone

    @allure.title('Проверка что получаем url')
    def test_telegram_link_url(self, tg_method):
        status_code, answer_respone = tg_method.get_telegram_link(data.ADMIN_MCTEST, data.ONLY_TOKEN)
        assert data.ANSWER_TG_LINK_URL in answer_respone


    @pytest.mark.parametrize('user', [data.ADMIN_ONLY_NAME, data.ADMIN_ONLY_BASE ])
    @allure.title('Проверка что без юзера или базы не зарегаться')
    def test_telegram_link_not_enough_data(self, tg_method, user):
        status_code, answer_respone = tg_method.get_telegram_link(user, data.ONLY_TOKEN)
        assert status_code == 400

    @allure.title('Проверяем что без токена не получить ссыль')
    def test_telegram_link_without_link(self, tg_method):
        status_code, answer_respone = tg_method.get_telegram_link(data.ADMIN_MCTEST, data.NO_TOKEN)
        assert status_code == 400

    @allure.title('Проверяем что c пустым токеном не получить ссыль')
    def test_telegram_link_with_empty_link(self, tg_method):
        status_code, answer_respone = tg_method.get_telegram_link(data.ADMIN_MCTEST, data.EMPTY_TOKEN)
        assert status_code == 400

    @allure.title('Проверяем что c неправильным токеном не получить ссыль')
    def test_telegram_link_with_wrong_token_link(self, tg_method):
        status_code, answer_response = tg_method.get_telegram_link(data.ADMIN_MCTEST, data.WRONG_TOKEN)
        assert status_code == 200 and answer_response['ok'] is False

    @allure.title('Проверяем что связка удалилась')
    def test_delete_telegram_knot(self, tg_method):
        status_code, answer_response, user_id = tg_method.delete_telegram_knot(data.ADMIN_MCTEST, data.ONLY_TOKEN)
        assert status_code == 200 and answer_response['ok'] is True

    @allure.title('Проверяем что связка удалилась для указанного юзера')
    def test_delete_telegram_knot(self, tg_method):
        status_code, answer_response, user_id = tg_method.delete_telegram_knot(data.ADMIN_MCTEST, data.ONLY_TOKEN)
        assert user_id == answer_response['id']

    @allure.title('Проверяем что при повторном удаление ничего не происходит')
    def test_delete_telegram_knot(self, tg_method):
        status_code, answer_response = tg_method.double_delete_knot()
        assert answer_response['ok'] is False

    @allure.title('Проверяем что без токена не удалить ничего')
    def test_delete_without_token(self, tg_method):
        status_code, answer_response = tg_method.delete_knot(data.WRONG_TOKEN, data.EMPTY_TOKEN)
        assert status_code == 400







