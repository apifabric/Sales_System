# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text, DECIMAL
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime


logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py

from sqlalchemy.dialects.sqlite import *


class Customer(Base):
    """
    description: Table for storing customer information including their details.
    """
    __tablename__ = 'Customers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    created_date = Column(DateTime, default=datetime.utcnow)
    address = Column(String)


class Order(Base):
    """
    description: Table for storing order information including referencing customers and containing notes.
    """
    __tablename__ = 'Orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_date = Column(DateTime, default=datetime.utcnow)
    customer_id = Column(Integer, ForeignKey('Customers.id'))
    notes = Column(String)


class Product(Base):
    """
    description: Table representing products available in the store.
    """
    __tablename__ = 'Products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    stock_quantity = Column(Integer)


class Item(Base):
    """
    description: Table representing items within an order, linking products and orders.
    """
    __tablename__ = 'Items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('Orders.id'))
    product_id = Column(Integer, ForeignKey('Products.id'))
    quantity = Column(Integer)
    price = Column(Integer)


# end of model classes


try:
    
    
    
    
    # ALS/GenAI: Create an SQLite database
    
    engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    
    Base.metadata.create_all(engine)
    
    
    
    Session = sessionmaker(bind=engine)
    
    session = Session()
    
    
    
    # ALS/GenAI: Prepare for sample data
    
    
    
    session.commit()
    customer1 = Customer(name="John Doe", email="john.doe@example.com", phone="1234567890", address="123 Elm St, Springfield")
    customer2 = Customer(name="Jane Smith", email="jane.smith@example.com", phone="0987654321", address="456 Maple Ave, Greenville")
    customer3 = Customer(name="Alice Johnson", email="alice.j@example.com", phone="5551234567", address="789 Pine Rd, Hilltown")
    customer4 = Customer(name="Bob Brown", email="bob.b@example.com", phone="5559876543", address="321 Oak Dr, Lakecity")
    order1 = Order(order_date=date(2023, 1, 10), customer_id=1, notes="Urgent delivery")
    order2 = Order(order_date=date(2023, 1, 15), customer_id=2, notes="Include a gift note")
    order3 = Order(order_date=date(2023, 1, 20), customer_id=3, notes="Deliver during afternoon")
    order4 = Order(order_date=date(2023, 1, 25), customer_id=4, notes="No packaging")
    product1 = Product(name="Laptop", description="15-inch screen, 8GB RAM", price=1000, stock_quantity=50)
    product2 = Product(name="Smartphone", description="64GB, Dual SIM", price=800, stock_quantity=100)
    product3 = Product(name="Headphones", description="Noise cancelling", price=150, stock_quantity=200)
    product4 = Product(name="Monitor", description="27-inch 4K display", price=300, stock_quantity=75)
    item1 = Item(order_id=1, product_id=1, quantity=2, price=950)
    item2 = Item(order_id=2, product_id=2, quantity=1, price=800)
    item3 = Item(order_id=3, product_id=3, quantity=3, price=145)
    item4 = Item(order_id=4, product_id=4, quantity=1, price=290)
    
    
    
    session.add_all([customer1, customer2, customer3, customer4, order1, order2, order3, order4, product1, product2, product3, product4, item1, item2, item3, item4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
