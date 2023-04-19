import algorithmSearch
import numpy as np
from algorithmSearch import Nodes
#from Datos import Letter

init = ''
goal = ''
nro_filas = 8
listAdj = []
for i in range(nro_filas):
    listAdj.append([])

heuristicas = dict()
def Data():
    with open("grafo.txt","r") as graph:
        # Obtener los valores de  Init y Goal
        global init,goal
        for index, lineas in enumerate(graph):
            line = lineas.replace(',',"")
            line = line.split()
            words = len(line)
            if (index == 0 or index == 1):
                line = lineas.split();
                if index == 0:
                    init = Nodes[line[1]]
                else:    
                    goal = Nodes[line[1]] 
            elif words == 2:
                heuristicas[Nodes[line[0]]] = int(line[1]) 
            else:
                #print(f"{Nodes[line[0]]}  {line[1]} costo: {int(line[2])}")
                listAdj[Nodes[line[0]]].append([Nodes[line[1]],int(line[2])])


Data()
print(" -----------------------> BÚSQUEDA EN PROFUNDIDAD  <----------------------------")
Reco = [ -1, -1, -1, -1, -1, -1, -1, -1]
visited = [0 , 0 , 0 , 0 , 0 , 0 , 0, 0]
nodesExpan = [0 , 0 , 0 , 0 , 0 , 0 , 0, 0]
algorithmSearch.DFS(listAdj,init,goal,visited,Reco,nodesExpan)
algorithmSearch.ResultDFS(listAdj,init,goal,nodesExpan)


print(" -----------------------> BÚSQUEDA COSTO UNIFORME  <----------------------------")
Reco = [ -1, -1, -1, -1, -1, -1, -1, -1]
visited = [0 , 0 , 0 , 0 , 0 , 0 , 0, 0]
nodesExpan = [0 , 0 , 0 , 0 , 0 , 0 , 0, 0]
algorithmSearch.Uniforme(listAdj,init,goal,visited,Reco,nodesExpan)
#algorithmSearch.ResultUniform(listAdj,init,goal,Reco,nodesExpan)




print(" -----------------------> GREEDY BFS  <----------------------------")
Reco = [ -1, -1, -1, -1, -1, -1, -1, -1]
visited = [0 , 0 , 0 , 0 , 0 , 0 , 0, 0]
nodesExpan = [0 , 0 , 0 , 0 , 0 , 0 , 0, 0]
algorithmSearch.Greddy_BFS(listAdj, init, goal, heuristicas, visited, Reco,nodesExpan)
#algorithmSearch.ResultGreedyBFS(listAdj,init,goal,Reco,nodesExpan)



print(" ----------------------->    A *      <----------------------------")
Reco = [ -1, -1, -1, -1, -1, -1, -1, -1]
visited = [0 , 0 , 0 , 0 , 0 , 0 , 0, 0]
nodesExpan = [0 , 0 , 0 , 0 , 0 , 0 , 0, 0]
algorithmSearch.AS(listAdj, init, goal, heuristicas, visited, Reco,nodesExpan)
#algorithmSearch.ResultAS(listAdj,init,goal,Reco,nodesExpan)
