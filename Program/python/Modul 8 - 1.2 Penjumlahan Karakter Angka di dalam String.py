def sumStringDigit(strNum):
    if strNum.isdigit():
        if len(strNum)==1:
            return int(strNum[0])
        else:
            total=int(strNum[-1])+sumStringDigit(strNum[:-1])
            return total
    else:
        return 'Tidak dapat dikonversi menjadi angka'

strNum='4'
print(sumStringDigit(strNum))