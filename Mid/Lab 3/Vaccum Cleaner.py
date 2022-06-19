def moveRight(start, end, direction, state):

    print(" . . . Moving Right . . . \n")
    vCleaner = 0
    i = 0
    for i in range(start, end, direction):
        if state[i] == "clean":
            print("Block ", i+1, " is clean.\n")
            vCleaner = 1
        elif state[i] == "dirty":
            print("Block ", i+1, " is dirty.")
            state[i] = "clean"
            print("Block ", i+1, " is now clean.\n")
            vCleaner = 0


def moveLeft(start, end, direction, state):

    print(" . . . Moving Left . . . \n")
    vCleaner = 0
    i = 0
    for i in range(start, end, direction):
        if state[i] == "clean":
            print("Block ", i+1, " is clean.\n")
            vCleaner = 1
        elif state[i] == "dirty":
            print("Block ", i+1, " is dirty.")
            state[i] = "clean"
            print("Block ", i+1, " is now clean.\n")
            vCleaner = 0


def startCleaner(start, end, iterations, state):
    for i in range(0, int(iterations)):
        moveRight(start, end, 1, state)
        moveLeft(end-1, start-1, -1, state)


# . . . Main Func . . . #

block = ["clean", "dirty", "dirty"]
x = 3
startCleaner(0, len(block), x, block)
