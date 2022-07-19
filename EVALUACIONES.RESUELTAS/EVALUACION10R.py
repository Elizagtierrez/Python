"""
Proyecto Básico de Python (El Ahorcado).
Basado en el proyecto de: Kylie Ying (@kylieyying). 
"""
import random #Importa random para palabras al azar
import string #para cadenas
from palabras import palabras #Importamos paquete 
from ahorcado_diagramas import vidas_diccionario_visual #Se importa un modulo

#creamos una funcion con atributo en palabras 
def obtener_palabra_válida(palabras):
    palabra = random.choice(palabras) #variable palabra que elige palabras al azar

#bucle mientras la palabra este en palabra
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)

    return palabra.upper() #convierte la palabra en mayúsculas

#creamos la función
def ahorcado():
#imprimimos la entrada
    print("=======================================")
    print(" ¡Bienvenido(a) al juego del Ahorcado! ")
    print("=======================================")

#creamos las variables 

    palabra = obtener_palabra_válida(palabras)
#
    letras_por_adivinar = set(palabra)  
    abecedario = set(string.ascii_uppercase) #devuelve una cadena de texto
    letras_adivinadas = set()  

    vidas = 7 #oportuniades

    #crear bucle while mientras las letras sean mayor a 0 y las oportunidades tambien
    while len(letras_por_adivinar) > 0 and vidas > 0:
    #imprime las vidas que te quedan
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")

    #crear lista de   de las letras adivinadas
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        print(vidas_diccionario_visual[vidas]) 
        #imprime las palabras
        print(f"Palabra: {' '.join(palabra_lista)}")#hacemos que la palabra continue en ls lista de palabras

     
        letra_usuario = input('Escoge una letra: ').upper() #Pide una letra, y la covierte en mayúscula

        if letra_usuario in abecedario - letras_adivinadas:#Con la condicional if para las palabras en abecedario, si esta en palabras adivinadas
            letras_adivinadas.add(letra_usuario) #la añade
       
            if letra_usuario in letras_por_adivinar: #Si la retra ya esta en letras adivinadas la remueve o borra
                letras_por_adivinar.remove(letra_usuario)
                print('')
         
            else:
                vidas = vidas - 1 #Sino muestra las vidas que le quedan e imprime que no esta 
                print(f"\nTu letra, {letra_usuario} no está en la palabra.")
        
        elif letra_usuario in letras_adivinadas:#Si repite la letra imprime la frase siguiente
            print("\nYa escogiste esa letra. Por favor escoge una letra nueva.")
        else: #sino, y escoge otro caracter que no sea letra lo invalida
            print("\nEsta letra no es válida.")

   #Si la opotunidad restante es 0 imprime la frase siguiente
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"¡Ahorcado! Perdiste. Lo lamento mucho. La palabra era: {palabra}")
    else:#Sino adivinonla palabra
        print(f'¡Excelente! ¡Adivinaste la palabra {palabra}!')

#MUESTRA LA FUNCIÓN
    ahorcado()