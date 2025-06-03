import pandas as pd

def save_to_csv(df: pd.DataFrame, filename='products.csv'):
    try:
        df.to_csv(filename, index=False)
        print(f"[CSV] Data saved to {filename}")
    except Exception as e:
        print(f"[CSV] Error saving data: {e}")


def save_to_gsheet(df: pd.DataFrame, spreadsheet_id: str, sheet_name: str, service_account_file: str):
    try:
        import gspread
        from gspread_dataframe import set_with_dataframe
        from google.oauth2.service_account import Credentials

        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_file(service_account_file, scopes=scope)
        client = gspread.authorize(creds)

        spreadsheet = client.open_by_key(spreadsheet_id)
        worksheet = spreadsheet.worksheet(sheet_name)
        worksheet.clear()
        set_with_dataframe(worksheet, df)
        print(f"[Google Sheets] Data uploaded to spreadsheet: {spreadsheet_id}, sheet: {sheet_name}")
    except Exception as e:
        print(f"[Google Sheets] Error: {e}")


def save_to_postgres(df: pd.DataFrame, db_config: dict):
    try:
        from sqlalchemy import create_engine

        engine = create_engine(
            f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"
        )
        df.to_sql('fashion_products', con=engine, if_exists='replace', index=False)
        print("[PostgreSQL] Data saved to table: fashion_products")
    except Exception as e:
        print(f"[PostgreSQL] Error: {e}")
