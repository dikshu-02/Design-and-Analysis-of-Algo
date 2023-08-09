INF=9999
total=0
#minimum=9999
def find(u):
    while(parent[u]!=0):
        u=parent[u]
    return  u

def union(u,v):
    if(u!=v):
        parent[v]=u
        return True
    return False


def kruskal(cost,n):
    ne=1
    total=0
    while(ne<n):
        minimum=INF
        for i in  range(n):
            for j in range(n):
                if(minimum>cost[i][j]):
                    minimum=cost[i][j]
                    a,u=i,i
                    b,v=j,j
        #print(u)
        print((a,b))
        u=find(u)
        v=find(v)
        if(union(u,v)):
            print(ne,a,b,minimum)
            total+=minimum
            ne+=1
            #print(ne)
            print(parent)
        cost[a][b]=cost[b][a]=999

    print("Minimum cost:",total)



    
V=int(input("Enter the numbr of vertices"))
g=[]
ne=0
global parent
parent=[0 for i in range(V)]
print("Enter the adjacency matrix")
for i in range(V):
    temp=[]
    temp=input().split()
    for i in range(V):
        temp[i]=int(temp[i])
    g.append(temp)
for i in range(V):
    for j in range(V):
        if(g[i][j]==0):
            g[i][j]=9999
print(parent)
kruskal(g,V)

                
