#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """test case for place class"""

    def __init__(self, *args, **kwargs):
        """place test init"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """tests city id"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """tests user id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """tests name"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """tests description"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """tests number rooms"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """tests number bathrooms"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """tests max guests"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """test case for price by night"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """tests latitude"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """tests longitude"""
        new = self.value()
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """tets amenity id"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

    def test_reviews_relationship(self):
        """Test the relationship between Place and Review"""
        place = self.value()
        review1 = Review(place_id=place.id)
        review2 = Review(place_id=place.id)
        self.assertIn(review1, place.reviews)
        self.assertIn(review2, place.reviews)

    def test_amenities_relationship(self):
        """Test the relationship between Place and Amenity"""
        place = self.value()
        amenity1 = Amenity()
        amenity2 = Amenity()
        place.amenities.append(amenity1)
        place.amenities.append(amenity2)
        self.assertIn(amenity1, place.amenities)
        self.assertIn(amenity2, place.amenities)

    def test_amenities_setter(self):
        """Test the amenities setter method"""
        place = self.value()
        amenity = Amenity()
        place.amenities = amenity
        self.assertIn(amenity, place.amenities)
