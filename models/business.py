#!/usr/bin/env python3
""" Defines the Business class """
from sqlalchemy import Column, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from models.base import Base, BaseModel


class Business(BaseModel, Base):
    """ Business Model """

    __tablename__ = "businesses"

    merchant_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)

    products = relationship("Product", backref="business")
