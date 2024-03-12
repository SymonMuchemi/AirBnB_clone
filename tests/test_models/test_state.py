#!/usr/bin/python3
"""Test the State class"""
from models.state import State
from unittest import TestCase


class TestState(TestCase):
    """Basecases for the States class"""
    state = State()

    def test_state_name(self):
        """Should have no name"""
        self.assertIsInstance(self.state.name, str, "Name is a string")
        self.assertEqual(self.state.name, "", "Name is empty")
