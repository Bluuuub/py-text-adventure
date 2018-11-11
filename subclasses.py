import classes

class testRoom(classes.room):
    
    def __init__(self):

        self.name = "Test Room 1"
        self.description = "This is a test room. There is a passage to the north"
        self.roomsAdj = [testRoom2, None, None, None]
        self.items = []
        self.interactables = [] 


class testRoom2(classes.room):

    def __init__(self):

        self.name = "Test Room 2"
        self.description = "This is another test room. Sweet."
        self.roomsAdj = [None, testRoom, None, None]
        self.items = []
        self.interactables = []


class me(classes.player):

    def __init__(self):

        self.isAt = testRoom

testRoom = testRoom()
testRoom2 = testRoom2()
me = me()

