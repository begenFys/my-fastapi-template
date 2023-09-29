from typing import List
from src.logger import AdvLogger

from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from src.api.dependencies.uow import UOWDep
from src.database.services.test import TestService
from src.database.schemas.test import TestSchema

router = APIRouter(
    prefix="/role",
    tags=["Role"]
)

logger = AdvLogger(logger_name="api.routers.test")

@router.get("/get_all")
async def get_all_test(
        uow: UOWDep,
) -> List[dict]:
    try:
        test = await TestService().get_tests(uow=uow)
        return test
    except Exception as e:
        logger.write_log("WARNING", f"Exception in get_all_test. Error: {e}")
        raise HTTPException(status_code=500, detail=f"Unsuccessfully getting all test. Error: {e}")