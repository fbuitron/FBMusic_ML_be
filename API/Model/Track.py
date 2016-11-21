from json import *

class Track:
  
  def __init__(self, json=None):
    if json != None:
      self.fromJson(json)

  def fromJson(self, json):
    self.href = json['href']
    self.id = json['id']
    self.name = json['name']
    self.playbackURL = json['preview_url']
    self.popularity = json['popularity']
    if json['album'] != None:
      self.albumName = json['album']['name']							
      if len(json['album']['images']) > 0:
        self.albumImageURL = json['album']['images'][0]['url']
      else:
        self.albumImageURL = ""
    else:
      self.albumName = ""
    if len(json['artists']) > 0:
      self.artistId = json['artists'][0]['id']
      self.artistName = json['artists'][0]['name']
    else:
      self.artistId = ""
      self.artistName = ""

  def toSQLInsert(self, extra_fields = {}):
    keys = ",".join(extra_fields.keys())
    columns = "(ID,href,name,playbackURL,popularity,albumName,albumImageURL,artistID,artistName,"+keys+")"
    values = (self.id,self.href,self.name,str(self.playbackURL),str(self.popularity),self.albumName,self.albumImageURL, self.artistId, self.artistName) #"('"+self.id+"','"+self.href+"','"+self.name+"','"+str(self.playbackURL)+"',"+str(self.popularity)+",'"+self.albumName+"','"+self.albumImageURL+"','"+self.artistId+"','"+self.artistName+"', "+valuesextra+")"
    for x in extra_fields:
      values = values + (extra_fields[x],)
    
    return columns, values



