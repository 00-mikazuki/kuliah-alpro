hari = 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'
hariPertama=input('Masukkan informasi, hari pertama bulan ini, jatuh pada hari : ')
tanggal=int(input('Masukkan tanggal yang ingin diketahui harinya : '))

n=0
for i in hari:
    if hariPertama.capitalize()==i:
        hari=hari[n:]+hari[:n]
    n+=1

print(hari)

hitung=tanggal%7
hariTanggal=hari[hitung-1]
print('Tanggal',tanggal,'adalah hari',hariTanggal)