from src.database.models.test import Test
from src.database.utils.repository import SQLAlchemyRepository


class TestRepository(SQLAlchemyRepository):
    model = Test
