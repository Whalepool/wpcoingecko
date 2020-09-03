#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
from pprint import pprint

from .ping import Ping 
from .simple import Simple 
from .coins import Coins 
from .contract import Contract 
from .exchanges import Exchanges 
from .finance import Finance 
from .indexes import Indexes 
from .derivatives import Derivatives 
from .status import Status 
from .events import Events 
from .exchangerates import ExchangeRates 
from .trending import Trending 
from .gglobal import GGlobal 


class WpCoinGecko(
	Ping, 
	Simple, 
	Coins, 
	Contract, 
	Exchanges, 
	Finance, 
	Indexes,
	Derivatives,
	Status,
	Events,
	ExchangeRates,
	Trending,
	GGlobal
	):

	__name__ = 'CoinGecko'
	_base_url = "https://api.coingecko.com/api/v3/"
	_debug = False 


	def __init__(self, debug=False):
		self._debug = debug

	def _log(self, out):
		if self._debug == True:
			if type(out) == str:
				print(out)
			else:
				pprint(out)


	def _request(self, funcname, endpoint, params={}):

		url = self._base_url+endpoint

		self._log('Requesting: {}'.format(url))

		response = requests.get(url, params=params).text
		data = json.loads(response)

		if 'error' in data: 
			self._handle_api_error( funcname, url, params, response )

		self._log(data)

		return data



	def _handle_api_error(self, funcname, url, params={}, response={} ):

		out = '\u001b[38;5;196m ---------------------------------------------------------- \033[0m \n'
		out += '\u001b[38;5;196m ----- {} ERROR ------------ {} ERROR ------- \033[0m \n'.format(self.__name__, self.__name__)
		out += '\u001b[38;5;109m  {} \033[0m \n'.format(eval("self."+funcname).__doc__)
		out += '\u001b[38;5;83m  Function name: {} \033[0m \n'.format(funcname)
		out += '\u001b[38;5;83m  URL: {} \033[0m \n'.format(url)
		out += '\u001b[38;5;83m  Params: {} \033[0m \n'.format(str(params))
		out += '\u001b[38;5;226m  Response: {} \033[0m \n'.format(str(response))
		out += '\u001b[38;5;196m ---------------------------------------------------------- \033[0m \n'

		print( out )

