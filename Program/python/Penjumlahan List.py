list1=[]
list2=[]
penjumlahan=[]

print('-in-')
sizeList1=int(input())
print('')
for i in range(sizeList1):
    list1.append(int(input(' ')))

print('')

sizeList2=int(input())
print('')
for i in range(sizeList2):
    list2.append(int(input(' ')))

print('\n-out-')
print(list1)
print(list2)

if sizeList1>sizeList2:
    listBanyak=list1
    listSedikit=list2
    tambah0=sizeList1-sizeList2
else:
    listBanyak=list2
    listSedikit=list1
    tambah0=sizeList2-sizeList1

for i in range(tambah0):
    listSedikit.append(0)

for i in range(len(listBanyak)):
    jumlah=listBanyak[i]+listSedikit[i]
    penjumlahan.append(jumlah)

print(penjumlahan)