from queue import Queue

class USMapa:
    '''
    Clase para representar el grafo.
    
    Atributes
    ---------
    m_numeroNodos : int
        Asigna el número de nodos
    m_Nodos : int
        Asigna el rango de los nodos
    
    Methods
    -------
    AgregarBorde(self,nodo1,nodo2,peso=1):
        Agrega un nodo a partir del primer nodo tiene un peso por defecto de 1
    
    ImprimirLista(self):
        Imprime por pantalla la lista de adyacencia
    
    dfs_traversal(self,start_node):
        Realiza la búsqueda por amplitud en el grafo
    
    '''
    
    
    
    def __init__(self, tamanio, dirigido=False):
        
        '''
        Constructor
                
                Parametros:
                    self(class)
                    numeroNodos(int): Numero de nodos
                    dirigido(boolean): El grafo no es dirigido por defecto
                    
                Retorna:
                    nada
        '''
        
        #Se asigna el número de nodos
        self.nodos = tamanio
        #Asigna el rango de los nodos
        self.rangoNodos = range(self.nodos)
        # Es dirigido o no es dirigido
        self.esDirigido = dirigido
        # Representación del grafo es por lista de adyacencia
        # Se usa un diccionario para añadir los nods
        self.listaAdy = {nodo: set() for nodo in self.rangoNodos}
	
    # Agregar borde al grafo
    def AgregarBorde (self, nodo1, nodo2, peso=1):
        '''
        Agrega un nodo dentro de la lista de adyacencia
        
            Parametros:
                self(class)
                nodo1(int): Primer nodo
                nodo2(int): Segundo node
                peso(int): Agrega un peso al nodo a ingresar
                
            Retorna:
                nada
        
        '''
        
        #Agrega el segundo nodo en la posición del primer nodo
        self.listaAdy[nodo1].add((nodo2,peso))
        #En caso de no ser dirigido se agrega el primer nodo en
        #en la posición del primero
        if not self.esDirigido:
            self.listaAdy[nodo2].add((nodo1,peso))
    
    # Imprime el grafo usando la lista de ayacencia como representación
    def Lista(self):
        '''
        Imprime la lista de adyacencia
        
            Parametros:
                self(class)
                
            Retorna:
                nada
        '''
        
        #Bucle para la impresión
        for llave in self.listaAdy.keys():
            print("nodo", llave, ": ", self.listaAdy[llave])


    def DFS(self, inicio, objetivo, camino = [], visitado = set()):
        '''
        Realiza la búsqueda a profundidad
        
            Parametros:
                self(class)
                inicio(int): Nodo desde el que parte la búsqueda
                objetivo(int): El nodo al que se desea llegar
                camino(list): Lista donde se guarda el recorrido
                visitado(collection): Colección que guardará los nodos visitados
            
            Returns:
                resultado: recursividad
                None: Nulo
        '''
        #Agregar el inicio tanto al camino como al visitado
        camino.append(inicio)
        visitado.add(inicio)
        #Si el inicio es igual al objetivo entonces retorna el mismo nodo
        if inicio == objetivo:
            return camino
        #Recorre los nodos adyacentes y si no ha sido visitado inicia el recorrido
        #desde ese nodo 
        for (vecino,peso) in self.listaAdy[inicio]:
            if vecino not in visitado:
                resultado = self.DFS(vecino, objetivo, camino, visitado)
                if resultado is not None:
                    return resultado
                
        #Retorna el último elemento del camino       
        camino.pop()
        return None

    def setMapa(self):
        self.AgregarBorde(0, 1)
        self.AgregarBorde(0, 2)
        self.AgregarBorde(1, 2)
        self.AgregarBorde(1, 4)
        self.AgregarBorde(1, 5)
        self.AgregarBorde(2, 3)
        self.AgregarBorde(2, 6)
        self.AgregarBorde(2, 5)
        self.AgregarBorde(2, 8)
        self.AgregarBorde(5, 6)
        self.AgregarBorde(5, 7)
        self.AgregarBorde(5, 4)
        self.AgregarBorde(4, 7)   
        self.AgregarBorde(6, 7)
        self.AgregarBorde(6, 8)
        self.AgregarBorde(6, 9)
        self.AgregarBorde(6, 10)
        self.AgregarBorde(7, 10)
        self.AgregarBorde(7, 9)
        self.AgregarBorde(3, 8)
        self.AgregarBorde(3, 17)
        self.AgregarBorde(3, 16)
        self.AgregarBorde(8, 9)
        self.AgregarBorde(8, 16)
        self.AgregarBorde(8, 15)
        self.AgregarBorde(9, 15)
        self.AgregarBorde(9, 12)
        self.AgregarBorde(9, 13)
        self.AgregarBorde(9, 10)
        self.AgregarBorde(10, 11)
        self.AgregarBorde(11, 13)
        self.AgregarBorde(11, 22)
        self.AgregarBorde(12, 13)
        self.AgregarBorde(12, 15)
        self.AgregarBorde(15, 16)
        self.AgregarBorde(16, 17)
        self.AgregarBorde(17, 18)
        self.AgregarBorde(16, 18)
        self.AgregarBorde(16, 19)
        self.AgregarBorde(15, 19)
        self.AgregarBorde(15, 20)
        self.AgregarBorde(12, 20)
        self.AgregarBorde(13, 21)
        self.AgregarBorde(21, 22)
        self.AgregarBorde(21, 20)
        self.AgregarBorde(20, 19)
        self.AgregarBorde(19, 18)
        self.AgregarBorde(18, 23)
        self.AgregarBorde(19, 23)
        self.AgregarBorde(20, 24)
        self.AgregarBorde(19, 24)
        self.AgregarBorde(21, 26)
        self.AgregarBorde(21, 25)
        self.AgregarBorde(21, 22)
        self.AgregarBorde(25, 26)
        self.AgregarBorde(24, 29)
        self.AgregarBorde(23, 24)
        self.AgregarBorde(24, 28)
        self.AgregarBorde(26, 29)
        self.AgregarBorde(25, 30)
        self.AgregarBorde(26, 30)
        self.AgregarBorde(29, 28)
        self.AgregarBorde(29, 31)
        self.AgregarBorde(29, 34)
        self.AgregarBorde(29, 35)
        self.AgregarBorde(28, 31)
        self.AgregarBorde(27, 31)
        self.AgregarBorde(27, 28)
        self.AgregarBorde(31, 34)
        self.AgregarBorde(34, 35)
        self.AgregarBorde(35, 36)
        self.AgregarBorde(30, 32)
        self.AgregarBorde(30, 33)
        self.AgregarBorde(32, 33)
        self.AgregarBorde(32, 37)
        self.AgregarBorde(37, 36)
        self.AgregarBorde(35, 39)
        self.AgregarBorde(31, 38)
        self.AgregarBorde(34, 38)
        self.AgregarBorde(39, 40)
        self.AgregarBorde(39, 38)
        self.AgregarBorde(38, 41)
        self.AgregarBorde(38, 42)
        self.AgregarBorde(41, 42)
        self.AgregarBorde(42, 43)
        self.AgregarBorde(42, 45)
        self.AgregarBorde(42, 46)
        self.AgregarBorde(46, 47)    
        self.AgregarBorde(47, 48)
        self.AgregarBorde(43, 44)
        return 'Se ha asignado el mapa'
    
    def BFS(self, nodoInicial, nodoFinal):
        '''
        Busqueda por amplitud busca la ruta mas corta desde un nodo inicial
        
            Parametros:
                self(class)
                nodoInicial(int): El valor del nodo
            
            Retorna:
                nada
        '''
        
        
        # Asigna los nodos visitados para evitar bucles
        visitado = set()
        # Se instancia la clase cola
        cola = Queue()
        ruta = [[nodoInicial]]
        # Añade el nodo inicial a la cola y a visitados
        cola.put(nodoInicial)
        visitado.add(nodoInicial)
        
        
        
        #Mientras la cola no esté vacía 
        while not cola.empty():
            #Extrae el nodo de la cola para imprimirlo
            nodoActual = cola.get()
            print(nodoActual, end = " ")
            #Extrae los nodos adyacentes, si el nodo siguiente no ha sido visitado
            #lo agrega a la cola
            for (nodoSiguiente,peso) in self.listaAdy[nodoActual]:
                if nodoSiguiente not in visitado:
                    cola.put(nodoSiguiente)
                    visitado.add(nodoSiguiente)
    
    
                    


if __name__ == "__main__":
    #### EJEMPLO #####

    #Instancia la clase
    mapa = USMapa(49, dirigido = False)

    # Añaden los nodos, pueden agregarse los pesos
    
    print(mapa.setMapa())
    
    while True:
        try:
            inicio = int(input("Ingrese el nodo inicial (0-48): "))
            fin = int(input("Ingrese el nodo final (0-48): "))
            if(inicio >= 0 and inicio <= 48 and fin >= 0 and fin <= 48):
                break
            else:
                print("Ingrese un número dentro del rango")
        except:
            print("Ingrese un número")
    
    # Imprime la lista de adyacencia
    mapa.Lista()
    
    #Se realiza la búsqueda y se guarda en una lista
    caminoTraversal = []
    caminoTraversal = mapa.DFS(inicio, fin)
    print(f" Búsqueda desde el nodo {inicio} hasta el {fin} es {caminoTraversal}")
    #mapa.BFS(inicio)