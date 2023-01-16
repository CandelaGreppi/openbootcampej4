def Bisiesto(year):
    if year % 4 != 0:
        print("No Bisiesto")
    elif year % 4 == 0 & year % 100 !=0:
        print("Bisiesto")
    elif year % 4 == 0 & year % 100 == 0 & year % 400 !=0:
        print("No es Bisiesto")
    elif year % 4 == 0 & year % 100 == 0 & year % 400 ==0:
        print("Bisiesto")
        

Bisiesto(1989)