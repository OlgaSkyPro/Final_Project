# Final_Project
Тестирование сайта Читай-город
## Шаблон для автоматизации тестирования на python

Интернет-магазин книг Читай-город.

Сайт: https://www.chitai-gorod.ru/

«Читай-город»— российская федеральная сеть книжных магазинов, основанная в 2008 году. Самая крупная книготорговая сеть в России. Помимо книг в «Читай-город» можно найти канцтовары, сладости, подарочную упаковку и идеи для сюрпризов близким.
Компания предлагает огромный выбор книг и других товаров, удобную доставку, бонусную программу и множество акций и скидок.
Заказчик тестирования: SkyPro

2. Тестируется основной функционал сайта Читай-город### Стек:
- pytest
- selenium
- requests
- _sqlalchemy_

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)

Основная функциональность портала пользователя.

    авторизация,
    поиск товара,
    выбор товара — наполнение корзины.

Требования к системе:

    Пользователь должен иметь возможность авторизоваться
    Пользователь должен иметь возможность положить выбранную книгу в корзину
    Пользователь должен иметь возможность скорректировать количество экземпляров выбранной книги
    Пользователь должен иметь возможность удалить книгу из корзины
    Пользователь должен иметь возможность оформить заказ на покупку товаров

## Шаги

1. Склонировать проект `git clone https://github.com/....`
2. Установить зависимости
3. Определить ключ авторизации. Для этого в DevTools на закладке Network найти элемент {;}short; далее в разделе Request Headers найти ключ авторизации (Autorization). Ключ должен использоваться без Bearer
4. Запустить тесты с указанием пути к директории результатов тестирования `pytest --alluredir allure_files`
5. Открыть отчет `allure serve allure_files`

## Стек

- pytest<br>
- selenium<br>
- requests<br>
- allure<br>
- config<br>

## Структура

- ./test - тесты
    - \_\_init\_\_.py
    - /api_test.py - API-тесты
    - /ui_test.py - UI-тесты
- ./web_pages - описание страниц
    - /SearchApi.py - описание API-методов
    - /MainPage.py - описание методов на главной странице
    - /ResultPage.py - описание результатов
- ./pytest.ini - файл конфигурации для pytest, который содержит настройки тестирования, такие как параметры командной
  строки и плагины.
- README.md - файл с документацией проекта
- requirements.txt - файл с используемыми зависимостями

## Полезные ссылки

- [Веб-интерфейс сервиса Читай город ](https://www.chitai-gorod.ru/)

## Библиотеки

- pip3 install pytest
- pip3 install selenium
- pip3 install webdriver-manager
- pip3 install allure-pytest
- pip3 install requests

## Запуск тестов

- `pytest -m ui_test.py` (запуск только UI тестов)
- `pytest -m api_test.py` (запуск только API тестов)
- `pytest --alluredir allure-result` (запуск тестов и сохранение отчета о результатах тестирования)
- `allure serve allure-result/` (формирование отчета о тестировании)
