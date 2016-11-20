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





jsonData = """
{
        "collaborative": false,
        "external_urls": {
          "spotify": "http://open.spotify.com/user/spotify/playlist/49wvzum0Lh9mcAdqhLbDbe"
        },
        "href": "https://api.spotify.com/v1/users/spotify/playlists/49wvzum0Lh9mcAdqhLbDbe",
        "id": "49wvzum0Lh9mcAdqhLbDbe",
        "images": [
          {
            "height": null,
            "url": "https://u.scdn.co/images/pl/default/829ff4d4ba8b12d670a525d030d268bcaedc5bf1",
            "width": null
          }
        ],
        "name": "Dancehall Official",
        "owner": {
          "external_urls": {
            "spotify": "http://open.spotify.com/user/spotify"
          },
          "href": "https://api.spotify.com/v1/users/spotify",
          "id": "spotify",
          "type": "user",
          "uri": "spotify:user:spotify"
        },
        "public": null,
        "snapshot_id": "cAhyEA/FThYSHMdpaAUkCQLVR20la4QulNxJx3d/m41mlgz0vkOQSaJ7etUs6oqL",
        "tracks": {
          "href": "https://api.spotify.com/v1/users/spotify/playlists/49wvzum0Lh9mcAdqhLbDbe/tracks",
          "total": 70
        },
        "type": "playlist",
        "uri": "spotify:user:spotify:playlist:49wvzum0Lh9mcAdqhLbDbe"
      }
"""
jsonReal = loads(jsonData)
a = Playlist(jsonReal)
print(a.imageUrl)

