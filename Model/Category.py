{
  "href": "https://api.spotify.com/v1/browse/categories/blues",
  "icons": [
    {
      "height": 274,
      "url": "https://t.scdn.co/media/derived/icon-274x274_aeeb8eb70c80e2b701b25425390a1737_0_0_274_274.jpg",
      "width": 274
    }
  ],
  "id": "blues",
  "name": "Blues"
}

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





jsonData = '{"href": "https://api.spotify.com/v1/browse/categories/blues","icons": [{"height": 274,"url": "https://t.scdn.co/media/derived/icon-274x274_aeeb8eb70c80e2b701b25425390a1737_0_0_274_274.jpg","width": 274}],"id": "blues","name": "Blues"}'
jsonReal = loads(jsonData)
# print(jsonReal['width'])
a = Category(jsonReal)
print(a.imageUrl)

{"href": "https://api.spotify.com/v1/browse/categories/blues","icons": [{"height": 274,"url": "https://t.scdn.co/media/derived/icon-274x274_aeeb8eb70c80e2b701b25425390a1737_0_0_274_274.jpg","width": 274}],"id": "blues","name": "Blues"}