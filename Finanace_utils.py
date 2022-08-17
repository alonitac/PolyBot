# Import libraries

import json
import requests

def get_price_of_btc():
    """
    This function Show the current price of Bitcoin
    #:param video_name: string of the video name
    #:param num_results: integer representing how many videos to download
    :return: string of price of bitcoin
    """
    # defining key/request url
    key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

    # requesting data from url
    data = requests.get(key)
    data = data.json()
    # return(print(f"{data['symbol']} price is {data['price']}"))
    return(data['price'])


