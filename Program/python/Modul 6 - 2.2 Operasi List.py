def createList(sizeList):
    listcreate=[]
    for i in range(sizeList):
        temp='Masukkan data ke - '+str(i)+' : '
        listcreate.append(int(input(temp)))
    return listcreate

def avgList(list):
    total=0
    for i in list:
        total+=i
    rata2=total/len(list)
    return rata2

def addList(list1,list2):
    listJumlah=[]
    if len(list1)==len(list2):
        for i in range(len(list1)):
            tambah=list1[i]+list2[i]
            listJumlah.append(tambah)
        return listJumlah
    else:
        tdksama='Ukuran List Tidak Sama'
        return tdksama


data1=createList(3)
print('data - 1 = ',data1,' ; rata-rata list = ',avgList(data1))
data2=createList(4)
print('data - 2 = ',data2,' ; rata-rata list = ',avgList(data2))
hasil=addList(data1, data2)
hasil2=addList(hasil, hasil)
print(data1,'+',data2,'=',hasil)
if hasil!='Ukuran List Tidak Sama':
    print(hasil,'+',hasil,'=',hasil2)
else:
    print('ukuran list hasil tdk sama')