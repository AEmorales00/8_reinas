N = 8  # Tamaño del tablero

def es_valido(tablero, fila, columna):
    """
    Verifica si una reina puede colocarse en (fila, columna)
    sin ser atacada por otra reina ya colocada.
    """
    for i in range(fila):
        if tablero[i] == columna:
            return False  # Misma columna
        if abs(tablero[i] - columna) == abs(i - fila):
            return False  # Misma diagonal
    return True

def resolver(tablero, fila, soluciones, contador, encontrar_una=False):
    """
    Aplica DFS con backtracking para encontrar soluciones al problema de las 8 reinas.
    Si encontrar_una es True, se detiene al hallar la primera.
    """
    if fila == N:
        soluciones.append(tablero.copy())
        return True if encontrar_una else None

    for columna in range(N):
        if es_valido(tablero, fila, columna):
            tablero[fila] = columna
            contador[0] += 1  # Cuenta estados explorados
            resultado = resolver(tablero, fila + 1, soluciones, contador, encontrar_una)
            if encontrar_una and resultado:
                return True  # Corta recursión al encontrar una

def obtener_soluciones():
    """
    Devuelve una lista de soluciones válidas y el número de estados explorados.
    """
    tablero = [-1] * N
    soluciones = []
    estados_explorados = [0]
    resolver(tablero, 0, soluciones, estados_explorados)
    return soluciones, estados_explorados[0]

def obtener_una_solucion():
    """
    Devuelve una sola solución y el número de estados explorados.
    """
    tablero = [-1] * N
    soluciones = []
    estados_explorados = [0]
    resolver(tablero, 0, soluciones, estados_explorados, encontrar_una=True)
    return soluciones[0] if soluciones else None, estados_explorados[0]

def imprimir_tablero(tablero):
    """
    Imprime en consola el tablero con las reinas.
    """
    for fila in range(N):
        linea = ['.'] * N
        linea[tablero[fila]] = 'Q'
        print(" ".join(linea))
    print("\n")

def obtener_todas_las_soluciones():
    tablero = [-1] * 8
    soluciones = []
    estados = [0]
    resolver(tablero, 0, soluciones, estados)
    return soluciones, estados[0]
