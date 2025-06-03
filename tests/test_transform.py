import pandas as pd
import numpy as np
from utils.transform import clean_data  # Ganti your_module sesuai nama file/foldermu

def test_clean_data_filters_invalid_and_formats_columns():
    raw_data = pd.DataFrame({
        'title': ['Valid Shirt', 'Unknown Product', 'Image.png'],
        'price': ['$30.00', 'Invalid', '$50.00'],
        'rating': ['4.5⭐', 'Invalid', '3.0⭐'],
        'colors': ['Colors: 2', 'Colors: 3', 'Colors: 1'],
        'size': ['Size: M', 'Size: L', 'Size: S'],
        'gender': ['Gender: Men', 'Gender: Women', 'Gender: Unisex'],
        'timestamp': ['2025-06-03T09:56:27', '2025-06-03T09:56:27', '2025-06-03T09:56:27']
    })

    df_clean = clean_data(raw_data)

    assert df_clean.shape[0] == 1
    assert df_clean.iloc[0]['title'] == 'Valid Shirt'

    assert isinstance(df_clean.iloc[0]['price'], (int, np.integer))
    assert df_clean.iloc[0]['price'] == 480000

    assert isinstance(df_clean.iloc[0]['rating'], float)
    assert abs(df_clean.iloc[0]['rating'] - 4.5) < 1e-5

    assert isinstance(df_clean.iloc[0]['colors'], (int, np.integer))
    assert df_clean.iloc[0]['colors'] == 2

    assert df_clean.iloc[0]['size'] == 'M'
    assert df_clean.iloc[0]['gender'] == 'Men'

def test_clean_data_empty_input():
    empty_df = pd.DataFrame()
    result = clean_data(empty_df)
    assert result.empty

def test_clean_data_error_handling():
    bad_data = pd.DataFrame({
        'title': ['Bad Data'],
        'price': [None],
        'rating': [None],
        'colors': [None],
        'size': [None],
        'gender': [None],
        'timestamp': [None]
    })
    result = clean_data(bad_data)

    assert result.empty
