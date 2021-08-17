#REGISTRO COVID
pctg=0
op='0'
pmec=0
datos=[]
print("BIENVENIDO AL REGISTRO DE COVID (esperemos tener 0 contagiados)")
#aquí me abrirá un menú con 2 opciones
while(op!='2') :
	print(" 1)Ingresar Datos\n 2)Salir para calcular")
	op=input("Elige una opción: ")
	if op=='1':
		ed=input("Edad de la persona: ")
		rcv=input("Rango COVID [0-1] ")
		if float(rcv)>=0.8:
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
pmec=pmec+int(ed)
if pctg==0:
	print("El semaforo es verde. No hay infectados, puedes salir!!! (de prefencia siguete protegiendo) ")
elif pctg>=1 and pctg<=30:
	print("El semaforo se encuentra en amarillo")
	print("El número de infectados es",pctg,"favor de tomar las medidas sanitarias correspondientes")
elif pctg>=31 and pctg<=70 :
	print("El semaforo se encuentra en naranja")
	print("El número de infectados es",pctg,"favor de tomar las medidas sanitarias correspondientes, de ser necesario visite a un médico")
elif pctg>=71 and p<=100:
	print("El semaforo se encuentra en rojo, por favor no salga")
	print("El número de infectados es",pctg,"favor de tomar las medidas sanitarias correspondientes, acudan al médico!!!") 
pmec=pmec/pctg 
print("El promedio de edad de los contagiados es ",pmec)