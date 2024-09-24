#Statement Terminator
#Contoh 1
print("Apa Kabar")
web="Stikom banyuwangi"
print("sedang belajar bahasa python di"+web)
print ("semangat!!")

#Contoh 2
print("Apa Kabar");
web="Stikom banyuwangi";
print("sedang belajar bahasa python di"+web);
print ("semangat!!");

#Contoh 3
print("Apa Kabar");web="Stikom banyuwangi";print("sedang belajar bahasa python di"+web);print ("semangat!!")

#beda dari 3 contoh tsb adalah 
#contoh 1 tanpa titik koma 
#contoh 2 pakai tiitk koma diakhir kalimat
#Contoh 3 pakai titik koma dan digabungkan jadi satu 

#Coments
print("Apa kabar");
web="STIKOM Banyuwangi";
Web="STIKOM PGRI"
WEB="STIKOM PGRI Banyuwangi Kota"
print("sedang belajar bahasa python di"+web);
print("sedang belajar bahasa python di"+Web);
print("sedang belajar bahasa python di"+WEB);
print ("semangat!!");

#Variabel
website = "STIKOM Banyuwangi"
print(website)
harga = 5500
print(harga)
sukses = True
print(sukses)

#Tipe Data
#Tipe Data String
web = "Belajar Python di STIKOM Banyuwangi"
print(web)
#Tipe Data Integer
web = 5500
print(web)
#Tipe Data Float
web = 99.123
print(web)
#Tipe Data Complex Number
web = 4j
print(web)
#Tipe Data Boolean
web = True
print(web)
#Tipe Data List
web = ["satu", "dua", "tiga", "satu"]
print(web)
#Tipe Data Tuple
web = ("satu", "dua", "tiga", "satu")
print(web)
#Tipe Data Set
web = {"satu", "dua", "tiga", "empat"}
print(web)
#Tipe Data Dictionary
web = {"satu":1, "dua":2.13, "tiga":"a", "empat":True}
print(web)

#Operator Aritmatika
x = 7
y = 10

print('x =',x)
print('y =', y)
print('\n')

print('x == y hasilnya', x==y)
print('x != y hasilnya', x!=y)
print('x > y hasilnya', x>y)
print('x < y hasilnya', x<y)
print('x >= y hasilnya', x>=y)
print('x <= y hasilnya', x<=y)

#Operator Logika
print("Hasil Dari True and True :", True and True)
print("Hasil Dari True and False :", True and False)
print("Hasil Dari False and True :", False and True)
print("Hasil Dari False and False :", False and False)
print('\n')

print("Hasil Dari True or True :", True or True)
print("Hasil Dari True or False :", True or False)
print("Hasil Dari False or True :", False or True)
print("Hasil Dari False or False :", False or False)
print('\n')

"""print("Hasil Dari True not True :", True not True)
print("Hasil Dari True not False :", True not False)
print('\n')"""

#Operator Bitwise
x = 10
y = 12
print("x berisi angka",x, "desimal atau", bin(x),"biner")
print("x berisi angka",y, "desimal atau", bin(y),"biner")
print('\n')
print("x & y :", x & y)
print("x | y :", x | y)
print("x ^ y :", x ^ y)
print("~x :", ~x)
print("x << 1 :", x << 1)
print("x >> 1 :", x >> 1)

#Operator Assignment
a = 5
b = 3
c = b + 1
d = a + b
e = c + c + a
f = (c + d)* a

print("Isi Variabel a:", a)
print("Isi Variabel b:", b)
print("Isi Variabel c:", c)
print("Isi Variabel d:", d)
print("Isi Variabel e:", e)
print("Isi Variabel f:", f)

#Operator Identitas
a = 5
b = 5
c = 6
print("a is b :", a is b)
print("a is c :", a is c)
print("a is not c :", a is not c)
print('\n')

i = "STIKOM"
j = "STIKOM"
print("i is j :", i is j)
print("i is not j :", i is not j)
print('\n')

x = ["a", "b", "c"]
y = ["a", "b", "c"]
print("x is y :", x is y)
print("x is not y :", x is not y)

#Operatror Keanggotaan
bar = ["a", "b", "c"]
print("bar :", bar)
print("\"a\" in bar :", "a" in bar)
print("\"a\" not in bar :", "a" not in bar)
print("\"d\" not in bar :", "d" in bar)

baz = [12, 43, 102, 55]
print("baz :", baz)
print("102 in baz :", "102" in baz)
print("102 not in baz :", "a" not in baz)
print("35 not in baz :", "35" in baz)

#Kondisi if
#Contoh 1
a = 12
b = 10

if a > b:
    print("Variabel a lebih besae dari variabel b")

#Contoh 2
a = 7

if (a % 2) == 0:
    print("Variabel a berisi angka genap")
if (a % 2) != 0:
    print("Variabel a berisi angka ganjil")

#Contoh 3
a = 12
b = 12
if a > b:
    print("Variabel a lebih besar dari variabel b")
if a < b:
    print("Variabel a lebih kecil dari variabel b")
if a == b:
    print("Variabel a sama dengan variabel b")

#Kondisi If Else
#if condition itu true
#else condition itu false
nilai = 65
if nilai >= 75:
    print("Selamat, anda lulus")
else:
    print("Maaf, silahkan coba lagi tahun depan")

#Kondisi perulangan while
#Contoh 1
i = 1
while i <= 5:
    print("STIKOM")

#Contoh 2
i = 1
while i <= 5:
    print("STIKOM")
    i += 1

#Contoh 3
i = 1
while i <= 5:
    print("STIKOM",i)
    i += 1

#Contoh 4
i = 3
while i < 100:
    print("STIKOM",i)
    i += i + 3

#Kondisi Perulangan For
#Contoh 1
warna = ["Merah", "Biru", "Kuning", "Biru"]
for i in warna:
    print(i)

#Contoh 2
web = "STIKOM"
for huruf in web:
    print(huruf)

#Contoh function range
"""for i in range(5):
    print(i)"""

#Perintah break
i = 1
while i <= 10:
    print(i, "x", i, "=", i*i)
    i +=1

i = 1
while i <= 10:
    print(i, "x", i, "=", i*i)
    if i == 5:
        break
    i += 1

#Perintah Continue
for i in range (1, 11):
    print(i, "x", i, "=", i*i)

for i in range (1, 11):
    if i == 5:
        continue
    print(i, "x", i, "=", i*i)


while i < 10:
    i += 1
    if i == 5:
        continue
    print(i, "x", i, "=", i*i)
