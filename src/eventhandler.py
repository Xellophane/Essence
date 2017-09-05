import events

"""
eventhander.py

The basis of the EventManager. To allow the seperation of the main loop from
model, view, and controller.
"""

class EventManager:
    def __init__(self):
        # import WeakKeyDictionary, to allow for easy removal of listeners
        # when they no longer exist (ie, I don't have to manualy remove them)
        from weakref import WeakKeyDictionary
        self.listeners = WeakKeyDictionary()

    def add(self, listener):
        # register a listener so that events can be given to them
        self.listeners[listener] = 1

    def remove(self, listener):
        # remove a listener, for completeness sake
        del self.listeners[listener]

    def post(self, event):
        """
        Go through all the listeners and for those interested via EventKey,
        notify them of the event
        """
        # print("event '", event.Name, "' posted")
        for listener in self.listeners.keys():
            if listener.EVENTKEY == event.Key:
                listener.Notify(event)
