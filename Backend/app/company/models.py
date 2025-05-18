from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    company_name = Column(String(200), index=True, nullable=False)
    what_you_do = Column(Text, nullable=False)
    products_services = Column(Text, nullable=False)
    problems_solved = Column(Text, nullable=False)
    what_makes_special = Column(Text, nullable=False)
    success_stories = Column(Text, nullable=False)
    client_process = Column(Text, nullable=False)
    expected_results = Column(Text, nullable=False)
