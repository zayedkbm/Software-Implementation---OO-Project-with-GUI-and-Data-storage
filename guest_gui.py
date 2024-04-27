import tkinter as tk
from tkinter import messagebox, ttk
from guest_management import GuestManagement, Guest


class GuestGUI:
    def __init__(self, master):
        self.master = master
        self.guest_management = GuestManagement()
        self.create_widgets()

    def create_widgets(self):
        # Guest ID
        tk.Label(self.master, text="Guest ID:").grid(row=0, column=0, sticky="w")
        self.guest_id_entry = tk.Entry(self.master)
        self.guest_id_entry.grid(row=0, column=1, sticky="we")

        # Name
        tk.Label(self.master, text="Name:").grid(row=1, column=0, sticky="w")
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=1, column=1, sticky="we")

        # Address
        tk.Label(self.master, text="Address:").grid(row=2, column=0, sticky="w")
        self.address_entry = tk.Entry(self.master)
        self.address_entry.grid(row=2, column=1, sticky="we")

        # Contact Details
        tk.Label(self.master, text="Contact Details:").grid(row=3, column=0, sticky="w")
        self.contact_details_entry = tk.Entry(self.master)
        self.contact_details_entry.grid(row=3, column=1, sticky="we")

        # Buttons for operations
        self.add_button = tk.Button(
            self.master, text="Add Guest", command=self.add_guest
        )
        self.add_button.grid(row=4, column=0, sticky="we")

        self.delete_button = tk.Button(
            self.master, text="Delete Guest", command=self.delete_guest
        )
        self.delete_button.grid(row=4, column=1, sticky="we")

        self.modify_button = tk.Button(
            self.master, text="Modify Guest", command=self.modify_guest
        )
        self.modify_button.grid(row=5, column=0, sticky="we")

        self.display_button = tk.Button(
            self.master, text="Display Guest", command=self.display_guest
        )
        self.display_button.grid(row=5, column=1, sticky="we")

    def add_guest(self):
        guest_id = self.guest_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_details_entry.get()
        try:
            new_guest = Guest(guest_id, name, address, contact_details)
            self.guest_management.add_guest(new_guest)
            messagebox.showinfo("Success", "Guest added successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not add guest: {e}")

    def delete_guest(self):
        guest_id = self.guest_id_entry.get()
        try:
            self.guest_management.delete_guest(guest_id)
            messagebox.showinfo("Success", "Guest deleted successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not delete guest: {e}")

    def modify_guest(self):
        guest_id = self.guest_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_details_entry.get()
        try:
            self.guest_management.modify_guest(
                guest_id, name=name, address=address, contact_details=contact_details
            )
            messagebox.showinfo("Success", "Guest modified successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not modify guest: {e}")

    def display_guest(self):
        guest_id = self.guest_id_entry.get()
        try:
            guest = self.guest_management.get_guest(guest_id)
            guest_info = f"Guest ID: {guest.guest_id}\nName: {guest.name}\nAddress: {guest.address}\nContact Details: {guest.contact_details}"
            messagebox.showinfo("Guest Details", guest_info)
        except Exception as e:
            messagebox.showerror("Error", f"Could not display guest: {e}")
