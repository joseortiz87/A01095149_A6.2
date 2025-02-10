import unittest
from reservation_system import Hotel, Customer, Reservation

class TestHotelReservationSystem(unittest.TestCase):
    def setUp(self):
        # Initialize test data
        self.hotel1 = Hotel("H1", "Hacienda Santo Cristo", "PUE", 30)
        self.hotel2 = Hotel("H2", "Hotel La Aldea", "PUE", 40)
        self.hotel3 = Hotel("H3", "Luna Canela", "PUE", 25)
        
        self.customer1 = Customer("C1", "Jose Ortiz", "jose@example.com")
        self.customer2 = Customer("C2", "Juan Perez", "juan@example.com")
        self.customer3 = Customer("C3", "Valeria Pena", "valeria@example.com")

        self.reservation1 = Reservation("R1", "C1", "H1", "2025-02-10", "2025-02-15")
        self.reservation2 = Reservation("R2", "C2", "H2", "2025-02-12", "2025-02-18")
        
    def test_create_hotel(self):
        Hotel.create_hotel("H4", "New Hotel", "PUE", 20)
        hotels = Hotel.display_hotels()
        self.assertTrue(any(h["hotel_id"] == "H4" for h in hotels))

    def test_reserve_room(self):
        initial_rooms = self.hotel1.rooms_available
        Hotel.reserve_room("H1")
        hotels = Hotel.display_hotels()
        updated_rooms = next(h["rooms_available"] for h in hotels if h["hotel_id"] == "H1")
        self.assertEqual(updated_rooms, initial_rooms - 1)

    def test_cancel_reservation(self):
        # Create reservation to cancel
        Reservation.create_reservation("R1", "C1", "H1", "2025-02-10", "2025-02-15")
        
        # Cancel the reservation
        Reservation.cancel_reservation("R1")

        # Reload reservations to check status update
        reservations = Reservation.load_from_file()
        status = next(r["status"] for r in reservations if r["reservation_id"] == "R1")
        self.assertEqual(status, "Canceled")

    def test_modify_customer(self):
        # Create a Customer for modification
        Customer.create_customer("C1", "Jose Ortiz", "jose@example.com")

        # Modify customer email
        Customer.modify_customer("C1", {"email": "new_email@example.com"})

        # Reload customer data to check the modification
        customers = Customer.display_customers()
        updated_email = next(c["email"] for c in customers if c["customer_id"] == "C1")
        self.assertEqual(updated_email, "new_email@example.com")
    
    def test_reserve_room(self):
        # New hotel for the reservation
        Hotel.create_hotel("H1", "Hacienda Santo Cristo", "PUE", 30)

        initial_rooms = next(h["rooms_available"] for h in Hotel.display_hotels() if h["hotel_id"] == "H1")

        # Reserve a room
        Hotel.reserve_room("H1")

        # Reload the hotel data and verify the room count
        hotels = Hotel.display_hotels()
        updated_rooms = next(h["rooms_available"] for h in hotels if h["hotel_id"] == "H1")

        self.assertEqual(updated_rooms, initial_rooms - 1)

    def test_load_from_file_invalid_json(self):
        with open(Hotel.FILE_PATH, "w") as file:
            file.write("INVALID JSON")
        hotels = Hotel.load_from_file()
        self.assertEqual(hotels, [])

    def test_cancel_reservation_invalid_hotel(self):
        result = Hotel.cancel_reservation("H999")
        self.assertFalse(result)

    def test_delete_hotel(self):
        Hotel.delete_hotel("H1")
        hotels = Hotel.display_hotels()
        self.assertFalse(any(h["hotel_id"] == "H1" for h in hotels))
    
    def test_delete_nonexistent_hotel(self):
        initial_hotels = Hotel.display_hotels()
        Hotel.delete_hotel("H999")
        updated_hotels = Hotel.display_hotels()
        self.assertEqual(initial_hotels, updated_hotels)

    def test_modify_hotel(self):
        # New hotel to be modify
        Hotel.create_hotel("H1", "Hacienda", "PUE", 30)

        Hotel.modify_hotel("H1", {"name": "Updated Hacienda"})
        hotels = Hotel.display_hotels()
        updated_name = next(h["name"] for h in hotels if h["hotel_id"] == "H1")
        self.assertEqual(updated_name, "Updated Hacienda")
    
    def test_modify_nonexistent_hotel(self):
        initial_hotels = Hotel.display_hotels()
        Hotel.modify_hotel("H999", {"name": "Ghost Hotel"})
        updated_hotels = Hotel.display_hotels()
        self.assertEqual(initial_hotels, updated_hotels)

if __name__ == "__main__":
    unittest.main()
