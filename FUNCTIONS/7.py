def isPalindrome(num):
    a = str(num)
    b = a[::-1]
    return "Yes" if a == b else "No"

print(isPalindrome(141))