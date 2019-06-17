v=input()
p=False
h=False
for i in v:
  if(i.isalpha()):
    p=True
  if(i.digit()):
    h=True
if(p==True and h==True):
  print("yes")
else:
  print("no")
