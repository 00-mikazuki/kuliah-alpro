# def addMatriks(mat1,mat2):
#     newMat=[]
#     if len(mat1)==len(mat2) and len(mat1[0])==len(mat2[0]):
#         for i in range(mat1):
#             isi=[]
#             for j in range(mat1):
#                 jumlah=mat1[i][j]+mat2[i][j]
#                 isi.append(jumlah)
#             newMat.append(isi)

# def dispSparseMatriks(data):
#     for i in range(data):
#             for j in range(data):
#                 if data[i][j]!=0:
#                     dictData[i,j]=data[i][j]
#     temp=''
#     for i in range(baris):
#         for j in range(kolom):
#             if dictData.get((i,j))==None:
#                 temp=temp+str(0)+' '
#             else:
#                 temp=temp+str(dictData.get((i,j)))+' '
#         temp=temp+'\n'
#     print(temp)


def createSparseMatriks(baris,kolom):
    stop=False
    mat={'baris':baris,'kolom':kolom}
    while not(stop):
        indBaris=int(input('masukkan indeks baris = '))
        indKolom=int(input('masukkan indeks kolom = '))
        mat[indBaris,indKolom]=int(input('masukkan data = '))
        lagi=input('masukkan data lagi (y/t)? ')
        if lagi=='t':
            stop=True
    return mat

def addSparseMat(mat1,mat2):
    if mat1['baris']==mat2['baris'] and mat1['kolom']==mat2['kolom']:
        mat3={'baris':mat1['baris'],'kolom':mat1['kolom']}
        for i in range(mat1['baris']):
            for j in range(mat1['kolom']):
                if mat1.get((i,j))!=None and mat2.get((i,j))!=None:
                    mat3[(i,j)]=mat1[(i,j)]+mat2[(i,j)]
                elif mat1.get((i,j))!=None and mat2.get((i,j))==None:
                    mat3[(i,j)]=mat1[(i,j)]
                elif mat1.get((i,j))==None and mat2.get((i,j))!=None:
                    mat3[(i,j)]=mat2[(i,j)]
        return mat3
    else:
        return 'tidak sesuai'

def dispSparseMatriks(dictData):
    temp=''
    for i in range(dictData['baris']):
        for j in range(dictData['kolom']):
            if dictData.get((i,j))==None:
                temp=temp+str(0)+' '
            else:
                temp=temp+str(dictData.get((i,j)))+' '
        temp=temp+'\n'
    print(temp)

mat1=createSparseMatriks(4,5)
print(mat1)
dispSparseMatriks(mat1)
mat2=createSparseMatriks(4,5)
print(mat2)
dispSparseMatriks(mat2)
jum=addSparseMat(mat1, mat2)
print(jum)
dispSparseMatriks(jum)