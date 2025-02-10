"""
Reservation System Module

This module provides classes for managing hotels, customers, and reservations.
"""
import json
import os


class Hotel:
    """Class representing a hotel entity."""
    FILE_PATH = "hotels.json"

    def __init__(self, hotel_id, name, location, rooms_available):
        """Initialize a hotel with ID, name, location, and rooms."""
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.rooms_available = rooms_available

    def to_dict(self):
        """Convert hotel object to json."""
        return {
            "hotel_id": self.hotel_id,
            "name": self.name,
            "location": self.location,
            "rooms_available": self.rooms_available
        }

    @classmethod
    def save_to_file(cls, data):
        """Save hotel data to a file."""
        with open(cls.FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    @classmethod
    def load_from_file(cls):
        """Load hotel data from a file."""
        if not os.path.exists(cls.FILE_PATH):
            return []
        try:
            with open(cls.FILE_PATH, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    @classmethod
    def create_hotel(cls, hotel_id, name, location, rooms_available):
        """Create a new hotel entry."""
        hotels = cls.load_from_file()
        hotels.append({"hotel_id": hotel_id, "name": name,
                       "location": location,
                       "rooms_available": rooms_available})
        cls.save_to_file(hotels)

    @classmethod
    def delete_hotel(cls, hotel_id):
        """Delete hotel entry."""
        hotels = cls.load_from_file()
        hotels = [hotel for hotel in hotels if hotel["hotel_id"] != hotel_id]
        cls.save_to_file(hotels)

    @classmethod
    def display_hotels(cls):
        """Display hotels."""
        return cls.load_from_file()

    @classmethod
    def modify_hotel(cls, hotel_id, new_data):
        """Update hotels."""
        hotels = cls.load_from_file()
        for hotel in hotels:
            if hotel["hotel_id"] == hotel_id:
                hotel.update(new_data)
        cls.save_to_file(hotels)

    @classmethod
    def reserve_room(cls, hotel_id):
        """Reserve hotels."""
        hotels = cls.load_from_file()
        for hotel in hotels:
            if hotel["hotel_id"] == hotel_id and hotel["rooms_available"] > 0:
                hotel["rooms_available"] -= 1
                cls.save_to_file(hotels)
                return True
        return False

    @classmethod
    def cancel_reservation(cls, hotel_id):
        """Cancel hotel reservation."""
        hotels = cls.load_from_file()
        for hotel in hotels:
            if hotel["hotel_id"] == hotel_id:
                hotel["rooms_available"] += 1
                cls.save_to_file(hotels)
                return True
        return False


class Customer:
    """Class representing a customer entity."""
    FILE_PATH = "customers.json"

    def __init__(self, customer_id, name, email):
        """Initialize a customer with ID, name, and email."""
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def to_dict(self):
        """Convert customer object to json."""
        return {"customer_id": self.customer_id,
                "name": self.name,
                "email": self.email}

    @classmethod
    def save_to_file(cls, data):
        """Save customer data to a file."""
        with open(cls.FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    @classmethod
    def load_from_file(cls):
        """Load customer data from a file."""
        if not os.path.exists(cls.FILE_PATH):
            return []
        try:
            with open(cls.FILE_PATH, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    @classmethod
    def create_customer(cls, customer_id, name, email):
        """Create a new customer entry."""
        customers = cls.load_from_file()
        customers.append({"customer_id": customer_id,
                          "name": name,
                          "email": email})
        cls.save_to_file(customers)

    @classmethod
    def delete_customer(cls, customer_id):
        """Delete customer entry."""
        customers = cls.load_from_file()
        customers = [cust for cust in customers
                     if cust["customer_id"] != customer_id]
        cls.save_to_file(customers)

    @classmethod
    def display_customers(cls):
        """Display customers."""
        return cls.load_from_file()

    @classmethod
    def modify_customer(cls, customer_id, new_data):
        """Update customer by Id."""
        customers = cls.load_from_file()
        for customer in customers:
            if customer["customer_id"] == customer_id:
                customer.update(new_data)
        cls.save_to_file(customers)


class Reservation:
    """Class representing a reservation entity."""
    FILE_PATH = "reservations.json"

    def __init__(self, reservation_id, customer_id,
                 hotel_id, start_date, end_date, status="Active"):
        """Initialize a reservation with details."""
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id
        self.start_date = start_date
        self.end_date = end_date
        self.status = status

    def to_dict(self):
        """Convert reservation object to json."""
        return {
            "reservation_id": self.reservation_id,
            "customer_id": self.customer_id,
            "hotel_id": self.hotel_id,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "status": self.status
        }

    @classmethod
    def save_to_file(cls, data):
        """Save reservation data to a file."""
        with open(cls.FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    @classmethod
    def load_from_file(cls):
        """Fetch reservation data from file."""
        if not os.path.exists(cls.FILE_PATH):
            return []
        try:
            with open(cls.FILE_PATH, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    @classmethod
    def create_reservation(cls, reservation_id,
                           customer_id, hotel_id,
                           start_date, end_date):
        """Create a new reservation."""
        reservations = cls.load_from_file()
        reservations.append({"reservation_id": reservation_id,
                             "customer_id": customer_id,
                             "hotel_id": hotel_id,
                             "start_date": start_date,
                             "end_date": end_date,
                             "status": "Active"})
        cls.save_to_file(reservations)

    @classmethod
    def cancel_reservation(cls, reservation_id):
        """Cancel a reservation."""
        reservations = cls.load_from_file()
        for reservation in reservations:
            if reservation["reservation_id"] == reservation_id:
                reservation["status"] = "Canceled"
        cls.save_to_file(reservations)
