import tkinter as tk
from tkinter import messagebox, ttk
from venue_management import VenueManagement, Venue


class VenueGUI:
    def __init__(self, master):
        self.master = master
        self.venue_management = VenueManagement()
        self.create_widgets()

    def create_widgets(self):
        # Venue ID
        tk.Label(self.master, text="Venue ID:").grid(row=0, column=0, sticky="w")
        self.venue_id_entry = tk.Entry(self.master)
        self.venue_id_entry.grid(row=0, column=1, sticky="we")

        # Name
        tk.Label(self.master, text="Name:").grid(row=1, column=0, sticky="w")
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=1, column=1, sticky="we")

        # Address
        tk.Label(self.master, text="Address:").grid(row=2, column=0, sticky="w")
        self.address_entry = tk.Entry(self.master)
        self.address_entry.grid(row=2, column=1, sticky="we")

        # Contact
        tk.Label(self.master, text="Contact:").grid(row=3, column=0, sticky="w")
        self.contact_entry = tk.Entry(self.master)
        self.contact_entry.grid(row=3, column=1, sticky="we")

        # Minimum Guests
        tk.Label(self.master, text="Minimum Guests:").grid(row=4, column=0, sticky="w")
        self.min_guests_entry = tk.Entry(self.master)
        self.min_guests_entry.grid(row=4, column=1, sticky="we")

        # Maximum Guests
        tk.Label(self.master, text="Maximum Guests:").grid(row=5, column=0, sticky="w")
        self.max_guests_entry = tk.Entry(self.master)
        self.max_guests_entry.grid(row=5, column=1, sticky="we")

        # Buttons for operations
        self.add_button = tk.Button(
            self.master, text="Add Venue", command=self.add_venue
        )
        self.add_button.grid(row=6, column=0, sticky="we")

        self.delete_button = tk.Button(
            self.master, text="Delete Venue", command=self.delete_venue
        )
        self.delete_button.grid(row=6, column=1, sticky="we")

        self.modify_button = tk.Button(
            self.master, text="Modify Venue", command=self.modify_venue
        )
        self.modify_button.grid(row=7, column=0, sticky="we")

        self.display_button = tk.Button(
            self.master, text="Display Venue", command=self.display_venue
        )
        self.display_button.grid(row=7, column=1, sticky="we")

    def add_venue(self):
        venue_id = self.venue_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact = self.contact_entry.get()
        min_guests = self.min_guests_entry.get()
        max_guests = self.max_guests_entry.get()
        try:
            new_venue = Venue(
                venue_id, name, address, contact, int(min_guests), int(max_guests)
            )
            self.venue_management.add_venue(new_venue)
            messagebox.showinfo("Success", "Venue added successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not add venue: {e}")

    def delete_venue(self):
        venue_id = self.venue_id_entry.get()
        try:
            self.venue_management.delete_venue(venue_id)
            messagebox.showinfo("Success", "Venue deleted successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not delete venue: {e}")

    def modify_venue(self):
        venue_id = self.venue_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact = self.contact_entry.get()
        min_guests = self.min_guests_entry.get()
        max_guests = self.max_guests_entry.get()
        try:
            self.venue_management.modify_venue(
                venue_id,
                name=name,
                address=address,
                contact=contact,
                min_guests=int(min_guests),
                max_guests=int(max_guests),
            )
            messagebox.showinfo("Success", "Venue modified successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not modify venue: {e}")

    def display_venue(self):
        venue_id = self.venue_id_entry.get()
        try:
            venue = self.venue_management.get_venue(venue_id)
            venue_info = f"Venue ID: {venue.venue_id}\nName: {venue.name}\nAddress: {venue.address}\nContact: {venue.contact}\nMinimum Guests: {venue.min_guests}\nMaximum Guests: {venue.max_guests}"
            messagebox.showinfo("Venue Details", venue_info)
        except Exception as e:
            messagebox.showerror("Error", f"Could not display venue: {e}")
