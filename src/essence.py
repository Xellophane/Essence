#!/usr/bin/env python

"""
My personal game project.

No idea what will be done for story, but just building the engine right now.
"""

__version__ = '0.01'
__author__ = "Crystal Division Xellophane"

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import sys
import controllers
import pygame
import eventhandler
from pygame.locals import *
import Views.windows
import events
from game import Game

class Essence:
    def __init__(self):
        # Initialize pygame variables
        pygame.init()
        # Assign an eventkey
        self.EVENTKEY = "System"
        # Initialize the EventHandler
        self.messenger = eventhandler.EventManager()
        # Register self to EventHandler
        self.messenger.add(self)
        # Initialize Database, Story, ect. and register it to EventHandler
        self.ESSENCE = Game(self.messenger)
        # Initialize the view window(sceen), register it to EventHandler
        self.screen = Views.windows.Screen(1024, 720, self.messenger)
        # Initialize the menu sprite and menu group. (TEMP)
        self.main_menu = Views.windows.Menu(self.screen, 512, 360, 100, ["Start", "Quit"])
        self.menu_group = pygame.sprite.Group(self.main_menu)
        self.screen.register(self.menu_group)
        # Initialize the keyboard
        self.keyboard = controllers.KeyboardController("Controller", self.messenger)
        # Initialize the clock
        self.clock = pygame.time.Clock()
        # Update to display on the screen.
        self.screen.update()
        # enter the update Loop
        self.Run()

    def Run(self):
        # Set up while loop
        self.running = True
        while self.running:
            # Post to both the Controllers and Graphics.
            self.messenger.post(events.ControllerUpdateEvent())
            self.messenger.post(events.GraphicsUpdateEvent())
            # Tick the clock and limit to 60 frame per second
            self.clock.tick(60)
        # When loop is exited, quit/exit gracefully if possible.
        pygame.quit()
        sys.exit()

    def Notify(self, event):
        # Notify method for self: When it recieves the event 1001, set the boolean
        # to False to allow the main loop to quit, and the application to exit
        # gracefully.
        if event.ID == int(1001):
            self.running = False
            print("1001")

# Allow the file to be run as a "script".
if __name__ == "__main__":
    main = Essence()
