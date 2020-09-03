

# Ping
class Ping: 

	def ping(self):
		"""
		def ping(self)
		https://www.coingecko.com/api/documentations/v3#/ping/get_ping
		Check API server status 

		Arguments:
			- 

		Returns:
			dict response
			Status OK
		"""
		response = self._request( 'ping', 'ping')
		return response
