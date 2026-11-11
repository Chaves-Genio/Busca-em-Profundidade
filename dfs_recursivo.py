def dfs_recursivo(grafo, no, visitados=None):
    if visitados is None:
        visitados = set()

    visitados.add(no)
    print(no, end=" ")

    for vizinho in grafo.get(no, []):
        if vizinho not in visitados:
            dfs_recursivo(grafo, vizinho, visitados)


#Exemplo de um grafo representado por dicionário(lista de adjacência)
grafo = {
    0:[1,2],
    1:[3,4],
    2:[5,6],
    3:[7],
    4:[8,9],
    5:[10],
    6:[],
    7:[],
    8:[],
    9:[],
    10:[],
}

print('Percorrendo o grafo com DFS(Recursivo):')
dfs_recursivo(grafo, 0)


