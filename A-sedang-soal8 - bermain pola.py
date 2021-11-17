#Buatlah program untuk membuat pola berikut ini



n = str(input("Mendatar/Menurun?: "))

if(n== "Menurun"):
    m = int(input("Masukkan baris: "))
    print('*\n'*m)
elif(n== "Mendatar"):
    m = int(input("Masukkan kolom: "))
    print('#'*m)
else:
    print("Pola tidak dikenali")
