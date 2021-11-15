# Kalkulator replika penghitung nilai praktekkom

# Buatlah sebuah kalkulator replika nilai PrakTekKom.
# Kalkulator tersebut akan meminta inputan user sebanyak 3 yaitu nilai rata - rata UG,
# nilai TTS, dan nilai TAS.
# Nilai yang akan dimasukkan akan selalu berupa bilangan desimal yang nilainya lebih besar sama dengan nol.
# Bobot dari nilai rata-rata ug adalah 70%, nilai TTS 15%, dan nilai TAS 15%
# Dari ketiga nilai tersebut carilah nilai huruf yang didapatkan oleh seorang user kalkulator, menggunakan
# tabel Standar Nilai PrakTekKom yang ada pada E-Class.

ug = float(input("Masukkan nilai rata-rata UG anda: "))
tts = float(input("Masukkan nilai TTS anda: "))
tas = float(input("Masukkan nilai TAS anda: "))

nilai_akhir = ug*0.7 + tts*0.15 + tas*0.15

if nilai_akhir >= 85:
    nilai_huruf = "A"

elif nilai_akhir >= 80:
    nilai_huruf = "A-"

elif nilai_akhir >= 75:
    nilai_huruf = "B+"

elif nilai_akhir >= 70:
    nilai_huruf = "B"

elif nilai_akhir >= 65:
    nilai_huruf = "B-"

elif nilai_akhir >= 60:
    nilai_huruf = "C+"

elif nilai_akhir >= 55:
    nilai_huruf = "C"

elif nilai_akhir >= 45:
    nilai_huruf = "D"

else:
    nilai_huruf = "E"

print("=========================")
print("Nilai anda: ", nilai_akhir)
print("Nilai huruf anda: ", nilai_huruf)