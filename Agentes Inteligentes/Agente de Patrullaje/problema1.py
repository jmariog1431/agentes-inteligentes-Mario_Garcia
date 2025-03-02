import random
import time

mapa = [
    [' ', ' ', 'X', ' ', ' ', 'X'],
    ['X', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', 'X', ' '],
    ['X', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', 'X', ' ', ' ']
]

trayectoria = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (3, 3), (3, 4), (4, 4)]
posicion_agente = [0, 0]
indice_trayectoria = 0

def mostrar_mapa():
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if [i, j] == posicion_agente:
                print('A', end=' ')
            else:
                print(mapa[i][j], end=' ')
        print()
    print('\n')

def desplazar_agente():
    global indice_trayectoria
    if indice_trayectoria < len(trayectoria) - 1:
        nueva_posicion = list(trayectoria[indice_trayectoria + 1])
        
        if mapa[nueva_posicion[0]][nueva_posicion[1]] == 'X':
            print("¡Obstáculo detectado! Buscando nueva ruta...")
            intentos = 0
            while intentos < 3:
                nueva_ruta = random.choice(trayectoria)
                if mapa[nueva_ruta[0]][nueva_ruta[1]] != 'X':
                    posicion_agente[0], posicion_agente[1] = nueva_ruta
                    indice_trayectoria = trayectoria.index(nueva_ruta)
                    print("Nueva ruta establecida.")
                    return
                intentos += 1
            print("No se encontró una ruta alternativa. Manteniendo posición.")
        else:
            indice_trayectoria += 1
            posicion_agente[0], posicion_agente[1] = nueva_posicion
    else:
        print("Ruta completa. Reiniciando...")
        indice_trayectoria = 0
        posicion_agente[0], posicion_agente[1] = trayectoria[indice_trayectoria]

for _ in range(20):  
    mostrar_mapa()
    desplazar_agente()
    time.sleep(1)
