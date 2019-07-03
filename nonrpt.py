f=int(input())
z=list(map(int,input().split()))
for s in range (len(z)):
  if z.count(z[s])==1:
     print(z[s])
