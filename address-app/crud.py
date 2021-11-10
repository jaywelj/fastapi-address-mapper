from sqlalchemy.orm import Session
from . import models, schemas


def get_address(db: Session, address_id: int):
    return db.query(models.Address).filter(models.Address.id == address_id).first()


def get_address_by_coordinates(db: Session, longitude: float, latitude: float):
    return db.query(models.Address).filter(
        models.Address.latitude == latitude,
        models.Address.longitude == longitude,
    ).first()


def get_addresses(
        db: Session,
        latitude: float,
        longitude: float,
        distance_in_meters: float,
        skip: int = 0,
        limit: int = 100
):
    addresses = db.query(models.Address)
    if longitude and latitude and distance_in_meters:
        return [address for address in addresses
                if address.distance_in_meters(latitude, longitude) < distance_in_meters]

    return addresses.offset(skip).limit(limit).all()


def create_address(db: Session, address: schemas.AddressCreate):
    db_address = models.Address(
        address=address.address,
        latitude=address.latitude,
        longitude=address.longitude,
    )
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address


def update_address(db: Session, address: schemas.AddressCreate, address_id: int):
    db_address = get_address(db=db, address_id=address_id)
    db_address.address = address.address
    db_address.latitude = address.latitude
    db_address.longitude = address.longitude
    db.commit()
    db.refresh(db_address)
    return db_address


def delete_address(db: Session, address_id: int):
    db.query(models.Address).filter(models.Address.id == address_id).delete()
    db.commit()
