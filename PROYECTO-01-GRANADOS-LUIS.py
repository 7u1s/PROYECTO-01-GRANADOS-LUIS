from lifestore_file import lifestore_products
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_searches
sales= lifestore_sales
products=lifestore_products
searches=lifestore_searches
categorias=["procesadores","tarjetas de video","tarjeta madre", "discos duros", "memorias usb","pantallas","bocinas","audifonos"]
#print(lifestore_sales[1][2])

print("Wake up... ")
print("The matrix has you..")
print("please sign up to access to the true")
admin="admin"
users=["client1","client2"]
clave="neo2000"
#user="admin"
#password="neo2000"
user=input("please write your user name:   ")
password=input("write the password:  ")










#--------------------mas ventas-------------------------
frec1=[] #la matriz de frecuencias
x1=0 # es el contador 
P1=1#es el id de producto
suma1=0
for n in range(len(sales)):
  #print
  if sales[n][1]==P1:
     x1+=1
     #print(x)
  else :
     frec1.append(x1)
     x1=0
     P1+=1
     #print(frec)
x1=0
masventas=[]
#producsbusque 
#print(frec1)
for y in range(len(frec1)):
  #print(y)
  #suma+=y
  if frec1[y]!=0:
    #X2=1
    #menosventas.append(y+1)
    masventas.append([products[y][1],frec1[y]]) #aqui anda mie error 
#for i in range(len(masbusquedas)):
  #print(masbusquedas[i][1])
#ordenamiento
#print(masbusquedas)
#masbusquedasordenada=masbusquedas.sort(reverse=True)
masventas_ordenados1=[]
while masventas:
  minimo1= masventas[0][1]
  #print(minimo2)
  lista_actual1=masventas[0]
  #print(lista_actual2)
  for grupo1 in masventas:
    if grupo1[1]> minimo1:
      minimo1=grupo1[1]
      lista_actual1=grupo1
  masventas_ordenados1.append(lista_actual1)
  masventas.remove(lista_actual1)


#print(masventas_ordenados1)
#-------------------mas busquedas---------------------
frec2=[] #la matriz de frecuencias
x2=0 # es el contador 
P2=1#es el id de producto
suma2=0
for n in range(len(searches)):
  #print
  if searches[n][1]==P2:
     x2+=1
     #print(x)
  else :
     frec2.append(x2)
     x2=0
     P2+=1
     #print(frec)
x2=0
masbusquedas=[]
#producsbusque 
#print(frec2)
for y in range(len(frec2)):
  #print(y)
  #suma+=y
  if frec2[y]!=0:
    #X2=1
    #menosventas.append(y+1)
    masbusquedas.append([products[y][1],frec2[y]]) #aqui anda mie error 
#for i in range(len(masbusquedas)):
  #print(masbusquedas[i][1])
  #[nombre,veces]
#ordenamiento
#print(masbusquedas)
#masbusquedasordenada=masbusquedas.sort(reverse=True)
masbusquedas_ordenados2=[]
while masbusquedas:
  minimo2= masbusquedas[0][1]
  #print(minimo2)
  lista_actual2=masbusquedas[0]
  #print(lista_actual2)
  for grupo2 in masbusquedas:
    if grupo2[1]> minimo2:
      minimo2=grupo2[1]
      lista_actual2=grupo2
  masbusquedas_ordenados2.append(lista_actual2)
  masbusquedas.remove(lista_actual2)


#print(masbusquedas_ordenados2)
#----------------------------menos ventas-----------



frec3=[] #la matriz de frecuencias
x3=0 # es el contador 
P3=1#es el id de producto
suma3=0
for n in range(len(sales)):
  #print
  if sales[n][1]==P3:
     x3+=1
     #print(x)
  else :
     frec3.append(x3)
     x3=0
     P3+=1
     #print(frec)
x=0
menosventas=[] 
#print(frec)
for y in range(len(frec3)):
  #print(y)
  #suma+=y
  if frec3[y]==0:
    #menosventas.append(y+1)
    menosventas.append(products[y])

menosventas_ordenadas=[]   
procesador3=[]
tvideo3=[]
tmadre3=[]
dduros3=[]
musb3=[]
pantallas3=[]
bocinas3=[]
audifonos3=[]
temmst=[]
for menos in menosventas:
  if menos[0]<=9:
    procesador3.append(menos)
  elif menos[0]>9 and menos[0]<=28:
    tvideo3.append(menos)
  elif menos[0]>28 and menos[0]<=46:
    tmadre3.append(menos)
  elif menos[0]>46 and menos[0]<=59:
    dduros3.append(menos)
  elif menos[0]==60:
    musb3.append(menos)
  elif menos[0]>60 and menos[0]<=73:
    pantallas3.append(menos)
  elif menos[0]>73 and menos[0]<=83:
    bocinas3.append(menos)
  #elif menos[0]>83 and menos[0]<=96:
  else:
    audifonos3.append(menos)
  


