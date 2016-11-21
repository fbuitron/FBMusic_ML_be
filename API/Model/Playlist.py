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
    else:
      self.imageUrl = ""
    if json['owner'] != None:
    	self.ownerID = json['owner']['id']

  def toSQLInsert(self, extra_fields = {}):
    keys = ",".join(extra_fields.keys())
    columns = "(ID,href,name,imageURL,ownerID,"+keys+")"
    values = (self.id,self.href,self.name,self.imageUrl,self.ownerID)
    for x in extra_fields:
      values = values + (extra_fields[x],)
    return columns, values