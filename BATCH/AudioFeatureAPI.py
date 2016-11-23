from Networking import Networking
from Model import AudioFeatures
from SpotifyAPI import SpotifyAPI
import Security
import json


class AudioFeatureAPI(SpotifyAPI):

    def __init__(self, tracksIds):
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
    
        get = Networking.NetworkGET(self.base_url, self.getEndpoint())
        token = Security.get_Authorization_Header()
        trackIDs_param = ",".join(self.tracksIds)
        params = self.getParameters()
        params["ids"] = trackIDs_param
        get.get(success, self.failure, params)

    def hasPaging(self):
        return False
    
    def getEndpoint(self):
        return "/v1/audio-features"

    def getRootElement(self):
        return ""


