from app import app
from db import db

db.init_app(app)


@app.before_first_request #runs before first request into app
def create_tables():
    db.create_all()
