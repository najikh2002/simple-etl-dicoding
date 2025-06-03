import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    try:
        df = df.dropna()
        df = df.drop_duplicates()

        df = df[~df['title'].str.contains("Unknown Product", case=False)]
        df = df[~df['title'].str.contains(".jpeg|.jpg|.png", case=False)]
        df = df[~df['price'].str.contains("Invalid|None", case=False)]
        df = df[~df['rating'].str.contains("Invalid", case=False)]

        df['price'] = df['price'].str.replace('$', '', regex=False).astype(float) * 16000
        df['price'] = df['price'].astype(int)

        df['rating'] = df['rating'].str.extract(r'(\d+\.?\d*)').astype(float)

        df['colors'] = df['colors'].str.extract(r'(\d+)').astype(int)

        df['size'] = df['size'].str.replace('Size:', '', regex=False).str.strip()

        df['gender'] = df['gender'].str.replace('Gender:', '', regex=False).str.strip()

        df = df[['title', 'price', 'rating', 'colors', 'size', 'gender', 'timestamp']]

    except Exception as e:
        print(f"Transform error: {e}")
        return pd.DataFrame()

    return df
