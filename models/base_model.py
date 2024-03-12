#!/usr/bin/python3
"""Blueprint for other models"""
import uuid
from datetime import datetime

date_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """parent model
    """
    def __init__(self, *args, **kwargs):
        """the model blueprint
        """
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            for key, val in kwargs.items():
                if key == "id":
                    self.id = val
                if key == "created_at":
                    self.created_at = datetime.strptime(val, date_format)
                if key == "updated_at":
                    self.updated_at = datetime.strptime(val, date_format)

    def __str__(self):
        """gives a string representation of the BaseModel instance

        Returns:
            str: short representation
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the 'updated_at' attribute to the current time
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """converts 'created_at' and 'updated_at' attributes to ISO format,
        adds a __class__ attribute to the instance dictionary

        Returns:
            dict: the instance dictionary
        """
        self.__dict__["__class__"] = self.__class__.__name__
        self.created_at = self.created_at.strftime(date_format)
        self.updated_at = self.updated_at.strftime(date_format)

        return self.__dict__
