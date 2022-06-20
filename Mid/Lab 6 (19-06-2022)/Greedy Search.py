goalList = ['1', '2', '3', '8', ' ', '4', '7', '6', '5']

listCurrent = ['1', '8', '3', '1', '6', '4', '7', ' ', '5']


def move(list, direction):

    # . . . UP . . . #

    if direction == "up":
        for i in range(3, 9):
            if list[i] == ' ':
                swap = i-3
                list[i], list[swap] = list[swap], list[i]
                return(list)
        return False

    # . . . DOWN . . . #

    if direction == "down":
        for i in range(0, 6):
            if list[i] == ' ':
                swap = i+3
                list[i], list[swap] = list[swap], list[i]
                return(list)
        return False

    # # . . . LEFT . . . #

    if direction == "left":
        for i in range(0, 9):
            if list[i] == ' ' and i not in ['0', '3', '6']:
                swap = i-1
                list[i], list[swap] = list[swap], list[i]
                return(list)
        return False

    # # . . . RIGHT . . . #

    if direction == "right":
        for i in range(0, 9):
            if list[i] == ' ' and i not in ['2', '5', '8']:
                swap = i + 1
                list[i], list[swap] = list[swap], list[i]
                return(list)
        return False


# print(listCurrent[0], listCurrent[1], listCurrent[2])
# print(listCurrent[3], listCurrent[4], listCurrent[5])
# print(listCurrent[6], listCurrent[7], listCurrent[8])
# print('')
# move("up")
# print(listCurrent[0], listCurrent[1], listCurrent[2])
# print(listCurrent[3], listCurrent[4], listCurrent[5])
# print(listCurrent[6], listCurrent[7], listCurrent[8])
# print('')
# move("down")
# print(listCurrent[0], listCurrent[1], listCurrent[2])
# print(listCurrent[3], listCurrent[4], listCurrent[5])
# print(listCurrent[6], listCurrent[7], listCurrent[8])
# print('')


h_value = 0


def greedySearch(list, prevList):
    h_list = []
    newList = [list]

    # newList.append(move(prevList, "left"))

    print(newList)

    newList.append(move(list, "left"))
    print(newList)








    # for i in len(newList):
    #     if newList[i] != prevList and newList[i] != False:
    #         for j in range(0, 9):
    #             if newList[i][j] != goalList[j]:
    #                 h_list[i] += 1


greedySearch(listCurrent, listCurrent)