menosventas_ordenadas.append(procesador3)
menosventas_ordenadas.append(tvideo3)
menosventas_ordenadas.append(tmadre3)
menosventas_ordenadas.append(dduros3)
menosventas_ordenadas.append(musb3)
menosventas_ordenadas.append(pantallas3)
menosventas_ordenadas.append(bocinas3)
menosventas_ordenadas.append(audifonos3)
    






#print(menosventas)
#-------------------menos busquedas----------

frec4=[] #la matriz de frecuencias
x4=0 # es el contador 
P4=1#es el id de producto
suma4=0
for n in range(len(searches)):
  #print
  if searches[n][1]==P4:
     x4+=1
     #print(x)
  else :
     frec4.append(x4)
     x4=0
     P4+=1
     #print(frec)
x4=0
menosbusquedas=[] 
#print(frec)
for y in range(len(frec4)):
  #print(y)
  #x4+=1
  #suma+=y
  if frec4[y]==0:
    #menosventas.append(y+1)
    menosbusquedas.append(products[y])

menorbusquedas_ordenadas=[]
procesador4=[]
tvideo4=[]
tmadre4=[]
dduros4=[]
musb4=[]
pantallas4=[]
bocinas4=[]
audifonos4=[]
temmst=[]
for menos in menosventas:
  if menos[0]<=9:
    procesador4.append(menos)
  elif menos[0]>9 and menos[0]<=28:
    tvideo4.append(menos)
  elif menos[0]>28 and menos[0]<=46:
    tmadre4.append(menos)
  elif menos[0]>46 and menos[0]<=59:
    dduros4.append(menos)
  elif menos[0]==60:
    musb4.append(menos)
  elif menos[0]>60 and menos[0]<=73:
    pantallas4.append(menos)
  elif menos[0]>73 and menos[0]<=83:
    bocinas4.append(menos)
  #elif menos[0]>83 and menos[0]<=96:
  else:
    audifonos4.append(menos)
  


menorbusquedas_ordenadas.append(procesador4)
menorbusquedas_ordenadas.append(tvideo4)
menorbusquedas_ordenadas.append(tmadre4)
menorbusquedas_ordenadas.append(dduros4)
menorbusquedas_ordenadas.append(musb4)
menorbusquedas_ordenadas.append(pantallas4)
menorbusquedas_ordenadas.append(bocinas4)
menorbusquedas_ordenadas.append(audifonos4)




#print(menosbusquedas)

#------------mejores reseñas---------------------
frec5=[] #la matriz de frecuencias
x5=0 # es el contador 
P5=1#es el id de producto
suma5=0
for n in range(len(sales)):
  #print
  if sales[n][1]==P5:
    if sales[n][2]==5:
       x5+=1
     #print(x)
  else :
     frec5.append(x5)
     x5=0
     P5+=1
  
#print(frec3)
x5=0
mejores=[] 
#print(frec)
for y in range(len(frec5)):

  #print(y)
  #suma+=y
  if frec5[y]!=0:
    
    #menosventas.append(y+1)
    mejores.append(products[y])
    

#------------peores reseñas-----------------------

frec6=[] #la matriz de frecuencias
x6=0 # es el contador 
P6=1#es el id de producto
suma6=0
for n in range(len(sales)):
  #print
  if sales[n][1]==P6:
    if sales[n][2]==1:
      if sales[n][4]==0:
         x6+=1
     #print(x)
  else :
     frec6.append(x6)
     x6=0
     P6+=1
  
#print(frec3)
x6=0
peores=[] 
#print(frec)
for y in range(len(frec6)):

  #print(y)
  #suma+=y
  if frec6[y]!=0:
    
    #menosventas.append(y+1)
    peores.append(products[y])
    
#ingresos anuales (ingreso total)-----------------
frec7=[] #la matriz de frecuencias
x7=0 # es el contador 
P7=1#es el id de producto
suma7=0
for n in range(len(sales)):
  #print
  if sales[n][1]==P7:
     x7+=1
     #print(x)
  else :
     frec7.append(x7)
     x7=0
     P7+=1
     #print(frec)
