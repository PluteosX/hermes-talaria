import sys
import os

import numpy as np
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from constants import SPREADSHEET_ID, SHEET_NAME
from utils.utils.coingecko_utils import get_coins_price
from utils.utils.google_sheet_utils import get_google_sheet_data
from utils.utils.message_utils import send_message_to_telegram
from utils.utils.telegram_utils import send_message_text


def main():

    data = get_google_sheet_data(SPREADSHEET_ID, SHEET_NAME)
    df_data = data[data['no_monitorize'] == False]
    coin_data_info_json = get_coins_price(df_data['id'].tolist())
    coin_data_info = pd.DataFrame.from_dict(coin_data_info_json, orient='index').reset_index()

    coin_data_info.columns = ['id', 'current_price']

    columns = ['id', 'name', 'investment_price', 'current_price', 'percentage_max_to_sell', 'percentage_min_to_sell']
    df = pd.merge(left=df_data, right=coin_data_info, how='left', on='id')[columns]

    df['investment_price'] = df['investment_price'].str.replace(',', '.').astype(float)
    df['percentage_max_to_sell'] = df['percentage_max_to_sell'].astype(float)
    df['percentage_min_to_sell'] = df['percentage_min_to_sell'].astype(float)

    df['percentage_change'] = np.round(
        ((df['current_price'] - df['investment_price']) / df['investment_price']) * 100, 2)
    df['sell'] = (df['percentage_change'] > df['percentage_max_to_sell']) | \
                 (df['percentage_change'] < df['percentage_min_to_sell'])

    sells = df[df['sell']].to_dict(orient='records')
    no_sells = df[~df['sell']].to_dict(orient='records')

    print(f"SELLS: {sells}")
    print(f"NO SELLS: {no_sells}")

    if len(sells) > 0:
        sells_message = send_message_to_telegram(sells)
        send_message_text("<u><b>⚠️ Time to sell ⚠️</b></u>\n" + sells_message)
    if len(no_sells) > 0:
        no_sells_message = send_message_to_telegram(no_sells)
        send_message_text(f"<u><b>🚀 Price Update</b></u>\n" + no_sells_message)


if __name__ == "__main__":
    main()
