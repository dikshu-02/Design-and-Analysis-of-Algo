
def knapsack(W,wt,v):
    n=len(wt)
    mat=[[0 for x in range(W + 1)] for x in range(n + 1)]
    for item in range(n):
        for weight in range(W+1):
            #print(item)
            if item==0 or weight==0:
                mat[item][weight]=0
            elif (wt[item]<=weight):
                mat[item][weight]=max(mat[item-1][weight] , v[item]+mat[item-1][weight-wt[item]])
            else:
                mat[item][weight]=mat[item-1][weight]
    
    print("the final profit is ",mat[n-1][W])

    
n=int(input("enter the number of items"))
W=int(input("Enter the capacity"))
wt=[]
v=[]
wt.append(0)
v.append(0)
wt.extend(input("Enter weight values").split())
v.extend(input("Enter values values").split())
#print(wt)
for i in range(n+1):
    wt[i]=int(wt[i])

for i in range(n+1):
    v[i]=int(v[i])
    
knapsack(W,wt,v)
