#import pytest
import allure
from pages.SearchApi import SearchApi

API_URL = "https://web-gate.chitai-gorod.ru/api/v1"
# Заменить на рабочий токен.
BEARER_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzAxMzY2NzQsImlhdCI6MTcyOTk2ODY3NCwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6IjQ1ZGE2OTdhYTNiMDMxMTJlZDljMjM5NmMxOWNkZjVkYzU3OTk5ZTZiOTU2NGMyZGVlNTNjMDVkZjA2ZWJkYzUiLCJ0eXBlIjoxMH0.jnvpoejpL9Z7TMw1jHCP_LzoFof6cyLB74afpseIb2Y"  


@allure.title("Добавить продукт в Корзину")
@allure.description("Проверка добавления книги в Корзину")
@allure.severity(allure.severity_level.NORMAL)
#@pytest.mark.api_test
def test_add_book_to_cart_test():
    search_api = SearchApi(API_URL, BEARER_TOKEN)

    product_data = {
        "id": 2570683,
        "adData": {
            "item_list_name": "search",
            "product_shelf": ""
        }
    }

    with allure.step("Добавление продукта в Корзину"):
        response = search_api.add_product_to_cart(product_data)

    with allure.step("Проверка кода состояния ответа"):
        assert response.status_code == 200, "Ожидался статус код 200 OK"

   
@allure.title("Получить содержимое Корзины")
@allure.description("Тест проверяет функциональность получения содержимого Корзины")
@allure.feature("Управление Корзиной")
@allure.severity(allure.severity_level.NORMAL)
#@pytest.mark.api_test
def test_basket_cotents_test():
    search_api = SearchApi(API_URL, BEARER_TOKEN)

    with allure.step("Получение содержимого Корзины"):
        response = search_api.get_cart_contents()

    with allure.step("Проверка кода состояния ответа"):
        assert response.status_code == 200

    with allure.step("Проверка, что тело ответа не пустое"):
        assert response.json()

"""
        Получить заголовок книги по заданному href и title.

        :return: Текст заголовка книги.
        """
@allure.title("Очистить Корзину")
@allure.description("Тест проверяет функциональность очистки Корзины")
@allure.feature("Управление Корзиной")
@allure.severity(allure.severity_level.NORMAL)
#@pytest.mark.api_test
def test_clear_cart_test():
    search_api = SearchApi(API_URL, BEARER_TOKEN)

    with allure.step("Очистка Корзины"):
        response = search_api.clear_cart()

    with allure.step("Проверка кода состояния ответа. Cтатус код 204 No Content"):
        assert response.status_code == 204

    with allure.step("Проверка тела ответа"):
        assert response.text == ''


@allure.title("Получить список Магазинов")
@allure.description("Получить список Магазинов")
@allure.severity(allure.severity_level.MINOR)
#@pytest.mark.api_test
def test_shops_test():
    search_api = SearchApi(API_URL, BEARER_TOKEN)

    with allure.step("Получение списка Магазинов"):
        response = search_api.get_shops() 

    with allure.step("Проверка кода состояния ответа (200 OK)"):
        assert response.status_code == 200

