import allure
#import requests
from pages.api_search import SeachAPI

@allure.title("Search of a book")
@allure.description("The test checks the search operation")
@allure.feature("POST")
@allure.severity("blocker")
def seach_test():
    api = SeachAPI("https://web-gate.chitai-gorod.ru/api/","eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mjk4Njk3MzMsImlhdCI6MTcyOTcwMTczMywiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6IjliNzdkMTcxNDRlZWIyODkxZWIxNDc2ZTQ2ZmE3NWViOGM1NmU3YWMyYjQ2NWYyZmU1MGQxMzE5ZDNhY2NhOGYiLCJ0eXBlIjoxMH0.xOm11g-2S1FLWsYE2M48tgVZyZ9wLwcbom6-D_xex8c")
    tittle = "Колобок"
    resp_rez = api.seach_book(tittle)
    assert resp_rez.status_code == 200
    assert tittle == resp_rez.text