from json import *

class Playlist:
  
  def __init__(self, json=None):
    if json != None:
      self.fromJson(json)

  def fromJson(self, json):
    self.href = json['href']
    self.id = json['id']
    self.name = json['name']
    if len(json['images']) > 0:
      self.imageUrl = json['images'][0]['url']
    if json['owner'] != None:
    	self.ownerID = json['owner']['id']
