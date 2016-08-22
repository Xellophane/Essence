#1 /usr/bin/env python
from pygame.locals import *
import pygame
import events

"""
Controllers.py
- Holds all of the "Controllers in the game"
    - The main window will pull from here
"""
class ControlerPrototype:
    def __init__(self, Keytype):
        self.EventKey = Keytype


class KeyboardController:
    def __init__(self, Keytype, Manager):
        self.EventKey = Keytype
        self.Manager = Manager

    """
    The controller for the keyboard
    """

    def Update(self):
        for event in pygame.event.get(KEYDOWN):
            if event.key == K_ESCAPE:
                ev = events.QuitEvent()
                self.Manager.post(ev)


