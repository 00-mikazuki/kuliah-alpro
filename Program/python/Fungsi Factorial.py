# def factorial(x):
#     kali=1
#     for i in range(x):
#         kali=kali*x
#         x=x-1
#     return kali

# def factorial(x):
#     kali=1
#     for i in range(x,0,-1):
#         kali=kali*i
#     return kali

# def factorial(x):
#     if x==1:
#         return x
#     else:
#         kali=x*factorial(x-1)
#         return kali

def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))

print(factorial(4))