import requests
import time


def get_coins_price(id_coins, retries=10, wait_time=30):
    params = {
        'ids': ','.join(id_coins),
        'vs_currencies': 'usd'
    }
    try:
        response = requests.get('https://api.coingecko.com/api/v3/simple/price', params=params)
        response.raise_for_status()

        return response.json()

    except requests.exceptions.HTTPError as e:
        if response.status_code == 429 and retries > 0:
            print("WARN: Too many requests. Waiting before trying again...")
            time.sleep(wait_time)

            return get_coins_price(id_coins, retries - 1, wait_time * 2)

        else:
            print(f"Error in the request with status code: {response.status_code}."
                  f"Error: {e}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Connection error for getting market data info for the following coins: {id_coins}: {e}")
        return None
