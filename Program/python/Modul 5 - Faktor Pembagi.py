print('-in-')
bil1=int(input())
bil2=int(input())
pembagi1=[]
pembagi2=[]
pembagiSama=[]

if bil1>bil2:
    n=bil1
else:
    n=bil2

for i in range(1,n+1):
    if bil1%i==0:
        pembagi1.append(i)
    if bil2%i==0:
        pembagi2.append(i)

for j in pembagi1:
    for k in pembagi2:
        if j==k:
            pembagiSama.append(j)

print('-out-')
print(pembagi1)
print(pembagi2)
print(pembagiSama)