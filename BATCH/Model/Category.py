
from json import *

class Category:
  
  def __init__(self, json=None):
    if json != None:
      self.fromJson(json)

  def fromJson(self, json):
    self.href = json['href']
    self.id = json['id']
    self.name = json['name']
    if len(json['icons']) > 0:
      self.imageUrl = json['icons'][0]['url']

  def toSQLInsert(self, extra_fields = {}):
  	columns = "(ID,href,name,imageURL)"
  	values = (self.id,self.href,self.name,self.imageUrl)
  	return columns, values
