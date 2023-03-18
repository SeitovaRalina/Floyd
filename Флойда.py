import math

def printMatrix ( matrix ):
   for i in range ( len(matrix) ):
      for j in range ( len(matrix[i]) ):
          print ( "{:4d}".format(matrix[i][j]), end = "" )
      print ()

i = math.inf
g = [[0, 7, i, i, i, i],
     [i, 0, 2, i, 9, i],
     [i, i, 0, 1, 3, 11],
     [i, i, i, 0, i, 5],
     [13, i, i, 3, 0, 5],
     [i, i, i, i, i, 0]]

g = [[0, 8, 5],
     [3, 0, i],
     [i, 2, 0]]

g = [[0, 10, 18, 8, i, i],
     [10, 0, 16, 9, 21, i],
     [i, 16, 0, i, i, 15],
     [7, 9, i, 0, i, 12],
     [i, i, i, i, 0, 23],
     [i, i, 15, i, 23, 0]]
n = len(g)
p =[[i for i in range(n)] for j in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if g[i][j] > g[i][k] + g[k][j]:
                g[i][j] = g[i][k] + g[k][j]
                p[i][j] = k
printMatrix(g)
print('-'*30)
for i in range(n):
    for j in range(n):
        start = i
        end = j
        path = [start+1]
        while start != end:
            start = p[start][end]
            path.append(start+1)
        print(f'{i+1} -> {j+1} : путь = {path}, значение = {g[i][j]}')
