def add_string(str1):
  if(len(str1)>2):
   if(str1[-3:]=="ing"):
     str2=str1+"ly"
     return str2
   else:
     str3=str1+"ing"
     return str3
  else:
   return str1
str1="com"
print(add_string(str1))
