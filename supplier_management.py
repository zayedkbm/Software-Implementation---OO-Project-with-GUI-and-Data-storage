import pickle
import os

SUPPLIER_FILE_PATH = "suppliers.bin"


class Supplier:
    def __init__(self, supplier_id, name, address, contact_details, service_provided):
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.service_provided = service_provided


class SupplierManagement:
    def __init__(self):
        self.suppliers = self.load_suppliers()

    def load_suppliers(self):
        if os.path.exists(SUPPLIER_FILE_PATH):
            with open(SUPPLIER_FILE_PATH, "rb") as file:
                return pickle.load(file)
        return {}

    def save_suppliers(self):
        with open(SUPPLIER_FILE_PATH, "wb") as file:
            pickle.dump(self.suppliers, file)

    def add_supplier(self, supplier):
        if supplier.supplier_id in self.suppliers:
            raise Exception("Supplier ID already exists.")
        self.suppliers[supplier.supplier_id] = supplier
        self.save_suppliers()

    def delete_supplier(self, supplier_id):
        if supplier_id not in self.suppliers:
            raise Exception("Supplier not found.")
        del self.suppliers[supplier_id]
        self.save_suppliers()

    def modify_supplier(self, supplier_id, **kwargs):
        if supplier_id not in self.suppliers:
            raise Exception("Supplier not found.")
        supplier = self.suppliers[supplier_id]
        for key, value in kwargs.items():
            if hasattr(supplier, key):
                setattr(supplier, key, value)
            else:
                raise Exception(f"{key} is not a valid attribute of Supplier.")
        self.save_suppliers()

    def get_supplier(self, supplier_id):
        if supplier_id not in self.suppliers:
            raise Exception("Supplier not found.")
        return self.suppliers[supplier_id]

    def display_supplier(self, supplier_id):
        supplier = self.get_supplier(supplier_id)
        print(f"Supplier ID: {supplier.supplier_id}")
        print(f"Name: {supplier.name}")
        print(f"Address: {supplier.address}")
        print(f"Contact Details: {supplier.contact_details}")
        print(f"Service Provided: {supplier.service_provided}")
