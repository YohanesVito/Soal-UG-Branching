# #Buatlah program

n = int(input("Masukkan angka: ")) 

if(n%2==0 and n%3!=0):
    print("Bilangan tersebut habis dibagi 2 dan tidak habis dibagi 3? Jawab: YA \n")
    if(n%5!=0 or n%10==0):
        print("Apakah Bilangan tersebut juga tidak habis dibagi 5 atau habis dibagi 10? Jawab: IYA DONG")
    else:
        print("Apakah Bilangan tersebut juga tidak habis dibagi 5 atau habis dibagi 10? Jawab: TIDAK")
else:
    print("Bilangan tersebut tidak habis dibagi 2 dan habis dibagi 3. Program dihentikan")


# for i in range(100):
#     if(i%2==0 and i%3==1):
#         print("habis dibagi 0 dan sisa dibagi 3",i)
#         if(i%5==1 or i%10==0):
#             print("sisa dibagi 5 atau habis dibagi 10",i)
