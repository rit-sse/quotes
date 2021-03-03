"""
Defines models
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import relationship

from . import db

class Quote(db.Model, SerializerMixin):
    __tablename__ = 'quotes'
    id = Column(Integer, primary_key=True)
    body = Column(String)
    description = Column(String)
    approved = Column(Boolean, default=False)
    tags = relationship('Tag')

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_approved(cls):
        return cls.query.filter(cls.approved == True).all()

class Tag(db.Model, SerializerMixin):
    __tablename__ = 'quotes_tags'
    tagName = Column(String(255), primary_key=True)
    quoteId = Column(ForeignKey('quotes.id'), primary_key=True)
