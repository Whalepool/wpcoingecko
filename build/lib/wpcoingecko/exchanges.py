

# Exchanges
# https://www.coingecko.com/api/documentations/v3#/exchanges_(beta)

class Exchanges: 


	def exchanges(self, params={}):
		"""
		def exchanges(self):
		https://www.coingecko.com/api/documentations/v3#/exchanges_(beta)/get_exchanges
		List all exchanges

		Arguments:
			per_page:  int, Valid values: 1…250, Total results per page, Default value:: 100
			page: int, Page through results

		Returns:
			dict response
			List all exchanges
		"""
		response = self._request( 'exchanges', 'exchanges', params )
		return response


	def exchanges_list(self):
		"""
		def exchanges(self):
		https://www.coingecko.com/api/documentations/v3#/exchanges_(beta)/get_exchanges_list
		Use this to obtain all the markets’ id in order to make API calls

		Arguments:
			None

		Returns:
			dict response
			List all coins with id and name
		"""
		response = self._request( 'exchanges_list', 'exchanges/list' )
		return response


	def exchanges_id_tickers(self, _id, params={}):
		"""
		def exchanges_id_tickers(self, _id, params={}):
		https://www.coingecko.com/api/documentations/v3#/exchanges_(beta)/get_exchanges__id__tickers
		Get exchange tickers (paginated)

		IMPORTANT:
		Ticker is_stale is true when ticker that has not been updated/unchanged from the exchange for a while.
		Ticker is_anomaly is true if ticker’s price is outliered by our system.
		You are responsible for managing how you want to display these information (e.g. footnote, different background, change opacity, hide)

		Arguments:
			_id: required, string, pass the exchange id (can be obtained from /exchanges/list) eg. binance
			params: 
				coin_ids: string, filter tickers by coin_ids (ref: v3/coins/list)
				include_exchange_logo: string, flag to show exchange_logo
				page: int,  Page through results
				order: string, valid values: trust_score_desc (default), trust_score_asc and volume_desc

		Returns:
			dict response
			Get exchange tickers
		"""
		response = self._request( 'exchanges_id_tickers', 'exchanges/'+str(_id)+'/tickers', params )
		return response


	def exchanges_id_status_updates(self, _id, params={}):
		"""
		def exchanges_id_status_updates(self, _id, params={}):
		https://www.coingecko.com/api/documentations/v3#/exchanges_(beta)/get_exchanges__id__status_updates
		Get status updates for a given exchange

		Arguments:
			_id: required, string, pass the exchange id (can be obtained from /exchanges/list) eg. binance
			params: 
				per_page: int,  Total results per page
				page: int,  Page through results

		Returns:
			dict response	
			Get paginated status updates for a given coin
		"""
		response = self._request( 'exchanges_id_status_updates', 'exchanges/'+str(_id)+'/status_updates', params )
		return response


	def exchanges_id_volume_chart(self, _id, params={}):
		"""
		def exchanges_id_volume_chart(self, _id, params={}):
		https://www.coingecko.com/api/documentations/v3#/exchanges_(beta)/get_exchanges__id__volume_chart
		Get volume_chart data for a given exchange

		Arguments:
			_id: required, string, pass the exchange id (can be obtained from /exchanges/list) eg. binance
			params: 
				days: required, int, Data up to number of days ago (eg. 1,14,30)

		Returns:
			dict response	
			Get exchange volume_chart data
		"""
		response = self._request( 'exchanges_id_volume_chart', 'exchanges/'+str(_id)+'/volume_chart', params )
		return response

