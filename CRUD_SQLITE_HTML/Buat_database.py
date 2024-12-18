import sqlite3
import os

# Hapus database lama jika ada
if os.path.exists('database_siswa.db'):
    os.remove('database_siswa.db')

try:
    conn = sqlite3.connect('database_siswa.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE data_siswa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )''')
    
    # Masukkan beberapa data contoh
    cursor.execute("INSERT INTO data_siswa (nama, email) VALUES (?, ?)", 
                  ("Contoh Siswa", "siswa@example.com"))
    
    conn.commit()
    print("Database berhasil dibuat dan data contoh telah ditambahkan!")
    
except sqlite3.Error as e:
    print(f"Error: {e}")
finally:
    conn.close()