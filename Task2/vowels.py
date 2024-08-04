string=str(input("enter a string"))
def vowel():
    c=0
    v=['A','E','I','O','U','a','e','i','o','u']
    for i in string:
        if i in v:
            c+=1
    print("Count of vowel",c)
vowel()