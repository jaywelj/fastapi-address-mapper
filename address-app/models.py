from geopy import distance
from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.hybrid import hybrid_method

from .database import Base


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

    @hybrid_method
    def distance_in_meters(self, latitude, longitude):

        # Used geopy library to calculate distance between two pair of coordinates
        return distance.distance(
            (self.latitude, self.longitude), (latitude, longitude)
        ).m

