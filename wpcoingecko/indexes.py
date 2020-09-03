

# Indexes
# https://www.coingecko.com/api/documentations/v3#/indexes_(beta)

class Indexes: 


	def indexes(self, params={}):
		"""
		def indexes(self, params={}):
		https://www.coingecko.com/api/documentations/v3#/indexes_(beta)/get_indexes
		List all market indexes

		Arguments:
			per_page:  int, Total results per page
			page: int, page of results (paginated to 100 by default)

		Returns:
			dict response
			List all market indexes
		"""
		response = self._request( 'indexes', 'indexes', params )
		return response


	def indexes_id(self, _id):
		"""
		def indexes_id(self, _id):
		https://www.coingecko.com/api/documentations/v3#/indexes_(beta)/get_indexes__id_
		get market index by id

		Arguments:
			_id: required, string, pass the index id (can be obtained from /indexes/list)

		Returns:
			dict response
			get market index by id
		"""
		response = self._request( 'indexes_id', 'indexes/'+str(_id) )
		return response



	def indexes_list(self):
		"""
		def indexes_list(self, _id):
		https://www.coingecko.com/api/documentations/v3#/indexes_(beta)/get_indexes_list
		list market indexes id and name

		Arguments:
			None

		Returns:
			dict response
			list market indexes id and name
		"""
		response = self._request( 'indexes_list', 'indexes/list' )
		return response
