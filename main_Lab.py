class EstadoMaze:
    def __init__(self,estado,padre,movimiento,profundidad,costo,llave):
        self.estado = estado
        self.padre = padre
        self.movimiento = movimiento
        self.profundidad = profundidad
        self.costo = costo
        self.llave = llave
        if self.estado:
            self.mapa = ''.join(str(e) for e in self.estado)
            def __eq__(self,other):
                return self.mapa == other.mapa
            def __lt__(self,other):
                return self.mapa < other.mapa
            def __str__(self):
                return str(self.mapa)
    
Laberinto = []
EstadoObjetivo = [8,13]
NodoObjetivo = None
NodosExpandidos = 0
MaxBusquedaProf = 0

def BestFirst(estadoInicial):
    global MaxBusquedaProf, NodoObjetivo
    llave = Heuristica(estadoInicial)
    caminoVisitado = set()
    Queue = []
    Queue.append(EstadoMaze(estadoInicial,None,None,0,0,llave))

    while Queue:
        Queue.sort(key=lambda o: o.llave)
        nodo = Queue.pop(0)
        if nodo.estado == EstadoObjetivo:
            NodoObjetivo = nodo
            return Queue
        caminosPosibles = subNodos(nodo)
        for camino in caminosPosibles:
            esteCamino = camino.mapa[:]
            if esteCamino not in caminoVisitado:
                llave = Heuristica(camino.estado)
                camino.llave = llave + camino.profundidad
                Queue.append(camino)
                caminoVisitado.add(camino.mapa[:])
                if camino.profundidad > MaxBusquedaProf:
                    MaxBusquedaProf = 1 + MaxBusquedaProf

def Heuristica(estado):
    valorTotal = abs(EstadoObjetivo[0] - estado[0]) + abs(EstadoObjetivo[1] - estado[1])
    return valorTotal

def subNodos(nodo):
    global NodosExpandidos
    NodosExpandidos = NodosExpandidos + 1

    siguienteCaminos = []
    siguienteCaminos.append(EstadoMaze(Movimiento(nodo.estado, 1), nodo, 1, nodo.profundidad + 1, nodo.costo + 1, 0))
    siguienteCaminos.append(EstadoMaze(Movimiento(nodo.estado, 2), nodo, 2, nodo.profundidad + 1, nodo.costo + 1, 0))
    siguienteCaminos.append(EstadoMaze(Movimiento(nodo.estado, 3), nodo, 3, nodo.profundidad + 1, nodo.costo + 1, 0))
    siguienteCaminos.append(EstadoMaze(Movimiento(nodo.estado, 4), nodo, 4, nodo.profundidad + 1, nodo.costo + 1, 0))
    nodos = []
    for camino in siguienteCaminos:
        if(camino.estado != None):
            nodos.append(camino)
    return nodos

def Movimiento(estado, direccion):
    nuevoEstado = estado[:]

    if direccion == 1:
        try:
            nuevoEstado[1] = nuevoEstado[1]+1
            temp = Laberinto.index(nuevoEstado)
        except:
            return None
        else:
            return Laberinto[temp]
    elif direccion == 2:
        try:
            nuevoEstado[0] = nuevoEstado[0] + 1
            temp = Laberinto.index(nuevoEstado)
        except:
            return None
        else:
            return Laberinto[temp]
    elif direccion == 3:
        try:
            nuevoEstado[1] = nuevoEstado[1] - 1
            temp = Laberinto.index(nuevoEstado)
        except:
            return None
        else:
            return Laberinto[temp]
    elif direccion == 4:
        try:
            nuevoEstado[0] = nuevoEstado[0] - 1
            temp = Laberinto.index(nuevoEstado)
        except:
            return None
        else:
            return Laberinto[temp]

def main():
    global NodoObjetivo
    mat = [
        [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
        [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1],
        [0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0]
    ]
    for i in mat:
        for j in range(len(i)):
            if mat[mat.index(i)][j]:
                Laberinto.append([mat.index(i),j])
    src = [0,0]
    
    BestFirst(src)    
    profundidad = MaxBusquedaProf
    movimientos = []
    if NodoObjetivo != None:
        profundidad = NodoObjetivo.profundidad
        imprimir = []
        while src != NodoObjetivo.estado:
            if NodoObjetivo.movimiento == 1:
                camino = 'Derecha'
            elif NodoObjetivo.movimiento == 2:
                camino = 'Abajo'
            elif NodoObjetivo.movimiento == 3:
                camino = 'Izquierda'
            elif NodoObjetivo.movimiento == 4:
                camino = 'Arriba'
            movimientos.insert(0, camino)
            imprimir.insert(0, NodoObjetivo.estado)
            mat[NodoObjetivo.estado[0]][NodoObjetivo.estado[1]] = "*"
            NodoObjetivo = NodoObjetivo.padre
    
    mat[src[0]][src[1]] = "I"
    mat[EstadoObjetivo[0]][EstadoObjetivo[1]] = "M"
    laberinto = ""
    for y in mat:
        for x in y:
            if x == "I":
                laberinto = laberinto + "I"
            elif x == "M":
                laberinto = laberinto + "M"
            elif x == "*":
                laberinto = laberinto + "*"
            elif x:
                laberinto = laberinto + " "
            else:
                laberinto = laberinto + '█'
        laberinto = laberinto + "\n"

    print(laberinto)
    print("Camino: ", movimientos)
    print("Costo: ", NodosExpandidos)
    print("Nodos expandidos: ",str(NodosExpandidos))
    print("Profundidad: ",str(profundidad))
    print("MaxBusquedaProf: ",str(MaxBusquedaProf))

if __name__ == '__main__':
    main()