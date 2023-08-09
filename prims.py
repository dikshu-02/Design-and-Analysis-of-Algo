INF=9999
V=int(input("Enter the numbr of vertices"))
g=[]
print("Enter the adjacency matrix")
for i in range(V):
    temp=[]
    temp=input().split()
    for i in range(V):
        temp[i]=int(temp[i])
    g.append(temp)

comp_edges=0
selected=[]
for i in range(V):
    selected.append(False)

selected[0]=True
while(comp_edges<V-1):
    minimum=INF
    for i in range(V):
        if selected[i] is True:
            for j in range(V):
                if(selected[j] is False and g[i][j]!=0):
                    if(minimum>g[i][j]):
                        minimum=g[i][j]
                        x=i
                        y=j
    print(str(x),"->",str(y),minimum)
    selected[y]=True
    comp_edges+=1

    
    
