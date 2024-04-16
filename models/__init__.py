#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
import os
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity

# storage = FileStorage()
# storage.reload()
storage_type = os.getenv('HBNB_TYPE_STORAGE')
if storage_type == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
