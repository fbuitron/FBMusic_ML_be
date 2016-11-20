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

  def toSQLInsert(self, extra_fields = {}):
    keys = ",".join(extra_fields.keys())
    columns = "(acousticness,danceability,duration_ms,energy,instrumentalness,a_key,liveness,loudness,a_mode,speechiness,tempo,time_signature,valence,"+keys+")"
    values = (self.acousticness,self.danceability,self.duration_ms,self.energy,self.instrumentalness,self.key,self.liveness, self.loudness, self.mode,self.speechiness,self.tempo,self.time_signature,self.valence) #"('"+self.id+"','"+self.href+"','"+self.name+"','"+str(self.playbackURL)+"',"+str(self.popularity)+",'"+self.albumName+"','"+self.albumImageURL+"','"+self.artistId+"','"+self.artistName+"', "+valuesextra+")"
    for x in extra_fields:
      values = values + (extra_fields[x],)
    
    return columns, values
