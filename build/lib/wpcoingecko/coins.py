

# Coins
# https://www.coingecko.com/api/documentations/v3#/coins

class Coins: 


	def coins_list(self):
		"""
		def coins_list(self):
		https://www.coingecko.com/api/documentations/v3#/coins/get_coins_list
		Use this to obtain all the coins’ id in order to make API calls.

		Arguments:
			None 

		Returns:
			dict response
			List all coins with id, name, and symbol
		"""
		response = self._request( 'coins_list', 'coins/list' )
		return response


	def coins_markets(self, params={}):
		"""
		def coins_markets(self, params={}):
		https://www.coingecko.com/api/documentations/v3#/coins/get_coins_markets
		Use this to obtain all the coins market data (price, market cap, volume)

		Arguments:
			params: dict
				vs_currency: required, string, The target currency of market data (usd, eur, jpy, etc.)

				ids: string, The ids of the coin, comma separated crytocurrency symbols (base). refers to /coins/list. When left empty, returns numbers the coins observing the params limit and start
				category: string, filter by coin category, only decentralized_finance_defi is supported at the moment
				order: string, default: market_cap_desc, valid values: market_cap_desc, gecko_desc, gecko_asc, market_cap_asc, market_cap_desc, volume_asc, volume_desc, id_asc, id_desc  - sort results by field.
				per_page: int, default: 100, valid values: 1…250  - Total results per page
				page: int, default 1, page through results
				sparkline: bool, default: false, Include sparkline 7 days data (eg. true, false)
				price_change_percentage: string, Include price change percentage in 1h, 24h, 7d, 14d, 30d, 200d, 1y (eg. '1h,24h,7d' comma-separated, invalid values will be discarded)


		Returns:
			dict response
			List all coins with market data
		"""
		response = self._request( 'coins_markets', 'coins/markets', params )
		return response


	def coins_id(self, _id, params={}):
		"""
		def coins_id(self, _id, params={}):
		https://www.coingecko.com/api/documentations/v3#/coins/get_coins__id_
		Get current data (name, price, market, … including exchange tickers) for a coin.

		IMPORTANT:
		Ticker object is limited to 100 items, to get more tickers, use /coins/{id}/tickers
		Ticker is_stale is true when ticker that has not been updated/unchanged from the exchange for a while.
		Ticker is_anomaly is true if ticker’s price is outliered by our system.
		You are responsible for managing how you want to display these information (e.g. footnote, different background, change opacity, hide)

		Arguments:
			_id:  required, string, pass the coin id (can be obtained from /coins) eg. bitcoin
			params: dict
				localization: string, Include all localized languages in response (true/false) [default: true]
				tickers: bool, Include tickers data (true/false) [default: true]
				market_data: bool, Include market_data (true/false) [default: true]
				community_data: bool, Include community_data data (true/false) [default: true]
				developer_data: bool, Include developer_data data (true/false) [default: true]
				sparkline: bool, Include sparkline 7 days data (eg. true, false) [default: false]

		Returns:
			dict response
			Get current data for a coin
		"""
		response = self._request( 'coins_id', 'coins/'+str(_id), params )
		return response


	def coins_id_tickers(self, _id, params={}):
		"""
		def coins_id_tickers(self, _id, params={}):
		https://www.coingecko.com/api/documentations/v3#/coins/get_coins__id__tickers
		Get coin tickers (paginated to 100 items)

		IMPORTANT:
		Ticker is_stale is true when ticker that has not been updated/unchanged from the exchange for a while.
		Ticker is_anomaly is true if ticker’s price is outliered by our system.
		You are responsible for managing how you want to display these information (e.g. footnote, different background, change opacity, hide)

		Arguments:
			_id:  required, string, pass the coin id (can be obtained from /coins) eg. bitcoin
			params: dict
				exchange_ids: string, filter results by exchange_ids (ref: v3/exchanges/list)
				include_exchange_logo: string, flag to show exchange_logo
				page: int, page through results 
				order: string, valid values: trust_score_desc (default), trust_score_asc and volume_desc

		Returns:
			dict response
			Get coin tickers
		"""
		response = self._request( 'coins_id_tickers', 'coins/'+str(_id)+'/tickers', params )
		return response


	def coins_id_history(self, _id, params={}):
		"""
		def coins_id_history(self, _id, params={}):
		https://www.coingecko.com/api/documentations/v3#/coins/get_coins__id__history
		Get historical data (name, price, market, stats) at a given date for a coin

		Arguments:
			_id:  required, string, pass the coin id (can be obtained from /coins) eg. bitcoin
			params: dict
				data: string, The date of data snapshot in dd-mm-yyyy eg. 30-12-2017
				localization: string, Set to false to exclude localized languages in response

		Returns:
			dict response
			Get historical data at a given date for a coin
		"""
		response = self._request( 'coins_id_history', 'coins/'+str(_id)+'/history', params )
		return response


	def coins_id_market_chart(self, _id, params={}):
		"""
		def coins_id_market_chart(self, _id, params={}):
		https://www.coingecko.com/api/documentations/v3#/coins/get_coins__id__market_chart
		Get historical market data include price, market cap, and 24h volume (granularity auto)
		Minutely data will be used for duration within 1 day, Hourly data will be used for duration between 1 day and 90 days, Daily data will be used for duration above 90 days.

		Arguments:
			_id:  required, string, pass the coin id (can be obtained from /coins) eg. bitcoin
			params: dict
				vs_currency: required, string, The target currency of market data (usd, eur, jpy, etc.)
				days: required, string, Data up to number of days ago (eg. 1,14,30,max)

		Returns:
			dict response
			Get historical market data include price, market cap, and 24h volume
		"""
		response = self._request( 'coins_id_market_chart', 'coins/'+str(_id)+'/market_chart', params )
		return response


	def coins_id_market_chart_range(self, _id, params={}):
		"""
		def coins_id_market_chart_range(self, _id, params={}):
		https://www.coingecko.com/api/documentations/v3#/coins/get_coins__id__market_chart_range
		Get historical market data include price, market cap, and 24h volume within a range of timestamp (granularity auto)
		Minutely data will be used for duration within 1 day, Hourly data will be used for duration between 1 day and 90 days, Daily data will be used for duration above 90 days.

		Arguments:
			_id:  required, string, pass the coin id (can be obtained from /coins) eg. bitcoin
			params: dict
				vs_currency: required, string, The target currency of market data (usd, eur, jpy, etc.)
				from: required, string, From date in UNIX Timestamp (eg. 1392577232)
				to: required, string, To date in UNIX Timestamp (eg. 1422577232)

		Returns:
			dict response
			Get historical market data include price, market cap, and 24h volume
		"""
		response = self._request( 'coins_id_market_chart_range', 'coins/'+str(_id)+'/market_chart/range', params )
		return response


	def coins_id_status_updates(self, _id, params={}):
		"""
		def coins_id_status_updates(self, _id, params={}):
		https://www.coingecko.com/api/documentations/v3#/coins/get_coins__id__status_updates
		Get status updates for a given coin

		Arguments:
			_id:  required, string, pass the coin id (can be obtained from /coins) eg. bitcoin
			params: dict
				per_age: string, Total results per page
				page: string, Page through results

		Returns:
			dict response
			Get paginated status updates for a given coin
		"""
		response = self._request( 'coins_id_status_updates', 'coins/'+str(_id)+'/status_updates', params )
		return response


	def coins_id_ohlc(self, _id, params={}):
		"""
		def coins_id_ohlc(self, _id, params={}):
		https://www.coingecko.com/api/documentations/v3#/coins/get_coins__id__ohlc
		Candle’s body:
		1 - 2 days: 30 minutes
		3 - 30 days: 4 hours
		31 and before: 4 days


		Arguments:
			_id:  required, string, pass the coin id (can be obtained from /coins) eg. bitcoin
			params: dict
				vs_currency: required, string, The target currency of market data (usd, eur, jpy, etc.)
				days: required, int, Data up to number of days ago (1/7/14/30/90/180/365/max)

		Returns:
			dict response
			Get paginated status updates for a given coin
		"""
		response = self._request( 'coins_id_ohlc', 'coins/'+str(_id)+'/ohlc', params )
		return response