#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Base Model Module

This module defines all the common attributes and methods
for other classes. From this module the console will be
able to extract important info as to the unique ID of the object
when it was created and updated.
It will update the public instance attribute updated_at with
the current datetime.
It will return a dictionary containing all keys/values of __dict__ of
the instance

"""

from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """BaseModel class

        This is a  class that innitializes with common attributes
        It also serielizes and deserializes future instances


    Attributes:
        id (str): It is the UUID generated when the instane is created
        created_at (datetime): the date and time when the instance is created
        updated_at (datetime): the date and time wheb the instance is updated

    """

    def __init__(self, id=None, created_at=None, updated_at=None):
        """Base Model __init__ method
            The BaseModel class is innitialized with the given atttributes

        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Returns the string representation of the instance of the class

        Example:
            $ base_model = BaseModel(id, created_at, updated_at)
            $ print(bm)

            The format is:
            $ [<class name>] (<self.id>) <self.__dict__>

        """
        return '[{0}] ({1}) {2}'.format(
                self.__class__.__name__, self.id, self.__dict__
            )

    def save(self):
        """Updates the Base Model Instance datetime

        Updates the class instances with now date

        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """To dictionary making it easy to read class info

        Returns a new dictionary containing all keys/values
        of __dict__ of the instance.

        """
        class_details = self.__dict__.copy()
        class_details['__class__'] = self.__class__.__name__
        class_details['created_at'] = self.created_at.isoformat()
        class_details['updated_at'] = self.updated_at.isoformat()

        return class_details
