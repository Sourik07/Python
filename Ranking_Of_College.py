from array import *
facilities,academics,infrastructure,total=[],[],[],[]
result={}
#taking value from the user
for i in range(0,10):
    print("\nEnter details of college -")
    clg=input("College Name: ")
    print("Facilities: ")
    f=int(input())
    if f<=25:
        facilities.append(f)
    else:
        print("The entered values is greater than max score allowed (25)")
    print("Academics: ")
    a=int(input())
    if a<=50:
        academics.append(a)
    else:
        print("The entered value is greater than max score allowed (50)")
    print("Infrastructure: ")
    i=int(input())
    if i<=25:
        infrastructure.append(i)
    else:
        print("The entered values is greater than max score allowed (25)")
    sum=f+a+i
    total.append(sum)
    #creating a distionary for ranking college name with total score
    result[int(sum)]=clg
#sorting the result array in descending order
total.sort(reverse=True)
#displaying in desc order
for i in total:
    value=result.get(i)
    print("\n",i,"=>", value)