#REGISTRO COVID
pctg=0
op='0'
pmec=0
por=0
p=0
datos=[]
print("BIENVENIDO AL REGISTRO DE COVID (esperemos tener 0 contagiados)")
print("Las últimas cifras nos indican que tenemos una tendencia a la ALTA")
print("Por favor trata de quedarte en casa, y de ser necesario salir, tomas las precauciones sanitarias")
p=input("ingresa el numero de registros que realizarás: ")
#aquí me abrirá un menú con 2 opciones
while(op!='2') :
    print(" 1)Ingresar Datos\n 2)Salir para calcular")
    op=input("Elige una opción: ")
    if op=='1':
        ed=input("Edad de la persona: ")
        rcv=input("Rango COVID [0-1] ")
        if float(rcv)>=0.8:
#Lo que hago aquí es que si el paciente es Rango Covid (positivo)
#preguntarle los síntomas que presenta, y así decirle si sus síntomas son alarmantes o comunes
            print("De los siguientes grupos de síntomas, a cual perteneces?")
            print("Grupo 1:\nfiebre,Tos seca,cuerpo cortado,dolor de cabeza")
            print("Grupo 2:\nDificultad al respirar,Sensación de falta de aire,Dolor de Pecho,Incapacidad para moverse")
            while(op!='c'):
                print(" a)Grupo 1\n b)Grupo 2")
                op=input("Elige una opción: ")
                if op=='a':
                    print("Sus síntomas son los más comunes, son tratables bajo medicación. Tiene probabilidad de tratarse en casa, aún asi visite a un médico")
                    op='c'
                elif op=='b':
                    print("Los síntomas que presenta son de los mas alarmantes, favor de acudir a un médico PRONTO")
                    print("Tiene probabilidades de ser hospitalizado ;")
                    op='c'
                else:
                    print("error, opcion no valida")
            pctg=pctg+1
            pmec=pmec+int(ed)
        reg=ed+','+rcv+'\n'
        datos.append(reg)
#hasta que yo no seleccione la opión 2, no podré parar de ingresar datos, y calcular.
    elif op=='2':
        print("Gracias por tu preferencia")
    else:
#cualquier otro valor que no sea 2, será error
        print("Error, opción no válida")
print (datos)#aquí me imprime los datos de forma horizontal
#aqui genero mi base de datos en excel
a=open("bd.csv","a")
a.writelines(datos)
a.close()
por=int(pctg)*100/int(p)
if por==0:
    print("El semaforo es verde. No hay infectados, puedes salir!!! (de prefencia siguete protegiendo) ")
elif por>=1 and por<=25:
    print("El semaforo se encuentra en amarillo")
    print("El promedio de los contagios, de acuerdo con los registros que se hicieron fue",por,"%")
    print("favor de tomar las medidas sanitarias correspondientes")
elif por>=26 and por<=50 :
    print("El semaforo se encuentra en naranja")
    print("El promedio de los contagios, de acuerdo con los registros que se hicieron fue",por,"%")
    print("favor de tomar las medidas sanitarias correspondientes, de ser necesario visite a un médico")
elif por>=51 and por<=100:
    print("El semaforo se encuentra en rojo, por favor no salga")
    print("El promedio de los contagios, de acuerdo con los registros que se hicieron fue",por,"%")
    print("favor de tomar las medidas sanitarias correspondientes, acudan al médico!!!") 
