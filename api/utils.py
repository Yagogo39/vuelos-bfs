class Nodo:
    def __init__(self, datos, hijos=None): #Esta funcion es el constructor de la clase Nodo, que recibe los datos del nodo y los hijos del nodo, que son los nodos siguientes al nodo actual en el camino del laberinto
        self.datos = datos
        self.hijos = None
        self.padre = None
        self.costo = None
        self.set_hijos(hijos)

    def set_hijos(self, hijos): #Esta funcion asigna los hijos al nodo, que son los nodos siguientes al nodo actual en el camino del laberinto
        self.hijos = hijos
        if self.hijos != None:
            for h in self.hijos:
                h.padre = self

    def get_hijos(self): #Esta funcion devuelve los hijos del nodo, que son los nodos siguientes al nodo actual en el camino del laberinto
        return self.hijos
    
    def get_padre(self): #Esta funcion devuelve el padre del nodo, que es el nodo anterior al nodo actual en el camino del laberinto
        return self.padre
    
    def set_padre(self, padre): #Esta funcion asigna el padre al nodo, que es el nodo anterior al nodo actual en el camino del laberinto
        self.padre = padre

    def set_datos(self, datos): #Esta funcion asigna los datos al nodo, que es la posicion del nodo en el laberinto
        self.datos = datos

    def get_datos(self): #Esta funcion devuelve los datos del nodo, que es la posicion del nodo en el laberinto
        return self.datos

    def set_costo(self, costo): #Esta funcion asigna el costo al nodo, que es la distancia desde el nodo raiz hasta el nodo actual
        self.costo = costo

    def get_costo(self): #Esta funcion devuelve el costo del nodo, que es la distancia desde el nodo raiz hasta el nodo actual
        return self.costo

    def igual(self, nodo): #Esta funcion compara el nodo actual con otro nodo, para saber si son iguales o no
        if self.get_datos() == nodo.get_datos():
            return True
        else:
            return False
        
    def en_lista(self, lista_nodos): #Esta funcion revisa si el nodo actual esta en la lista de nodos, para evitar ciclos
        en_la_lista = False
        for n in lista_nodos:
            if self.igual(n):
                en_la_lista = True
        return en_la_lista
    
    def __str__(self): #Esta funcion devuelve una cadena de texto con los datos del nodo, para poder imprimir el nodo de manera legible
        return str(self.get_datos())
    

def buscar_solucion_BFS(conexiones, estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodos_inicial = Nodo(estado_inicial)
    nodos_frontera.append(nodos_inicial)
    while (not solucionado) and (len(nodos_frontera) != 0):
        nodo = nodos_frontera[0] #Extraer el nodo y añadirlo a la lista de nodos visitados pop(0), es para extraer el primer nodo de la lista, ya que BFS es una busqueda en amplitud
        #Extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))
        if nodo.get_datos() == solucion:
            #Solucion encontrada
            solucionado = True
            return nodo
        else:
            #Expandir nodos hijos (ciudades con conexion)
            dato_nodo = nodo.get_datos()

            lista_hijos = []
            #Recorrer las conexiones del nodo actual, para crear los nodos hijos, que son las ciudades con conexion al nodo actual
            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                lista_hijos.append(hijo)
                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                    nodos_frontera.append(hijo)
            
            nodo.set_hijos(lista_hijos) #Asignar los nodos hijos al nodo actual, para poder seguir el camino del laberinto


# if __name__ == "__main__":
#     conexiones = {
#         'Jiloyork': {'Celaya', 'CDMX', 'Queretaro'},
#         'Sonora': {'Zacatecas', 'Sinaloa'},
#         'Guanajuato': {'Aguascalientes'},
#         'Oaxaca': {'Queretaro'},
#         'Sinaloa': {'Celaya', 'Sonora', 'Jiloyork'},
#         'Queretaro': {'Monterrey'},
#         'Celaya': {'Jiloyork', 'Sinaloa'},
#         'Zacatecas': {'Sonora', 'Monterrey', 'Queretaro'},
#         'Monterrey': {'Zacatecas', 'Sinaloa'},
#         'Tamaulipas': {'Queretaro'},
#         'Queretaro': {'Tamaulipas', 'Zacatecas', 'Sinaloa', 'Jiloyork', 'Oaxaca'},
#         'Aguascalientes': {},
#         'CDMX': {}
#     }

#     estado_inicial = 'Jiloyork'
#     solucion = 'Monterrey'
#     nodo_solucion = buscar_solucion_BFS(conexiones, estado_inicial, solucion)
    
#     #Mostrar el resultado
#     resultado = []
#     nodo = nodo_solucion
#     while nodo.get_padre() != None:
#         resultado.append(nodo.get_datos())
#         nodo = nodo.get_padre()
#     resultado.append(estado_inicial)
#     resultado.reverse()
#     print(resultado)    