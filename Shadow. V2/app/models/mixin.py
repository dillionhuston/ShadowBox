import datetime
from sqlalchemy import Column, DateTime

class TimestampMixin:
    """Mixin that add timestamp (created/updated time)."""
    createdAt: datetime.datetime = Column(DateTime, default=lambda: datetime.datetime.now(datetime.UTC))
    updatedAt: datetime.datetime = Column(DateTime, default=lambda: datetime.datetime.now(datetime.UTC))