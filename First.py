n=int(input("Enter Number of Element " ))
arr=[]
for i in range(n):
    arr.append(int(input()))
for i in range(1,len(arr)):
    for j in range(i-1,-1,-1):
        if arr[j+1]<arr[j]:
            temp=arr[j+1]
            arr[j+1]=arr[j]
            arr[j]=temp
        else:
            break
print(arr)