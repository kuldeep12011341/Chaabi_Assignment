file=input('String for file types:')
n=int(input('number of files: '))
filenames=[]
for i in range(n):
    filenames.append(input())
tempList=list(file.split(";"))
typeDict={}
for i in tempList:
    strSplit=i.split(",")
    typeDict[strSplit[0]]=strSplit[1]
ansDict={}
for i in filenames:
    ansDict[i]="unknown"
    if "." in i and i.split(".")[1] in typeDict:
        ansDict[i]=typeDict[i.split(".")[1]]
print(ansDict)