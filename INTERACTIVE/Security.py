import config
import base64
from Networking import Networking
import json

#Security API is the class in charge of the managing tokens and refresh the access token that expires every 3600 seconds.

client_id = config.CLIENT_ID
client_secret = config.CLIENT_SECRET
refresh_token = config.REFRESH_TOKEN
access_token = config.ACCESS_TOKEN

class SecurityAPI():

	shared_access_token = access_token
	def __init__(self):
		None
	def renew_access_token(self):
		post = Networking.NetworkPOST("https://accounts.spotify.com","/api/token")
		token_encoded_bytes = base64.urlsafe_b64encode(bytes(client_id+":"+client_secret, 'utf-8'))
		token_encoded= token_encoded_bytes.decode('utf-8')
		headers = {"Authorization":"Basic "+token_encoded, "Content-Type":"application/x-www-form-urlencoded"}
		body = "grant_type=refresh_token&refresh_token="+refresh_token
	
		def success(data):
			json_data = json.loads(data)
			access_token = json_data['access_token']
			self.shared_access_token = access_token

		def failure(error):
			print(error.status_code+" -> "+error.content)

		post.post(success, failure, body, headers)


	def get_Authorization_Header(self):
		return access_token

