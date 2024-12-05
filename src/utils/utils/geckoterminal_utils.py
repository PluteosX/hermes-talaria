import requests
import time


def get_cryptos_data_for_network(id_coins, network, retries=10, wait_time=30):
    id_cryptos_str = ",".join(id_coins)

    url = f"https://api.geckoterminal.com/api/v2/networks/{network}/pools/multi/{id_cryptos_str}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        return response.json()['data']

    except requests.exceptions.HTTPError as e:
        if response.status_code == 429 and retries > 0:
            print("WARN: Too many requests. Waiting before trying again...")
            time.sleep(wait_time)

            return get_cryptos_data_for_network(id_coins, network, retries - 1, wait_time * 2)

        else:
            print(f"Error in the request with status code: {response.status_code}."
                  f"Error: {e}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Connection error for getting market data info for the following coins: {id_cryptos_str}: {e}")
        return None


