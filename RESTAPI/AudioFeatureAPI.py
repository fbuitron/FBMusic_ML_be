from Networking import Networking
from Model import AudioFeatures
from SpotifyAPI import SpotifyAPI
from Security import SecurityAPI
import json


class AudioFeatureAPI(SpotifyAPI):

    def __init__(self, tracksIds):
        self.dict_audio_features = {}
        self.tracksIds = tracksIds
        self.token = SecurityAPI().get_Authorization_Header()
        self.times = 0

   
    def tokenFailure(self, error):
        print("Token failed but we have retry")
        if self.times == 0:
            self.times +=1
            tokenSec = SecurityAPI()
            tokenSec.renew_access_token()
            self.token = tokenSec.shared_access_token
            self.getAudioFeatures()
        else:
            self.failure(error)


    def getAudioFeatures(self):

        def success(json_str):
            print(json_str)
            json_obj = json.loads(json_str)
            list_of_items = json_obj['audio_features']
            for item_index in range(len(list_of_items)):
                audio_features_json = json_obj['audio_features'][item_index]
                af = AudioFeatures.AudioFeatures(audio_features_json)
                trackID = audio_features_json['id']
                self.dict_audio_features[trackID] = af
    
        get = Networking.NetworkGET(self.base_url, self.getEndpoint())
        params = {}
        params["access_token"] = self.token
        trackIDs_param = ",".join(self.tracksIds)
        params["ids"] = trackIDs_param
        get.get(success, self.tokenFailure, params)

    def hasPaging(self):
        return False
    
    def getEndpoint(self):
        return "/v1/audio-features"

    def getRootElement(self):
        return ""


