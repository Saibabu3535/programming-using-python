def nearest_palindrome(number):
    number=number+1
    s=str(number)
    while(s!=s[::-1]):
        number=number+1
        s=str(number)
    return number

number=0
print(nearest_palindrome(number))
