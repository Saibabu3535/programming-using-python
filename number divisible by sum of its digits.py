def divisible_by_sum(number):
    num=0
    temp=number
    while(number):
      rem=number%10
      number=number//10
      num=num+rem
    if(temp%num==0):
      return True
    else: 
      return False
    
number=42
print(divisible_by_sum(number))
