import requests
import allure

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mjk4Njk3MzMsImlhdCI6MTcyOTcwMTczMywiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6IjliNzdkMTcxNDRlZWIyODkxZWIxNDc2ZTQ2ZmE3NWViOGM1NmU3YWMyYjQ2NWYyZmU1MGQxMzE5ZDNhY2NhOGYiLCJ0eXBlIjoxMH0.xOm11g-2S1FLWsYE2M48tgVZyZ9wLwcbom6-D_xex8c"

class SeachAPI:
    def __init__(self, url: str, token: str):
        self.url = url
        self.token = token

    @allure.step("Search for a specific book")
    def seach_book(self, name_book: str):
        my_headers = {
        "Content - Type": "application / json",
        "Authorization": f"Bearer {token}"
        }
        my_choice = {"phrase": name_book}
        response = requests.get(f"{self.url}v2/search/product?", headers=my_headers, params = my_choice)
        return response
    
    def add_book(self,id_book):
        id_book = 1
        print("Pause")