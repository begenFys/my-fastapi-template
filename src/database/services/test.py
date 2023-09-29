from typing import List

from src.database.utils.unitofwork import IUnitOfWork
from src.logger import AdvLogger

logger = AdvLogger("services.test")


class TestService:
    async def add_test(self, uow: IUnitOfWork, test: dict) -> str:
        async with uow:
            logger.write_log("DEBUG", f"Add new test: {test}")
            role_id = await uow.test.add_one(data=test, returning_field="role_id")
            await uow.commit()
            return role_id

    async def edit_test(self, uow: IUnitOfWork, test_id: str, data: dict) -> dict:
        async with uow:
            logger.write_log("DEBUG", f"Edit test: {test_id}")
            filter_by = {"test_id": test_id}
            edited_test = await uow.test.edit_by_filters(filter_by=filter_by, data=data)
            await uow.commit()
            return edited_test[0]

    async def delete_test(self, uow: IUnitOfWork, test_id: str) -> dict:
        async with uow:
            logger.write_log("DEBUG", f"Delete test: {test_id}")
            filter_by = {"role_id": test_id}
            deleted_test = await uow.test.delete_by_filters(filter_by=filter_by)
            await uow.commit()
            return deleted_test[0]

    async def get_tests(self, uow: IUnitOfWork) -> List[dict]:
        async with uow:
            logger.write_log("DEBUG", "Get all tests")
            tests = await uow.test.get_all()
            return tests

    async def get_tests_by_filters(self, uow: IUnitOfWork, filter_by: dict) -> List[dict]:
        async with uow:
            logger.write_log("DEBUG", f"Get all tests by filters: {filter_by}")
            tests = await uow.test.get_by_filters(filter_by=filter_by)
            return tests
