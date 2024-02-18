"""
Assumptions:
 solved for the equation : x^2-x-1
""" 
def f(x):
  return ((x*x)-x-1) 
a=float(input("Enter \"a\" value\n"))
b=float(input("Enter \"b\" value\n"))
e=float(input("Enter error\n"))
if((f(a)*f(b))>0):
  print("Invalid intervals")
else:
  m=(a+b)/2
  i=1
try :
   while(f(abs(f(m)))<e):
     print(i,a,b,m,f(m),f(a)*f(m))
     if((f(a)*f(m))>0):
       a=m
     else:
       b=m
     m=(a+b)/2
     i=i+1
     if i==50:
      break
   print(i,a,b,m,f(m),f(a)*f(m))
   print("Root are",m)
except:
  print("can\'t finding root" )