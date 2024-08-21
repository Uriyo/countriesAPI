from datetime import datetime
from db import db

class Country(db.Model):
    __tablename__ = 'countries'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cca3 = db.Column(db.String(3), nullable=False)
    currency_code = db.Column(db.String(3), nullable=False)
    currency = db.Column(db.String(50), nullable=False)
    capital = db.Column(db.String(100), nullable=False)
    region = db.Column(db.String(100), nullable=False)
    subregion = db.Column(db.String(100), nullable=False)
    area = db.Column(db.BigInteger, nullable=False)
    map_url = db.Column(db.String(255), nullable=False)
    population = db.Column(db.BigInteger, nullable=False)
    flag_url = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    neighbours = db.relationship(
        'CountryNeighbour',
        foreign_keys='CountryNeighbour.country_id',
        backref='country',
        lazy=True
    )

class CountryNeighbour(db.Model):
    __tablename__ = 'country_neighbours'

    id = db.Column(db.Integer, primary_key=True)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)
    neighbour_country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
