#!/usr/bin/python3
"""tests for the place class"""
from models.place import Place
from unittest import TestCase


class TestPlace(TestCase):
    """Basecases for the Place class"""
    place = Place()

    def test_place_name(self):
        """place should have no name"""
        self.assertEqual(self.place.name, "", "no name")

    def test_place_user_id(self):
        """should have no user id"""
        self.assertEqual(self.place.user_id, "", "No user Id")

    def test_place_city_id(self):
        """should have no city id"""
        self.assertEqual(self.place.city_id, "", "No city Id")

    def test_place_description(self):
        self.assertEqual(self.place.description, "", "No description")

    def test_place_number_of_bathrooms(self):
        """should be no bathrooms"""
        self.assertEqual(self.place.number_bathrooms, 0, "No bathrooms")

    def test_place_price_by_night(self):
        """price should be 0"""
        self.assertEqual(self.place.price_by_night, 0, "Price is 0")

    def test_place_number_rooms(self):
        """should no rooms"""
        self.assertEqual(self.place.number_rooms, 0, "No rooms")

    def test_place_longitude(self):
        """longitude should be 0"""
        self.assertEqual(self.place.longitude, 0, "Longitude 0")

    def test_place_latitude(self):
        """latitide should be 0"""
        self.assertEqual(self.place.latitude, 0, "Latitude 0")

    def test_place_max_guests(self):
        self.assertEqual(self.place.max_guest, 0, "No guests")

    def test_place_amenity_ids(self):
        """Amenity ids should be empty"""
        self.assertIsInstance(self.place.amenity_ids, list)
        self.assertEqual(len(self.place.amenity_ids), 0, "No amenity ids")
