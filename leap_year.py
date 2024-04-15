def leap_year():
    a=int(input())
    #print('Ingrese un año:',a)
    if a%4==0 and a%100==0 :
        if a%400==0 :
            print('El año',a,'es bisiesto')
        elif a%400!=0 :
            print('El año',a,'no es bisiesto')
    elif a%4==0 :
        print('El año',a,'es bisiesto')
    elif a%4!=0 :
        print('El año',a,'no es bisiesto')
