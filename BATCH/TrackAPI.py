from Networking import Networking
from Model import Track
from SpotifyAPI import SpotifyAPI
import Security
import json


class TrackAPI(SpotifyAPI):

    def __init__(self, userID, playlistID):
        super(TrackAPI, self).__init__()
        self.list_of_tracks = []
        self.userID = userID
        self.playlistID = playlistID

    def getTracks(self):

        def success(json_str):
            super(TrackAPI, self).success(json_str)
            json_obj = json.loads(json_str)
            list_of_items = json_obj['items']
            for item_index in range(len(list_of_items)):
                track_json = json_obj['items'][item_index]['track']
                t = Track.Track(track_json)
                self.list_of_tracks.append(t)
        
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
        return "/v1/users/#userid#/playlists/#playlistid#/tracks".replace("#userid#",self.userID).replace('#playlistid#',self.playlistID)

    def getRootElement(self):
        return ""


