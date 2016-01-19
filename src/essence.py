#!/usr/bin/env python

"""
Essence.py
"""

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from pygame.locals import *
import pygame
import views
screen = views.Screen(1024, 720)
pygame.font.init()
main_menu = views.Menu(180, screen.rect, ["Start", "Quit"])
menu_group = pygame.sprite.Group(main_menu)
menu_group.draw(screen.surface)
pygame.display.flip()
