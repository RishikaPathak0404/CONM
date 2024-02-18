'''
Gaussian Elimination Technique
->Triangular phase 
->Back substitution
'''

import numpy as np
n=int(input("Enter nth terms\n"))
mat=np.zeros((n,n+1))
x=np.zeros(n)
for i in range(n):
  for j in range(n+1):
    mat[i][j]=float(input())
for i in range(n):
  for j in range(i+1,n):
    u=(mat[j][i])/(mat[i][i])
    for k in range(n+1):
      mat[j][k]=mat[j][k]-u*mat[i][k]
x[n-1]=mat[n-1][n]/mat[n-1][n-1]
for i in range(n-2,-1,-1):
  x[i]=mat[i][n]
  for j in range(i+1,n):
    x[i]=x[i]-mat[i][j]*x[j]
    x[i]=x[i]/mat[i][i]
for i in range(n):
  print(x[i],end="\t")