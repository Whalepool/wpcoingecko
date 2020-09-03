

# Finance
# https://www.coingecko.com/api/documentations/v3#/finance_(beta)

class Finance: 


	def finance_platforms(self, params={}):
		"""
		def finance_platforms(self, params={}):
		https://www.coingecko.com/api/documentations/v3#/finance_(beta)/get_finance_platforms
		List all finance platforms

		Arguments:
			per_page:  int, Total results per page
			page: int, page of results (paginated to 100 by default)

		Returns:
			dict response
			List all finance platforms
		"""
		response = self._request( 'finance_platforms', 'finance_platforms', params )
		return response


	def finance_products(self, params={}):
		"""
		def finance_products(self, params={}):
		https://www.coingecko.com/api/documentations/v3#/finance_(beta)/get_finance_products
		List all finance produccts

		Arguments:
			per_page:  int, Total results per page
			page: int, page of results (paginated to 100 by default)
			start_at: string, start date of the financial products
			end_at: string, end date of the financial products

		Returns:
			dict response
			List all finance produccts
		"""
		response = self._request( 'finance_products', 'finance_products', params )
		return response

