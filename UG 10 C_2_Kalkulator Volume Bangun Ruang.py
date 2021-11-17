# Buatlah sebuah kalkulator penghitung volume bangun ruang Limas, Bola, dan Kerucut
# dengan ketentuan sebagai berikut:
# phi yang digunakan adalah 3.14
# inputan menu berupa bilangan bulat, sedangkan inputan yang lain berupa bilangan desimal.
# Apabila user memilih inputan tidak sesuai menu maka akan ditampilkan "Pilihan anda tidak tersedia di menu kalkulator ini"

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Kalkulator Volume Bangun Ruang")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Pilih bangun ruang yang ingin dihitung volumenya: ")
print("1. Limas")
print("2. Bola")
print("3. Kerucut")

opsi = int(input("Masukkan pilihan anda: "))

if(opsi == 1):
    alas = float(input("Masukkan panjang sisi alas limas: "))
    tinggi = float(input("Masukkan tinggi limas: "))
    print("Volume limas tersebut adalah",(1/3)*alas*alas*tinggi)
elif(opsi == 2):
    r = float(input("Masukkan panjang jari-jari bola: "))
    print("Volume bola tersebut adalah",(4/3)*3.14*(r**3))
elif(opsi == 3):
    r = float(input("Masukkan jari-jari kerucut: "))
    t = float(input("Masukkan tinggi kerucut: "))
    print("Volume kerucut tersebut adalah",(1/3)*3.14*r*r*t)
else:
    print("Pilihan anda tidak tersedia di menu kalkulator ini")
    
