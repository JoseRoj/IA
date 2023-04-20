import numpy as np
import random
from queue import PriorityQueue

Optima = [0,1,3,7]
Nodes = dict()
Nodes[0] = 'A'
Nodes[1] = 'B'
Nodes[2] = 'C'
Nodes[3] = 'D'
Nodes[4] = 'E'
Nodes[5] = 'F'
Nodes[6] = 'G'
Nodes[7] = 'H'
Nodes['A'] = 0
Nodes['B'] = 1
Nodes['C'] = 2
Nodes['D'] = 3
Nodes['E'] = 4
Nodes['F'] = 5
Nodes['G'] = 6
Nodes['H'] = 7


def IsOptima(Path):
    if Path == Optima:
        print("La solucion encontrada es la óptima")
    else:
        print("La solución encontrada no es la óptima")    

    
# FUNCION DE RECONSTRUCCION DE CAMINO #
def Reconstruccion(init, goal,Reco):
    Path = []
    aux = goal
    while aux != init:
        Path.insert(0,aux)
        aux = Reco[aux]
    Path.insert(0,init)
    return Path       



"""################################################################################################
                                BÚSQUEDA EN PROFUNDIDAD 
################################################################################################"""

Path = []
#costo = 0
# Contador de nodos expandidos
#nodesExpan = [0 , 0 , 0 , 0 , 0 , 0 , 0, 0]
def neighbors(listadj,init,visited):
    x = 0
    for v in listadj[init]:
        if visited[v[0]] == 0:
            x += 1 ;           
    return x    
        
def DFS(listadj,init,goal,visited,Reco,nodesExpan):
    #global costo
    visited[init] = 1
    nodesExpan[init] += 1
    if(init == goal):
        Path.append(goal)
        #print(Nodes[goal])
        return True
    if(len(listadj[init]) == 0):
        return  #Si llego al final volver
    #print(f"{Nodes[init]}",end= " --> ")
    while(neighbors(listadj,init,visited) > 0): # Mientras le queden vecinos 
        nodo = random.randint(0,(len(listadj[init]) - 1))
        #print(listadj[init][nodo])
        if visited[listadj[init][nodo][0]] == 0: 
            Reco[init] = listadj[init][nodo][0] ## Recordar camino
            #costo = costo + listadj[init][nodo][1]
            if(DFS(listadj,listadj[init][nodo][0],goal,visited,Reco,nodesExpan) == True): 
                Path.insert(0,init)
                return True

def ResultDFS(listadj,init,goal,nodesExpan):
    global costo
    # IMPRIMIR CAMINO
    for index,value in enumerate(Path):
        if index != (len(Path) - 1):
            print(Nodes[value], end = " --> ")
        else:
            print(Nodes[value])
    IsOptima(Path)
            
    # CALCULAR EL COSTO DE LA SOLUCION 
    for index in range(len(Path) - 1):
        for value in listadj[Path[index]]:
            if value[0] == Path[index + 1]: # obtener el de destino y su costo
                costo = costo + value[1]
    print(f"Costo: {costo}")
    
    # CALCULAR TODAS DE NODOS EXPANDIDOS PARA ENCONTRAR LA SOLUCION Y CANTIDAD DE VECES EXPANDIDO CADA UNO
    print("Expansión de nodos:")
    sum = 0
    for index, ex in enumerate(nodesExpan):
        sum += ex
    print(f"Total Nodos expandidos: {sum}")
    for index, ex in enumerate(nodesExpan):
        print(f"{Nodes[index]} : {ex}")       




"""################################################################################################
                                BÚSQUEDA COSTO UNIFORME 
################################################################################################"""

#cleanReco() # Debemos recordar el camino del nodo que lo llamo por ultima vez

#cleanVisited() # Limpiar Visited

nodesExpan = [0 , 0 , 0 , 0 , 0 , 0 , 0, 0]
costo = 0

def Uniforme(listadj, init ,goal,visited,Reco,nodesExpan):
    Path = []
    distAc = [0 , 0 , 0 ,0, 0 ,0 , 0 ,0 ]
    distancia = 0
    global costo
    pqU = PriorityQueue(maxsize = 0) # Dada las heuristicas
    visited[init] = 1
    pqU.put([distancia,init]) # 0 dado que la distancia a llegar al nodo es 0 
    distAc[init] = distancia,
    while (pqU.qsize() > 0):
        nodo = pqU.get()
        distancia = nodo[0]
        
        nodesExpan[nodo[1]] += 1
        #camino.append(nodo[1])  
        #print(f"Expande: { nodo[1]} --> Distancia: {nodo[0]}")
    
        if nodo[1] == goal:
            Results(listadj,init,goal,Reco,nodesExpan)
            #print("Se llego")
            #Reconstruccion(init, goal,Reco)
            #print(f"Expande: { nodo[1]} --> Distancia: {nodo[0]}")
            return
        for x in listadj[nodo[1]]:      # x = 0 --> Nodo a expandir , x = 1 --> costo camino
            if (visited[x[0]] == 0 or distAc[x[0]] > (distancia + x[1])): # Dado qu se debe alcanzar a un nodo por mas de uno debe expandirlo igual
                #Si la distancia que hay ya a ese nodo es mayor y el camino por otro es menor de puede moverse
                #nodesExpan[nodo[1]] += 1
                #print(f"Expande: { x[0]} --> Distancia: {distancia + x[1]}")
                visited[x[0]] = 1
                Reco[x[0]] = nodo[1]
                distAc[x[0]] = distancia + x[1] 
                pqU.put([distancia + x[1] , x[0]])

