ft=input()
if(len(ft)%2==0):
  ft[int(len(ft)/2)]='*'
  ft[int(len(ft)/2-1]='*'
else:
  ft[int(len(ft)/2]='*'
for k in range(0,len(fk)):
  print(ft[k],end=" ")
