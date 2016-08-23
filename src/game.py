from pygame.locals import *
import pygame
from eventhandler import EventManager

class Game:
    def __init__(self):
        from weakref import WeakKeyDictionary
        self.RUN = True
        self.EVENTKEY = "System"
        self.clock = pygame.time.Clock()
        self.modules = WeakKeyDictionary()
        self.eventmanager = EventManager()
        
    def register(self, module):
        self.modules[module] = 1

    def remove(self, group):
        del self.modules[module]

    def run(self):
        while self.RUN:
            for module in self.modules:
                module.update()
                self.clock.tick()
        pygame.quit()

    def notify(self, event):
        if event.name == "Game Exit Event":
            self.RUN = False
