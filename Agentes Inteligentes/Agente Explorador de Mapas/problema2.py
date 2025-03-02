import random
import time

mapa = [
    [' ', 'O', ' ', ' ', ' '],
    [' ', ' ', ' ', 'O', ' '],
    [' ', 'O', ' ', ' ', ' '],
    ['O', ' ', 'O', ' ', ' '],
    [' ', ' ', ' ', 'O', ' ']
]

posicion_agente = [0, 0]  
visitados = set()
direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]  

def imprimir_mapa():
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if [i, j] == posicion_agente:
                print('A', end=' ')
            elif (i, j) in visitados:
                print('.', end=' ')  # Marca las posiciones visitadas
            else:
                print(mapa[i][j], end=' ')
        print()
    print('\n')

def obtener_movimientos_validos():
    movimientos = []
    for dx, dy in direcciones:
        nueva_x, nueva_y = posicion_agente[0] + dx, posicion_agente[1] + dy
        if 0 <= nueva_x < len(mapa) and 0 <= nueva_y < len(mapa[0]) and mapa[nueva_x][nueva_y] != 'O' and (nueva_x, nueva_y) not in visitados:
            movimientos.append((nueva_x, nueva_y))
    return movimientos

def mover_agente():
    movimientos = obtener_movimientos_validos()
    if movimientos:
        nueva_posicion = random.choice(movimientos)
        posicion_agente[0], posicion_agente[1] = nueva_posicion
        visitados.add(tuple(nueva_posicion))
    else:
        print("No hay movimientos disponibles. Reiniciando exploración...")
        posicion_agente[0], posicion_agente[1] = 0, 0
        visitados.clear()

for _ in range(20):  
    imprimir_mapa()
    mover_agente()
    time.sleep(1)
