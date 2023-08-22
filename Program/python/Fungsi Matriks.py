# for i in range(len(data)):
#     for j in range(len(data[i])):
#         print(data[i][j])

def displayMat2D(mat):
    matprint=''
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            matprint=matprint+str(mat[i][j])+' '
        matprint=matprint+'\n'
    return matprint

def addMatriks2D(matriks1,matriks2):
    if len(matriks1)==len(matriks2) and len(matriks1[0])==len(matriks2[0]):
        baris=[]
        for i in range(len(matriks1)):
            kolom=[]
            for j in range(len(matriks1[i])):
                hasil=matriks1[i][j]+matriks2[i][j]
                kolom.append(hasil)
            baris.append(kolom)
        return baris
    else:
        return 'Ukuran matrix tidak sama'

data1=[[1,2,3],[4,5,6]]
data2=[[3,7,8],[8,9,0]]

print(displayMat2D(data1))
print(displayMat2D(data2))
jumlah=addMatriks2D(data1,data2)
print(displayMat2D(jumlah))