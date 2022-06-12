class roomAI:

    fanStatus = "OFF"
    lightStatus = "OFF"
    dayStatus = ""    # D = Day, N = Night
    personInRoom = 0
    personCount = 0

    def turnFanON(self):
        print(" . . Turning On Fan . .")
        self.fanStatus = "ON"

    def turnFanOFF(self):
        print(" . . Turning OFF Fan . .")
        self.fanStatus = "OFF"

    def turnLightON(self):
        print(" . . Turning On Light . .")
        self.lightStatus = "ON"

    def turnLightOFF(self):
        print(" . . Turning OFF Fan . .")
        self.lightStatus = "OFF"

    def nightMode(self):
        print("Night Mode ON")
        self.dayStatus = "N"

    def dayMode(self):
        print("Day Mode ON")
        self.dayStatus = "D"

    def personScanner(self):
        x = int(input("Enter Person Status (0 or 1): "))
        if (x == 0) or (x == 1):
            self.scanPerson(self, x)
        else:
            print("Invalid Person Status!! Please Enter Again.")
            self.personScanner(self)

    def scanPerson(self, x):

        if x == 0:
            self.personInRoom = 0
        else:
            self.personInRoom = 1

    def whenPersonEnters(self):

        print("Person Entering!")
        self.personScanner(self)
        if self.personInRoom == 0:

            if self.dayStatus == "D" and self.fanStatus == "OFF":
                print("Fan is turned OFF.")
                self.turnFanON(self)

            elif self.dayStatus == "N" and (self.fanStatus == "OFF" or self.lightStatus == "OFF"):
                self.turnLightON(self)
                self.turnFanON(self)
        else:
            print("There are already person in room.")

    def whenPersonLeaves(self):

        print("Person Leaving!")
        self.personScanner(self)
        if self.personInRoom == 0 and (self.fanStatus == "ON" or self.lightStatus == "ON"):
            if self.fanStatus == "ON":
                print("Fan is turned ON.")
                self.turnFanOFF(self)
            if self.lightStatus == "ON":
                print("Light is turned ON.")
                self.turnLightOFF(self)
        else:
            print("There are person in the room.")


# . . . Main Func() . . .
print("\n\n\n . . . . . PROGRAM START . . . . .\n\n\n")


room = roomAI
room.dayStatus = "D"

x = input("Enter Command: ")
if x == "enter":
    room.whenPersonEnters(room)
elif x == "exit":
    room.whenPersonLeaves(room)


print("\n\n\n . . . . . PROGRAM END . . . . .\n\n\n")
