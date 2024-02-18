import numpy as np
def fact(n):
    f = 1;
    for i in range(2, n + 1):
        f *= i;
    return f;
def cal(u,n):
  t=u
  for i in range(1,n):
    t=t*(u+i);
  return(t)
import numpy as np
n = int(input('Enter number of data points: '))
x = np.zeros((n))
y = np.zeros(n)
d=np.zeros((n,n))
for i in range(n):
    x[i] = float(input('x='))
    y[i]= float(input('y='))
for j in range(1,n):
    for i in range(j+1,n):
      if j==1:
        d[i][j]=y[i]-y[i-1]
      else:
        d[i][j] = d[i][j-1] - d[i-1][j-1]
for i in range(1,n):
    for j in range(1, i+1):
        print('\t\t%0.2f' %(d[i][j]), end='')
    print()
v=int(input("enter the value to calculate:\n"))
h=x[1]-x[0]
u=(v-x[n-1])/h
sum=y[n-1]
for i in range(1,n):
  sum+=(cal(u,i)*d[n-1][i])/fact(i)
print("the value of y at x=",v,"is",sum)