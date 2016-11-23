import requests
from enum import Enum

class HTTPMethod(Enum):
	GET = 1
	POST = 2

class ResponseType(Enum):
	json = 1
	image = 2
	data = 3 # used for audio if we have a playback feature

class NetworkError:
	def __init__(self, status_code, url, description):
		self.status_code = status_code
		self.url = url
		self.content = description

class NetworkOperation:
	def __init__(self, baseUrl, endpoint):
		self.baseUrl = baseUrl
		self.endpoint = endpoint

	def prepareURL(self, baseUrl, endpoint):
		completeURL = baseUrl+endpoint
		return completeURL

	def createError(self, request):
		error = NetworkError(request.status_code, request.url, request.text)
		return error

	def handleResponse(self, response, success, failure):
		if response.status_code > 399:
			error = self.createError(response)
			failure(error)
		elif response.status_code > 199 & response.status_code < 300:
			success(response.text)

class NetworkPOST(NetworkOperation):
	def post(self, success, failure, bodyData, headers={}):
		completeURL = self.prepareURL(self.baseUrl, self.endpoint)
		reqPOST = requests.post(completeURL, data=bodyData, headers = headers)
		self.handleResponse(reqPOST, success, failure)

class NetworkGET(NetworkOperation):
	def get(self, success, failure, urlStringParameters= {}):
		completeURL = self.prepareURL(self.baseUrl, self.endpoint)
		reqGet = requests.get(completeURL, urlStringParameters)
		self.handleResponse(reqGet, success, failure)






