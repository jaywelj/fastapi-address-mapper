from pydantic import BaseModel
from typing import Optional


class AddressBase(BaseModel):
    address: str
    latitude: float
    longitude: float


class AddressCreate(AddressBase):
    pass


class AddressUpdate(AddressBase):
    address: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None


class Address(AddressBase):
    id: int

    class Config:
        orm_mode = True
