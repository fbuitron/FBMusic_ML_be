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
