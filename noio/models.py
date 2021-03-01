from sqlalchemy import Boolean, Column, Integer, String

from noio.commons.exceptions import TooManyArgumentsProvided
from noio.database import base, session

local_session = session()


class ModelMixin:
    @classmethod
    def all(cls):
        return local_session.query(cls).all()

    @classmethod
    def get(cls, **kwargs):
        if len(kwargs.keys()) > 1:
            raise TooManyArgumentsProvided(
                "Too many arguments provided to `get` method."
            )

        data = (
            local_session.query(cls)
            .filter(*[getattr(cls, key) == value for key, value in kwargs.items()])
            .limit(1)
            .all()
        )
        return data[0] if len(data) == 1 else None

    @classmethod
    def filter(cls, **kwargs):
        data = (
            local_session.query(cls)
            .filter(*[getattr(cls, key) == value for key, value in kwargs.items()])
            .all()
        )
        return data

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)  # noqa
        local_session.add(instance)
        local_session.commit()
        return instance

    def save(self):
        local_session.add(self)
        local_session.commit()
        return self

    def delete(self):
        local_session.delete(self)
        local_session.commit()
        return self

    def __repr__(self):
        columns = list(self.__table__.columns)  # noqa
        return "<{model_name}({expression})>".format(
            model_name=self.__class__.__name__.capitalize(),  # noqa
            expression=", ".join(
                [f"{column.name}={getattr(self, column.name)}" for column in columns]
            ),
        )


class User(base, ModelMixin):
    """Model for store telegram users."""

    telegram_id = Column(Integer)
    name = Column(String(length=255))

    @classmethod
    def get_or_create(cls, **kwargs):
        data = cls.get(telegram_id=kwargs["telegram_id"])
        if data is not None:
            return data

        return cls(**kwargs).save()  # noqa


class Notice(base, ModelMixin):
    """Model for store the notices."""

    name = Column(String(length=255), default="No topic")
    link = Column(String(length=2000))
    is_new = Column(Boolean, default=True)
