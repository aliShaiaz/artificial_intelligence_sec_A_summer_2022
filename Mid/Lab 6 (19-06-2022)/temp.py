listCurrent = ['1', '8', '3', '1', '6', '4', '7', ' ', '5']


def move(list2):
    # list2[7], list2[6] = list2[6], list2[7]
    temp = list2[7]; list2[7] = list2[6]; list2[6] = temp;



list = []
list.append(listCurrent)
list.append(listCurrent)
list.popleft()


# list.append("{}".format(move(listCurrent)))

x = listCurrent

print(list)

temp = x[7]; x[7] = x[6]; x[6] = temp;


print(list)