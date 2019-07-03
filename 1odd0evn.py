f=int(input())
x=list(map(int,input().split()))
g=[]
for a in range(0,f):
  if x[a]%2!=0 and a%2==0:
     g.append(x[a])
  elif x[a]%2==0 and a%2!=0:
     g.append(x[a])
print(*g) 
