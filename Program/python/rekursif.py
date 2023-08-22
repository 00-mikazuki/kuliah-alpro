# def deret(a,b,n):
#     if n==1:
#         return a
#     else:
#         un=b+deret(a,b,n-1)
#         return un

# a=2
# b=4
# n=6
# hasil=deret(a,b,n)
# print(f"suku ke {n} adalah {hasil}")

x = int(input('Masukkan Bilangan = '))
n = int(input('Masukkan pangkat = '))
def expNumber (x,n) :
    if n == 0 :
        return 1
    else :
        pangkat = x * expNumber (x,n-1)
        return pangkat
hasil = expNumber (x,n)
print(x,' pangkat ',n,' = ',hasil)