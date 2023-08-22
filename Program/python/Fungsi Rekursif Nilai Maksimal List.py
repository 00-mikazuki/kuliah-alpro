# def maksList(data): #data dari awal
#     if len(data)==1:
#         return data[0]
#     else:
#         if data[0]>maksList(data[1:]):
#             return data[0]
#         else:
#             return maksList(data[1:])

def maksList(data): #data dari akhir
    if len(data)==1:
        return data[0]
    else:
        if data[-1]>maksList(data[:-1]):
            return data[-1]
        else:
            return maksList(data[:-1])

data=[3,1,10,7,8,12,4]
print(maksList(data))