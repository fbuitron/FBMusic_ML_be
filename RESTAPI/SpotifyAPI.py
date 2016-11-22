import json
import Security

class SpotifyAPI:
	base_url = "https://api.spotify.com"
	def __init__(self):
		self.limit = 20
		self.offset = 0

	def getParameters(self):
		token = Security.get_Authorization_Header()
		params = {"access_token": token}
		if self.hasPaging():
			params['limit'] = self.limit
			params['offset'] = self.offset
		return params
	
	def success(self, json_str):
		json_obj = json.loads(json_str)
		root_obj = json_obj
		if self.hasPaging():
			if self.getRootElement():
				root_obj = json_obj[self.getRootElement()]

			if root_obj['next'] == None:
				self.stillPaging = False
			else:
				self.offset += self.limit
				self.stillPaging = True

	def failure(self, error):
		print("error")
		print(error.content)
		self.stillPaging = False

# All the APIs classes should inherit from SpotifyAPI that will hold most of the general logic: retry/paging/token_renewal_detection/generalError Management