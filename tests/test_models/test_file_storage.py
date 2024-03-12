#!/usr/bin/python3
"""Tests for the file storage class"""
import unittest
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Basecases for the FileStorage class"""
    def setUp(self):
        """Setting up"""
        self.storage = FileStorage()
        self.model1 = BaseModel()
        self.model2 = User()
        self.model3 = State()
        self.model4 = City()
        self.model5 = Review()
        self.model6 = Amenity()
        self.model7 = Place()

    def tearDown(self):
        """tear down operations
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_new(self):
        """This test ensures that the 'new' method properly adds a
        new object to the storage, and that the object
        is retrievable from the storage with the correct key.
        """
        self.storage.new(self.model3)
        all_objects = self.storage.all()
        self.assertIn("State." + self.model3.id, all_objects)
        self.assertEqual(all_objects["State." + self.model3.id], self.model3)


if __name__ == "__main__":
    unittest.main()
