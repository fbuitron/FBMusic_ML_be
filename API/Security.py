import config
import base64
from Networking import Networking
import json

client_id = config.CLIENT_ID
client_secret = config.CLIENT_SECRET
refresh_token = config.REFRESH_TOKEN
access_token = config.ACCESS_TOKEN


def renew_access_token():
	post = Networking.NetworkPOST("https://accounts.spotify.com","/api/token")
	token_encoded_bytes = base64.urlsafe_b64encode(bytes(client_id+":"+client_secret, 'utf-8'))
	token_encoded= token_encoded_bytes.decode('utf-8')
	headers = {"Authorization":"Basic "+token_encoded, "Content-Type":"application/x-www-form-urlencoded"}
	body = "grant_type=refresh_token&refresh_token="+refresh_token


	def success(data):
		print(data)
		json_data = json.loads(data)
		print(json_data)
		access_token = json_data['access_token']
		config.ACCESS_TOKEN = json_data['access_token']

	def failure(error):
		print(error.status_code+" -> "+error.content)

	post.post(success, failure, body, headers)

def get_Authorization_Header():
	return access_token



