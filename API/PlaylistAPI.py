from Networking import Networking
from Model import Playlist
import Security
import json


class PlaylistAPI():
    endpoint = "/v1/browse/categories/#category#/playlists"
    base_url = "https://api.spotify.com"

    def __init__(self, categoryID):
        self.list_of_playlist = []
        self.categoryID = categoryID

    def getPlaylists(self):

        def success(json_str):
            json_obj = json.loads(json_str)
            list_of_items = json_obj['playlists']['items']
            for item_index in range(len(list_of_items)):
                playlist_json = json_obj['playlists']['items'][item_index]
                print(playlist_json)
                p = Playlist.Playlist(playlist_json)
                self.list_of_playlist.append(p)
            self.stillPaging = False
        def failure(error):
        	print(error.content)
        	self.stillPaging = False

        self.endpoint = self.endpoint.replace("#category#",self.categoryID)
        print(self.endpoint)
        if self.hasPaging():
            self.stillPaging = True
            i = 0
            while(self.stillPaging):
                get = Networking.NetworkGET(self.base_url, self.endpoint)
                token = Security.get_Authorization_Header()
                print("Token " + token)
                params = {"access_token": token}
                get.get(success, failure, params)

    def hasPaging(self):
        return True


