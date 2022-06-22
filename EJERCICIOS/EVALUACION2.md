## Práctica 2. 6 puntos
2 Práctica 2. Números enteros y reales.

Realiza los ejercicios de acuerdo a las indicaciones

2.1 Ejercicio 1 (1.5 puntos)

Escribir un programa que convierta un valor dado en grados Fahrenheit a grados
Celsius.

      #programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
      dato1 = int(input('Ingrese una temperatura en grados Fahrenheit: '))
      celsius = (dato1 - 32) * 5.0/9.0
      # Hacemos uso de la funcion str.format() para darle formato a nuestra respuesta
      print('{} grados Fahrenheit son {} grados Celsius '.format(dato1, celsius))
      300 grados Fahrenheit son 148.88888888888889 grados Celsius 
      
 
 ![image](https://user-images.githubusercontent.com/90996552/174939545-13b2dc89-c043-4032-a191-acb417722a71.png)


2.2 Ejercicio 2 (1.5 puntos)

Dados dos números, mostrar la suma, resta, división y multiplicación de
ambos.

            #Ejercicio2. Dados dos números mostrar la suma, resta, división y multiplicación de ambos.
            num_1 = int(input('Ingrese un número: '))
            num_2 = int(input('Ingrese el segundo número: '))
            suma = num_1 + num_2
            resta = num_1 - num_2
            multi = num_1 * num_2
            divi = num_1 / num_2
            print('la suma de los dos números dados es: {} \nla resta de los dos números es: {} \nla multipliacación de los dos números es: {} \nla división entre los dos números es: {}'.format(suma,resta,multi,divi))
            la suma de los dos números dados es: 4 
            la resta de los dos números es: 0 
            la multipliacación de los dos números es: 4 
            la división entre los dos números es: 1.0


![image](https://user-images.githubusercontent.com/90996552/174941346-8111e395-e013-48ec-a94a-b29cabf6dc4a.png)


2.3 Ejercicio 3 (1.5 puntos)

Calcular el perímetro y área de un rectángulo dada su base y su altura.
Respuesta:

                  #Calcular el perímetro y área de un rectángulo dada su base y su altura.
                  lado1 = int(input('Ingrese la medida del primer lado del triángulo en centímetros: '))
                  lado2 = int(input('Ingrese la medida del segundo lado del triángulo en centímetros: '))
                  lado3 = int(input('Ingrese la medida del tercer lado del triángulo en centímetros: '))
                  peri = lado1 + lado2 + lado3
                  print('Resultado: el perímetro del triángulo es {} cm.'.format(peri))
                  base = int(input('Ingrese la medida de la base del triángulo en centímetros: '))
                  altura = int(input('Ingrese la medida de la altura del triángulo en centímetros: '))
                  area = (base * altura) / 2
                  print('Resultado: el área del triángulo es {} cm2.'.format(area))
                  Resultado: el perímetro del triángulo es 6 cm.
                  Resultado: el área del triángulo es 7.5 cm2.
 
![image](https://user-images.githubusercontent.com/90996552/174942975-85934ea3-6f94-4e28-a2e1-62655179f475.png)



