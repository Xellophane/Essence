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
        # self.ID makes for easier filtering. As it should be more easily typed.
        self.ID = 0000

class QuitEvent(Event):
    def __init__(self):
        self.Name = "Game Exit Event"
        self.Key = "System"
        self.ID = 1001

class ControllerUpdateEvent(Event):
    def __init__(self):
        self.Name = "Controller Update Event"
        self.Key = "Controller"
        self.ID = 2001

class GraphicsUpdateEvent(Event):
    def __init__(self):
        self.Name = "Graphics Update Event"
        self.Key = "View"
        self.ID = 3001
