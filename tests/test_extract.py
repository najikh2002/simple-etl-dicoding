import pandas as pd
from utils.extract import scrape_main

def test_scrape_main_returns_dataframe():
    df = scrape_main()
    assert isinstance(df, pd.DataFrame), "Hasil harus berupa pandas DataFrame"

def test_scrape_main_columns():
    df = scrape_main()
    expected_columns = {'title', 'price', 'rating', 'colors', 'size', 'gender', 'timestamp'}
    assert expected_columns.issubset(df.columns), f"DataFrame harus memiliki kolom: {expected_columns}"

def test_scrape_main_no_empty_titles():
    df = scrape_main()
    assert df['title'].notnull().all() and (df['title'] != '').all(), "Semua title harus ada dan tidak kosong"

def test_scrape_main_price_format():
    df = scrape_main()
    for price in df['price']:
        try:
            float(price.replace('$', '').replace('.', ''))
        except Exception:
            assert False, f"Price '{price}' tidak bisa dikonversi ke angka"
