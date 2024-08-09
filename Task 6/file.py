fc=open("file.txt","x")
fw=open("file.txt","w")
Names=["Anu","Ammu","Achu"]
for name in Names:
    fw.write( name + '\n')
fr=open("file.txt","r")
r=fr.readlines()
print(r)