x7=0
ingresonual=[]
#producsbusque 
#print(frec1)
for y in range(len(frec7)):
  #print(y)
  #suma+=y
  if frec7[y]!=0:
    #X7=1
    #menosventas.append(y+1)
    #print(products[y][2] ,frec7[y], "=" ,products[y][2]*frec7[y])
    ingresonual.append(products[y][2]*frec7[y])
ingresototal=0
for ingre in range(len(ingresonual)):
  ingresototal+=ingresonual[ingre]

#print(ingresototal)
#ingresos promedio mensuales---------------------8
ingresopromediomensual=ingresototal/9
#mes con mas ventas -----------------------------
frec9=[] #la matriz de frecuencias
x9=0 # es el contador 
P9=1#es el id de producto
suma9=0
meses=[1,2,3,4,5,6,7,8,9]
for mes in range(len(meses)):
  mesada=mes+1
  for n in range(len(sales)):
    if mesada==int(sales[n][3][4]):
      x9+=1
    else:
      continue
  #print(x9)
  frec9.append(x9)
  x9=0
ventasmensuales=[]
for y in range(len(frec9)):
  #print(y)
  #suma+=y
  
    #X2=1
    #menosventas.append(y+1)
  ventasmensuales.append([meses[y],frec9[y]])

ventasmensuales_ordenados9=[]
while ventasmensuales:
  minimo9= ventasmensuales[0][1]
  #print(minimo2)
  lista_actual9=ventasmensuales[0]
  #print(lista_actual2)
  for grupo9 in ventasmensuales:
    if grupo9[1]> minimo9:
      minimo9=grupo9[1]
      lista_actual9=grupo9
  ventasmensuales_ordenados9.append(lista_actual9)
  ventasmensuales.remove(lista_actual9)

    
#print(ventasmensuales_ordenados9)  


#-----------accesos--------------------------------

if user==admin and clave==password:
  print("hello master, i'm here to serve you")
  #print("what would you want to see?")
  ver_opciones=input("¿Do you want to see somenthing? (si/no)  ")
  if ver_opciones=="si":
   option=int(input("selecciona una opcion numerica 1- los mas vendidos 2- los mas buscados 3-los menos vendidos 4-los menos buscados 5.-los productos con mejores reseñas 6.-los productos con peores reseñas 7.- ingreso total anual 8.-promedio mensual 9.-meses con mas ventas  "))
  else:
    exit()
elif  user==users[0]:
  print("eres un cliente no puede acceder, solo VIPs")
  exit()
elif user==users[1]:
  print("eres un cliente no puede acceder, solo VIPs ")
  exit()
else:
  print("tanos dijo: ni si quiera ser quien eres ")
  exit()



while ver_opciones=="si":
  
  if option==1:
   print("estos son los objetos mas vendidos")
    #print(masventas)
   for mas in masventas_ordenados1:
      print(mas)
  elif option==2:
    print("Estos son los objetos mas buscados")
    for mayor in masbusquedas_ordenados2:
      print(mayor)
    #print()
  elif option==3:
    print("Estos son los objetos con menos ventas o ventas nulas por categorias :") 
    for menos in range(len(categorias)):
      print(categorias[menos],": ",menosventas_ordenadas[menos])
    #print(menosventas)
  elif option==4:
    print("estos son los objetos con menos busquedas")
    for menos in range(len(categorias)):
      print(categorias[menos],": ",menorbusquedas_ordenadas[menos])
    
    #for menor in menosbusquedas:
      #print(menorbusquedas_ordenadas)
    #print(menosbusque)
  elif option==5 :
    print("Los productos con mejores reseñas son:  ")
    for me in mejores:
      print(me)

  elif option==6 :
    print("Los productos con peores reseñas y con devolución:  ")
    for pe in peores:
      print(pe)

  elif option==7  :
    print("El total de ventas  es:  ")
    print("$ ",ingresototal)
  
  elif option==8  :
    print("El ingreso mensual promedio es:  ", ingresopromediomensual)

  elif option==9  :
    print("los meses con mas ventas son en este año: ")
    for men in range(3):
      print(ventasmensuales_ordenados9[men]) 
  else:
    print("no es una opcion valida")

  
  ver_opciones=input("¿deseas ver otra opción? (si/no)   ")
  if ver_opciones=="si":
    option=int(input("selecciona una opcion 1- los mas vendidos 2- los mas buscados 3-los menos vendidos 4-los menos buscados 5.-los productos con mejores reseñas 6.-los productos con peores reseñas 7.- ingreso total anual 8.-promedio mensual 9.-meses con mas ventas  "))
  else:
    #os.system("clear")
    exit()






