from Networking import Networking
from Model import Track
import Security
import json


class TrackAPI():
    endpoint = "/v1/users/#userid#/playlists/#playlistid#/tracks"
    base_url = "https://api.spotify.com"

    def __init__(self, userID, playlistID):
        self.list_of_tracks = []
        self.userID = userID
        self.playlistID = playlistID

    def getTracks(self):

        def success(json_str):
            json_obj = json.loads(json_str)
            list_of_items = json_obj['items']
            for item_index in range(len(list_of_items)):
                track_json = json_obj['items'][item_index]['track']
                print(track_json)
                t = Track.Track(track_json)
                self.list_of_tracks.append(t)
            self.stillPaging = False
        def failure(error):
        	print(error.content)
        	self.stillPaging = False

        self.endpoint = self.endpoint.replace("#userid#",self.userID).replace('#playlistid#',self.playlistID)
        print(self.endpoint)
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

