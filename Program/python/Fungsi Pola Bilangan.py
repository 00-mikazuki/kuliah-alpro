def polaBilangan(n):
    a1=1
    a2=0
    for i in range(n):
        jumlah=a1+a2
        a2=a1
        a1=jumlah
    return jumlah

print(polaBilangan(4))