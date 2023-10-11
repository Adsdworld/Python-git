#with open ("fichier2.txt", "r") as File:
#    for lines in File:
#        print(lines)
###
WindowsFile=open("Fileread.txt", "r", encoding='utf8')
print(WindowsFile.readlines())
WindowsFile=open("Filewrite.txt", "w", encoding='utf8')
WindowsFile=open("Fileadd.txt", "a", encoding='utf8')
WindowsFile.write("\nMaxime")

WindowsFile=open("FicLaser.txt", "r", encoding='utf8')
firstline=WindowsFile.readline()
listname=[]
word=""
for i in firstline:
    if i==',':
        listname.append(word)
        word=""
    else:
        word+=i
print(listname)

firstline=WindowsFile.readlines()
print(firstline)
listvalues=[]
word=""
for i in firstline:
    if i==',':
        listvalues.append(word)
        word=""
    else:
        word+=i
print(listvalues)

for i in range(len(listvalues)):
    #i+=4
    print(listvalues[i])


