from Networking import Networking
from Model import AudioFeatures
from SpotifyAPI import SpotifyAPI
from Security import SecurityAPI
import json


class SearchAPI(SpotifyAPI):

    def __init__(self):
        self.result_list = []
        self.token = SecurityAPI().get_Authorization_Header()
        self.query = ""
        self.times = 0
        


    def tokenFailure(self, error):
        print("Token failed but we have retry")
        if self.times == 0:
            self.times +=1
            tokenSec = SecurityAPI()
            tokenSec.renew_access_token()
            self.token = tokenSec.shared_access_token
            self.getSearch(self.query)
        else:
            self.failure(error)

    def getSearch(self, query):
        self.query = query
        def success(json_str):
            json_obj = json.loads(json_str)
            list_of_items = json_obj['tracks']['items']
            for item_index in range(len(list_of_items)):
                resItem = {'id':list_of_items[item_index]['id'], 'name':list_of_items[item_index]['name']}
                self.result_list.append(resItem)
    
        get = Networking.NetworkGET(self.base_url, self.getEndpoint())
        params = {}
        params["access_token"] = self.token
        params["type"] = 'track'
        params["q"] = query.replace(" ", "%20")
        get.get(success, self.tokenFailure, params)

    def hasPaging(self):
        return False
    

    def getEndpoint(self):
        return "/v1/search"

    def getRootElement(self):
        return ""

    def searchInteractive(self, query):
        self.getSearch(query)
        return self.result_list

SearchAPI().getSearch("persiana")
