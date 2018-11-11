class DirectionError(Exception):
    
    pass


class player:

    cardinals = {
            'N': 1,
            'S': 2,
            'E': 3,
            'W': 4,
            }

    def __init__(self):

        self.names = ("me", "myself", "self")
        self.description = "Example text for self-examination"
        self.inventory = []
        self.isAt = None

    def go(self, direction):
        
        card_dir = cardinals[direction[0].upper()]
        if self.isAt.roomsAdj[card_dir] != None:
            self.isAt = self.isAt.roomsAdj[card_dir]
        else:
            raise DirectionError

    
    def lookAround(self):
        """
        This function is gonna be the primary method of writing to
        console.
        """

class interactable:

    def __init__(self):
        
        self.names = []
        self.description = ""
        self.roomText = ""

    def useOn(self, item):

        doThings()


class items:
    
    def __init__(self):

        self.name = ""
        self.description = ""
        self.interactsWith = [ ]
        self.roomText = ""

    def useSolo(self):

        doJunk()


class room:
    
    def __init__(self):
        
        self.name = ""
        self.description = ""
        self.roomsAdj = []
        self.items = []
        self.interactables = []


    def use(self, primaryItem, secondaryItem=None):
        
        if secondaryItem != None:
            secondaryItem.useOn(primaryItem)
        else:
            try:
                primaryItem.useSolo()
            except AttributeError:
                return "I can't seem to do this right now."

