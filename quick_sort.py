#quick sort

def partition_index(a,start,end):
    PI=start
    pivot=a[end]
    for i in range(start,end):
        if a[i]<=pivot:
            a[i],a[PI]=a[PI],a[i]
            PI=PI+1
    #print("In func 1 end start={},end={},PI={}".format(start,end,PI))
    a[PI],a[end]=a[end],a[PI]
    return PI

def quicksort(a,start,end):
    if start<end:
        PI=partition_index(a,start,end)
        quicksort(a,start,PI-1)
        quicksort(a,PI+1,end)



x=int(input("enter the number of elements"))
a=[]
for i in range(x):
    a.append(int(input("enter the "+str(i+1)+" value")))
quicksort(a,0,x-1)
print(a)
