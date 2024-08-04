a=[2,4,6,7,9,5]
def large():
  max=a[0]
  for i in a:
    if i>max:
        max=i
    print(max)
large()