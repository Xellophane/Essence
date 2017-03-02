"""
events.py
A Module to hold all of your events
"""

class Event:
    def __init__(self):
        self.name = "Generic Debug Event"
        self.type = "Generic Debug Event"

class QuitEvent(Event):
    def __init__(self):
        self.name = "Game Exit Event"
        self.type = "System"
