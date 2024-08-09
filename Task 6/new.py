f=open("NewFile.txt","r")
text=f.read()
word=text.split()
print(len(word))
f.close()

