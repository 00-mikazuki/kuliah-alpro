rupiah=(100000, 50000, 20000, 10000, 5000, 2000, 1000)
strRupiah=('100ribu', '50ribu', '20ribu', '10ribu', '5ribu', '2ribu', '1ribu')

uang=int(input('Berapa uang = '))

a=0
for i in rupiah:
    bagi=uang//i
    if bagi!=0:
        print(bagi,' lembar ',strRupiah[a])
    uang=uang%i
    a+=1