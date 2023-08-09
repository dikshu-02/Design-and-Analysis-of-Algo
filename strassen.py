import numpy as np
def split(matrix):
    row,col=matrix.shape
    row2, col2 = row//2, col//2
    return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]

def strassen(x,y):
    if len(x)==1 or len(y)==1:
        return x*y

    a00,a01,a10,a11=split(x)
    b00,b01,b10,b11=split(y)

    m1=strassen((a00+a11),(b00+b11))
    m2=strassen((a10+a11),b00)
    m5=strassen((a00+a01),b11)
    m3=strassen((b01-b11),a00)
    m4=strassen((b10-b00),a11)
    m6=strassen((a10-a00),(b00+b01))
    m7=strassen((a01-a11),(b10+b11))

    c00=m1+m4-m5+m7
    c01=m3+m5
    c10=m2+m4
    c11=m1+m3-m2+m6

    c=np.vstack((np.hstack((c00,c01)),np.hstack((c10,c11))))
    return c

a=[]
b=[]
rc=int(input("Enter the no of rows"))
for i in range(rc):
    temp=[]
    temp=input().split()
    for j in range(rc):
        temp[j]=int(temp[j])
    a.append(temp)

for i in range(rc):
    temp=[]
    temp=input().split()
    for j in range(rc):
        temp[j]=int(temp[j])
    b.append(temp)

x=np.array(a)
y=np.array(b)
print("The resultant matrix is\n ",strassen(x,y))

