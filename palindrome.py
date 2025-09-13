def Palindrome(x):
    s=str(x)
    rev=s[::-1]
    if(s==rev):
        return True
    else:
        return False
x=int(input())
print(Palindrome(x))
