s=input("Enter a word")
def palindrome():
    if s==s[::-1]:
       print("palindrome")
    else:
       print("not palindrome")
palindrome()