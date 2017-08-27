import pygame

class Screen:
    #0000#
    """
    Screen Object
    - Container for all graphical objects in game
    - Objects are stored in groups in a weakref dict list
    - update() calls the draw() function of the groups in the list[].
    - register() adds a group to the list[]
    - remove() removes a group from the list[]
    """

    #- Contructor -#
    def __init__(self, width, height, manager):
        # setting up a weak key dictionary.
        from weakref import WeakKeyDictionary
        # adding self to EventHandler
        manager.add(self)
        # Setting EventKey for EventHandler filtering
        self.EVENTKEY = "View"
        # Initialize the display.
        self.surface = pygame.display.set_mode((width, height))
        # getting a rect from the surface.
        self.rect = self.surface.get_rect()
        # sets up a groups.
        self.groups = WeakKeyDictionary() #different than pygame groups

    # add a subsurface to the WeakKeyDictionary.
    def register(self, group):
        self.groups[group] = 1 # different than pygame groups

    # remove a subsurface from the WeakKeyDictionary
    def remove(self, group):
        del self.groups[group]

    def Notify(self, event):
        if event.ID == 3001:
            self.update()

    def update(self):
        # loop over the pygame groups in groups.keys and blit them to
        # self.surface. Then flip the display
        for group in self.groups.keys():
            group.draw(self.surface) # this DOES refer to pygame groups
        pygame.display.flip() # "Flip" to show what was drawn


class Window(pygame.sprite.Sprite):
    """
    Basic Window Class
    Super class for every window here in
    """
    #0001#
    #- Constructor -#
    def __init__(self, parent, x, y, width, height):
        super().__init__()

        self.surface = parent.subsurface(x, y, width, height)
        self.image = self.surface.copy()
        # get rect to store x, y
        self.rect = self.image.get_rect()


class Menu(Window):
    """
    Basic Menu Class
    Todo:
    - Write update logic.
    """
    #0002#
    #- Basic Menu Object -#
    # Constructor #
    def __init__(self, parent, x, y, width, items, active = False):
        # Call Super
        super().__init__(parent, x, y, width, len(items) * 80)

        # Assign local variables
        self.items = items # class scope to hold passed items
        self.options = [] # list to hold the rendered font items
        self.font = pygame.font.Font(None, 60) # initializing a font object

        for i in range(len(self.items)) : # looping through the items list and assign the resulting surface object to options[]
            self.options.append(self.font.render(items[i], True, pygame.Color("white")))

        self.draw()

    def draw(self):
        """
        -
        -blit to the image surface
        """

        for i in range(len(self.options)):
            rect = self.options[i].get_rect() # grabbing rect from the surface object
            # setting up x and y co-ordinates
            rect.x = self.rect.centerx - rect.centerx
            rect.y = i * rect.height
            # blitting the image.
            self.image.blit(self.options[i], self.options[i].get_rect())
