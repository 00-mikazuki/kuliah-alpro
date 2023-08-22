def create2D(baris,kolom):
    list2D=[]
    for i in range(baris):
        isi=[]
        for j in range(kolom):
            temp='list ['+str(i)+','+str(j)+'] : '
            isi.append(int(input(temp)))
        list2D.append(isi)
    return list2D

matriks1=create2D(2,3)
print('matriks1 = ',matriks1)