def createList(sizeList):
    listcreate=[]
    for i in range(sizeList):
        temp='Masukkan data ke - '+str(i)+' : '
        listcreate.append(int(input(temp)))
    return listcreate

def isPrime(bil):
    pembagi=0
    if bil>=2:
        for i in range(1,bil+1):
            if bil%i==0:
                pembagi+=1
        if pembagi==2:
            return True
        else:
            return False
    else:
        return False

def createListPrime(list):
    listPrime=[]
    for n in list:
        prime=isPrime(n)
        if prime==True:
            if n not in listPrime:
                listPrime.append(n)
    return listPrime

data=createList(10)
print('data list = ',data)
prima=createListPrime(data)
print('data prima = ',prima)