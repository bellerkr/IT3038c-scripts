lowlimit = int(input("Enter the low end of the range: "))
highlimit = int(input("enter the high end of the range: "))

for k in range(lowlimit, highlimit+1):
    if(k%2!=0):
        print(k)
