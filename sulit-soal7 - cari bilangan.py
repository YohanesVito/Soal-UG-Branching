#Buatlah program

n = int(input("Masukkan angka: ")) 

if(n%2==0 and n%3==0):
    print("Bilangan tersebut habis dibagi 2 dan 3? Jawab: YA \n")
    if(n%5==0):
        print("Apakah Bilangan tersebut juga habis dibagi 5? Jawab: YA")
    else:
        print("Apakah Bilangan tersebut juga habis dibagi 5? Jawab: TIDAK")
else:
    print("Bilangan tersebut tidak habis dibagi 2 dan 3. Program dihentikan")


# for i in range(100):
#     if(i%2==0 and i%3==0 and i%5==0):
#         print(i)