from datetime import date,timedelta
def function(dateGiven,n):
    dateTemp=dateGiven.split('-')
    dateStamp=date(2000+int(dateTemp[0]),int(dateTemp[1]),int(dateTemp[2]))
    return dateStamp-timedelta(days=n)
inputDate=input()
n=int(input())
newDate=str(function(inputDate,n))
print(newDate[2::])