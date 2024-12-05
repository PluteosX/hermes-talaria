import textwrap


def send_message_to_telegram(cryptos):
    cryptos_message = ""
    for crypto in cryptos:
        cryptos_message += _set_message_content(crypto)
    return cryptos_message


def _set_message_content(crypto):
    message = ''
    percentage_change = crypto.get('percentage_change')
    if percentage_change > 0:
        message += textwrap.dedent(f"""
        <b>🔺 {crypto.get('name')}: </b>
        💰 ${crypto.get('current_price')}
        📈{percentage_change}%
        \n\n
        """).strip()
    else:
        message += textwrap.dedent(f"""
        <b>🔻 {crypto.get('name')}: </b>
        💰 ${crypto.get('current_price')}
        📉{percentage_change}%
        \n\n
        """).strip()

    return message
