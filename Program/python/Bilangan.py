def penjumlahan(n1,n2):
    penj=n1+n2
    print(penj)
    return penj

def bilprima(n):
    pembagi=0
    if n>=2:
        for i in range(1,n+1):
            if n%i==0:
                pembagi+=1
        if pembagi==2:
            print(n,'adalah bilangan prima')
        else :
            print(n,'bukan bilangan prima')
    else:
        print(n,'bukan bilangan prima')

def cekGanjilGenap(n):
    if n%2==0:
        print(n,'adalah bil genap')
    else:
        print(n,'adalah bil ganjil')

def listPembagi(n):
    pembagi=[]
    bkn=[]
    for i in range(1,n+1):
        if n%i==0:
            pembagi.append(i)
        else:
            bkn.append(i)
    print(pembagi)
    print(bkn)