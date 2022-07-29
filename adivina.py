
import random

def adivina_la_palabra(palabra_exitosa):
    intento = 1
    ganar = False
    while(intento<=6 and ganar == False):
        
        print("__Intento %s__" % intento)
        
        palabra = input("Ingrese la palabra: ")
        
        if(len(palabra) == 5):
            
            if(palabra == palabra_exitosa):
                ganar = True
            else:
                for i in range(len(palabra)):
                    if(palabra[i] == palabra_exitosa[i]):
                        print(palabra[i]+"+", end="")
                    else:
                        pertenece = False
                        for letra in palabra_exitosa:
                            if(letra == palabra[i]):
                                pertenece = True
                        if pertenece == True:
                            print(palabra[i]+"*", end="")
                        else:
                            print(palabra[i]+"-", end="")
                print("\n")
                intento+=1
                        
                
        else:
            print("Tu intento debe ser de 5 letras")
            intento+=1
    
    
    if ganar == True:
        print("Felicidades, ganaste!!!! La palabra era " + palabra_exitosa)
    else:
        print("Agotaste tus intentos. La palabra era " + palabra_exitosa)

palabras_clave = ["anual","anole","anoto","apios","apipa","anoel","appia"]
palabra_exitosa = palabras_clave[random.randint(0, len(palabras_clave) - 1)]

adivina_la_palabra(palabra_exitosa)








