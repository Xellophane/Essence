from pygame.locals import *
import pygame
from eventhandler import EventManager

class Game:
    def __init__(self, eventmanager):
        # I have no idea if I'll need the following code later. Keeping it for now
        #from weakref import WeakKeyDictionary
        #self.RUN = True
        #self.EVENTKEY = "System"
        self.EVENTKEY = "Game"
        #self.modules = WeakKeyDictionary()
        #self.eventmanager = EventManager()

    #def register(self, module):
        #self.modules[module] = 1

    def remove(self, group):
        del self.modules[module]

    def run(self):
        while self.RUN:
            for module in self.modules:
                module.update()
        pygame.quit()

    #def notify(self, event):
        #if event.name == "Game Exit Event":
            #self.RUN = False
