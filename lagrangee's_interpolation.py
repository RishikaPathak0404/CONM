import numpy as np
n = int(input('Enter number of data points: '))
v=int(input("Enter the value for calculate: "))
x = np.zeros((n))
y = np.zeros(n)
for i in range(n):
    x[i] = float(input('x='))
    y[i]= float(input('y='))
sum=0.0
for i in range(n):
  l=1.0
  for j in range(n):
    if i!=j:
      l*=(v-x[j])/(x[i]-x[j])
  sum+=l*y[i]
print("the value of y at x=",v,"is",sum)