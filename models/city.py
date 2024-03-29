#!/usr/bin/python3
"""The `city` module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """A city in the application.

    Attributes:
        name
        state_id
    """
    name = ""
    state_id = ""
