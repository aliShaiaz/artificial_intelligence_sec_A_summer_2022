from asyncio import constants
from operator import truediv
from tracemalloc import start


graph = {
    'A': {'C': [7, 4], 'D': [3, 1]},
    'B': {'E': [8, 3], 'F': [2, 1]},
    'C': {},
    'D': {},
    'E': {'H': [4, 5]},
    'F': {'I': [9, 2], 'G': [0, 3]},
    'H': {},
    'I': {},
    'S': {'A': [12, 3], 'B': [4, 2]},
    'G': {}
}

list = {}

ucsList = []


def printGraph(graph):
    for x in graph:
        print(x, " : ", graph[x])
    input("\nReturn to Main Menu \"Press Enter\"")
    programStart()


def GreedyBestFirst(graph, start, end):
    if start == end:
        print(start)
        input("\nReturn to Main Menu \"Press Enter\"")
        programStart()

    elif len(graph[start]) != 0:
        print(start, end=" -> ")
        key = ""
        temp = 100
        for x in graph[start]:
            if temp > graph[start][x][0]:
                temp = graph[start][x][0]
                key = x
        GreedyBestFirst(graph, key, end)
        return

    else:
        print("?")
        return


def aStarSearch(graph, start, end, list, lastList):

    if lastList == "start":
        aStarSearch(graph, 'S', 'G', list, "")
        for x in list:
            print(x[0], end="")
            for y in range(1, len(x)):
                print(" -> ", end=x[y])
        print("\nF(n) =", list[x][0])

        input("\nReturn to Main Menu \"Press Enter\"")
        programStart()

    else:

        if len(graph[start]) != 0:
            for x in graph[start]:
                if lastList in list.keys():
                    entry = lastList + x
                    fn = int(list[lastList][0]) + int(graph[start]
                                                      [x][0]) + int(graph[start][x][1])
                else:
                    entry = lastList + start + x
                    fn = int(graph[start][x][0]) + int(graph[start][x][1])

                if x == end:
                    isGoal = True
                else:
                    isGoal = False
                list[entry] = [fn, isGoal]

        if lastList != "" and lastList in list.keys():
            del list[lastList]

        key = ""
        value = 100
        for i in list:
            if int(list[i][0]) < value and list[i][1] == False:
                key = i
                value = list[i][0]
        if key != "":
            index = len(key)-1
            aStarSearch(graph, key[index], end, list, key)
        return


def UninformedCostSearch(graph, start, end, list):

    if list == "start":
        if UninformedCostSearch(graph, 'S', 'G', ucsList):
            print(ucsList[len(ucsList)-1], end="")
            for i in range(len(ucsList)-2, -1, -1):
                print(" -> ", end=ucsList[i])
            input("\nReturn to Main Menu \"Press Enter\"")
            programStart()

        else:
            print("No Output!")

    else:
        if start == end:
            list.append(start)
            return True

        elif len(graph[start]) != 0:
            costs = []
            for i in graph[start]:
                costs.append(graph[start][i][1])

            costs.sort()
            for i in costs:
                for j in graph[start]:
                    if int(graph[start][j][1]) == int(i):
                        if UninformedCostSearch(graph, str(j), end, list):
                            list.append(start)
                            return True
            return False
        else:
            return False


def programStart():
    print("\n\nEnter Numbers to run operation:")
    print("1. Print Graph")
    print("2. Greedy Best First Search")
    print("3. A* Search")
    print("4. Uninformed Cost Search")
    print("0. Exit")

    try:
        inp = int(input())

        if inp == 1:
            print("\n\nPrinting Graph:\n")
            printGraph(graph)
        elif inp == 2:
            print("\n\nPrinting GreedyBestFirst:\n")
            GreedyBestFirst(graph, 'S', 'G')
        elif inp == 3:
            print("\n\nPrinting A* Search:\n")
            aStarSearch(graph, 'S', 'G', list, "start")
        elif inp == 4:
            print("\n\nPrinting Uninformed Cost Search:\n")
            UninformedCostSearch(graph, 'S', 'G', "start")
        elif inp == 0:
            print("\n\nExiting..\n")
            exit()
        else:
            print("\nInvalid inp!")
            input("\nReturn to Main Menu \"Press Enter\"")
            programStart()
    except:
        print("\nInvalid inp!")
        input("\nReturn to Main Menu \"Press Enter\"")
        programStart()


# / / . . . Main Function . . . / /

programStart()
