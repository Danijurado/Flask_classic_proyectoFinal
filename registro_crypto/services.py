import requests
from config import API_KEY


def get_exchange(base,quota):
    url = f'https://rest.coinapi.io/v1/exchangerate/{base}/{quota}'
    headers = {'X-CoinAPI-Key' : API_KEY}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()['rate']