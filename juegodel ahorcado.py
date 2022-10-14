import time
nombre=input("Como te llamas ")
print("Hola, "+nombre," Bienvenido al Juego")
print(" ")
time.sleep(1)
print("comienza a adivinar")
time.sleep(0.5)
palabra="marieA"
tupalabra=" "
vidas=5

while vidas > 0:
    fallas=0
    for letra in palabra:
        if letra in tupalabra:
            print(letra,end="")
        else:
            print("*",end="")
            fallas+=1
    if fallas==0:
        print('')
        print("felicidades, ganaste")   
        break

    tuletra=input("introduce una letra: ")
    tupalabra+=tuletra

    if tuletra not in palabra:
        vidas-=1
        print("equivocacion")
        print("tu tienes ",+vidas," vidas")
    if vidas== 0:
        print("perdiste!")
else:
    input()
    print("gracias por participar")
    input()