

# Contract
# https://www.coingecko.com/api/documentations/v3#/contract

class Contract: 


	def coins_id_contract(self, _id, _contract_address):
		"""
		def coins_id_contract(self, _id, _contract_address):
		https://www.coingecko.com/api/documentations/v3#/contract/get_coins__id__contract__contract_address_
		Get coin info from contract address

		Arguments:
			_id:  required, string, Asset platform (only ethereum is supported at this moment)
			_contract_address: required, string, Token’s contract address	

		Returns:
			dict response
			Get current data for a coin
		"""
		response = self._request( 'coins_id_contract', 'coins/'+str(_id)+'/contract/'+str(_contract_address) )
		return response


	def coins_id_contract_market_chart(self, _id, _contract_address, params={}):
		"""
		def coins_id_contract_market_chart(self, _id, _contract_address):
		https://www.coingecko.com/api/documentations/v3#/contract/get_coins__id__contract__contract_address__market_chart_
		Get historical market data include price, market cap, and 24h volume (granularity auto)

		Arguments:
			_id:  required, string, Asset platform (only ethereum is supported at this moment)
			_contract_address: required, string, Token’s contract address	
			params:
				vs_currency: required, string, The target currency of market data (usd, eur, jpy, etc.)
				days: required, string, Data up to number of days ago (eg. 1,14,30,max)

		Returns:
			dict response
			Get historical market data include price, market cap, and 24h volume
		"""
		response = self._request( 'coins_id_contract_market_chart', 'coins/'+str(_id)+'/contract/'+str(_contract_address)+'/market_chart', params )
		return response


	def coins_id_contract_market_chart_range(self, _id, _contract_address, params={}):
		"""
		def coins_id_contract_market_chart_range(self, _id, _contract_address):
		https://www.coingecko.com/api/documentations/v3#/contract/get_coins__id__contract__contract_address__market_chart_range
		Get historical market data include price, market cap, and 24h volume within a range of timestamp (granularity auto)

		Arguments:
			_id:  required, string, Asset platform (only ethereum is supported at this moment)
			_contract_address: required, string, Token’s contract address	
			params:
				vs_currency: required, string, The target currency of market data (usd, eur, jpy, etc.)
				from: required, string, From date in UNIX Timestamp (eg. 1392577232)
				to: required, string, To date in UNIX Timestamp (eg. 1422577232)

		Returns:
			dict response
			Get historical market data include price, market cap, and 24h volume
		"""
		response = self._request( 'coins_id_contract_market_chart_range', 'coins/'+str(_id)+'/contract/'+str(_contract_address)+'/market_chart/range', params )
		return response

