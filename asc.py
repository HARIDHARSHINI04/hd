f=int(input()
z=list(map(int,input().split()))
for i in z:
  if(z[i]>z[i+1]):
    print(i)
    break;
