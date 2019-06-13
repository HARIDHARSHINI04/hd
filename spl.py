a=input()
c=0
count=0
for i in range(0,len(a)):
  if a[i].isdigit() or a[i].isalpha() or a[i]== " ":
      c+=1
  else:
      count+=1
print(count)
