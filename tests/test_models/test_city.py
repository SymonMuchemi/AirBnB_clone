#!/usr/bin/python3
"""Tests for the city class"""
from models.city import City
from unittest import TestCase


class TestCity(TestCase):
    """Basecases for the City class"""
    city = City()

    def test_city_name(self):
        """Name should be empty"""
        self.assertIsInstance(self.city.name, str)
        self.assertEqual(self.city.name, "", "Name is empty")

    def test_city_state_id(self):
        """State id should be empty"""
        self.assertIsInstance(self.city.state_id, str, "String data")
        self.assertEqual(self.city.state_id, "", "Empty state id")
