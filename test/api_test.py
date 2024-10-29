import allure
from pages.SearchApi import SearchApi

API_URL = "https://web-gate.chitai-gorod.ru/api/v1"
# Заменить на рабочий токен.
# Как определить ключ авторизации:
# Для этого в DevTools на закладке Network найти элемент {;}short;
# далее в разделе Request Headers найти ключ авторизации (Autorization).
# Ключ должен использоваться без Bearer

BEARER_TOKEN = "<put your token>"


@allure.title("Добавить продукт в Корзину")
@allure.description("Проверка добавления книги в Корзину")
@allure.severity(allure.severity_level.NORMAL)
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
@allure.description("Тест проверяет содержимое Корзины")
@allure.feature("Управление Корзиной")
@allure.severity(allure.severity_level.NORMAL)
def test_basket_cotents_test():
    search_api = SearchApi(API_URL, BEARER_TOKEN)

    with allure.step("Получение содержимого Корзины"):
        response = search_api.get_cart_contents()

    with allure.step("Проверка кода состояния ответа"):
        assert response.status_code == 200

    with allure.step("Проверка, что тело ответа не пустое"):
        assert response.json()


@allure.title("Очистить Корзину")
@allure.description("Тест проверяет функциональность очистки Корзины")
@allure.feature("Управление Корзиной")
@allure.severity(allure.severity_level.NORMAL)
def test_clear_cart_test():
    search_api = SearchApi(API_URL, BEARER_TOKEN)

    with allure.step("Очистка Корзины"):
        response = search_api.clear_cart()

    with allure.step("Проверка статус кода: 204 No Content"):
        assert response.status_code == 204

    with allure.step("Проверка тела ответа"):
        assert response.text == ''


@allure.title("Получить список Магазинов")
@allure.description("Получить список Магазинов")
@allure.severity(allure.severity_level.MINOR)
def test_shops_test():
    search_api = SearchApi(API_URL, BEARER_TOKEN)

    with allure.step("Получение списка Магазинов"):
        response = search_api.get_shops()

    with allure.step("Проверка кода состояния ответа (200 OK)"):
        assert response.status_code == 200
