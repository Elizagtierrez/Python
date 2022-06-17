Realiza un cuaderno de Python en Jupiter con el nombre Ejercicio1.ipynb

Dentro vaamos a resolver los siguientes problemas:

1. Una línea de código que  muestre la fecha de hoy.

          from datetime import date
          date.today()
          print("La fecha de hoy es " + str(date.today()))
          La fecha de hoy es 2022-06-16


![image](https://user-images.githubusercontent.com/90996552/174404935-24ce7d10-6f17-4329-82e6-4535e2635a75.png)


2. Construir un convertidor de unidades de centimetros a metros (el formato del resultado deberá ser: X cm son igual a X metros, según el usuarios ingrese la cantidad a convertir).

          print("Convertidor de centimetros a metros")
          cent = input("Ingresa la cantidad de centimetros")
          met = int(cent) /100
          print(str(cent) + " cm, son " + str(met) + " m ")
          Convertidor de centimetros a metros
          300 cm, son 3.0 m 

![image](https://user-images.githubusercontent.com/90996552/174408802-45861889-cf28-49c3-bb36-63b96f634c57.png)



3. Exploremos cómo podemos crear un programa que pueda calcular la distancia entre dos planetas EN KILOMETROS Y EN MILLAS. Comenzaremos usando dos distancias de planetas al sol: Tierra (149.597.870 km) y Júpiter (778.547.200 km). Calcular cuanta distancia hay en kilometos y en millas entre estos dos planetas.

Nota: Quita las comas cuando uses los valores.

          tierra = 149597870
          jupiter = 778547200
          distanciakm = jupiter - tierra
          distanciamill = distanciakm * 0.6
          print(' La distancia entre Jupiter y la tierra es de ' + str(distanciakm) + 'KM, y de ' + str(distanciamill) + ' MILLAS')
          La distancia entre Jupiter y la tierra es de 628949330km, y de 377369598.0 millas
          
<img width="1205" alt="Captura de Pantalla 2022-06-17 a la(s) 17 33 12" src="https://user-images.githubusercontent.com/90996552/174409069-590ae9a1-4dc8-41a1-b8a5-3f3f0d87afd7.png">


Crear una aplicación para trabajar con números y entrada de usuario


Para crear nuestra aplicación, queremos leer la distancia del sol para dos planetas, y luego mostrar la distancia entre los planetas. Haremos esto usando input para leer los valores, int para convertir a entero y luego abs para convertir el resultado en su valor absoluto.

PASOS:

a) Lee los valores

Usando input, agrega el código para leer la distancia del sol para cada planeta, considerando 2 planetas.

b)Convertir a número

Debido a que input devuelve valores de cadena, necesitamos convertirlos en números. Para nuestro ejemplo, usaremos int

c)Realizar el cálculo y convertir a valor absoluto

Con los valores almacenados como números, ahora puedes agregar el código para realizar el cálculo, restando el primer planeta del segundo. Debido a que el segundo planeta podría ser un número mayor, usarás abs para convertirlo a un valor absoluto

d)Prueba tu aplicación

Para probar el proyecto, ejecuta tu notebook. En la parte superior de vscode surgirá un cuadro de diálogo para que proporciones las distancias. Puede utilizar los datos de la tabla siguiente:

Planeta	Y Distancia al sol

Mercurio	57900000

Venus	108200000

Tierra	149600000

Marte	227900000

Júpiter	778600000

Saturno	1433500000

Urano	2872500000

Neptuno	4495100000

          planeta1 = int(input ('Ingresa la distancia del primer planeta'))
          planeta2 = int(input ('Ingresa la distancia del planeta 2'))
          distancia = planeta1 - planeta2
          print('LA DISTANCIA ES DE ', distancia)
          LA DISTANCIA ES DE  42078500002
          
![image](https://user-images.githubusercontent.com/90996552/174409630-bb45ab05-e7bb-422d-ac98-2178ffb1c76c.png)

