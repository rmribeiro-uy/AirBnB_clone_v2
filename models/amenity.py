#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """Amenities class"""
    if models.typestorage == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)

    else:
        name = ""
