#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """ """
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
        