'''
Gauss Jordan elimination 
->Forward elimination
'''

import numpy as np
n=int(input("Enter nth terms\n"))
mat=np.zeros((n,n+1))
x=np.zeros(n)
for i in range(n):
  for j in range(n+1):
    mat[i][j]=float(input())
for i in range(n):
  for j in range(n):
    if i!=j:
      u=mat[j][i]/mat[i][i]
      for k in range(n+1):
        mat[j][k]=mat[j][k]-u*mat[i][k]
for i in range(n):
  x[i]=mat[i][n]/mat[i][i]
   
for i in range(n):
  print(x[i],end="\t")