def koordinatY(x,m,c):
    y=[m*xi+c for xi in x]
    return y

x=[3,4,1,2,5]
y=koordinatY(x,2,4)
print(x)
print(y)

print('')

x=[3,4,1,2,5]
y=koordinatY(x,3,2)
print(x)
print(y)