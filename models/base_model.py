#!/usr/bin/python3
"""Blueprint for other models"""
import uuid
from datetime import datetime


class BaseModel:
    """parent model
    """
    def __init__(self):
        """the model blueprint
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        
    def __str__(self):
        """gives a string representation of the BaseModel instance

        Returns:
            str: short representation
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        
    def save(self):
        """updates the 'updated_at' attribute to the current time
        """
        self.updated_at = datetime.now()
        
    def to_dict(self):
        """converts 'created_at' and 'updated_at' attributes to ISO format,
        adds a __class__ attribute to the instance dictionary

        Returns:
            dict: the instance dictionary
        """
        self.__dict__["__class__"] = self.__class__.__name__
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        
        return self.__dict__
