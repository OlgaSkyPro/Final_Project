import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.MainPage import MainPage
from pages.ResultPage import ResultPage


@allure.title("Тестирование Корзины")
@allure.description("Проверка текста заголовка страницы Корзины")
@allure.severity(allure.severity_level.MINOR)
def test_open_cerd_test():
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))
    try:
        main_page = MainPage(browser)
        main_page.open_cart()

        cart_page = ResultPage(browser)
        cart_text = cart_page.get_cart_text()

        with allure.step("Проверка текста заголовка Корзины"):
            assert cart_text == "КОРЗИНА", f"Expected 'Корзина' but got '{cart_text}'"
    finally:
        browser.quit()


@allure.title("Тестирование открытия страницы Доставка и оплата")
@allure.description("Проверка текста заголовка страницы Доставка и оплата.")
@allure.severity(allure.severity_level.MINOR)
def test_delivery_and_pay_test():

    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))
    try:
        main_page = MainPage(browser)
        main_page.delivery_and_pay()

        delivery_page = ResultPage(browser)
        delivery_text = delivery_page.get_delivery_text()

        with allure.step("Проверка текста заголовка Доставка и оплата"):
            assert delivery_text == "ДОСТАВКА И ОПЛАТА", f"Expected 'ДОСТАВКА И ОПЛАТА' but got '{delivery_text}'"
    finally:
        browser.quit()


# @pytest.mark.ui_test
@allure.title("Тестрование страницы Подарочные сертификаты")
@allure.description("Проверка текста заголовка стр Подарочные сертификаты")
@allure.severity(allure.severity_level.MINOR)
def test_gift_certificate_test():

    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))
    try:
        main_page = MainPage(browser)
        main_page.gift_card()

        gift_page = ResultPage(browser)
        gift_text = gift_page.get_gift_text()

        with allure.step("Проверка текста заголовка"):
            assert gift_text == "Книга – лучший подарок"
    finally:
        browser.quit()


# @pytest.mark.ui_test
@allure.title("Тестирование страницы Магазинов")
@allure.description("роверка текста заголовка страницы магазинов")
@allure.severity(allure.severity_level.MINOR)
def test_shops_test():

    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))
    try:
        main_page = MainPage(browser)
        main_page.shops()

        shops_page = ResultPage(browser)
        shops_text = shops_page.get_shops_text()

        with allure.step("Проверка текста заголовка Магазинов"):
            assert shops_text == "НАШИ МАГАЗИНЫ", f"Expected 'НАШИ МАГАЗИНЫ' but got '{shops_text}'"
    finally:
        browser.quit()


# @pytest.mark.ui_test
@allure.title("Проверка соответствия заголовка книги поиску")
@allure.description("Проверка соответствия заголовка книги поиску")
@allure.severity(allure.severity_level.NORMAL)
def test_find_book_test():
    search_value = "Колобок"
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))

    try:
        main_page = MainPage(browser)
        main_page.find_books(search_value)

        result_page = ResultPage(browser)
        first_book_title = result_page.get_book_title()

        assert first_book_title == search_value, f"Expected '{search_value}' but got '{first_book_title}'"
    finally:
        browser.quit()
