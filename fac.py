n=int(input())
fac=1
if(n<0):
  print("does not exist")
elif(n==0):
  print("1")
else:
  for i  in range(1,n+1):
     fac=fac*i
  print(fac)
     
