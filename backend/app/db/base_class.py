from datetime import datetime, timezone
import re
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.orm import declarative_base, declared_attr

class CustomBase:
    __allow_unmapped__ = True
    
    id = Column(Integer, primary_key=True, index=True)
    
    # Automatically generate __tablename__ in lowercase from class name
    @declared_attr
    def __tablename__(cls) -> str:
        name = cls.__name__
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False
    )

Base = declarative_base(cls=CustomBase)
