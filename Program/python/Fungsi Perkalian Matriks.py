def perkalianMat(mat1,mat2):
    xmat=[]
    if len(mat1[0])==len(mat2):
        for i in range(len(mat1)):
            mat=[]
            for j in range(len(mat2[0])):
                tambah=0
                for k in range(len(mat1[0])):
                    kali=mat1[i][k]*mat2[k][j]
                    tambah+=kali
                mat.append(tambah)
            xmat.append(mat)
        return xmat
    elif len(mat2[0])==len(mat1):
        for i in range(len(mat2)):
            mat=[]
            for j in range(len(mat1[0])):
                tambah=0
                for k in range(len(mat2[0])):
                    kali=mat2[i][k]*mat1[k][j]
                    tambah+=kali
                mat.append(tambah)
            xmat.append(mat)
        return xmat

mat2=[[2,1],[1,-1]]
mat1=[[-1,1,2],[2,0,-1]]
print(perkalianMat(mat1, mat2))