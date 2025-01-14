from db import Base
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from models.teachers import Teacher


class Subject(Base):
    __tablename__ = "subjects"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
      

    teacher: Mapped["Teacher"] = relationship("Teacher", back_populates="subjects")
    teacher_id: Mapped[int] = mapped_column(Integer, ForeignKey("teachers.id"))

    marks: Mapped[list["Mark"]] = relationship("Mark", back_populates="subject")
