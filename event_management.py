import pickle
import os

EVENT_FILE_PATH = "events.bin"


class Event:
    def __init__(
        self,
        event_id,
        event_type,
        theme,
        date,
        time,
        duration,
        venue_address,
        client_id,
        guest_list,
        catering_company,
        cleaning_company,
        decorations_company,
        entertainment_company,
        furniture_supply_company,
        invoice,
    ):
        self.event_id = event_id
        self.event_type = event_type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue_address = venue_address
        self.client_id = client_id
        self.guest_list = guest_list
        self.catering_company = catering_company
        self.cleaning_company = cleaning_company
        self.decorations_company = decorations_company
        self.entertainment_company = entertainment_company
        self.furniture_supply_company = furniture_supply_company
        self.invoice = invoice


class EventManagement:
    def __init__(self):
        self.events = self.load_events()

    def load_events(self):
        if os.path.exists(EVENT_FILE_PATH):
            with open(EVENT_FILE_PATH, "rb") as file:
                return pickle.load(file)
        return {}

    def save_events(self):
        with open(EVENT_FILE_PATH, "wb") as file:
            pickle.dump(self.events, file)

    def add_event(self, event):
        if event.event_id in self.events:
            raise Exception("Event ID already exists.")
        self.events[event.event_id] = event
        self.save_events()

    def delete_event(self, event_id):
        if event_id not in self.events:
            raise Exception("Event not found.")
        del self.events[event_id]
        self.save_events()

    def modify_event(self, event_id, **kwargs):
        if event_id not in self.events:
            raise Exception("Event not found.")
        event = self.events[event_id]
        for key, value in kwargs.items():
            if hasattr(event, key):
                setattr(event, key, value)
            else:
                raise Exception(f"{key} is not a valid attribute of Event.")
        self.save_events()

    def get_event(self, event_id):
        if event_id not in self.events:
            raise Exception("Event not found.")
        return self.events[event_id]

    def display_event(self, event_id):
        event = self.get_event(event_id)
        print(f"Event ID: {event.event_id}")
        print(f"Type: {event.event_type}")
        print(f"Theme: {event.theme}")
        print(f"Date: {event.date}")
        print(f"Time: {event.time}")
        print(f"Duration: {event.duration}")
        print(f"Venue Address: {event.venue_address}")
        print(f"Client ID: {event.client_id}")
        print("Guest List:")
        for guest in event.guest_list:
            print(f" - {guest}")
        print(f"Catering Company: {event.catering_company}")
        print(f"Cleaning Company: {event.cleaning_company}")
        print(f"Decorations Company: {event.decorations_company}")
        print(f"Entertainment Company: {event.entertainment_company}")
        print(f"Furniture Supply Company: {event.furniture_supply_company}")
        print(f"Invoice: {event.invoice}")
