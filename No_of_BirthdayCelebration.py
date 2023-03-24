flag="do_not_exit"
while True:
    dd=int(input("Enter date of birth:  "))
    mm=int(input("Enter month of birth: "))
    if(((mm==1 or mm==3) or (mm==5 or mm==7)) or ((mm==8 or mm==10) or mm==12) and (dd>0 and dd<=31)):
        break
    elif(((mm==4 or mm==6) or (mm==9 or mm==11)) and (dd>0 and dd<31)):
        break
    elif((mm==2 and (dd>0 and dd<=28)) or (mm==2 and (dd>0 and dd<=29))):
        break
    else:
        input("Invalid Input")
yy=int(input("Enter year of birth: "))
current_year=int(input("Enter the year: "))
if(current_year<yy):
    print("Invalid Input")
    flag="exit"

def check_yr(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
             return True
    else:
        return False

if(flag!="exit"):

    if(check_yr(yy)):
        if(dd==29):
            yr_dif=current_year-yy
            no_of_bd=yr_dif//4
            print("Number of Birthday Celebrated: ",no_of_bd)
        else:
            yr_dif=current_year-yy
            no_of_bd=yr_dif
            print("Number of Birthday Celebrated: ",no_of_bd)

    else:
        yr_dif=current_year-yy
        no_of_bd=yr_dif
        print("Number of Birthday Celebrated: ",no_of_bd)