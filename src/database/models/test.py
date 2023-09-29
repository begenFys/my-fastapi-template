from src.database.database import Base
from src.database.schemas.test import TestSchema
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class Test(Base):
    __tablename__ = "test"
    test_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    test_text: Mapped[str] = mapped_column(String, unique=True, nullable=True, default=None)

    def to_read_model(self) -> TestSchema:
        return TestSchema(
            test_id=self.test_id,
            test_text=self.test_text
        )