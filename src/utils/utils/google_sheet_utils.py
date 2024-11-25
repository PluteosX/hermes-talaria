import pandas as pd


def get_google_sheet_data(spreadsheet_id,sheet_name):
    url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        print(f"Error reading Google Sheet: {e}")
        return None
