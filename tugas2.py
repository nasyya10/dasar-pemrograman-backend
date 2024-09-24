password_benar = "admin123"  # Password yang benar
percobaan = 3  # Batas percobaan

while percobaan > 0:
    password = input("Masukkan password: ")

    if password == password_benar:
        print("Selamat datang bos!")
        break  
    else:
        percobaan -= 1
        print("Password salah, coba lagi!")
        
    if percobaan == 0:
        print("Terimakasih sudah menggunakan aplikasi kami")