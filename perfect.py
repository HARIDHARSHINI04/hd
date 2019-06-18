h,k=list(map(int,input().split()))
f=h*k
for i in range(0,f+1):
  if(i**2==0):
    print("yes")
    break;
else:
  print("no")
    
