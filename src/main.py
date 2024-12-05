import sys
import os

import numpy as np
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from constants import SPREADSHEET_ID, SHEET_NAME, NETWORK
from utils.utils.geckoterminal_utils import get_cryptos_data_for_network
from utils.utils.google_sheet_utils import get_google_sheet_data
from utils.utils.message_utils import send_message_to_telegram
from utils.utils.telegram_utils import send_message_text


def main():

    data = get_google_sheet_data(SPREADSHEET_ID, SHEET_NAME)
    df_data = data[data["no_monitorize"] == False]
    df_coin_data_info = _get_contracts_info(df_data["id"].tolist())

    columns = ["id", "name", "investment_price", "current_price", "percentage_max_to_sell", "percentage_min_to_sell"]
    df = pd.merge(left=df_data, right=df_coin_data_info, how="left", on="id")[columns]

    df["investment_price"] = df["investment_price"].str.replace(",", ".").astype(float)
    df["percentage_max_to_sell"] = df["percentage_max_to_sell"].astype(float)
    df["percentage_min_to_sell"] = df["percentage_min_to_sell"].astype(float)

    df["percentage_change"] = np.round(
        ((df["current_price"] - df["investment_price"]) / df["investment_price"]) * 100, 2)
    df["sell"] = (df["percentage_change"] > df["percentage_max_to_sell"]) | \
                 (df["percentage_change"] < df["percentage_min_to_sell"])

    sells = df[df["sell"]].to_dict(orient="records")
    no_sells = df[~df["sell"]].to_dict(orient="records")

    if len(sells) > 0:
        sells_message = send_message_to_telegram(sells)
        send_message_text("<u><b>⚠️ Time to sell ⚠️</b></u>\n\n" + sells_message)
    if len(no_sells) > 0:
        no_sells_message = send_message_to_telegram(no_sells)
        send_message_text(f"<u><b>🚀 Price Update</b></u>\n\n" + no_sells_message)


def _get_contracts_info(id_coins):
    data = []
    # GeckoTerminal API limits requests to 30 addresses at a time.
    ids_chunks = np.array_split(id_coins, len(id_coins) // 30 + (len(id_coins) % 30 > 0))
    for ids in ids_chunks:
        data.extend(get_cryptos_data_for_network(id_coins=ids, network=NETWORK))

    df = pd.DataFrame(data)
    df["id"] = df["id"].replace(f"{NETWORK}_", "", regex=True)
    df["current_price"] = df["attributes"].apply(lambda x: x["base_token_price_usd"]).astype(float)

    return df[["id", "current_price"]]


if __name__ == "__main__":
    main()
