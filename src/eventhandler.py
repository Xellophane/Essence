import events

"""
eventhander.py
"""

class EventManager:
    def __init__(self):
        from weakref import WeakKeyDictionary
        self.listeners = WeakKeyDictionary()

    def add(self, listener):
        self.listeners[listener] = 1

    def remove(self, listener):
        del self.listeners[listener]

    def post(self, event):
        """
        Post a new Event, will only be broadcast to those that are interested
        """
        print("event %s posted.", event.name)
        for listener in self.listeners.keys():
            if listener.EventKey == event.type:
                listener.Notify(event)
