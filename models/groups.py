from db import Base
from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column, relationship, Mapped



class Group(Base):
    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    students: Mapped[list['Student']] = relationship("Student", back_populates="group")
