# Kalkulator Advance Sederhana

# Buatlah Program Kalkulator Advance sederhana yang memuat fitur-fitur:
# Menghitung sisa hasil bagi antara dua bilangan
# Menghitung hasil bagi antara dua bilangan
# Menghitung akar kubik sebuah bilangan

# Ketentuan:
# Tidak boleh memakai library math
# Input hanya berupa bilangan desimal, bukan bilangan bulat


print("############################")
print("Kalkulator Advance Sederhana")
print("############################")
print("1. Menghitung sisa hasil bagi")
print("2. Membulatkan ke bawah hasil pembagian")
print("3. Mencari akar kubik sebuah bilangan")

menu = int(input("Masukkan menu yang anda pilih: "))

if(menu==1):
    bil1 = float(input("Masukkan bilangan yang ingin dibagi: "))
    bil2 = float(input("Masukkan bilangan pembagi: "))
    print("Sisa hasil bagi",bil1,"dibagi dengan",bil2,"adalah", bil1%bil2)
elif(menu==2):
    bil1 = float(input("Masukkan bilangan yang ingin dibagi: "))
    bil2 = float(input("Masukkan bilangan pembagi: "))
    print("Hasil pembagian",bil1,"dibagi dengan",bil2,"dibulatkan kebawah adalah", bil1//bil2)
elif(menu==3):
    bil1 = float(input("Masukkan bilangan yang ingin dicari akar kubiknya: "))
    print("Akar kubik dari",bil1,"adalah", bil1**(1/3))
else:
    print("Menu yang anda pilih tidak tersedia")
