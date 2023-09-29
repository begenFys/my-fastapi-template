from typing import Union

from pydantic import BaseModel


class TestSchema(BaseModel):
    test_id: int
    test_text: Union[str, None] = None