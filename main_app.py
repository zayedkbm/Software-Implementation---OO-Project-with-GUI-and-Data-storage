import tkinter as tk
from tkinter import ttk

from client_gui import ClientGUI
from employee_gui import EmployeeGUI
from event_gui import EventGUI
from guest_gui import GuestGUI
from supplier_gui import SupplierGUI
from venue_gui import VenueGUI


class ManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Events Company Management System")
        self.geometry("500x400")

        self.tab_control = ttk.Notebook(self)
        self.init_tabs()
        self.tab_control.pack(expand=1, fill="both")

    def init_tabs(self):
        self.client_tab = ttk.Frame(self.tab_control)
        self.client_gui = ClientGUI(self.client_tab)
        self.client_tab.pack(fill="both", expand=True)
        self.tab_control.add(self.client_tab, text="Clients")

        # Employee Tab
        self.employee_tab = ttk.Frame(self.tab_control)
        self.employee_gui = EmployeeGUI(self.employee_tab)
        self.employee_tab.pack(fill="both", expand=True)
        self.tab_control.add(self.employee_tab, text="Employees")

        # Event Tab
        self.event_tab = ttk.Frame(self.tab_control)
        self.event_gui = EventGUI(self.event_tab)
        self.event_tab.pack(fill="both", expand=True)
        self.tab_control.add(self.event_tab, text="Events")

        # Guest Tab
        self.guest_tab = ttk.Frame(self.tab_control)
        self.guest_gui = GuestGUI(self.guest_tab)
        self.guest_tab.pack(fill="both", expand=True)
        self.tab_control.add(self.guest_tab, text="Guests")

        # Supplier Tab
        self.supplier_tab = ttk.Frame(self.tab_control)
        self.supplier_gui = SupplierGUI(self.supplier_tab)
        self.supplier_tab.pack(fill="both", expand=True)
        self.tab_control.add(self.supplier_tab, text="Suppliers")

        # Venue Tab
        self.venue_tab = ttk.Frame(self.tab_control)
        self.venue_gui = VenueGUI(self.venue_tab)
        self.venue_tab.pack(fill="both", expand=True)
        self.tab_control.add(self.venue_tab, text="Venues")


if __name__ == "__main__":
    app = ManagementApp()
    app.mainloop()
