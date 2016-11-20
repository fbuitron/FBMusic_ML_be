from Networking import Networking
from Model import Category
import Security
import json


class CategoriesAPI():
    endpoint = "/v1/browse/categories"
    base_url = "https://api.spotify.com"

    def __init__(self):
        self.list_of_categories = []

    def getCategories(self):

        def success(json_str):
            json_obj = json.loads(json_str)
            list_of_items = json_obj['categories']['items']
            for item_index in range(len(list_of_items)):
                category_json = json_obj['categories']['items'][item_index]
                print(category_json)
                c = Category.Category(category_json)
                self.list_of_categories.append(c)
            self.stillPaging = False
        def failure(error):
        	print("error")
        	print(error)
        	self.stillPaging = False

        if self.hasPaging():
            self.stillPaging = True
            i = 0
            while(self.stillPaging):
                get = Networking.NetworkGET(self.base_url, self.endpoint)
                Security.renew_access_token()
                token = Security.get_Authorization_Header()
                print("Token " + token)
                params = {"access_token": token}
                get.get(success, failure, params)

    def hasPaging(self):
        return True
