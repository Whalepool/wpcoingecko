

# Status
# https://www.coingecko.com/api/documentations/v3#/status_updates_(beta)

class Status: 


	def status_updates(self, params={}):
		"""
		def status_updates(self, params={}):
		https://www.coingecko.com/api/documentations/v3#/status_updates_(beta)/get_status_updates
		List all status_updates with data (description, category, created_at, user, user_title and pin)

		Arguments:
			param:
				category: string, Filtered by category (eg. general, milestone, partnership, exchange_listing, software_release, fund_movement, new_listings, event)
				project_type: string, Filtered by Project Type (eg. coin, market). If left empty returns both status from coins and markets.
				per_page: int, Total results per page
				page: int, Page through results

		Returns:
			dict response
			List all status_updates with data (description, category, created_at, user, user_title and pin)
		"""
		response = self._request( 'status_updates', 'status_updates', params )
		return response

