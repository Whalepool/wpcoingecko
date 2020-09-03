

# GGlobal
# https://www.coingecko.com/api/documentations/v3#/global

class GGlobal: 


	def gglobal(self):
		"""
		def gglobal(self):
		https://www.coingecko.com/api/documentations/v3#/global/get_global
		Get cryptocurrency global data 

		Arguments:
			None

		Returns:
			dict response
			Get cryptocurrency global data 
		"""
		response = self._request( 'gglobal', 'global' )
		return response

