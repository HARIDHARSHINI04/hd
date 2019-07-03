f=input()
h=1
for d in range (len(f)-1):
  ph=f[d]+f[d+1]
  m=int(ph)
  if m<=26 and f[d]!="0":
      h+=1
if h==3:
  print(h)
else:
  print(h+(h-1)//2)
