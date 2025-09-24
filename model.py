from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float, Enum
from sqlalchemy.orm import relationship
from app.utills.db import Base  # assuming Base = declarative_base()

class Institute(Base):
    __tablename__ = "institutes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=True)

    courses = relationship("Course", back_populates="institute")


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    institute_id = Column(Integer, ForeignKey("institutes.id"))

    institute = relationship("Institute", back_populates="courses")
    batches = relationship("Batch", back_populates="course")


class Batch(Base):
    __tablename__ = "batches"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)
    course_id = Column(Integer, ForeignKey("courses.id"))

    course = relationship("Course", back_populates="batches")
    students = relationship("Student", back_populates="batch")


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    phone = Column(String, nullable=True)
    batch_id = Column(Integer, ForeignKey("batches.id"))

    batch = relationship("Batch", back_populates="students")
    fees = relationship("Fee", back_populates="student")


class Fee(Base):
    __tablename__ = "fees"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    total_fee = Column(Float, nullable=False)
    paid_amount = Column(Float, default=0.0)
    due_amount = Column(Float, default=0.0)

    student = relationship("Student", back_populates="fees")
    installments = relationship("Installment", back_populates="fee")


class Installment(Base):
    __tablename__ = "installments"

    id = Column(Integer, primary_key=True, index=True)
    fee_id = Column(Integer, ForeignKey("fees.id"))
    amount = Column(Float, nullable=False)
    paid_on = Column(Date, nullable=True)

    fee = relationship("Fee", back_populates="installments")