

# Derivatives
# https://www.coingecko.com/api/documentations/v3#/derivatives_(beta)

class Derivatives: 


	def derivatives(self, params={}):
		"""
		def derivatives(self, params={}):
		https://www.coingecko.com/api/documentations/v3#/derivatives_(beta)/get_derivatives
		List all derivative tickers

		Arguments:
			param:
				include_tickers: string, ['all’, ‘unexpired’] - expired to show unexpired tickers, all to list all tickers, defaults to unexpired

		Returns:
			dict response
			List all derivative tickers
		"""
		response = self._request( 'derivatives', 'derivatives', params )
		return response


	def derivatives_exchanges(self, params={}):
		"""
		def derivatives_exchanges(self, params={}):
		https://www.coingecko.com/api/documentations/v3#/derivatives_(beta)/get_derivatives_exchanges
		List all derivative exchanges

		Arguments:
			param:
				order: string, 
				per_page: int, 
				page: int, 

		Returns:
			dict response
			List all derivative exchanges
		"""
		response = self._request( 'derivatives_exchanges', 'derivatives/exchanges', params )
		return response


	def derivatives_exchanges_id(self, _id, params={}):
		"""
		def derivatives_exchanges_id(self, params={}):
		https://www.coingecko.com/api/documentations/v3#/derivatives_(beta)/get_derivatives_exchanges__id_
		show derivative exchange data

		Arguments:
			_id: required, string, pass the exchange id (can be obtained from derivatives/exchanges/list) eg. bitmex
			param:
				include_tickers: string, ['all’, ‘unexpired’] - expired to show unexpired tickers, all to list all tickers, leave blank to omit tickers data in response

		Returns:
			dict response
			show derivative exchange data
		"""
		response = self._request( 'derivatives_exchanges_id', 'derivatives/exchanges/'+str(_id), params )
		return response


	def derivatives_exchanges_list(self):
		"""
		def derivatives_exchanges_list(self, params={}):
		https://www.coingecko.com/api/documentations/v3#/derivatives_(beta)/get_derivatives_exchanges_list
		List all derivative exchanges name and identifier

		Arguments:
			None

		Returns:
			dict response
			List all derivative exchanges name and identifier
		"""
		response = self._request( 'derivatives_exchanges_list', 'derivatives/exchanges/list' )
		return response

