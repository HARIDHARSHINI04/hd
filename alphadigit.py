v=input()
p=False
h=False
for i in v:
  if(i.isalpha()):
    p=True
  if(i.isdigit()):
    h=True
if(p==True and h==True):
  print("Yes")
else:
  print("No")
