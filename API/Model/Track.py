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
    
    if len(json['artists']) > 0:
      self.artistId = json['artists'][0]['id']
      self.artistName = json['artists'][0]['name']




