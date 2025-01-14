from db import Base
from sqlalchemy import Integer, ForeignKey, Date
from sqlalchemy.orm import mapped_column, Mapped, relationship


class Mark(Base):
    __tablename__ = "marks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    mark: Mapped[str] = mapped_column(Integer)
    date: Mapped[Date] = mapped_column(Date)

    student_id: Mapped[int] = mapped_column(Integer, ForeignKey("students.id"))
    student: Mapped["Student"] = relationship("Student", back_populates="marks")

    subject_id: Mapped[int] = mapped_column(Integer, ForeignKey("subjects.id"))
    subject: Mapped["Subject"] = relationship("Subject", back_populates="marks")






    

 
