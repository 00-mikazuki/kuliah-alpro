def maxList2D(data,jenisMax):
    listMax=[]
    if jenisMax=='kolom':
        for i in range(len(data)):
            compare=0
            for j in range(len(data[0])):
                if data[i][j]>compare:
                    compare=data[i][j]
            listMax.append(compare)
    elif jenisMax=='baris':
        for j in range(len(data[0])):
            compare=0
            for i in range(len(data)):
                if data[i][j]>compare:
                    compare=data[i][j]
            listMax.append(compare)
    return listMax

data=[[1,5,8,3],[5,2,9,2],[10,1,3,14]]
maksList=maxList2D(data,'baris')
print(data)
print(maksList)

data=[[1,5,8,3],[5,2,9,2],[10,1,3,14]]
maksList=maxList2D(data,'kolom')
print(data)
print(maksList)

data=[[1,5,8,3,11,2],[5,2,9,2,9,0],[10,1,3,14,0,20]]
maksList=maxList2D(data,'baris')
print(data)
print(maksList)

data=[[1,5,8,3,11,2],[5,2,9,2,9,0],[10,1,3,14,0,20]]
maksList=maxList2D(data,'kolom')
print(data)
print(maksList)