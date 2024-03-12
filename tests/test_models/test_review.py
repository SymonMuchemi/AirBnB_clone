#!/usr/bin/python3
"""Tests for the Review class"""
from models.review import Review
from unittest import TestCase


class TestReview(TestCase):
    """Base cases for the review class"""
    review = Review()

    def test_review_text(self):
        """Text should be an empty string"""
        self.assertIsInstance(self.review.text, str, "Text is str")
        self.assertEqual(self.review.text, "", "Text is empty")

    def test_review_user_id(self):
        """user id should be an empty string"""
        self.assertIsInstance(self.review.user_id, str, "uid is str")
        self.assertEqual(self.review.user_id, "", "uid empty")

    def test_review_place_id(self):
        """place id should be an empty string"""
        self.assertIsInstance(self.review.place_id, str, "PID is str")
        self.assertEqual(self.review.place_id, "", "PID empty")
