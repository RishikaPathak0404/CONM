import numpy as np
n = int(input('Enter number of data points: '))
x = np.zeros((n))
y = np.zeros(n)
d=np.zeros((n,n))
for i in range(n):
    x[i] = float(input('x='))
    y[i]= float(input('y='))
for j in range(1,n):
    for i in range(0,n-j):
      if j==1:
        d[i][j]=y[i+1]-y[i]
      else:
        d[i][j] = d[i+1][j-1] - d[i][j-1]
for i in range(0,n):
    for j in range(1, n-i):
        print('\t\t%0.2f' %(d[i][j]), end='')
    print()