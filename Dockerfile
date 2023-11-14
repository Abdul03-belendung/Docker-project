# Gunakan image Python
FROM python:3.9

# Set direktori kerja ke /app
WORKDIR /app

# Salin file ke direktori kerja kontainer
COPY data_ingestion_script.py /app/
COPY requirements.txt /app/

# Instal dependensi Python
RUN pip install --no-cache-dir -r requirements.txt

# Eksekusi skrip saat kontainer dijalankan
CMD [ "python", "data_ingestion_script.py" ]
