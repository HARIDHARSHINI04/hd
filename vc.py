n=input()
if(n=='a' or n=='e' or n=='i' or n=='o' or n=='u' or n=='A' or n=='E' or n=='I' or n=='O' n=='U'):
   print("vowel")
elif n in('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'):
   print("consonant")
else:
   print("invalid")
