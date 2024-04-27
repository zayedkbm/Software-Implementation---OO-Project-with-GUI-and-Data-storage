import pickle
import os

CLIENT_FILE_PATH = "clients.bin"


class Client:
    def __init__(self, client_id, name, address, contact_details, budget):
        self.client_id = client_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.budget = budget


class ClientManagement:
    def __init__(self):
        self.clients = self.load_clients()

    def load_clients(self):
        if os.path.exists(CLIENT_FILE_PATH):
            with open(CLIENT_FILE_PATH, "rb") as file:
                return pickle.load(file)
        return {}

    def save_clients(self):
        with open(CLIENT_FILE_PATH, "wb") as file:
            pickle.dump(self.clients, file)

    def add_client(self, client):
        if client.client_id in self.clients:
            raise Exception("Client ID already exists.")
        self.clients[client.client_id] = client
        self.save_clients()

    def delete_client(self, client_id):
        if client_id not in self.clients:
            raise Exception("Client not found.")
        del self.clients[client_id]
        self.save_clients()

    def modify_client(self, client_id, **kwargs):
        if client_id not in self.clients:
            raise Exception("Client not found.")
        client = self.clients[client_id]
        for key, value in kwargs.items():
            if hasattr(client, key):
                setattr(client, key, value)
            else:
                raise Exception(f"{key} is not a valid attribute of Client.")
        self.save_clients()

    def get_client(self, client_id):
        if client_id not in self.clients:
            raise Exception("Client not found.")
        return self.clients[client_id]

    def display_client(self, client_id):
        client = self.get_client(client_id)
        print(f"Client ID: {client.client_id}")
        print(f"Name: {client.name}")
        print(f"Address: {client.address}")
        print(f"Contact Details: {client.contact_details}")
        print(f"Budget: {client.budget}")
