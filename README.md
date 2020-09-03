# WpCoinGecko  
  
### Install  
```bash
git clone https://github.com/whalepool/wpcoingecko.git
cd wpcoingecko

pip install -r requirements.txt
python setup.py install
```
  
Reference coingecko v3 api   
https://www.coingecko.com/api/documentations/v3#/  

  
### Use
```python

from wpcoingecko import WpCoinGecko
coingecko = WpCoinGecko(debug=True)


# Ping
coingecko.ping() 

# Simple 
# coingecko.simple_price( )  # No params so will return api error 
# coingecko.simple_price( {'ids':'bitcoin', 'vs_currencies': 'usd' } )
# coingecko.simple_token_price( 'ethereum', {'contract_addresses':'0x0f4ca92660efad97a9a70cb0fe969c755439772c', 'vs_currencies':'usd'})
# coingecko.simple_supported_vs_currencies()

# Coins
# coingecko.coins_list()
# coingecko.coins_markets( {'vs_currency': 'usd', 'order':'market_cap_desc', 'per_page': 2})
# coingecko.coins_id( 'bitcoin', {'tickers':'false', 'market_data': 'false'} )
# coingecko.coins_id_tickers( 'bitcoin', {'exchange_ids': 'bitfinex'} )
# coingecko.coins_id_history( 'bitcoin', {'date': '30-01-2020', 'localization': 'false'} )
# coingecko.coins_id_market_chart( 'bitcoin', {'vs_currency': 'usd', 'days':'max'} )
# coingecko.coins_id_market_chart_range( 'bitcoin', {'vs_currency': 'usd', 'from':'1392577232', 'to': '1422577232'} )
# coingecko.coins_id_status_updates( 'ethereum', {'per_page': '2' } )
# coingecko.coins_id_ohlc( 'bitcoin', {'vs_currency': 'usd', 'days':'1'} )

# Contract
# coingecko.coins_id_contract( 'ethereum', '0x0f4ca92660efad97a9a70cb0fe969c755439772c' )
# coingecko.coins_id_contract_market_chart( 'ethereum', '0x0f4ca92660efad97a9a70cb0fe969c755439772c', {'vs_currency': 'usd', 'days': '1'} )
# coingecko.coins_id_contract_market_chart_range( 'ethereum', '0x0f4ca92660efad97a9a70cb0fe969c755439772c', {'vs_currency': 'usd', 'from':'1392577232', 'to': '1422577232'} )

# Exchanges
# coingecko.exchanges( {'per_page': 2})
# coingecko.exchanges_list()
# coingecko.exchanges_id_tickers('bitfinex')
# coingecko.exchanges_id_status_updates('bitfinex')
# coingecko.exchanges_id_volume_chart('bitfinex', {'days': 1})

# Finance
# coingecko.finance_platforms( {'per_page': 2} )
# coingecko.finance_products( {'per_page': 2} )

# Indexes
# coingecko.indexes()
# coingecko.indexes_id( 'BTC' )
# coingecko.indexes_list()

# Derivatives
# coingecko.derivatives()
# coingecko.derivatives_exchanges( {'order':'trade_volume_24h_btc_desc', 'per_page': 2})
# coingecko.derivatives_exchanges_id( 'binance_futures', { 'include_tickers': 'unexpired'})
# coingecko.derivatives_exchanges_list()

# Status_updates
# coingecko.status_updates( {'per_page': 2})

# Events
# coingecko.events( {'country_code': 'RU' })
# coingecko.events_countries()
# coingecko.events_types()

# Exchange Rates
# coingecko.exchange_rates()

# Trending
# coingecko.trending()

# GGlobal
# coingecko.gglobal()
```