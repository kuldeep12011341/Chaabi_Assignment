n=int(input("Enter number of elements: "))
list=[]
for i in range(n):
    list.append(int(input()))
start=int(input())
end=int(input())
x=list[start:end+1:2]
print(x)