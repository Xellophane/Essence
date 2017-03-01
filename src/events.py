"""
events.py
A Module to hold all of your events


"""

class Event:
    def __init__(self):
        # self.Name names the event
        self.Name = "Generic Debug Event"
        # self.Key allows for filtering, making sure only the event only finds
        # those who need it.
        self.Key = "Generic Debug Event"

class QuitEvent(Event):
    def __init__(self):
        self.Name = "Game Exit Event"
        self.Key = "System"
