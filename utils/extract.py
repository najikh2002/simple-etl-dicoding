import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd

def scrape_main():
    base_url = "https://fashion-studio.dicoding.dev"
    items = []
    timestamp = datetime.now().isoformat()

    try:
        for page in range(1, 51):
            url = base_url if page == 1 else f"{base_url}/page{page}"
            print(f"Scraping {url} ...")
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            products = soup.select('.collection-card')

            for product in products:
                try:
                    title = product.select_one('.product-title').get_text(strip=True)
                    price = product.select_one('.price').get_text(strip=True)
                    rating_text = product.find(text=lambda t: t and 'Rating:' in t)
                    rating = rating_text.split("⭐")[1].split("/")[0].strip() if rating_text else None
                    colors = product.find(text=lambda t: t and 'Colors' in t).strip()
                    size = product.find(text=lambda t: t and 'Size:' in t).split(":")[1].strip()
                    gender = product.find(text=lambda t: t and 'Gender:' in t).split(":")[1].strip()

                    items.append({
                        'title': title,
                        'price': price,
                        'rating': rating,
                        'colors': colors,
                        'size': size,
                        'gender': gender,
                        'timestamp': timestamp
                    })
                except Exception as e:
                    print(f"⚠️ Error parsing product: {e}")
    except Exception as e:
        print(f"❌ Scraping failed: {e}")

    print(f"✅ Scraped {len(items)} total items.")
    return pd.DataFrame(items)
