n = int(input("Masukkan angka: ")) 

if(n%5==0 or n%3==0):
    print("Bilangan tersebut habis dibagi 5 atau 3? Jawab: YA \n")
    if(n%2==0 and n%4==0):
        print("Apakah Bilangan tersebut juga habis dibagi 2 dan 4? Jawab: TENTU")
    else:
        print("Apakah Bilangan tersebut juga habis dibagi 2 dan 4? Jawab: TIDAK")
else:
    print("Bilangan tersebut tidak habis dibagi 5 atau 3. Program dihentikan")

# for i in range(100):
#     if(i%5==0 or i%3==0):
#         print("habis dibagi 5 atau 3",i)
#         if(i%2==0 and i%4==0):
#             print("habis dibagi 2 dan 4",i)
