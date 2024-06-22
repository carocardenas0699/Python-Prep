
import sys
import datetime

if len(sys.argv)==4:
    t=sys.argv[1]
    h=int(sys.argv[2])
    ll=sys.argv[3]
    fh=int(datetime.datetime.timestamp(datetime.datetime.now()))
   
    if h<0 or h>100:
        print('El valor de Humedad no es valido')
    elif ll!='True' and ll!='False':
        print('El valor de Lluvia no es valido')
    else:
        b=open('clase09_ej2.csv','a')
        b.write(f'\n{fh}, {sys.argv[1]}, {sys.argv[2]}, {sys.argv[3]}')
        b.close()
        print(fh)
        print(f'Temperatura: ',t, 'Humedad:',h, 'Lluvia:',ll)

else:
    print('Debe ingresar valores para Temperatura (C), Humedad (%) y Lluvia (True/False)')

