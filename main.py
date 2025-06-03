from utils.extract import scrape_main
from utils.transform import clean_data
from utils.load import save_to_csv, save_to_gsheet, save_to_postgres

SPREADSHEET_ID = "1QOs6Kmldyw51hohHzIPivpG6d8uNubS_3u0ZRRZTW2g"
SHEET_NAME = "Sheet1"
SERVICE_ACCOUNT_FILE = "google-sheets-api.json"

DB_CONFIG = {
    'host': 'localhost',
    'port': '5432',
    'user': 'postgres',
    'password': 'root',
    'database': 'root'
}

def main():
    print("\n🔄 Starting ETL process...\n")

    # 1. Extract
    try:
        df_raw = scrape_main()
        print(f"✅ Extracted {len(df_raw)} records.\n")
    except Exception as e:
        print(f"❌ Error during extraction: {e}")
        return

    # 2. Transform
    try:
        df_clean = clean_data(df_raw)
        print(f"✅ Cleaned data: {len(df_clean)} records remain.\n")
        print("📌 Sample cleaned data:")
        print(df_clean.head(3).to_string(index=False))
        print()
    except Exception as e:
        print(f"❌ Error during transformation: {e}")
        return

    # 3. Load
    try:
        save_to_csv(df_clean)
    except Exception as e:
        print(f"❌ Error saving to CSV: {e}")

    try:
        save_to_gsheet(df_clean, SPREADSHEET_ID, SHEET_NAME, SERVICE_ACCOUNT_FILE)
    except Exception as e:
        print(f"❌ Error saving to Google Sheets: {e}")

    try:
        save_to_postgres(df_clean, DB_CONFIG)
    except Exception as e:
        print(f"❌ Error saving to PostgreSQL: {e}")

    print("✅ ETL process completed.\n")


if __name__ == "__main__":
    main()
