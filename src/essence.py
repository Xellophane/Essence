#!/usr/bin/env python

"""
Essence.py
"""

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import controllers
import pygame
import eventhandler
from pygame.locals import *
from views import Screen, Window, Menu
from game import Game

class Essence:
    def __init__(self):
        pygame.init()
        self.ESSENCE = Game()
        self.screen = Screen(1024, 720)
        self.ESSENCE.register(self.screen)
        self.main_menu = Menu(self.screen.surface, 512, 360, 80, ["Start", "Quit"])
        self.menu_group = pygame.sprite.Group(self.main_menu)
        self.screen.register(self.menu_group)
        self.messenger = eventhandler.EventManager()
        self.keyboard = controllers.KeyboardController("keyboard", self.messenger)
        self.messenger.add(self.ESSENCE)
        self.clock = pygame.time.Clock()
        self.Run()

    def Run(self):
        self.RUN = True
        while self.RUN:
            self.keyboard.Update()
            self.clock.tick(60)

        pygame.quit()

    def Notify(self, event):
        if event.name == "Game Exit Event":
            self.RUN = False

if __name__ == "__main__":
    main = Essence()
