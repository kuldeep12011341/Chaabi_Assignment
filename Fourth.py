n=int(input("Enter number of dict pairs: "))
Dic={}
for i in range(n):
    stringTemp=input()
    Dic[stringTemp.split(":")[0]]=stringTemp.split(":")[1]
for k,v in Dic.items():
    Dic[v]=k
    del Dic[k]
print(Dic)
    