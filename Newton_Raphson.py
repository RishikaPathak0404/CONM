"""
Assumptions:
 solved for the equation : x^2-x-1
""" 
def f(x):
  return ((x*x)-x-1)
def f1(x1):
  return (2*x1-1) 
b=float(input("Enter \"b\" value\n"))
e=float(input("Enter error\n"))
if(f(b)==0):
  print("Invalid intervals")
else:
  m=b-(f(b)/f1(b))
  i=1
try :
   while(f(abs(f(m)))<e):
     print(i,b,m,f(m))
     b=m
     m=b-(f(b)/f1(b))
     i=i+1
     if i==50:
      break
   print(i,b,m,f(m))
   print("Root are",m)
except:
  print("can\'t finding root" )