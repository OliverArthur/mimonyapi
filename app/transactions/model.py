from pydantic import BaseModel
from typing import List


class Transaction(BaseModel):
    title: str
    note: str
    amount: float
    createAt: str
    categories: List[str]