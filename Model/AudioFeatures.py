from json import *

class AudioFeatures:
  
  def __init__(self, json=None):
    if json != None:
      self.fromJson(json)

  def fromJson(self, json):
    self.duration_ms = json['duration_ms']
    self.danceability = json['danceability']
    self.energy = json['energy']
    self.key = json['key']
    self.loudness = json['loudness']
    self.mode = json['mode']
    self.speechiness = json['speechiness']
    self.acousticness = json['acousticness']
    self.instrumentalness = json['instrumentalness']
    self.liveness = json['liveness']
    self.valence = json['valence']
    self.tempo = json['tempo']
    self.time_signature = json['time_signature']
    self.anlysis_url = json['analysis_url']





jsonData = """
{
  "danceability" : 0.735,
  "energy" : 0.578,
  "key" : 5,
  "loudness" : -11.840,
  "mode" : 0,
  "speechiness" : 0.0461,
  "acousticness" : 0.514,
  "instrumentalness" : 0.0902,
  "liveness" : 0.159,
  "valence" : 0.624,
  "tempo" : 98.002,
  "type" : "audio_features",
  "id" : "06AKEBrKUckW0KREUWRnvT",
  "uri" : "spotify:track:06AKEBrKUckW0KREUWRnvT",
  "track_href" : "https://api.spotify.com/v1/tracks/06AKEBrKUckW0KREUWRnvT",
  "analysis_url" : "https://api.spotify.com/v1/audio-analysis/06AKEBrKUckW0KREUWRnvT",
  "duration_ms" : 255349,
  "time_signature" : 4
}
"""
jsonReal = loads(jsonData)
a = AudioFeatures(jsonReal)
print(a.loudness)

