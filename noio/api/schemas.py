from __future__ import annotations

from typing import Generic, TypeVar

from pydantic import BaseModel, validator
from pydantic.datetime_parse import datetime
from pydantic.generics import GenericModel
from sqlalchemy.orm import Query

MESSAGE = TypeVar("MESSAGE")


class OrmBase(BaseModel):
    @validator("*", pre=True)
    def evaluate_lazy_columns(cls, v):  # noqa
        if isinstance(v, Query):
            return v.all()
        return v

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True


class APIResponse(GenericModel, Generic[MESSAGE]):
    status: int
    details: MESSAGE

    class Config:
        arbitrary_types_allowed = True


class NoticeBase(OrmBase):
    name: str
    link: str


class NoticeCreate(NoticeBase):
    pass


class NoticeSchema(NoticeBase):
    id: int
    created_at: datetime
    updated_at: datetime
