#buat matriks
def createMat2D (baris,kolom) :
    matriks = [ ]
    for i in range (baris) :
        isi = [ ]
        for y in range (kolom) :
            mat = int(input('matrik[' + str(i) + ',' + str(y) + ']= '))
            isi.append(mat)
        matriks.append(isi)
    return matriks
#nampilin matriks
def dispMat2D (matr,strmatr) :
    print (strmatr)
    if matr == False :
        print ('Ukuran Matriks Tidak Sama')
    else :
        for z in range (len(matr)) :
            print ('|',end='')
            for a in range (len(matr[1])) :
                data = str(matr[z][a])
                print (' '*(5-len(data))+ data,end='')
            print('    |')

print ('Create Mat 1')
matriks1 = createMat2D(2,3)
print ('Create Mat 2')
matriks2 = createMat2D(2,3)
dispMat2D(matriks1,'Matrik1 =')
dispMat2D(matriks2,'Matrik2 = ')