graph = {
    'Arad': ['Timisoara', 'Sibiu', 'Zerind'],
    'Timisoara': ['Lugoj'],
    'Sibiu': ['Rimnicu Vilcea', 'Fagaras', 'Oradea'],
    'Zerind': ['Oradea'],
    'Lugoj': ['Mehadia'],
    'Rimnicu Vilcea': ['Craiova','Pitesti'],
    'Fagaras':['Bucharest'],
    'Oradea':[],
    'Mehadia':['Drobeta'],
    'Pitesti':['Craiova', 'Bucharest'],
    'Bucharest':['Giurgiu', 'Urziceni'],
    'Drobeta':['Craiova'],
    'Giurgiu':[],
    'Urziceni':['Hirsova', 'Vaslui'],
    'Craiova':[],
    'Hirsova':['Eforie'],
    'Vaslui':['Iasi'],
    'Eforie':[],
    'Iasi':['Neamt'],
    'Neamt':[],
}

visited =[]
stack=[]

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# . . . Program Start . . . #

print("\n// . . . Program Start . . . //\n\n")

print("Following is the Breadth-First Search")
dfs(visited, graph, 'Arad')

print("\n\n\n// . . . Program End . . . //\n")
