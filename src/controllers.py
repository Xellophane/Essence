#1 /usr/bin/env python
from pygame.locals import *
import pygame
import events

"""
Controllers.py

The prototype will allow for other classes to be built from it.
Goals:

Current:
- self.EventKey allows for filtering for the EventManager.
- self.Manager allows the controller to register itself with the EventManager
- Update() will pull from the pygame event loop and notify the EventManager
  based on what happens on the loop.
"""
class ControlerPrototype:
    def __init__(self, Keytype, Manager):
        self.EventKey = Keytype
        self.Manager = Manager
        self.Manager.add(self)


class KeyboardController(ControlerPrototype):
    def __init__(self, Keytype, Manager):
        super().__init__()

    """
    The controller for the keyboard
    """

    def Update(self):
        for event in pygame.event.get(KEYDOWN):
            if event.key == K_ESCAPE:
                ev = events.QuitEvent()
                self.Manager.post(ev)
