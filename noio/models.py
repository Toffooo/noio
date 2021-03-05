from sqlalchemy import Boolean, Column, Integer, String

from noio.commons.exceptions import TooManyArgumentsProvided
from noio.database import base, session
from contextlib import contextmanager
from sqlalchemy.orm.exc import DetachedInstanceError

@contextmanager
def make_session_scope():
    """Provide a transactional scope around a series of operations."""
    _session = session()
    _session.expire_on_commit = False

    try:
        yield _session
        _session.commit()
    except Exception as e:
        _session.rollback()
        raise e
    finally:
        _session.close()


class ModelMixin:
    @classmethod
    def all(cls):
        with make_session_scope() as _session:
            return _session.query(cls).all()

    @classmethod
    def get(cls, **kwargs):
        if len(kwargs.keys()) > 1:
            raise TooManyArgumentsProvided(
                "Too many arguments provided to `get` method."
            )
        with make_session_scope() as _session:
            data = (
                _session.query(cls)
                .filter(*[getattr(cls, key) == value for key, value in kwargs.items()])
                .limit(1)
                .all()
            )
            return data[0] if len(data) == 1 else None

    @classmethod
    def filter(cls, **kwargs):
        with make_session_scope() as _session:
            data = (
                _session.query(cls)
                .filter(*[getattr(cls, key) == value for key, value in kwargs.items()])
                .all()
            )
            return data

    @classmethod
    def create(cls, **kwargs):
        with make_session_scope() as _session:
            instance = cls(**kwargs)  # noqa
            _session.add(instance)
            return instance

    def update(self):
        with make_session_scope() as _session:
            _session.commit()
            return self

    def save(self):
        with make_session_scope() as _session:
            _session.add(self)
            return self

    def delete(self):
        with make_session_scope() as _session:
            _session.delete(self)
            return self

    # def __repr__(self):
    #     try:
    #         columns = list(self.__table__.columns)  # noqa
    #         string = "<{model_name}({expression})>".format(
    #             model_name=self.__class__.__name__.capitalize(),  # noqa
    #             expression=", ".join(
    #                 [f"{column.name}={getattr(self, column.name)}" for column in columns]
    #             ),
    #         )
    #         return string
    #     except DetachedInstanceError:
    #


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
