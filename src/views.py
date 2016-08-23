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
    def __init__(self, width, height):
        from weakref import WeakKeyDictionary
        self.surface = pygame.display.set_mode((width, height))
        self.rect = self.surface.get_rect()
        self.groups = WeakKeyDictionary()

    def register(self, group):
        self.groups[group] = 1

    def remove(self, group):
        del self.groups[group]

    def update(self):
        for group in self.groups.keys():
            group.draw(self.surface)
        pygame.display.flip()


class Window(pygame.sprite.Sprite):
    """
    Basic Window Class
    Super class for every window here in
    """
    #0001#
    #- Constructor -#
    def __init__(self, width, height, active=False):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        # Fetch a rectangle to store the dimensions
        self.rect = self.image.get_rect()


class Menu(pygame.sprite.Sprite):
    """
    Basic Menu Class
    """
    #0002#
    #- Basic Menu Object -#
    # Constructor #
    # Pass the width, height, a number of items,  and color of the object
    def __init__(self, width, screen_rect, items, active=False):
        # Call the Parent Class(Sprite) Constructor
        pygame.sprite.Sprite.__init__(self)

        # Assign local variables
        self.items = items
        self.options = []
        self.font = pygame.font.Font(None, 60)

        # Create an image object for the menu (This could also be an image)
        self.image = pygame.Surface([width, len(items) * 80])

        # Fetch a rectangle object that has the dimensions of the image
        # Update the position of the sprite by setting the rect values
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_rect.centerx
        self.rect.centery = screen_rect.centery

        # Put the font objects into a list and add the rects afterwards

        for i in range(len(items)) :
            self.options.append([])
            self.options[i].append(self.font.render(items[i], True, pygame.Color("white")))
            self.options[i].append(self.options[i][0].get_rect())

        self.draw()

    def draw(self):
        """
        -populate the two arrays
        -blit to the image surface
        """

        for i in range(len(self.items)):
            self.options[i][1].x = self.rect.centerx - (self.options[i][1].width / 2)
            self.options[i][1].y = self.rect.centery - self.options[i][1].height + (self.options[i][1].height * i)

            #- Something Wrong HERE V -#
            self.image.blit(self.options[i][0], (self.rect.centerx - (self.options[i][1].width / 2), self.rect.centery - self.options[i][1].height + (self.options[i][1].height * i)))


            #- For whatever reason, THIS works -#
            self.image.blit(self.options[i][0], (0, i * 60))
