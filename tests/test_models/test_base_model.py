#!/usr/bin/python3
"""unit testing the BaseModel class"""
from models.base_model import BaseModel
from unittest import TestCase


class TestBaseModel(TestCase):
    """Tests for the base model"""
    baseModel = BaseModel()
    
    def test_empty_initialization(self):
        """check to see the if module attributes exists
        """
        self.assertIsNotNone(self.baseModel.created_at)
        self.assertIsNotNone(self.baseModel.updated_at)
        self.assertIsNotNone(self.baseModel.id)
        
    def test_str(self):
        """test that the __str__ method returns the correct description
        of the instance model
        """
        class_name = "BaseModel"
        model_id = self.baseModel.id
        model_dict = self.baseModel.__dict__
        
        model_string_rep = f"[{class_name}] ({model_id}) {model_dict}"
        
        self.assertEqual(model_string_rep, self.baseModel.__str__())
        
    def test_to_dict(self):
        
        model_dict = self.baseModel.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIsNotNone(model_dict)
        self.assertIsNotNone(model_dict["__class__"])
        self.assertIsNotNone(model_dict["id"])
        self.assertIsNotNone(model_dict["created_at"])
        self.assertIsNotNone(model_dict["updated_at"])
