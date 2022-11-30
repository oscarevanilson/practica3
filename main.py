class EstadoPuzzle:
    def __init__(self, estado, padre, movimiento, profundidad, costo, llave):
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
            def __lt__(self, other):
                return self.mapa < other.mapa
            def __str__(self):
                return str(self.mapa)

EstadoObjetivo = [1,2,3,4,5,6,7,8,0]
NodoObjetivo = None
NodosExpandidos = 0
MaxBusquedaProf = 0
MaxFrontera = 0

def BestFirst(estadoInicial):
    global MaxFrontera, MaxBusquedaProf, NodoObjetivo
    nodo1 = ""
    for poss in estadoInicial:
        nodo1 = nodo1 + str(poss)

    llave = Heuristica(nodo1)
    caminoVisitado = set()
    Queue = []
    Queue.append(EstadoPuzzle(estadoInicial, None, None, 0, 0, llave))
    caminoVisitado.add(nodo1)

    while Queue:
        Queue.sort(key=lambda o: o.llave)
        nodo = Queue.pop(0)
        if nodo.estado ==EstadoObjetivo:
            NodoObjetivo = nodo
            return Queue
        caminosPosibles = subNodos(nodo)
        for camino in caminosPosibles:
            esteCamino = camino.mapa[:]
            if esteCamino not in caminoVisitado:
                llave = Heuristica(camino.mapa)
                camino.llave = llave + camino.profundidad
                Queue.append(camino)
                caminoVisitado.add(camino.mapa[:])
                if camino.profundidad > MaxBusquedaProf:
                    MaxBusquedaProf = 1 + MaxBusquedaProf

valores_0 = [0,1,2,1,2,3,2,3,4]
valores_1 = [1,0,1,2,1,2,3,2,3]
valores_2 = [2,1,0,3,2,1,4,3,2]
valores_3 = [1,2,3,0,1,2,1,2,3]
valores_4 = [2,1,2,1,0,1,2,1,2]
valores_5 = [3,2,1,2,1,0,3,2,1]
valores_6 = [2,3,4,1,2,3,0,1,2]
valores_7 = [3,2,3,2,1,2,1,0,1]
valores_8 = [4,3,2,3,2,1,2,1,0]

def Heuristica(nodo):
    global valores_0, valores_1, valores_2, valores_3, valores_4, valores_5, valores_6, valores_7, valores_8
    v0 = valores_0[nodo.index("0")]
    v1 = valores_1[nodo.index("1")]
    v2 = valores_2[nodo.index("2")]
    v3 = valores_3[nodo.index("3")]
    v4 = valores_4[nodo.index("4")]
    v5 = valores_5[nodo.index("5")]
    v6 = valores_6[nodo.index("6")]
    v7 = valores_7[nodo.index("7")]
    v8 = valores_8[nodo.index("8")]
    valorTotal = v0+v1+v2+v3+v4+v5+v6+v7+v8
    return valorTotal

def subNodos(nodo):
    global NodosExpandidos
    NodosExpandidos = NodosExpandidos + 1

    siguienteCaminos = []
    siguienteCaminos.append(EstadoPuzzle(Movimiento(nodo.estado, 1), nodo, 1, nodo.profundidad + 1, nodo.costo + 1, 0))
    siguienteCaminos.append(EstadoPuzzle(Movimiento(nodo.estado, 2), nodo, 2, nodo.profundidad + 1, nodo.costo + 1, 0))
    siguienteCaminos.append(EstadoPuzzle(Movimiento(nodo.estado, 3), nodo, 3, nodo.profundidad + 1, nodo.costo + 1, 0))
    siguienteCaminos.append(EstadoPuzzle(Movimiento(nodo.estado, 4), nodo, 4, nodo.profundidad + 1, nodo.costo + 1, 0))
    nodos = []
    for camino in siguienteCaminos:
        if(camino.estado != None):
            nodos.append(camino)
    return nodos

