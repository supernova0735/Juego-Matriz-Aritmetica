#Juego aritmetico David Mayen , Mario Rodriguez , Elman Norato 




import random
import time

#tamaño tablero
def generar_tablero(n):
    tablero = []
    for _ in range(n):
        fila = []
        for _ in range(n):
            fila.append(random.randint(0, 11))
        tablero.append(fila)
    return tablero

# imprimir el tablero
def imprimir_tablero(tablero):
    for fila in tablero:
        for elemento in fila:
            print(elemento, end='\t')
        print()

#  revelar los vecinos de una celda
def revelar_vecinos(tablero, fila, columna):
    n = len(tablero)
    for i in range(fila-1, fila+2):
        for j in range(columna-1, columna+2):
            if 0 <= i < n and 0 <= j < n:
                tablero[i][j] = str(tablero[i][j])  # Convertir el número en un string

# Función para calcular el resultado de la suma y multiplicación
def calcular_resultado(tablero, fila, columna):
    suma = 0
    n = len(tablero)
    for i in range(fila-1, fila+2):
        for j in range(columna-1, columna+2):
            if 0 <= i < n and 0 <= j < n:
                suma += tablero[i][j]
    resultado = suma * tablero[fila][columna]
    return resultado

#mstrar opciones
def mostrar_opciones(respuesta):
    opciones = [respuesta]
    while len(opciones) < 4:
        opcion = respuesta + random.randint(-5, 5)
        if opcion != respuesta and opcion not in opciones:
            opciones.append(opcion)
    random.shuffle(opciones)
    for i, opcion in enumerate(opciones):
        print(f"{i+1}. {opcion}")

#respuestas 
def obtener_respuesta():
    while True:
        try:
            opcion = int(input("Ingrese el número de la opción elegida: "))
            if 1 <= opcion <= 4:
                return opcion
            else:
                print("Ingrese un número válido (1-4).")
        except ValueError:
            print("Ingrese un número válido (1-4).")

#empezae juego
def jugar_partida(jugador, tablero):
    puntaje = 0
    n = len(tablero)

    for _ in range(cantidad_turnos):
        print(f"\nTurno de {jugador}")
        imprimir_tablero(tablero)

        while True:
            try:
                fila = int(input("Ingrese la fila de la celda: "))
                columna = int(input("Ingrese la columna de la celda: "))
                if 0 <= fila < n and 0 <= columna < n:
                    break
                else:
                    print(f"Ingrese valores válidos para fila (0-{n-1}) y columna (0-{n-1}).")
            except ValueError:
                print("Ingrese valores válidos para fila (0-{n-1}) y columna (0-{n-1}).")

        
        revelar_vecinos(tablero, fila, columna)

        
        resultado = calcular_resultado(tablero, fila, columna)
        print(f"\nRealice el siguiente cálculo: ({'+'.join(str(x) for x in tablero[fila])}) * {tablero[fila][columna]} = ?")
        mostrar_opciones(resultado)

        
        tiempo_inicio = time.time()
        respuesta = obtener_respuesta()
        tiempo_transcurrido = time.time() - tiempo_inicio

        
        if tiempo_transcurrido > 25:
            print("¡Tiempo agotado! No se acumulan puntos.")
        elif respuesta == opciones.index(resultado) + 1:
            puntaje += 3
            print("¡Respuesta correcta! Se acumulan 3 puntos.")
        else:
            print("Respuesta incorrecta. No se acumulan puntos.")

        tablero = [["?" for _ in range(n)] for _ in range(n)]

    return puntaje

n = int(input("Ingrese el tamaño del tablero (N x N): "))
cantidad_turnos = int(input("Ingrese la cantidad de turnos por jugador: "))

tablero = [["?" for _ in range(n)] for _ in range(n)]

jugador1 = input("Ingrese el nombre del primer jugador: ")
jugador2 = input("Ingrese el nombre del segundo jugador: ")

print("¡Comienza el juego!\n")
puntaje_jugador1 = jugar_partida(jugador1, tablero)
puntaje_jugador2 = jugar_partida(jugador2, tablero)


print(f"\n--- Resultados finales ---")
print(f"{jugador1}: {puntaje_jugador1} puntos")
print(f"{jugador2}: {puntaje_jugador2} puntos")

if puntaje_jugador1 > puntaje_jugador2:
    print(f"\n¡{jugador1} es el ganador!")
elif puntaje_jugador2 > puntaje_jugador1:
    print(f"\n¡{jugador2} es el ganador!")
else:
    print("\n¡Es un empate!")



