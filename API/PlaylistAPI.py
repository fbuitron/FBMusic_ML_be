from Networking import Networking
from Model import Playlist
from SpotifyAPI import SpotifyAPI
import Security
import json


class PlaylistAPI(SpotifyAPI):
    
    base_url = "https://api.spotify.com"

    def __init__(self, categoryID):
        super(PlaylistAPI, self).__init__()
        self.list_of_playlist = []
        self.categoryID = categoryID

    def getPlaylists(self):

        def success(json_str):
            super(PlaylistAPI, self).success(json_str)
            json_obj = json.loads(json_str)
            list_of_items = json_obj['playlists']['items']
            for item_index in range(len(list_of_items)):
                playlist_json = json_obj['playlists']['items'][item_index]
                p = Playlist.Playlist(playlist_json)
                self.list_of_playlist.append(p)

        def failure(error):
        	print(error.content)
        	self.stillPaging = False

        if self.hasPaging():
            self.stillPaging = True
            i = 0
            while(self.stillPaging):
                get = Networking.NetworkGET(self.base_url, self.getEndpoint())
                params = self.getParameters()
                get.get(success, failure, params)

    def hasPaging(self):
        return True

    def getEndpoint(self):
        return "/v1/browse/categories/#category#/playlists".replace("#category#",self.categoryID)

    def getRootElement(self):
        return "playlists"

