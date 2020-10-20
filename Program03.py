# catat informasi
totalTempuh = 795
jarakPerLiter = 12
efisiensiBbm = 1

# hitung konsumsi bbm
konsumsiBbmTotal = float(totalTempuh/(jarakPerLiter/efisiensiBbm))

# hitung berapa kali minimal pengisian ulang bbm
kapasitasTangki = 50
pengisianUlangMin = konsumsiBbmTotal/kapasitasTangki
print("mengisi ulang sebanyak", (pengisianUlangMin), "atau jika dibulatkan mengisi ulang tangki minimal sebanyak", int(pengisianUlangMin), "kali")
