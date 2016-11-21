from Networking import Networking
from Model import Category
from SpotifyAPI import SpotifyAPI
import Security
import json


class CategoriesAPI(SpotifyAPI):
    def __init__(self):
        super(CategoriesAPI, self).__init__()
        self.list_of_categories = []
        # self.offset = 0
        # self.limit = 20

    def getCategories(self):

        def success(json_str):
            super(CategoriesAPI, self).success(json_str)
            json_obj = json.loads(json_str)
            list_of_items = json_obj['categories']['items']
            for item_index in range(len(list_of_items)):
                category_json = json_obj['categories']['items'][item_index]
                c = Category.Category(category_json)
                self.list_of_categories.append(c)

        if self.hasPaging():
            self.stillPaging = True
            i = 0
            while(self.stillPaging):
                get = Networking.NetworkGET(self.base_url, self.getEndpoint())  
                params = self.getParameters()   
                get.get(success, self.failure, params)

    def hasPaging(self):
        return True

    def getEndpoint(self):
        return "/v1/browse/categories"

    def getRootElement(self):
        return "categories"
