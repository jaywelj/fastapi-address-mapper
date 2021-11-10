from typing import List

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/addresses/", response_model=schemas.Address, status_code=status.HTTP_201_CREATED)
def create_address(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    db_address = crud.get_address_by_coordinates(
        db,
        latitude=address.latitude,
        longitude=address.longitude,
    )
    if db_address:
        raise HTTPException(status_code=400, detail="Address is existing")
    return crud.create_address(db=db, address=address)


@app.put("/addresses/{address_id}/", response_model=schemas.Address)
def update_address(address_id: int, address: schemas.AddressCreate, db: Session = Depends(get_db)):
    db_address = crud.get_address(db, address_id=address_id)
    if not db_address:
        raise HTTPException(status_code=404, detail="Address is not found")
    return crud.update_address(db=db, address=address, address_id=address_id)


@app.delete("/addresses/{address_id}/")
def delete_address(address_id: int, db: Session = Depends(get_db)):
    db_address = crud.get_address(db, address_id=address_id)
    if not db_address:
        raise HTTPException(status_code=404, detail="Address is not found")
    crud.delete_address(db, address_id=address_id)
    return {"message": f"successfully delete address with id: {address_id}"}


@app.get("/addresses/", response_model=List[schemas.Address])
def read_addresses(
        skip: int = 0,
        limit: int = 100,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        distance_in_meters: Optional[float] = None,
        db: Session = Depends(get_db)
):
    addresses = crud.get_addresses(
        db,
        skip=skip,
        limit=limit,
        latitude=latitude,
        longitude=longitude,
        distance_in_meters=distance_in_meters,
    )
    return addresses


@app.get("/addresses/{address_id}/", response_model=schemas.Address)
def read_address(address_id: int, db: Session = Depends(get_db)):
    db_address = crud.get_address(db=db, address_id=address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address
