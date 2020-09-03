

# Derivatives
# https://www.coingecko.com/api/documentations/v3#/events

class Events: 


	def events(self, params={}):
		"""
		def events(self, params={}):
		https://www.coingecko.com/api/documentations/v3#/events/get_events
		Get events, paginated by 100

		Arguments:
			param:
				country_code: string, country_code of event (eg. ‘US’). use /api/v3/events/countries for list of country_codes
				type: string, type of event (eg. ‘Conference’). use /api/v3/events/types for list of types
				page: string, page of results (paginated by 100)
				upcoming_events_only: string, lists only upcoming events. true, false  (defaults to true, set to false to list all events)
				from_date: string, lists events after this date yyyy-mm-dd
				to_date: string,  lists events before this date yyyy-mm-dd (set upcoming_events_only to false if fetching past events)

		Returns:
			dict response
			Get events, paginated by 100
		"""
		response = self._request( 'events', 'events', params )
		return response


	def events_countries(self):
		"""
		def events_countries(self):
		https://www.coingecko.com/api/documentations/v3#/events/get_events_countries
		Get list of event countries 

		Arguments:
			None

		Returns:
			dict response
			Get list of event countries 
		"""
		response = self._request( 'events_countries', 'events/countries' )
		return response


	def events_types(self):
		"""
		def events_types(self):
		https://www.coingecko.com/api/documentations/v3#/events/get_events_types
		Get list of event types 

		Arguments:
			None

		Returns:
			dict response
			Get list of event types 
		"""
		response = self._request( 'events_types', 'events/types' )
		return response

