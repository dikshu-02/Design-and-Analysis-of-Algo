n=int(input("Enter the number of items"))
w=int(input("Enter the maximum capacity"))
array=[]
for i in range(n):
    x=int(input("W"+str(i+1)+":"))
    y=int(input("V"+str(i+1)+":"))
    wbyv=y/x
    temp=[x,y,wbyv]
    array.append(temp)

print(array)
for i in range(n):
    maxi=i
    for j in range(i+1,n):
        if (array[maxi][2]<array[j][2]):
            maxi=j
    temp=array[i]
    array[i]=array[maxi]
    array[maxi]=temp

print(array)
cap=0
max_val=0
for i in range(n):
    if (cap+array[i][0]<=w):
        cap+=array[i][0]
        max_val+=array[i][1]
        print(max_val)
    else:
      break

max_val+=(((w-cap)/(array[i][0]))*(array[i][1]))
print("The maximum value is",max_val)
