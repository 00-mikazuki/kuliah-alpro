hari = 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'
haripertama=(input('hari pertama = '))
tanggal=(int(input('tgl yg dicari = ')))
indexhari=hari.index(haripertama)
tgl=tanggal%7

for i in range(tgl-1):
    indexhari+=1
    if indexhari==7:
        indexhari=0

haridicari=hari[indexhari]
print(haridicari)