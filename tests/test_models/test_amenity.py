#!/usr/bin/python3
"""Tests fo the Amenity class"""
from models.amenity import Amenity
from unittest import TestCase


class TestAmenity(TestCase):
    """Basecases for the amenity class"""
    amenity = Amenity()

    def test_amenity_name(self):
        """Name should be an empty string"""
        self.assertIsInstance(self.amenity.name, str, "Name is str")
        self.assertEqual(self.amenity.name, "", "Name is empty")
