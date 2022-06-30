# Práctica 4. 6 puntos
## Tipos de colección de datos.
### 4.1 Ejercicio 1(1.2 puntos)
Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10)
y posteriormente muestre en pantalla cada elemento de la lista junto con su
cuadrado y su cubo.
Respuesta:


      import random # para poder generar los números aleatorios
      lista_numeros = [] # la lista donde se guardarán
      # Primer recorrido para leer la lista
      for indice in range(1,11):
        lista_numeros.append(random.randint(1,10))
      ## Segundo recorrido para mostrar el resultado
      for numero in lista_numeros:
        print(numero," ",numero ** 2," ",numero ** 3)
        2   4   8
        1   1   1
        6   36   216
        6   36   216
        2   4   8
        7   49   343
        10   100   1000
        4   16   64
        10   100   1000
        4   16   64

### 4.2 Ejercicio 2 (1.2 puntos)
Crea una lista e inicializarla con 5 cadenas de caracteres leídas por teclado. Copia
los elementos de la lista en otra lista pero en orden inverso, y muestra sus
elementos por la pantalla.

     lista1 = []
     lista2 = []
     for indice in range(1,6):
         lista1.append(input('Dame la cadena %d: ' % indice))
         lista2 = lista1[::-1]
     for cadena in lista2:
         print(cadena)
     estopa
     dado
     escuela
     ana
     hola

### 4.3 Ejercicio 3 (1.2 puntos)
Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un
alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas,
la nota media, la nota más alta que ha sacado y la menor.

     #Se quiere realizar un programa que lea por teclado 
     # las 5 notas obtenidas por un alumno 
     # (comprendidas entre 0 y 10). 
     # A continuación debe mostrar todas las notas,
     #  la nota media, la nota más alta que ha sacado y 
     # la menor.
     notas = []
     cont = 1
     while cont<6:
         nota = int(input("Introduce la nota %i: " % cont))
         if nota>=0 and nota<=10:
             cont=cont+1
             notas.append(nota)
         else:
             print('formato incorrecto, ingresa de nuevo la calificación')
     print('Notas: ')
     print('_________________')
     print('Nota media: ',sum(notas)/len(notas))
     print("Nota max: ",max(notas))
     print("Nota min: ",min(notas))
     Notas: 
     _________________
     Nota media:  8.2
     Nota max:  9
     Nota min:  7



### 4.4 Ejercicio 4 (1.2 puntos)
Codifica un programa en python que nos permita guardar los nombres de los
alumnos de una clase y las notas que han obtenido. Cada alumno puede tener
distinta cantidad de notas. Guarda la información en un diccionario cuya claves
serán los nombres de los alumnos y los valores serán listados con las notas de
cada alumno.

El programa pedirá el número de alumnos que vamos a introducir, pedirá su
nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo. Al
final el programa nos mostrará la lista de alumnos y la nota media obtenida por
cada uno de ellos. Nota: si se introduce el nombre de un alumno que ya existe el
programa nos dará un error.

      #crear un diccionario y una lista de los nombres de almnos y las notas
      alumnos = {}
      notas = []
      #crear la lista de la cantidad de alumnos a guardar
      cantidad = int(input("Introduce la cantidad de alumnos que vamos a guardar: "))
      for num in range(cantidad):
          alumno = input("Nombre del alumno: ")
          while alumno in alumnos:
              print("Alumno ya existe")
              alumno = input("Nombre del alumno: ")
          nota = int(input("Introduce una nota del alumno (negativa para finalizar): "))
          while nota > 0:
              notas.append(nota)
              nota = int(input("Introduce una nota del alumno (negativa para finalizar): "))
              alumnos[alumno] = notas.copy()
          for alumno, notas in alumnos.items():
              print("%s ha sacado de nota media %f" % (alumnos,sum(notas)/len(notas))) 


### 4.5 Ejercicio 5 (1.2 puntos)
Crea una tupla con los meses del año, pide números al usuario, si el número está
entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino
muestra un mensaje de error. El programa termina cuando el usuario introduce un
cero.

       meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
       "Noviembre", "Diciembre")
       numero = int(input("Dame un numero: "))
       while (numero!=0):
         if(numero>=1 and numero<=len(meses)):
           print(meses[numero-1])
           numero = int(input("Dame un numero: "))
         else:
           print("Inserta un número entre 1 y ",len(meses))
           numero = int(input("Dame un numero: "))
       else:
         print('adios')

 TRATA DE RESOLVER Y AVANZAR LO MÁS POSIBLE EN LOS EJERICICIOS, EL MARTES HABILITO "AYUDAS" EN CADA EJERCICIO
