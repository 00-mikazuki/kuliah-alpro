def create2D(baris,kolom):
    list2D=[]
    for i in range(baris):
        list2D.append([])
        for j in range(kolom):
            temp='masukkan anggota baris '+str(i)+' kolom '+str(j)+' = '
            list2D[i].append(int(input(temp)))
    return list2D

def addMatriks2D(matriks1,matriks2):
    matriksJumlah=[]
    for i in range(len(matriks1)):
        matriksJumlah.append([])
        for j in range(len(matriks1[i])):
            hasil=matriks1[i][j]+matriks2[i][j]
            print('baris '+str(i)+' kolom '+str(j)+' = '+str(matriks1[i][j])+' + '+str(matriks2[i][j])+' = '+str(hasil))
            matriksJumlah[i].append(hasil)
    return matriksJumlah


matriks1=create2D(2,3)
print('matriks1 = ',matriks1)
matriks2=create2D(2,3)
print('matriks2 = ',matriks2)
jumlah=addMatriks2D(matriks1, matriks2)
print(matriks1,' + ',matriks2,' = ',jumlah)
