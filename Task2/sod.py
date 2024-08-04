
def sod(num):
    s=0
    while num>0:
        s+=num %10
        num //=10
    print("Sum of digit",s)
sod(123)