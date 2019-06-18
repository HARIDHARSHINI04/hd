y=int(input())
if y==1:
  print("no")
elif(y>1):
 for z in range(2,y):
    if(y%z==0):
       print("yes")
       break;
    else:
       print("no")
else:
  print("no")
