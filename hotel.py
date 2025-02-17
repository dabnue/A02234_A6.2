import json
import os
import unittest
from typing import Dict

class Hotel:
    FILE_PATH = "hotels.json"

    def __init__(self, hotel_id: int, name: str, location: str, rooms: int):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.rooms = rooms
        self.reservations = []

    def save_to_file(self):
        hotels = self.load_from_file()
        if not isinstance(hotels, dict):
            hotels = {}
        hotels[str(self.hotel_id)] = self.__dict__
        with open(self.FILE_PATH, "w") as file:
            json.dump(hotels, file, indent=4)

    @classmethod
    def load_from_file(cls) -> Dict:
        if not os.path.exists(cls.FILE_PATH):
            with open(cls.FILE_PATH, "w") as file:
                json.dump({}, file)
            return {}
        try:
            with open(cls.FILE_PATH, "r") as file:
                data = json.load(file)
                return data if isinstance(data, dict) else {}
        except (json.JSONDecodeError, IOError):
            print("Error loading hotel data.")
            return {}

    @classmethod
    def delete_hotel(cls, hotel_id: int):
        hotels = cls.load_from_file()
        if str(hotel_id) in hotels:
            del hotels[str(hotel_id)]
            with open(cls.FILE_PATH, "w") as file:
                json.dump(hotels, file, indent=4)

    @classmethod
    def modify_hotel(cls, hotel_id: int, name: str, location: str, rooms: int):
        hotels = cls.load_from_file()
        if str(hotel_id) in hotels:
            hotels[str(hotel_id)]["name"] = name
            hotels[str(hotel_id)]["location"] = location
            hotels[str(hotel_id)]["rooms"] = rooms
            with open(cls.FILE_PATH, "w") as file:
                json.dump(hotels, file, indent=4)

class Customer:
    FILE_PATH = "customers.json"

    def __init__(self, customer_id: int, name: str, email: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def save_to_file(self):
        customers = self.load_from_file()
        if not isinstance(customers, dict):
            customers = {}
        customers[str(self.customer_id)] = self.__dict__
        with open(self.FILE_PATH, "w") as file:
            json.dump(customers, file, indent=4)

    @classmethod
    def load_from_file(cls) -> Dict:
        if not os.path.exists(cls.FILE_PATH):
            with open(cls.FILE_PATH, "w") as file:
                json.dump({}, file)
            return {}
        try:
            with open(cls.FILE_PATH, "r") as file:
                data = json.load(file)
                return data if isinstance(data, dict) else {}
        except (json.JSONDecodeError, IOError):
            print("Error loading customer data.")
            return {}

    @classmethod
    def delete_customer(cls, customer_id: int):
        customers = cls.load_from_file()
        if str(customer_id) in customers:
            del customers[str(customer_id)]
            with open(cls.FILE_PATH, "w") as file:
                json.dump(customers, file, indent=4)

    @classmethod
    def modify_customer(cls, customer_id: int, name: str, email: str):
        customers = cls.load_from_file()
        if str(customer_id) in customers:
            customers[str(customer_id)]["name"] = name
            customers[str(customer_id)]["email"] = email
            with open(cls.FILE_PATH, "w") as file:
                json.dump(customers, file, indent=4)

class Reservation:
    FILE_PATH = "reservations.json"

    def __init__(self, reservation_id: int, hotel_id: int, customer_id: int):
        self.reservation_id = reservation_id
        self.hotel_id = hotel_id
        self.customer_id = customer_id

    def save_to_file(self):
        reservations = self.load_from_file()
        if not isinstance(reservations, dict):
            reservations = {}
        reservations[str(self.reservation_id)] = self.__dict__
        with open(self.FILE_PATH, "w") as file:
            json.dump(reservations, file, indent=4)

    @classmethod
    def load_from_file(cls) -> Dict:
        if not os.path.exists(cls.FILE_PATH):
            with open(cls.FILE_PATH, "w") as file:
                json.dump({}, file)
            return {}
        try:
            with open(cls.FILE_PATH, "r") as file:
                data = json.load(file)
                return data if isinstance(data, dict) else {}
        except (json.JSONDecodeError, IOError):
            print("Error loading reservation data.")
            return {}

    @classmethod
    def delete_reservation(cls, reservation_id: int):
        reservations = cls.load_from_file()
        if str(reservation_id) in reservations:
            del reservations[str(reservation_id)]
            with open(cls.FILE_PATH, "w") as file:
                json.dump(reservations, file, indent=4)

# Unit Tests
class TestHotelSystem(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel(1, "Grand Hotel", "New York", 100)
        self.customer = Customer(1, "John Doe", "johndoe@example.com")
        self.reservation = Reservation(1, 1, 1)
        self.hotel.save_to_file()
        self.customer.save_to_file()

    def test_hotel_creation(self):
        hotels = Hotel.load_from_file()
        self.assertIn("1", hotels)

    def test_customer_creation(self):
        customers = Customer.load_from_file()
        self.assertIn("1", customers)

    def test_reservation_creation(self):
        self.reservation.save_to_file()
        reservations = Reservation.load_from_file()
        self.assertIn("1", reservations)

    def test_hotel_deletion(self):
        Hotel.delete_hotel(1)
        hotels = Hotel.load_from_file()
        self.assertNotIn("1", hotels)

    def test_customer_deletion(self):
        Customer.delete_customer(1)
        customers = Customer.load_from_file()
        self.assertNotIn("1", customers)

    def test_reservation_deletion(self):
        self.reservation.save_to_file()
        Reservation.delete_reservation(1)
        reservations = Reservation.load_from_file()
        self.assertNotIn("1", reservations)

    def test_hotel_modification(self):
        Hotel.modify_hotel(1, "Updated Hotel", "Los Angeles", 200)
        hotels = Hotel.load_from_file()
        self.assertEqual(hotels["1"]["name"], "Updated Hotel")

    def test_customer_modification(self):
        Customer.modify_customer(1, "Jane Doe", "janedoe@example.com")
        customers = Customer.load_from_file()
        self.assertEqual(customers["1"]["name"], "Jane Doe")

if __name__ == "__main__":
    unittest.main()