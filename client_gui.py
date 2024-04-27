import tkinter as tk
from tkinter import messagebox
from client_management import ClientManagement, Client


class ClientGUI:
    def __init__(self, master):
        self.master = master
        self.client_management = ClientManagement()
        self.create_widgets()

    def create_widgets(self):
        # Client ID
        tk.Label(self.master, text="Client ID:").grid(row=0, column=0, sticky="w")
        self.client_id_entry = tk.Entry(self.master)
        self.client_id_entry.grid(row=0, column=1, sticky="we")

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

        # Budget
        tk.Label(self.master, text="Budget:").grid(row=4, column=0, sticky="w")
        self.budget_entry = tk.Entry(self.master)
        self.budget_entry.grid(row=4, column=1, sticky="we")

        # Buttons
        self.add_button = tk.Button(
            self.master, text="Add Client", command=self.add_client
        )
        self.add_button.grid(row=5, column=0, sticky="we")

        self.delete_button = tk.Button(
            self.master, text="Delete Client", command=self.delete_client
        )
        self.delete_button.grid(row=5, column=1, sticky="we")

        self.modify_button = tk.Button(
            self.master, text="Modify Client", command=self.modify_client
        )
        self.modify_button.grid(row=6, column=0, sticky="we")

        self.display_button = tk.Button(
            self.master, text="Display Client", command=self.display_client
        )
        self.display_button.grid(row=6, column=1, sticky="we")

    def add_client(self):
        client_id = self.client_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_details_entry.get()
        budget = self.budget_entry.get()
        try:
            budget = float(budget)
            client = Client(client_id, name, address, contact_details, budget)
            self.client_management.add_client(client)
            messagebox.showinfo("Success", "Client added successfully.")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_client(self):
        client_id = self.client_id_entry.get()
        try:
            self.client_management.delete_client(client_id)
            messagebox.showinfo("Success", "Client deleted successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def modify_client(self):
        client_id = self.client_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_details_entry.get()
        budget = self.budget_entry.get()
        try:
            budget = float(budget)
            self.client_management.modify_client(
                client_id,
                name=name,
                address=address,
                contact_details=contact_details,
                budget=budget,
            )
            messagebox.showinfo("Success", "Client modified successfully.")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def display_client(self):
        client_id = self.client_id_entry.get()
        try:
            client = self.client_management.get_client(client_id)
            info = f"Client ID: {client.client_id}\nName: {client.name}\nAddress: {client.address}\nContact Details: {client.contact_details}\nBudget: {client.budget}"
            messagebox.showinfo("Client Details", info)
        except Exception as e:
            messagebox.showerror("Error", str(e))
