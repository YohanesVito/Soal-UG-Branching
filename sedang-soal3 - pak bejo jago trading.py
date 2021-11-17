# Pak Bejo Jago Trading

# Pak Bejo adalah seorang trader Cryptocurrency, suatu hari dia
# mengamati pergerakan harga Bitcoin yang sedang volatil.
# Pak Bejo bingung menentukan beli atau jual karena kondisi market
# yang tidak stabil. Dalam mengambil keputusan jual/beli Pak Bejo menggunakan
# beberapa Indikator trading seperti RSI dan MACD.


# Oleh karena itu bantulah Pak Bejo membuat program pengambil keputusan
# untuk menjual atau membeli Bitcoin, dengan aturan dan ketentuan
# sebagai berikut:

# Indikator RSI: lebih besar sama dengan 70 maka overbought = sinyal jual
#                lebih kecil sama dengan 30 maka oversold  = sinyal beli


# Indikator MACD: terdapat golden-cross = sinyal beli
#                 terdapat death-cross = sinyal jual

# Indikator RSI lebih diprioritaskan daripada Indikator MACD.
# Artinya, jika RSI sudah menandakan sinyal jual, sedangkan MACD menunjukkan sinyal beli, maka akan tampilkan
# pesan "Tunggu MACD sampai death-cross"

# jika RSI sudah menandakan sinyal beli, sedangkan MACD menunjukkan sinyal jual, maka akan tampilkan
# pesan "Tunggu MACD sampai golden-cross"


# Inputan RSI berupa bilangan bulat positif lebih dari sama dengan nol
# Inputan MACD berupa string "death-cross" atau "golden-cross"
# Output harus berupa kondisi masing masing Indikator dan keputusan yang harus diambil Pak Bejo
# seperti Test Case berikut ini


rsi = int(input("Masukkan besar RSI: "))
macd = str(input("Masukkan kondisi MACD: "))

kondisi = ""

if rsi >= 70:
    kondisi+=  "RSI Overbougt dan"
    if macd == "golden-cross":
        kondisi += " MACD Golden-cross,"
        keputusan = " Tunggu MACD sampai death-cross"
    elif macd == "death-cross":
        kondisi += " MACD Death-cross,"
        keputusan = " saatnya Jual"
        
elif rsi <= 30:
    kondisi += "RSI Oversold dan"
    if macd == "golden-cross":
        kondisi += " MACD Golden-cross,"
        keputusan = " saatnya Beli"
       
    elif macd == "death-cross":
        kondisi += " MACD Death-cross,"
        keputusan = " Tunggu MACD sampai Golden-cross"
      
print(kondisi+keputusan)

 