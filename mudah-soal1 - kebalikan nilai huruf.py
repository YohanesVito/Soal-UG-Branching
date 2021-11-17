# Program pencari rentang nilai praktekkom

# Buatlah sebuah program sederhana pencari rentang nilai PrakTekKom.
# Program tersebut akan meminta inputan user berupa nilai huruf yang didapatkan peserta mata kuliah PrakTekKom.
# Nilai huruf selalu bernilai A, A-, B+, B, B-, C+, C, D, dan E. Apabila user memasukkan inputan selain huruf tersebut maka
# akan muncul pesan "Inputan anda salah atau nilai huruf tidak ada pada Standar Nilai"

# Carilah rentang nilai PrakTekKom menggunakan tabel Standar Nilai PrakTekKom yang ada pada E-Class.


nilai_huruf = str(input("Masukkan nilai huruf PrakTekKom anda: "))

if nilai_huruf == "A":
    nilai = "Rentang nilai PrakTekKom anda adalah 85 - 100"

elif nilai_huruf == "A-":
    nilai = "Rentang nilai PrakTekKom anda adalah 80 - 84"

elif nilai_huruf == "B+":
    nilai = "Rentang nilai PrakTekKom anda adalah 75 - 79"

elif nilai_huruf == "B":
    nilai = "Rentang nilai PrakTekKom anda adalah 70 - 74"

elif nilai_huruf == "B-":
    nilai = "Rentang nilai PrakTekKom anda adalah 65 - 69"

elif nilai_huruf == "C+":
    nilai = "Rentang nilai PrakTekKom anda adalah 60 - 64"

elif nilai_huruf == "C":
    nilai = "Rentang nilai PrakTekKom anda adalah 55 - 59"

elif nilai_huruf == "D":
    nilai = "Rentang nilai PrakTekKom anda adalah 45 - 54"

elif nilai_huruf == "E":
    nilai = "Rentang nilai PrakTekKom anda adalah 0 - 44"

else:
    nilai = "Inputan anda salah atau nilai huruf tidak ada pada Standar Nilai"

print("=========================")
print(nilai)