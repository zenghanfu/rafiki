from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from .utils import generate_uuid, generate_datetime
from .Base import Base

class App(Base):
    __tablename__ = 'app'

    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, unique=True, nullable=False)
    task = Column(String, nullable=False)
    datetime_created = Column(DateTime, nullable=False, default=generate_datetime)
    train_dataset_id = Column(String, ForeignKey('dataset.id'), nullable=False)
    test_dataset_id = Column(String, ForeignKey('dataset.id'), nullable=False)
    train_dataset = relationship('Dataset', foreign_keys=[train_dataset_id], uselist=False)
    test_dataset = relationship('Dataset', foreign_keys=[test_dataset_id], uselist=False)
    