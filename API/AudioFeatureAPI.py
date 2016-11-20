from Networking import Networking
from Model import AudioFeatures
import Security
import json


class AudioFeatureAPI():
    endpoint = "/v1/audio-features"
    base_url = "https://api.spotify.com"

    def __init__(self, *tracksIds):
        self.dict_audio_features = {}
        self.tracksIds = tracksIds

    def getAudioFeatures(self):

        def success(json_str):
            json_obj = json.loads(json_str)
            list_of_items = json_obj['audio_features']
            for item_index in range(len(list_of_items)):
                audio_features_json = json_obj['audio_features'][item_index]
                af = AudioFeatures.AudioFeatures(audio_features_json)
                trackID = audio_features_json['id']
                self.dict_audio_features[trackID] = af
            self.stillPaging = False
        def failure(error):
        	print(error.content)
        	self.stillPaging = False

        print(self.endpoint)
        if self.hasPaging():
            self.stillPaging = True
            i = 0
            while(self.stillPaging):
                get = Networking.NetworkGET(self.base_url, self.endpoint)
                token = Security.get_Authorization_Header()
                trackIDs_param = ",".join(self.tracksIds[0])
                params = {"access_token": token, "ids": trackIDs_param}
                get.get(success, failure, params)

    def hasPaging(self):
        return True