"""################################################################################################
                                GREEDY  BEST FIRST SEARCH 
################################################################################################"""

def Greddy_BFS(listadj, init ,goal, heuristicas, visited, Reco,nodesExpan):
    pq = PriorityQueue(maxsize = 0) # Dada las heuristicas
    visited[init] = 1
    pq.put([heuristicas[init],init])
    while (pq.qsize() > 0):        
        nodo = pq.get()
        nodesExpan[nodo[1]] += 1
        if nodo[1] == goal:
            Results(listadj,init,goal,Reco,nodesExpan)
            #Reconstruccion(init,goal)
            return
        for x in listadj[nodo[1]]:      # x = 0 --> Nodo a expandir , x = 1 --> costo camino
            # No es necesario agregar otra condicion debido a que la h es una sola por nodo y ya se va tomando la con menor valor
            # ,no como el costo que puede alterar dependiendo el camino que mantien

            if(visited[x[0]] == 0): 
            #print(listadj[nodo[1]][x[0]])
                Reco[x[0]] = nodo[1]
                visited[x[0]] = 1
                pq.put([heuristicas[x[0]],x[0]])
 
"""################################################################################################
                                        A * 
################################################################################################"""
def AS(listadj, init ,goal, heuristicas, visited, Reco,nodesExpan):
    distAc = [0 , 0 , 0 , 0, 0 , 0 , 0, 0 ]
    pq = PriorityQueue(maxsize = 0) # Dada las heuristicas
    visited[init] = 1
    dist = 0
    DHC = heuristicas[init]
    pq.put([DHC,dist,init]) # Distancia acumualda es 0 [DistanciaAcumulada,Distancia + H, nodo]
    """
    List[1] = [ 3 , 2 ] [ 4 , 5] # entrega los vecinos
    List[1][1] = [ 3 , 2] # camino 
    List[1][1] = [ 2 ] # consto de ir de 1 a 2  
    """
    while (pq.qsize() > 0):        
        nodo = pq.get() #nodo[1] = numero de nodo & nodo[0] = Costo acumulado + heuristica
        nodesExpan[nodo[2]] += 1
        dist1 = nodo[0] # #distacia acumulada + g(n) + h
        dist = nodo[1] #distancia Acumuladas sum(g(n)) sin herirusticas
        #print(f"Expande: { Nodes[nodo[2]]} --> H: {nodo[0]}")
        if nodo[2] == goal:
            Results(listadj,init,goal,Reco,nodesExpan)
            #Reconstruccion(init,goal)
            return
        for x in listadj[nodo[2]]:      # x = 0 --> Nodo a expandir , x = 1 --> costo camino
            if(visited[x[0]] == 0 or distAc[x[0]] > (dist + x[1] + heuristicas[x[0]])):
                #print(listadj[nodo[1]][x[0]])U
                #distAc[x[0]] = distancia + x[1] # Dsitancia Acumulada
                visited[x[0]] = 1
                distAc[x[0]] = (dist + x[1] + heuristicas[x[0]])
                Reco[x[0]] = nodo[2] # Recordar el ultimo nodo que lo expandio
                pq.put([(dist + x[1] + heuristicas[x[0]]),(dist + x[1]),x[0]])


""" ##################### RESULT #########################"""

def Results(listadj,init,goal,Reco,nodesExpan):
    costo = 0
    Path = Reconstruccion(init,goal,Reco)
    #print(Path)
    
    # IMPRIMIR CAMINO
    for index,value in enumerate(Path):
        if index != (len(Path) - 1):
            print(Nodes[value], end = " --> ")
        else:
            print(Nodes[value])
    IsOptima(Path)
    # CALCULAR EL COSTO DE LA SOLUCION 
    for index in range(len(Path) - 1):
        for value in listadj[Path[index]]:
            if value[0] == Path[index + 1]: # obtener el de destino y su costo
                costo = costo + value[1]
    print(f"Costo: {costo}")
    
    # CALCULAR TODAS DE NODOS EXPANDIDOS PARA ENCONTRAR LA SOLUCION Y CANTIDAD DE VECES EXPANDIDO CADA UNO
    print("Expansión de nodos:")
    sum = 0
    for index, ex in enumerate(nodesExpan):
        sum += ex
    print(f"Total Nodos expandidos: {sum}")
    for index, ex in enumerate(nodesExpan):
        print(f"{Nodes[index]} : {ex}")    
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
