from db import Base
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship



class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))

    group_id: Mapped[int] = mapped_column(Integer, ForeignKey("groups.id"))
    group: Mapped["Group"] = relationship("Group", back_populates="students")

    marks: Mapped[list["Mark"]] = relationship("Mark", back_populates="student")
