from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from . import models, crud, database
from .api import notes
from jinja2 import Environment, FileSystemLoader

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Note Taking App")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Register API routers
app.include_router(notes.router, prefix="/api", tags=["notes"])

# Setup Jinja2 templates
templates = Environment(loader=FileSystemLoader("app/templates"))


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request, db: Session = Depends(database.get_db)):
    all_notes = crud.get_notes(db)
    template = templates.get_template("index.html")
    return template.render(request=request, notes=all_notes)
