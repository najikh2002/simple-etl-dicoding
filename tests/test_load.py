import os
import pandas as pd
import pytest
from utils.load import save_to_csv, save_to_gsheet, save_to_postgres

df_test = pd.DataFrame([{
    'title': 'Test Shirt',
    'price': 480000,
    'rating': 4.5,
    'colors': 2,
    'size': 'M',
    'gender': 'Women',
    'timestamp': '2025-06-02T00:00:00'
}])

def test_save_to_csv_creates_file(tmp_path):
    file_path = tmp_path / "test_output.csv"
    save_to_csv(df_test, filename=str(file_path))
    assert file_path.exists()
    df_loaded = pd.read_csv(file_path)
    assert df_loaded.shape[0] == 1

#@pytest.mark.skip(reason="Requires live Google Sheets API and spreadsheet ID")
def test_save_to_gsheet_runs():
    spreadsheet_id = "1QOs6Kmldyw51hohHzIPivpG6d8uNubS_3u0ZRRZTW2g"
    sheet_name = "Sheet1"
    service_account_file = "google-sheets-api.json"

    try:
        save_to_gsheet(df_test, spreadsheet_id, sheet_name, service_account_file)
    except Exception as e:
        pytest.fail(f"Google Sheets save failed: {e}")

@pytest.mark.skipif(
    not os.environ.get("POSTGRES_TEST", False),
    reason="Set POSTGRES_TEST=1 to run PostgreSQL tests"
)
def test_save_to_postgres():
    db_config = {
        'host': 'localhost',
        'port': '5432',
        'user': 'postgres',
        'password': 'root',
        'database': 'root'
    }

    try:
        save_to_postgres(df_test, db_config)
        assert True
    except Exception as e:
        pytest.fail(f"PostgreSQL save failed: {e}")
