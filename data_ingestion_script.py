import psycopg2
import requests
from bs4 import BeautifulSoup

# Koneksi ke PostgreSQL
conn = psycopg2.connect(
    database="Penjualan_Sepatu",
    user="postgres",
    password="admin",
    host="localhost",
    port="5432"
)

# Membuat kursor
cursor = conn.cursor()

# Mendefinisikan URL
url = 'https://www.petsecure.com.au/pet-care/a-guide-to-worldwide-pet-ownership/'

# Meminta data dari URL
response = requests.get(url)

# Periksa apakah permintaan berhasil
if response.status_code == 200:
    # Menggunakan BeautifulSoup untuk mengekstrak data dari halaman web
    soup = BeautifulSoup(response.text, 'html.parser')

    # Contoh: Mengekstrak tabel data dengan tag <table>
    table = soup.find('table')

    if table:
        rows = table.find_all('tr')

        for row in rows[1:]:  # Mengabaikan baris header
            columns = row.find_all('td')
            negara = columns[0].get_text()
            jumlah = columns[1].get_text()

            # Menyimpan data ke PostgreSQL
            cursor.execute("INSERT INTO Population (negara, jumlah) VALUES (%s, %s)", (negara, jumlah))

        # Commit perubahan ke database
        conn.commit()

# Tutup koneksi
cursor.close()
conn.close()
