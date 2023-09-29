from abc import ABC, abstractmethod
from typing import Union, List

from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError

    @abstractmethod
    async def edit_by_filters():
        raise NotImplementedError

    @abstractmethod
    async def find_all():
        raise NotImplementedError

    @abstractmethod
    async def find_by_filters():
        raise NotImplementedError

    @abstractmethod
    async def delete_by_filters():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict, returning_field: str) -> Union[str, int]:
        stmt = insert(self.model).values(**data).returning(eval(f"self.model.{returning_field}"))
        results = await self.session.execute(stmt)
        return results.scalar_one()

    async def edit_by_filters(self, filter_by: dict, data: dict) -> List[dict]:
        stmt = update(self.model).values(**data).filter_by(**filter_by).returning(self.model)
        results = await self.session.execute(stmt)
        results = [result.to_read_model().model_dump() for result in results.scalars()]
        return results

    async def delete_by_filters(self, filter_by: dict) -> List[dict]:
        stmt = delete(self.model).filter_by(**filter_by).returning(self.model)
        results = await self.session.execute(stmt)
        results = [result.to_read_model().model_dump() for result in results.scalars()]
        return results

    async def get_all(self) -> List[dict]:
        stmt = select(self.model)
        results = await self.session.execute(stmt)
        results = [result.to_read_model().model_dump() for result in results.scalars()]
        return results

    async def get_by_filters(self, filter_by: dict) -> List[dict]:
        stmt = select(self.model).filter_by(**filter_by)
        results = await self.session.execute(stmt)
        results = [result.to_read_model().model_dump() for result in results.scalars()]
        return results
