import tkinter as tk
from tkinter import messagebox, ttk
from supplier_management import SupplierManagement, Supplier


class SupplierGUI:
    def __init__(self, master):
        self.master = master
        self.supplier_management = SupplierManagement()
        self.create_widgets()

    def create_widgets(self):
        # Supplier ID
        tk.Label(self.master, text="Supplier ID:").grid(row=0, column=0, sticky="w")
        self.supplier_id_entry = tk.Entry(self.master)
        self.supplier_id_entry.grid(row=0, column=1, sticky="we")

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

        # Service Provided
        tk.Label(self.master, text="Service Provided:").grid(
            row=4, column=0, sticky="w"
        )
        self.service_provided_entry = tk.Entry(self.master)
        self.service_provided_entry.grid(row=4, column=1, sticky="we")

        # Buttons for operations
        self.add_button = tk.Button(
            self.master, text="Add Supplier", command=self.add_supplier
        )
        self.add_button.grid(row=5, column=0, sticky="we")

        self.delete_button = tk.Button(
            self.master, text="Delete Supplier", command=self.delete_supplier
        )
        self.delete_button.grid(row=5, column=1, sticky="we")

        self.modify_button = tk.Button(
            self.master, text="Modify Supplier", command=self.modify_supplier
        )
        self.modify_button.grid(row=6, column=0, sticky="we")

        self.display_button = tk.Button(
            self.master, text="Display Supplier", command=self.display_supplier
        )
        self.display_button.grid(row=6, column=1, sticky="we")

    def add_supplier(self):
        supplier_id = self.supplier_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_details_entry.get()
        service_provided = self.service_provided_entry.get()
        try:
            new_supplier = Supplier(
                supplier_id, name, address, contact_details, service_provided
            )
            self.supplier_management.add_supplier(new_supplier)
            messagebox.showinfo("Success", "Supplier added successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not add supplier: {e}")

    def delete_supplier(self):
        supplier_id = self.supplier_id_entry.get()
        try:
            self.supplier_management.delete_supplier(supplier_id)
            messagebox.showinfo("Success", "Supplier deleted successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not delete supplier: {e}")

    def modify_supplier(self):
        supplier_id = self.supplier_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_details_entry.get()
        service_provided = self.service_provided_entry.get()
        try:
            self.supplier_management.modify_supplier(
                supplier_id,
                name=name,
                address=address,
                contact_details=contact_details,
                service_provided=service_provided,
            )
            messagebox.showinfo("Success", "Supplier modified successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not modify supplier: {e}")

    def display_supplier(self):
        supplier_id = self.supplier_id_entry.get()
        try:
            supplier = self.supplier_management.get_supplier(supplier_id)
            supplier_info = f"Supplier ID: {supplier.supplier_id}\nName: {supplier.name}\nAddress: {supplier.address}\nContact Details: {supplier.contact_details}\nService Provided: {supplier.service_provided}"
            messagebox.showinfo("Supplier Details", supplier_info)
        except Exception as e:
            messagebox.showerror("Error", f"Could not display supplier: {e}")
