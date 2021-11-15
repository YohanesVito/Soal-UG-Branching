# cari operator pada kalimat

# Buatlah program untuk mengubah sebuah kata menjadi sebuah operator matematika.
# Berikut adalah tabel kata dan operator:
# tambah -> +
# kurang -> -
# bagi -> /
# kali -> *

# Program akan meminta inputan sebanyak 3 kali, yang terdiri dari bilangan 1 berupa float,
# bilangan 2 berupa float, dan 1 operator berupa string kalimat yang mengandung 1 kata operator tertentu

# contoh input adalah sebagai berikut:

# "Brendi meminta anda mengkalikan bilangan tersebut"

# "Berapakah hasil pembagian kedua bilangan di atas"
bil1 = float(input("Masukkan bilangan pertama: "))
bil2 = float(input("Masukkan bilangan kedua: "))
kata = str(input("Masukkan kalimat: "))


if "tambah" in kata:
    print("Hasil penjumlahan",bil1,"dengan",bil2,"adalah",bil1 + bil2)
elif "kurang" in kata:
    print("Hasil pengurangan",bil1,"dengan",bil2,"adalah",bil1 - bil2)
elif "kali" in kata:
    print("Hasil perkalian",bil1,"dengan",bil2,"adalah",bil1 * bil2)
elif "bagi" in kata:
    print("Hasil pengurangan",bil1,"dengan",bil2,"adalah",bil1 - bil2)