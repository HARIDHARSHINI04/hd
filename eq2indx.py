f=int(input())
z=list(map(int,input().split()))
i=[]
for h in range(0,int(len(z))):
  if(h=z[h]):
    i.append(h)
if(int(len(i)))!=0:
    for s in i:
      print(s,end=" ")
else:
   print(-1)
     
