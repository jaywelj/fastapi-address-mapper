from pydantic import BaseModel
from typing import Optional


class AddressBase(BaseModel):
    address: str
    latitude: float
    longitude: float


class AddressCreate(AddressBase):
    pass


class Address(AddressBase):
    id: int

    class Config:
        orm_mode = True
