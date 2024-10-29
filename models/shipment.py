#!/usr/bin/env python3
""" Represents the Shipment information """
from models.base import Base, BaseModel
from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class Shipment(BaseModel, Base):
    """ Shipment class """
    __tablename__ = "shipments"

    order_id = Column(String(60), ForeignKey("orders.id"), nullable=False)
    shipping_address =  Column(String(400), nullable=False)
    status = Column(String(30), nullable=False, default="Processing")
    shipping_cost = Column(Float, nullable=False, default=0.0)
    tracking_number = Column(String(50))

    def __init__(self, *args, **kwargs):
        """ Initialize the shipment instance """
        super().__init__(*args, **kwargs)
