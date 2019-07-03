f=int(input())
k=list(map(int,input().spilt()))
s=''
for i in k:
   if i in s and i!=" ":
     print(int(i))
     break
   else:
     s+=i
if(s==k):
  print("unique")
   
