#Membuat Fungsi dalam Bahasa Python
def sapa_lisa():
    print("Hasil Lisa");
def sapa_sari():
    print("Morning, Sari");
def sapa_rudi():
    print("Halo bro, ...");
sapa_lisa
sapa_sari
sapa_rudi

def hitung_luas_segitiga():
    alas = 5
    tinggi = 7
    luas = (alas * tinggi)/2
    print("Luas segitiga adalah :", luas)
hitung_luas_segitiga

#Membuat Fungsi Dengan Parameter
def sapa_teman(nama):
    print("Hai", nama);
sapa_teman("Lisa")
def sapa_teman(nama1, nama2, nama3):
    print("Hai", nama1, nama2, nama3);
sapa_teman("Lisa", "Nova", "Putri")
def hitung_luas_segitiga(alas, tinggi):
    luas = (alas * tinggi)/2
    print("Luas Segitiga Adalah :", luas)
hitung_luas_segitiga(5, 7)
hitung_luas_segitiga(2, 10)
hitung_luas_segitiga(191, 357)

#Perintah Return Dalam Fungsi
def harga_setelah_pajak(harga_dasar):
    return harga_dasar + (harga_dasar * 10/100)
harga_cilok = 5000
harga_final_cilok = harga_setelah_pajak(harga_cilok)
print("Harga cilok 1 porsi RP.", harga_final_cilok)

#Default Parameter dalam Python
#Contoh 1
def tambah(var1 = 5, var2 = 2):
    return var1 + var2
print(tambah())
print(tambah(1))
print(tambah(1,2))
print(tambah(5,4))
#Contoh 2
def pangkat(angka, pangkat = 2):
    hasil = 1
    for i in range(0, pangkat):
        hasil = hasil * angka
    return hasil;
print(pangkat(3))       #9
print(pangkat(5))       #25
print(pangkat(10))      #100
print(pangkat(3,3))     #27
print(pangkat(5,4))     #625
print(pangkat(6,6))     #46656

#Arbitrary Arguments (*args)
#Contoh 1 Yang Salah 
def sapa_teman(nama1, nama2, nama3):
    print("Hallo", nama1)
    print("Hallo", nama2)
    print("Hallo", nama3)
sapa_teman("Alex", "Nisa", "Sari", "Risa")
#Contoh 2 Yang Benar
def sapa_teman(*args):
    print(args)
    print(type(args))
sapa_teman("Alex", "Nisa", "Sari", "Risa")

#Arbitrary Arguments (**kwargs)
#Contoh 1
def sambung_kata(**kwargs):
    print(kwargs)
    print(type(kwargs))
sambung_kata(a="Belajar", b="Python", c="di", d="Stikom")
#Contoh 2
def sambung_kata(**kata):
    for i in kata.values():
        print(i)
sambung_kata(a="Belajar", b="Python", c="di", d="Stikom")
