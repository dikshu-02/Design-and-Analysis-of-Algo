def issafe(mat,r,c):
    for i in range(r):
        if mat[i][c]=='Q':
            return False

    i,j=r,c
    while(i>=0 and j>=0):
        if (mat[i][j]=='Q'):
            return False
        i=i-1
        j=j-1

    i,j=r,c
    while(i>=0 and j<len(mat)):
        if (mat[i][j]=='Q'):
            return False
        i=i-1
        j=j+1
        
    return True
    
def printsoln(mat):
    for row in mat:
        print(" ".join(row))
    print()
    

def nqueens(mat,r):
    if r==len(mat):
        printsoln(mat)
        return

    for i in range(len(mat)):
        if issafe(mat,r,i):
            mat[r][i]='Q'
            nqueens(mat,r+1)
            mat[r][i]='-'


n=int(input("Enter number of queens:"))
mat=[['-' for x in range(n)] for y in range(n)]
nqueens(mat,0)
