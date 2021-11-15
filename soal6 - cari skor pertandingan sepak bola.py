#cari skor pertandingan sepak bola

# Juki seorang yang gemar membaca artikel sedang mencoba mencari berita bola terkini di sosial media.
# Seperti biasanya, Juki selalu mencari nama klub sepak bola terlebih dahulu sebelum mencari angka skornya
# Akan tetapi, Juki mengeluh karena banyak sekali artikel yang muncul pada halaman utama sosmednya.
# Ia meminta tolong kepada anda untuk mencarikan nama klub bola favoritnya dan skor pertandingan saat itu.

# Ketentuan program:
# Program akan meminta inputan sebanyak 3, yaitu; artikel, nama klub sepak bola, dan skornya
# Jika pada artikel tersebut hanya ditemukan nama klubnya maka akan ditampilkan pesan "Hanya nama klub yang ditemukan pada artikel ini"
# Jika pada artikel tersebut hanya ditemukan skor pertandingan maka akan ditampilkan pesan "Hanya skor pertandingan yang ditemukan pada artikel ini"
# Jika pada artikel tersebut ditemukan keduanya, maka akan ditampilkan "Hasil pencarian ditemukan"

# contoh artikel: Kondisi Manchester United belum kondusif pada musim 2021-2022. 

# Mereka masih tercecer di urutan keenam klasemen sementara Liga Inggris dengan 17 poin dari 11 pekan. 

# Setan Merah juga menelan dua kekalahan kandang beruntun di Old Trafford. 

# Mereka digulung 0-5 oleh Liverpool pada 24 Oktober 2021 dan menyerah 0-2 dari Manchester City pada 6 November lalu. 


artikel = str(input("Masukkan artikel yang ingin dipindai: "))
namaKlub = str(input("Masukkan nama klub favorit anda: "))
skor = str(input("Masukkan skor yang ingin dicari: "))

if(namaKlub in artikel and skor in artikel):
    print("Hasil pencarian ditemukan")
elif(namaKlub in artikel and skor not in artikel):
    print(f"Hanya kata {namaKlub} yang ditemukan pada artikel ini")
elif(namaKlub not in artikel and skor in artikel):
    print(f"Hanya skor {skor} yang ditemukan pada artikel ini")
else:
    print(f"Hasil pencarian {namaKlub} dan {skor} tidak ditemukan")