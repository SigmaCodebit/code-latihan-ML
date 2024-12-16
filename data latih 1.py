import psycopg2
import random

# Fungsi untuk membuat koneksi ke database PostgreSQL
def create_connection():
    conn = psycopg2.connect(
        dbname="data_latih_1",  # Ganti dengan nama database Anda
        user="postgres",         # Ganti dengan username Anda
        password="ronggo24",     # Ganti dengan password Anda
        host="192.168.100.26",        # Ganti dengan host Anda jika perlu
        port="5432"              # Ganti dengan port Anda jika perlu
    )
    return conn

# Fungsi untuk menyisipkan data ke dalam tabel
def insert_data(conn, flowrate_produksi, flowrate_pelanggan, label):
    with conn.cursor() as cursor:
        cursor.execute("""
            INSERT INTO data_latihan_1 (flowrate_produksi, flowrate_pelanggan, label)
            VALUES (%s, %s, %s)
        """, (flowrate_produksi, flowrate_pelanggan, label))
        conn.commit()

# Fungsi utama
def main():
    conn = create_connection()
    
    try:
        for _ in range(1000):  # Menghasilkan 10 entri
            flowrate_produksi = round(random.uniform(100, 500), 2)
            flowrate_pelanggan = round(random.uniform(100, 500), 2)
            label = "Bocor" if flowrate_produksi > flowrate_pelanggan else "Normal"
            
            insert_data(conn, flowrate_produksi, flowrate_pelanggan, label)
            print(f"Inserted: Flowrate Produksi={flowrate_produksi}, Flowrate Pelanggan={flowrate_pelanggan}, Label={label}")
    
    finally:
        conn.close()

if __name__ == "__main__":
    main()