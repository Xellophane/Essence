#!/usr/bin/env python

"""
Essence.py
"""

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from pygame.locals import *
import pygame
from views import Screen, Window, Menu
from controllers import KeyboardController
from game import Game

class Essence:
    def __init__(self):
        pygame.init()
        self.ESSENCE = Game()
        screen = Screen(1024, 720)
        self.ESSENCE.register(screen)
        main_menu = Menu(180, self.screen.rect, ["Start", "Quit"])
        menu_group = pygame.sprite.Group(self.main_menu)
        screen.register(menu_group)
        messenger = eventhandler.EventManager()
        keyboard = KeyboardController("keyboard", messenger)
        messenger.add(self.ESSENCE)
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
