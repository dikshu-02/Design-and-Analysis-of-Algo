#merge sort
def merge(a,l,r):
    i=0
    j=0
    k=0
    while(i<len(l)) and (j<len(r)):
        if(l[i]<r[j]):
            a[k]=l[i]
            i=i+1
            k=k+1
        else:
            a[k]=r[j]
            j=j+1
            k=k+1
    while(i<len(l)):
        a[k]=l[i]
        i=i+1
        k=k+1
    while(j<len(r)):
        a[k]=r[j]
        j=j+1
        k=k+1
    print(a)



def sort(a,n):
    if len(a)<=1:
        return
    else:
        x=n//2 
        l=a[0:x]
        r=a[x:]
        sort(l,x)
        sort(r,n-x)
        merge(a,l,r)


a=[]
n=int(input("enter the number of elements:"))
for i in range(n):
    a.append(int(input("enter a value:")))
sort(a,n)
print(a)
        
