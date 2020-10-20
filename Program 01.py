# tarif rental
A = 200000
B = 10000

# waktu rental
jamMulai = 6
jamSelesai = 23
menitMulai = 0
menitSelesai = 50
lamaRentJam = jamSelesai - jamMulai
lamaRentMenit = menitSelesai - menitMulai
lamaRentNonPromo = lamaRentJam - 12

# hitung tarif
tarifRentJam = lamaRentNonPromo*B
tarifRentMenit = lamaRentMenit*B/60
totalTarifRentNonPromo = tarifRentJam + tarifRentMenit
tarifTotal = A + totalTarifRentNonPromo
print(tarifTotal, "atau jika dibulatkan maka menjadi", int(tarifTotal), "rupiah")
