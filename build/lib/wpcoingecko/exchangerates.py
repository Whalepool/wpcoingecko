

# ExchangeRates
# https://www.coingecko.com/api/documentations/v3#/exchange_rates

class ExchangeRates: 


	def exchange_rates(self):
		"""
		def exchange_rates(self):
		https://www.coingecko.com/api/documentations/v3#/exchange_rates/get_exchange_rates
		Get BTC-to-Currency exchange rates

		Arguments:
			None

		Returns:
			dict response
			Get BTC-to-Currency exchange rates
		"""
		response = self._request( 'exchange_rates', 'exchange_rates' )
		return response

