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
        self.EVENTKEY = Keytype
        self.Manager = Manager
        self.Manager.add(self) # registers self to manager


class KeyboardController(ControlerPrototype):
    # very basic controller for the keyboard.
    def __init__(self, Keytype, Manager):
        super().__init__(Keytype, Manager)

    """
    The controller for the keyboard
    """
    def Notify(self, event):
        # ID to sort by, allowing only the event it's interested in to be grabbed.
        if event.ID == 2001:
            self.Update()

    def Update(self):
        # construct a collection to exit game with esc key.
        for event in pygame.event.get(KEYDOWN):
            if event.key == K_ESCAPE:
                ev = events.QuitEvent()
                self.Manager.post(ev)
