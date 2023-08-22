# def inversMat(data):
#     if len(mat)==2 and len(mat[0]==2):
#         det=data[0][0]*data[1][1]-data[0][1]*data[1][0]
#         inv=1/det
#         print(inv)
#         x=data[0][0]
#         y=data[1][1]

#         data[0][0]=y
#         data[1][1]=x

#         newMat=[]
#         for i in range(len(data)):
#             isi=[]
#             for j in range(len(data[0])):
#                 if data[i][j]==data[0][1] or data[i][j]==data[1][0]:
#                     data[i][j]=-data[i][j]
#                 kali=data[i][j]*inv
#                 isi.append(int(kali))
#             newMat.append(isi)
#         return newMat

def inversMat(data):
    if len(data)==2 and len(data[0])==2:
        a=data[0][0]
        b=data[1][1]
        c=data[0][1]
        d=data[1][0]
        seperdet=1/(a*b-c*d)
        tempMat=[[d*seperdet,(-1*b)*seperdet],[(-1*c)*seperdet,a*seperdet]]
        return tempMat


a=[[2,5],[1,3]]
print(inversMat(a))