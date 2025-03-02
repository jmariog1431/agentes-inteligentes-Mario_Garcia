class Navegador:
    def __init__(self, mapa, inicio, destino):
        self.mapa = mapa
        self.inicio = inicio
        self.destino = destino

    def vecinos(self, x, y):
        movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
        opciones = []
        
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(self.mapa) and 0 <= ny < len(self.mapa[0]):
                opciones.append((nx, ny))

        return opciones

    def utilidad(self, ruta):
        return sum(self.mapa[x][y] for x, y in ruta)

    def mejor_ruta(self):
        mejor_camino = []
        mejor_valor = float('-inf')  

        def explorar(x, y, ruta):
            nonlocal mejor_camino, mejor_valor
            
            if (x, y) == self.destino:
                valor = self.utilidad(ruta)
                if valor > mejor_valor:
                    mejor_valor = valor
                    mejor_camino = ruta
                return

            for nx, ny in self.vecinos(x, y):
                if (nx, ny) not in ruta:  
                    explorar(nx, ny, ruta + [(nx, ny)])

        explorar(self.inicio[0], self.inicio[1], [self.inicio])
        return mejor_camino, mejor_valor

mapa = [
    [1, -1, 2, 0, 1],
    [2,  1, -1, 3, 0],
    [0,  2,  1, -1, 2],
    [1,  3,  2, 1, -1],
    [0, 1, 0,  2, 3]
]

inicio = (0, 0)
destino = (4, 4)

agente = Navegador(mapa, inicio, destino)
ruta, valor = agente.mejor_ruta()

if ruta:
    print("Ruta óptima:", ruta)
    print("Valor total:", valor)
else:
    print("No se encontró una ruta.")
