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
queue=[]

def bfs (visited, graph, node, endNode):
    visited.append(node)
    queue.append(node)

    while queue:
        m=queue.pop(0)
        if m==endNode:
            break
        print(m, end = " ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# . . . Program Start . . . #

print("\n// . . . Program Start . . . //\n\n")

print("Following is the Breadth-First Search")
bfs(visited, graph, 'Arad', 'Bucharest')

print("\n\n\n// . . . Program End . . . //\n")
