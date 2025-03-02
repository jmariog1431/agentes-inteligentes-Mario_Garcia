from collections import deque
import time

class Laberinto:
    def __init__(self, laberinto, inicio, meta):
        self.laberinto = [list(fila) for fila in laberinto]
        self.inicio = inicio
        self.meta = meta
        self.filas = len(laberinto)
        self.columnas = len(laberinto[0])

    def obtener_vecinos(self, nodo):
        x, y = nodo
        movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        vecinos = []
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.filas and 0 <= ny < self.columnas and self.laberinto[nx][ny] != '#':
                vecinos.append((nx, ny))
        return vecinos

    def buscar_ruta(self):
        queue = deque([(self.inicio, [self.inicio])])
        visitados = set()
        while queue:
            nodo_actual, camino = queue.popleft()
            if nodo_actual == self.meta:
                return camino
            if nodo_actual not in visitados:
                visitados.add(nodo_actual)
                for vecino in self.obtener_vecinos(nodo_actual):
                    if vecino not in visitados:
                        queue.append((vecino, camino + [vecino]))
        return None

    def imprimir_laberinto(self, ruta_actual=[]):
        laberinto_copia = [fila[:] for fila in self.laberinto]
        for x, y in ruta_actual:
            if laberinto_copia[x][y] not in ('S', 'M'):
                laberinto_copia[x][y] = '.'
        for fila in laberinto_copia:
            print(' '.join(fila))
        print("\n")

    def animar_ruta(self, ruta):
        for i in range(len(ruta)):
            self.imprimir_laberinto(ruta[:i+1])
            time.sleep(0.5)

laberinto = [
    ['S', ' ', '#', ' ', ' '],
    ['#', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', '#', ' '],
    [' ', ' ', ' ', ' ', '#'],
    ['#', '#', ' ', ' ', 'M']
]

inicio = (0, 0)
meta = (4, 3)

agente = Laberinto(laberinto, inicio, meta)
camino = agente.buscar_ruta()

if camino:
    print("Camino encontrado:", camino)
    agente.animar_ruta(camino)
    print("¡Salida encontrada!")
else:
    print("No se encontró un camino.")

