a=int(input())
n1=0
n2=1
for i in range(0,a):
  print(n2,end=" ")
  p=n1+n2
  n1=n2
  n2=p
