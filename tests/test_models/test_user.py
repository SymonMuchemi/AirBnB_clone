#!/usr/bin/python3
"""Testing the user module"""
from models.user import User
from unittest import TestCase


class TestUser(TestCase):
    """Checking the user model"""
    user = User()

    def test_user_has_id(self):
        """see if the user has an ID from base model"""
        self.assertIsNotNone(self.user.id)

    def test_user_has_no_email(self):
        """user should not have an email address"""
        self.assertEqual(self.user.email, "", "user has no email")

    def test_user_has_no_password(self):
        """user should not have a firstname"""
        self.assertEqual(self.user.password, "", "no password")

    def test_user_has_no_first_name(self):
        """user should not have a firstname"""
        self.assertEqual(self.user.first_name, "", "no first name")

    def test_user_has_no_last_name(self):
        """user should not have a last name"""
        self.assertEqual(self.user.last_name, "", "No last name")
