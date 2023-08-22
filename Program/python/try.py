# nilai = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
# strNilai = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']

# angka = int(input('Masukkan Angka => '))
# sisa = angka
# start = True
# jumlah = 0
# konv=''
# while start :
#     konversi = sisa // nilai [jumlah]
#     if konversi !=0 :
#         konv+=konversi*strNilai[jumlah]
#     sisa = sisa % nilai[jumlah]
#     if sisa == 0 :
#         start = False
#     jumlah += 1
# print(konv)

nilai = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
strNilai = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']

angka = int(input('Masukkan Angka => '))
sisa = angka
start = True
jumlah = 0
while start :
    konversi = sisa // nilai [jumlah]
    if konversi !=0 :
        print (konversi*strNilai[jumlah],end='')
    sisa = sisa % nilai[jumlah]
    if sisa == 0 :
        start = False
    jumlah += 1