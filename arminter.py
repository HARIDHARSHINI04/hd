a=int(input())
b=int(input())
for n in range(a+1,b-1):
   order=len(str(n))
   temp=n
   sum=0
   while(temp>0):
     dig=temp%10
     sum=sum+dig**order
     temp=temp//10
     if(n==sum):
       print(n)
