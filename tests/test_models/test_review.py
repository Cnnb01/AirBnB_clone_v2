#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """test case for review class"""

    def __init__(self, *args, **kwargs):
        """review test init"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """tests place id"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """tests user id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """tests text"""
        new = self.value()
        self.assertEqual(type(new.text), str)

    def test_table_name(self):
        """test tablename"""
        self.assertEqual(Review.__tablename__, 'reviews')
