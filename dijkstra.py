
def dijkstra(g,n,start,end):
    distance=[ 99999 for i in range(n)]
    visited=[0 for i in range(n)]
    pred=[-1 for i in range(n)]

    for i in range(n):
        for j in range(n):
            if(g[i][j]==0):
                g[i][j]=99999
    for i in range(n):
        distance[i]=g[start][i]
        pred[i]=start

    visited[start]=1
    distance[start]=0
    pred[start]=0
    nextnode=start
    for i in range(n):
        minimum=99999
        #nextnode=start
        for j in range(n):
            #print(visited[j],distance[j])
            if(visited[j]==0 and minimum>distance[j]):
                minimum=distance[j]
                nextnode=j

        visited[nextnode]=1

        for j in range(n):
            if(visited[j]==0 and minimum+g[nextnode][j]<distance[j]):
                distance[j]=g[nextnode][j]+minimum
                pred[j]=nextnode
        
    if(visited[end]==0):
        print("NO path")
    else:
        i=end
        while(i!=start):
            print(i,end=" ")
            i=pred[i]

    print("DISTANCE")
    print(distance)

g=[]
n=int(input("enter the number of vertices:"))
for i in range(n):
    temp=input().split()
    for i in range(n):
        temp[i]=int(temp[i])
    g.append(temp)

start=int(input("enter the start vertex:"))
end=int(input("enter the end vertex:"))
dijkstra(g,n,start,end)
