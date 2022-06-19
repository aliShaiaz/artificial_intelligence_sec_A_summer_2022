from telnetlib import STATUS


class aiDoor:
    doorStat = "C"  # C = Closed, OF = Open Front, OB = Open Back
    pPos = "E"  # F = Front, B = Back

    def pNone(Self):
        Self.pPos = "E"

    def closeDoor(self):
        print("Closing Door")
        self.doorStat = "C"

    def openFront(self):
        print("Opening Door to Front.")
        self.doorStat = "OF"

    def openBack(self):
        print("Opening Door to Back.")
        self.doorStat = "OB"

    def pFront(self):
        self.pPos = "F"

    def pBack(self):
        self.pPos = "B"

    def operation(self):
        print("\n\n")
        if self.pPos != "E":
            if self.pPos == "F":
                print("Person in Front:")
                self.openBack(self)
                self.pNone(self)
                self.closeDoor(self)
            elif self.pPos == "B":
                print("Person in Back:")
                self.openFront(self)
                self.pNone(self)
                self.closeDoor(self)
        else:
            print("No Person Near Door!")

        print("\n\n")


    def scan(self, x):
        if x == "0":
            self.pNone(self)
        elif x == "1":
            self.pFront(self)
        elif x == "2":
            self.pBack(self)
        else:
            print("Invalid Value!")
            return "-1"


# . . . Main Func() . . .

door = aiDoor

for i in range(0, 10):
  x = input("enter x: ")
  door.scan(door, x)
  door.operation(door)
