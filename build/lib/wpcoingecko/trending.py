

# Trending
# https://www.coingecko.com/api/documentations/v3#/trending

class Trending: 


	def trending(self):
		"""
		def trending(self, params={}):
		https://www.coingecko.com/api/documentations/v3#/trending/get_search_trending
		Top-7 trending coins on CoinGecko as searched by users in the last 24 hours (Ordered by most popular first)

		Arguments:
			None
			
		Returns:
			dict response
			Top-7 trending coins on CoinGecko as searched by users in the last 24 hours (Ordered by most popular first)
		"""
		response = self._request( 'trending', 'search/trending' )
		return response

