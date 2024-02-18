"""
Assumptions:
 solved for the equation : x^2-x-1
""" 
def f(x):
  return ((x*x)-x-1) 
a=float(input("Enter \"a\" value\n"))
b=float(input("Enter \"b\" value\n"))
e=float(input("Enter error\n"))
m=(a*f(b)-b*f(a))/(f(b)-f(a))
i=1
try :
   while(f(abs(f(m)))<e):
     print(i,a,b,m,f(m))
     a=b
     b=m
     if (f(b)-f(a)==0):
      break
     m=(a*f(b)-b*f(a))/(f(b)-f(a))
     i=i+1
     if i==50:
      break
   print(i,a,b,m,f(m))
   print("Root are",m)
except:
  print("can\'t finding root" )