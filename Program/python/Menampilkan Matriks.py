# def createMat2D(baris,kolom):
#     list2D=[]
#     dataPrint='|\t'
#     for i in range(baris):
#         isi=[]
#         for j in range(kolom):
#             temp='list ['+str(i)+','+str(j)+'] : '
#             add=int(input(temp))
#             isi.append(add)
#             dataPrint=dataPrint+str(add)+'\t'
#         dataPrint=dataPrint+'|'
#         list2D.append(isi)
#     return dataPrint

# def createMat2D(baris,kolom):
#     list2D=[]
#     for i in range(baris):
#         isi=[]
#         for j in range(kolom):
#             temp='list ['+str(i)+','+str(j)+'] : '
#             isi.append(int(input(temp)))
#         list2D.append(isi)
#     return list2D

# def displayMat2D(mat,ketik):
#     print(ketik)
#     for i in range(len(mat)):
#         matprint='|\t'
#         for j in range(len(mat[i])):
#             matprint=matprint+str(mat[i][j])+'\t'
#         matprint=matprint+'|'
#         print(matprint)

# def displayMat2D2(mat,ketik):
#     matprint=ketik+'\n'
#     for i in range(len(mat)):
#         matprint+='|\t'
#         for j in range(len(mat[i])):
#             matprint+=str(mat[i][j])+'\t'
#         matprint+='|\n'
#     print(matprint)

# matriks1=createMat2D(2, 3)
# print(matriks1)
# print(displayMat2D2(matriks1,'Matrik1 = '))

def sumList(data):
    if len(data)==1:
        return data[0]
    else:
        print(data[:-1],'+',data[-1])
        total=data[-1]+sumList(data[:-1])
        return total

dataList=[1,2,3]
print(sumList(dataList))