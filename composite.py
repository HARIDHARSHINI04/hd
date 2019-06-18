y=input()
if(y>0):
 for z in range(2,y):
    if(y%z==0):
       print("no")
       break;
    else:
       print("yes")
else:
  print("no")
