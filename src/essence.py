#!/usr/bin/env python

"""
Essence.py
"""

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from pygame.locals import *
import pygame
from views import Screen, Window, Menu
from controllers import KeyboardController
import eventhandler

class Essence:
    def __init__(self):
        pygame.init()
        self.RUN = True
        self.EventKey = "System"
        self.screen = Screen(1024, 720)
        pygame.font.init()
        self.main_menu = Menu(180, self.screen.rect, ["Start", "Quit"])
        self.menu_group = pygame.sprite.Group(self.main_menu)
        self.menu_group.draw(self.screen.surface)
        pygame.display.flip()
        self.messenger = eventhandler.EventManager()
        self.keyboard = KeyboardController("keyboard", self.messenger)
        self.messenger.add(self)
        self.clock = pygame.time.Clock()
        self.Run()

    def Run(self):
        while self.RUN:
            self.keyboard.Update()
            self.clock.tick(60)

        pygame.quit()

    def Notify(self, event):
        if event.name == "Game Exit Event":
            self.RUN = False

if __name__ == "__main__":
    main = Essence()
