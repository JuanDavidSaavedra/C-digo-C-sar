# Cifrado Cesar

ABECEDARIO = 26 # 26 para encriptación y desencriptación con el abecedario en inglés y 27 para el español.

def obtenerModo():
    while True:
        print('¿Deseas encriptar o desencriptar un mensaje?')
        modo = input().lower()
        if modo in 'encriptar e desencriptar d'.split():
            return modo
        else:
            print('Ingresa "encriptar" o "e" o "desencriptar" o "d"')

def obtenerMensaje():
    print('Ingresa tu mensaje:')
    return input()

def obtenerClave():
    clave = 0
    while True:
        print('Ingresa el número de clave (Rotación entre el 1 y el %s)' % (ABECEDARIO))
        clave = int(input())
        if (clave >= 1 and clave <= ABECEDARIO):
            return clave

def obtenerMensajeTraducido(modo, mensaje, clave):
    if modo[0] == 'd':
        clave= -clave
    traduccion = ''

    for simbolo in mensaje:
        if simbolo.isalpha():
            num = ord(simbolo)
            num += clave

            if simbolo.isupper():
                if num > ord('Z'):
                    num -= ABECEDARIO
                elif num < ord('A'):
                    num += ABECEDARIO

            elif simbolo.islower():
                if num > ord('z'):
                    num -= ABECEDARIO
                elif num < ord('a'):
                    num += ABECEDARIO

            traduccion += chr(num)
        else:
            traduccion += simbolo
    return traduccion

modo = obtenerModo()
mensaje = obtenerMensaje()
clave = obtenerClave()

print('Su texto traducido es:')
print(obtenerMensajeTraducido(modo, mensaje, clave))