def Movimiento(estado, direccion):
    nuevoEstado = estado[:]

    indice = nuevoEstado.index(0)

    if indice == 0:
        if direccion == 1:
            return None
        elif direccion == 2:
            temp = nuevoEstado[0]
            nuevoEstado[0] = nuevoEstado[3]
            nuevoEstado[3] = temp
        elif direccion == 3:
            return None
        elif direccion == 4:
            temp = nuevoEstado[0]
            nuevoEstado[0] = nuevoEstado[1]
            nuevoEstado[1] = temp
        return nuevoEstado
    elif indice == 1:
        if direccion == 1:
            return None
        elif direccion == 2:
            temp = nuevoEstado[1]
            nuevoEstado[1] = nuevoEstado[4]
            nuevoEstado[4] = temp
        elif direccion == 3:
            temp = nuevoEstado[1]
            nuevoEstado[1] = nuevoEstado[0]
            nuevoEstado[0] = temp
        elif direccion == 4:
            temp = nuevoEstado[1]
            nuevoEstado[1] = nuevoEstado[2]
            nuevoEstado[2] = temp
        return nuevoEstado
    elif indice == 2:
        if direccion == 1:
            return None
        elif direccion == 2:
            temp = nuevoEstado[2]
            nuevoEstado[2] = nuevoEstado[5]
            nuevoEstado[5] = temp
        elif direccion == 3:
            temp = nuevoEstado[2]
            nuevoEstado[2] = nuevoEstado[1]
            nuevoEstado[1] = temp
        elif direccion == 4:
            return None
        return nuevoEstado
    elif indice == 3:
        if direccion == 1:
            temp = nuevoEstado[3]
            nuevoEstado[3] = nuevoEstado[0]
            nuevoEstado[0] = temp
        elif direccion == 2:
            temp = nuevoEstado[3]
            nuevoEstado[3] = nuevoEstado[6]
            nuevoEstado[6] = temp
        elif direccion == 3:
            return None
        elif direccion == 4:
            temp = nuevoEstado[3]
            nuevoEstado[3] = nuevoEstado[4]
            nuevoEstado[4] = temp
        return nuevoEstado
    elif indice == 4:
        if direccion == 1:
            temp = nuevoEstado[4]
            nuevoEstado[4] = nuevoEstado[1]
            nuevoEstado[1] = temp
        elif direccion == 2:
            temp = nuevoEstado[4]
            nuevoEstado[4] = nuevoEstado[7]
            nuevoEstado[7] = temp
        elif direccion == 3:
            temp = nuevoEstado[4]
            nuevoEstado[4] = nuevoEstado[3]
            nuevoEstado[3] = temp
        elif direccion == 4:
            temp = nuevoEstado[4]
            nuevoEstado[4] = nuevoEstado[5]
            nuevoEstado[5] = temp
        return nuevoEstado
    elif indice == 5:
        if direccion == 1:
            temp = nuevoEstado[5]
            nuevoEstado[5] = nuevoEstado[2]
            nuevoEstado[2] = temp
        elif direccion == 2:
            temp = nuevoEstado[5]
            nuevoEstado[5] = nuevoEstado[8]
            nuevoEstado[8] = temp
        elif direccion == 3:
            temp = nuevoEstado[5]
            nuevoEstado[5] = nuevoEstado[4]
            nuevoEstado[4] = temp
        elif direccion == 4:
            return None
        return nuevoEstado
    elif indice == 6:
        if direccion == 1:
            temp = nuevoEstado[6]
            nuevoEstado[6] = nuevoEstado[3]
            nuevoEstado[3] = temp
        elif direccion == 2:
            return None
        elif direccion == 3:
            return None
        elif direccion == 4:
            temp = nuevoEstado[6]
            nuevoEstado[6] = nuevoEstado[7]
            nuevoEstado[7] = temp
        return nuevoEstado
    elif indice == 7:
        if direccion == 1:
            temp = nuevoEstado[7]
            nuevoEstado[7] = nuevoEstado[4]
            nuevoEstado[4] = temp
        elif direccion == 2:
            return None
        elif direccion == 3:
            temp = nuevoEstado[7]
            nuevoEstado[7] = nuevoEstado[6]
            nuevoEstado[6] = temp
        elif direccion == 4:
            temp = nuevoEstado[7]
            nuevoEstado[7] = nuevoEstado[8]
            nuevoEstado[8] = temp
        return nuevoEstado
    elif indice == 8:
        if direccion == 1:
            temp = nuevoEstado[8]
            nuevoEstado[8] = nuevoEstado[5]
            nuevoEstado[5] = temp
        elif direccion == 2:
            return None
        elif direccion == 3:
            temp = nuevoEstado[8]
            nuevoEstado[8] = nuevoEstado[7]
            nuevoEstado[7] = temp
        elif direccion == 4:
            return None
        return nuevoEstado

def main():
    global NodoObjetivo
    estadoInicial = [1,2,3,5,6,8,4,7,0]
    BestFirst(estadoInicial)

    profundidad = MaxBusquedaProf
    movimientos = []
    if NodoObjetivo != None:
        profundidad = NodoObjetivo.profundidad
        imprimir = []
        while estadoInicial != NodoObjetivo.estado:
            if NodoObjetivo.movimiento == 1:
                camino = 'Arriba'
            elif NodoObjetivo.movimiento == 2:
                camino = 'Abajo'
            elif NodoObjetivo.movimiento == 3:
                camino = 'Izquierda'
            elif NodoObjetivo.movimiento == 4:
                camino = 'Derecha'
            movimientos.insert(0, camino)
            imprimir.insert(0, NodoObjetivo.estado)
            NodoObjetivo = NodoObjetivo.padre
    
    for estado in imprimir:
        for i in range(0,8,3):
            print(estado[i],estado[i+1],estado[i+2])
        print()

    print("Camino: ", movimientos)
    print("Costo: ", NodosExpandidos)
    print("Nodos expandidos: ",str(NodosExpandidos))
    print("Profundidad: ",str(profundidad))
    print("MaxBusquedaProf: ",str(MaxBusquedaProf))

if __name__ == '__main__':
    main()