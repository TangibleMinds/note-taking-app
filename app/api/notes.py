from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud, database

router = APIRouter()


@router.post("/notes/", response_model=schemas.NoteInDB)
def create_note(note: schemas.NoteCreate, db: Session = Depends(database.get_db)):
    return crud.create_note(db=db, note=note)


@router.get("/notes/", response_model=List[schemas.NoteInDB])
def read_notes(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    notes = crud.get_notes(db, skip=skip, limit=limit)
    return notes


@router.get("/notes/{note_id}", response_model=schemas.NoteInDB)
def read_note(note_id: int, db: Session = Depends(database.get_db)):
    db_note = crud.get_note(db, note_id=note_id)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note


@router.put("/notes/{note_id}", response_model=schemas.NoteInDB)
def update_note(
    note_id: int, note: schemas.NoteUpdate, db: Session = Depends(database.get_db)
):
    db_note = crud.update_note(db, note_id=note_id, note=note)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note


@router.delete("/notes/{note_id}", response_model=schemas.NoteInDB)
def delete_note(note_id: int, db: Session = Depends(database.get_db)):
    db_note = crud.delete_note(db, note_id=note_id)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note
