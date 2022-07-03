from bs4 import BeautifulSoup
import requests
import re

name = ['Aave', 'bnb', 'Bitcoin', 'Cardano', 'Chainlink', 'Cosmos',
 'Crypto.com Coin', 'Dogecoin', 'EOS', 'Ethereum', 'IOTA', 'Litecoin', 'Monero',
 'NEM', 'Polkadot', 'Solana', 'Stellar', 'Tether', 'TRON', 'Uniswap', 'USD Coin',
 'Wrapped Bitcoin', 'XRP']
symbol = ['AAVE', 'BNB', 'BTC', 'ADA', 'LINK', 'ATOM', 'CRO', 'DOGE', 'EOS', 'ETH', 'MIOTA',
     'LTC', 'XMR', 'XEM', 'DOT', 'SOL', 'XLM', 'USDT', 'TRX', 'UNI', 'USDC', 'WBTC',
     'XRP']
#url= f'https://coinmarketcap.com/currencies/{name[5].lower()}/'
#urlopenpage = requests.get(url)
#print(urlopenpage, url)
#soup = BeautifulSoup(urlopenpage.text, 'html.parser')
#
img_pic = []
"""
try:
    for na in name:
        url= f'https://coinmarketcap.com/currencies/{na.lower()}/'
        urlopenpage = requests.get(url)
        print(urlopenpage, url)
        soup = BeautifulSoup(urlopenpage.text, 'html.parser')
        images = soup.findAll('img')
        for image in images:
            #print(image)
            if "/static/img/coins/" in image['src']:
                #print(image)
                img_pic.append(image['src'])

except Exception as e:
    print(e)
    pass
"""
#print(list(set(img_pic)))
"""
https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png
https://s2.coinmarketcap.com/static/img/coins/64x64/1.png
https://s2.coinmarketcap.com/static/img/coins/64x64/1839.png
https://s2.coinmarketcap.com/static/img/coins/64x64/1975.png
https://s2.coinmarketcap.com/static/img/coins/64x64/2010.png

"""
pics = ['https://s2.coinmarketcap.com/static/img/coins/64x64/2010.png',
 'https://s2.coinmarketcap.com/static/img/coins/64x64/7334.png',
  'https://s2.coinmarketcap.com/static/img/coins/64x64/1.png',
   'https://s2.coinmarketcap.com/static/img/coins/64x64/6535.png',
    'https://s2.coinmarketcap.com/static/img/coins/64x64/1765.png',
     'https://s2.coinmarketcap.com/static/img/coins/64x64/14556.png',
      'https://s2.coinmarketcap.com/static/img/coins/64x64/1958.png',
       'https://s2.coinmarketcap.com/static/img/coins/64x64/52.png',
        'https://s2.coinmarketcap.com/static/img/coins/64x64/14803.png',
         'https://s2.coinmarketcap.com/static/img/coins/64x64/4256.png',
          'https://s2.coinmarketcap.com/static/img/coins/64x64/1975.png',
           'https://s2.coinmarketcap.com/static/img/coins/64x64/3890.png',
            'https://s2.coinmarketcap.com/static/img/coins/64x64/2.png',
             'https://s2.coinmarketcap.com/static/img/coins/64x64/5802.png',
              'https://s2.coinmarketcap.com/static/img/coins/64x64/873.png',
               'https://s2.coinmarketcap.com/static/img/coins/64x64/1831.png',
                'https://s2.coinmarketcap.com/static/img/coins/64x64/2087.png',
                 'https://s2.coinmarketcap.com/static/img/coins/64x64/2530.png',
                  'https://s2.coinmarketcap.com/static/img/coins/64x64/3794.png',
                   'https://s2.coinmarketcap.com/static/img/coins/64x64/2502.png',
                    'https://s2.coinmarketcap.com/static/img/coins/64x64/6836.png',
                     'https://s2.coinmarketcap.com/static/img/coins/64x64/2469.png',
                      'https://s2.coinmarketcap.com/static/img/coins/64x64/4660.png',
                       'https://s2.coinmarketcap.com/static/img/coins/64x64/4747.png',
                        'https://s2.coinmarketcap.com/static/img/coins/64x64/7083.png',
                         'https://s2.coinmarketcap.com/static/img/coins/64x64/11841.png',
                          'https://s2.coinmarketcap.com/static/img/coins/64x64/9285.png',
                           'https://s2.coinmarketcap.com/static/img/coins/64x64/2777.png',
                            'https://s2.coinmarketcap.com/static/img/coins/64x64/6636.png',
   'https://s2.coinmarketcap.com/static/img/coins/64x64/3635.png',
    'https://s2.coinmarketcap.com/static/img/coins/64x64/3626.png',
   'https://s2.coinmarketcap.com/static/img/coins/64x64/5426.png',
                                'https://s2.coinmarketcap.com/static/img/coins/64x64/5919.png',
                                 'https://s2.coinmarketcap.com/static/img/coins/64x64/328.png',
                                  'https://s2.coinmarketcap.com/static/img/coins/64x64/1720.png',
                                   'https://s2.coinmarketcap.com/static/img/coins/64x64/9640.png',
                                    'https://s2.coinmarketcap.com/static/img/coins/64x64/15165.png',
'https://s2.coinmarketcap.com/static/img/coins/64x64/5601.png',
'https://s2.coinmarketcap.com/static/img/coins/64x64/8267.png',
'https://s2.coinmarketcap.com/static/img/coins/64x64/4030.png',
'https://s2.coinmarketcap.com/static/img/coins/64x64/4172.png',
'https://s2.coinmarketcap.com/static/img/coins/64x64/5805.png',
'https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png',
'https://s2.coinmarketcap.com/static/img/coins/64x64/5453.png',
'https://s2.coinmarketcap.com/static/img/coins/64x64/3945.png',
'https://s2.coinmarketcap.com/static/img/coins/64x64/825.png',
'https://s2.coinmarketcap.com/static/img/coins/64x64/1274.png',
'https://s2.coinmarketcap.com/static/img/coins/64x64/7653.png',
'https://s2.coinmarketcap.com/static/img/coins/64x64/74.png',
'https://s2.coinmarketcap.com/static/img/coins/64x64/512.png',
'https://s2.coinmarketcap.com/static/img/coins/64x64/5604.png',
'https://s2.coinmarketcap.com/static/img/coins/64x64/7505.png',
'https://s2.coinmarketcap.com/static/img/coins/64x64/1839.png',
'https://s2.coinmarketcap.com/static/img/coins/64x64/2570.png',
'https://s2.coinmarketcap.com/static/img/coins/64x64/7278.png',
 'https://s2.coinmarketcap.com/static/img/coins/64x64/3513.png']

print(pics[0].split("/")[-1])
for picture in pics:

    response = requests.get(picture)
    name_png = picture.split("/")[-1]
    file = open(f"{name_png}", "wb")
    file.write(response.content)
    file.close()