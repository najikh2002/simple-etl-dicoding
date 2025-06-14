Proyek ini adalah pipeline ETL sederhana untuk mengolah data produk dari [Fashion Studio Dicoding](https://fashion-studio.dicoding.dev). Pipeline ini mencakup proses _Extract_, _Transform_, dan _Load_ ke berbagai tujuan seperti CSV, Google Sheets, dan PostgreSQL.

---

## 📁 Struktur Proyek

```

submission-pemda/
├── main.py
├── requirements.txt
├── .gitignore
├── README.md
├── products.csv
├── google-sheets-api.json (di-ignore)
├── utils/
│ ├── extract.py
│ ├── transform.py
│ └── load.py
└── tests/
├── test_extract.py
├── test_transform.py
└── test_load.py

```

---

## ⚙️ Instalasi & Setup

### 1. Buat virtual environment

**Mac/Linux**:

```bash
python3.11 -m venv env
source env/bin/activate
```

**Windows**:

```bash
python -m venv env
env\Scripts\activate
```

### 2. Install dependensi

```bash
pip install -r requirements.txt
```

---

## 🚀 Menjalankan ETL

```bash
python main.py
```

---

## 🧪 Testing

Jalankan semua test:

```bash
pytest tests
```

Jalankan hanya test tertentu:

```bash
pytest tests/test_transform.py
```

---

## 🧼 Contoh Output (`products.csv`)

| title     | price   | rating | colors | size | gender | timestamp              |
| --------- | ------- | ------ | ------ | ---- | ------ | ---------------------- |
| T-shirt 2 | 1634400 | 3.9    | 3      | M    | Women  | 2025-06-03T09:56:27... |
| Hoodie 3  | 7950080 | 4.8    | 3      | L    | Unisex | 2025-06-03T09:56:27... |
| Pants 4   | 7476960 | 3.3    | 3      | XL   | Men    | 2025-06-03T09:56:27... |

---

## 📦 Output

- ✅ `products.csv`
- ✅ Google Sheets (dengan `google-sheets-api.json`)
- ✅ PostgreSQL (localhost)

---

## 🛠️ Teknologi

- `Python 3.11`
- `BeautifulSoup`, `requests` – Web scraping
- `pandas` – Data wrangling
- `sqlalchemy`, `psycopg2` – PostgreSQL
- `gspread`, `oauth2client` – Google Sheets API
- `pytest` – Testing

---
