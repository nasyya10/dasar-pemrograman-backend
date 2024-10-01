# Program Menghitung Gaji Karyawan
def hitung_gaji(nama, golongan, jam_kerja):
    # Tarif per jam berdasarkan golongan
    if golongan == 'A':
        upah_per_jam = 5000
    elif golongan == 'B':
        upah_per_jam = 7000
    elif golongan == 'C':
        upah_per_jam = 8000
    elif golongan == 'D':
        upah_per_jam = 10000
    else:
        return "Golongan tidak valid"
    
    # Menghitung uang lembur
    if jam_kerja > 48:
        uang_lembur = (jam_kerja - 48) * 4000
    else:
        uang_lembur = 0
    
    # Menghitung gaji total
    gaji = (jam_kerja * upah_per_jam) + uang_lembur
    
    # Output hasil
    print(f"Nama Karyawan: {nama}")
    print(f"Golongan: {golongan}")
    print(f"Jumlah jam kerja: {jam_kerja}")
    print(f"{nama} menerima upah Rp. {gaji} per minggu")

# Contoh penggunaan
nama_karyawan = input("Masukkan nama karyawan: ")
golongan_karyawan = input("Masukkan golongan (A/B/C/D): ")
jam_kerja_karyawan = int(input("Masukkan jumlah jam kerja: "))

hitung_gaji(nama_karyawan, golongan_karyawan, jam_kerja_karyawan)
