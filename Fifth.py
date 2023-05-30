n1=int(input("Enter number of first list items"))
n2=int(input("Enter number of second list items"))
mainstream=[]
must_watch=[]
for i in range(n1):
    mainstream.append(input())
for i in range(n2):
    must_watch.append(input())
temp1=set(mainstream)
temp2=set(must_watch)
print(list(temp1&temp2),",",list(temp1^temp2))