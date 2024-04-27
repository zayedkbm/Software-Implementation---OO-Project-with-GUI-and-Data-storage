import tkinter as tk
from tkinter import messagebox, ttk
from event_management import EventManagement, Event


class EventGUI:
    def __init__(self, master):
        self.master = master
        self.event_management = EventManagement()
        self.create_widgets()

    def create_widgets(self):
        labels = [
            "Event ID:",
            "Type:",
            "Theme:",
            "Date:",
            "Time:",
            "Duration:",
            "Venue Address:",
            "Client ID:",
            "Catering Company:",
            "Cleaning Company:",
            "Decorations Company:",
        ]
        self.entries = {}
        for i, label in enumerate(labels):
            tk.Label(self.master, text=label).grid(row=i, column=0, sticky="w")
            entry = tk.Entry(self.master)
            entry.grid(row=i, column=1, sticky="we")
            self.entries[label.strip(":")] = entry

        operations = [
            ("Add Event", self.add_event),
            ("Delete Event", self.delete_event),
            ("Modify Event", self.modify_event),
            ("Display Event", self.display_event),
        ]
        for i, (text, command) in enumerate(operations, start=len(labels)):
            button = tk.Button(self.master, text=text, command=command)
            button.grid(row=i, columnspan=2, sticky="we")

    def add_event(self):
        try:
            event_data = {key: entry.get() for key, entry in self.entries.items()}

            del event_data["Guest List"]

            new_event = Event(**event_data)
            self.event_management.add_event(new_event)
            messagebox.showinfo("Success", "Event added successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not add event: {e}")

    def delete_event(self):
        event_id = self.entries["Event ID"].get()
        try:
            self.event_management.delete_event(event_id)
            messagebox.showinfo("Success", "Event deleted successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not delete event: {e}")

    def modify_event(self):
        event_id = self.entries["Event ID"].get()
        updates = {
            key: entry.get() for key, entry in self.entries.items() if entry.get()
        }
        try:
            self.event_management.modify_event(event_id, **updates)
            messagebox.showinfo("Success", "Event modified successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not modify event: {e}")

    def display_event(self):
        event_id = self.entries["Event ID"].get()
        try:
            event = self.event_management.get_event(event_id)
            event_info = "\n".join(
                f"{key}: {getattr(event, key.lower().replace(' ', '_'), '')}"
                for key in self.entries
            )
            messagebox.showinfo("Event Details", event_info)
        except Exception as e:
            messagebox.showerror("Error", f"Could not display event: {e}")
