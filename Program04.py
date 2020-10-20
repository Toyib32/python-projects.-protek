# catat informasi
jarak1 = 125
jarak2 = 256
waktuMulai = 6
durasiIstirahatDalamMenit = 45
kecepatan1 = 62
kecepatan2 = 70

# hitung
durasiPerjalanan1 = jarak1/kecepatan1
durasiIstirahatDalamJam = durasiIstirahatDalamMenit/60
durasiPerjalanan2 = jarak2/kecepatan2
waktuSampai = waktuMulai + durasiPerjalanan1 + durasiIstirahatDalamJam + durasiPerjalanan2
print("sampai di kota C pada pukul", (waktuSampai), "yang jika di sederhanakan menjadi pukul 12.42")



