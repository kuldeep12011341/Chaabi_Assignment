from datetime import date
def solve(from_date,to_date,diff):
    fromTemp=from_date.split('-')
    toTemp=to_date.split('-')
    fromDate=date(2000+int(fromTemp[0]),int(fromTemp[1]),int(fromTemp[2]))
    toDate=date(2000+int(toTemp[0]),int(toTemp[1]),int(toTemp[2]))
    difference=toDate-fromDate
    return (difference.days<diff)
from_date=input()
to_date=input()
diff=int(input())

print(solve(from_date,to_date,diff))