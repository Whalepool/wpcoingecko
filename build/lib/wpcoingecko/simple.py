

# Simple
# https://www.coingecko.com/api/documentations/v3#/simple

class Simple: 


	def simple_price(self, params={}):
		"""
		def simple_price(self, params={})
		https://www.coingecko.com/api/documentations/v3#/simple/get_simple_price

		Arguments:
			params: dict
				ids: required, string, comma-separated if querying more than 1 coin, *refers to coins/list
				vs_currencies: required, string, comma-separated if querying more than 1 vs_currency

				include_market_cap: string, true/false to include market_cap, default: false
				include_24hr_vol: string, true/false to include 24hr_vol, default: false
				include_24hr_change: string, true/false to include 24hr_change, default: false
				include_last_updated_at: string, true/false to include last_updated_at of price, default: false

		Returns:
			dict response
			price(s) of cryptocurrency
		"""
		response = self._request( 'simple_price', 'simple/price', params)
		return response


	def simple_token_price(self, _id, params={}):
		"""
		def simple_token_price(self, id, params):
		https://www.coingecko.com/api/documentations/v3#/simple/get_simple_token_price__id_
		Get current price of tokens (using contract addresses) for a given platform in any other currency that you need.

		Arguments:
			id: required, string, The id of the platform issuing tokens (Only ethereum is supported for now)
			params: dict
				contract_addresses: required, string, The contract address of tokens, comma separated
				vs_currencies: required, string, comma-separated if querying more than 1 vs_currency, *refers to simple/supported_vs_currencies

				include_market_cap: string, true/false to include market_cap, default: false
				include_24hr_vol: string, true/false to include 24hr_vol, default: false
				include_24hr_change: string, true/false to include 24hr_change, default: false
				include_last_updated_at: string, true/false to include last_updated_at of price, default: false

		Returns:
			dict response
			price(s) of cryptocurrency
		"""
		response = self._request( 'simple_token_price', 'simple/token_price/'+str(_id), params)
		return response


	def simple_supported_vs_currencies(self):
		"""
		def simple_supported_vs_currencies(self):
		https://www.coingecko.com/api/documentations/v3#/simple/get_simple_supported_vs_currencies
		Get list of supported_vs_currencies.

		Arguments:
			None 

		Returns:
			dict response
			list of supported_vs_currencies
		"""
		response = self._request( 'simple_supported_vs_currencies', 'simple/supported_vs_currencies/' )
		return response
