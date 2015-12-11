#!/usr/bin/env python

"""
Essence.py
"""

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from pygame.locals import *
import pygame
screen = pygame.display.set_mode((1024, 720))
color = (255, 255, 255)
class Menu(pygame.sprite.Sprite):
        """Basic Menu Class"""
	#- Basic Menu Object -#
	# Constuctor #
	# Pass the width, height, and color of the object
	def __init__(self, width, items[], color):
	    # Call the Parent class's (Sprite) Constructor
	    pygame.sprite.Sprite.__init__(self)
	    
	    # Create an image object for the menu (This could also be an image)
	    self.image = pygame.Surface([width, len(items) * 80])
	    
	    # Fetch the rectangle object that has the dimensions of the
	    # image.
	    # Update the position of the sprite by setting the rect
	    # values
	    self.rect = self.image.get_rect()
		
            # Set active value
	    self.active = False

            # NOT DONE: Selection_Rect = pygame.Rect(rect.
