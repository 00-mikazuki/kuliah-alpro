def sumList(data):
    if len(data)==1:
        return data[0]
    else:
        print(data[:-1],'+',data[-1])
        total=data[-1]+sumList(data[:-1])
        return total

dataList=[4]
print(sumList(dataList))