def line():
    A=float(input('Ingrese el coeficiente A: '))
    B=float(input('Ingrese el coeficiente B: '))
    X1=float(input('Ingrese el coeficiente X1: '))
    X2=float(input('Ingrese el coeficiente X2: '))
    print('El coeficiente A de su ecuación de la recta es:',A)
    print('El coeficiente B de su ecuación de la recta es:',(B))
    print('El coeficiente X1 de su ecuación de la recta es:',(X1))
    print('El coeficiente X2 de su ecuación de la recta es:',(X2))
    print('')
    print('Para la siguiente ecuación:\n\tY =',str((A))+'X','+',str((B)))
    print('')
    print('Dados los siguientes puntos:')
    Y1=(A)*(X1)+(B)
    Y2=(A)*(X2)+(B)
    print('\tP1 ('+str((X1))+',',str(Y1)+')')
    print('\tP2 ('+str((X2))+',',str(Y2)+')')
    print('')
    distancia=(((X2-X1)**2)+((Y2-Y1)**2))**(1/2)
    print('La distancia entre ellos es:',distancia)
    
