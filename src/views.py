#! /usr/bin/env python

"""
Menu.py
"""

import pygame

class Menu(pygame.sprite.Sprite):
    """
    Basic Menu Class
    #0001#
    """
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
            self.image.blit(self.options[i][0], (self.rect.centerx - (self.options[i][1].width / 1), self.rect.centery - self.options[i][1].height + (self.options[i][1].height * i)))

            #- For whatever reason, THIS works -#
            # self.image.blit(self.options[i][0], (0, i * 60))





class Screen():
    """
    Screen object
    - Will store a pygame surface that represents the pygame window.
    - Will store said surface's rect.
    #0002#
    """
    #- Screen Object -#
    # Constructor #
    # Pass the width and the height of the screen #
    def __init__(self, width, height):
        self.surface = pygame.display.set_mode((width, height))
        self.rect = self.surface.get_rect()


