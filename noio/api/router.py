import typing as tp
from http import HTTPStatus

from fastapi import APIRouter

from noio.api.schemas import APIResponse, NoticeCreate, NoticeSchema
from noio.models import Notice

v1 = APIRouter()


@v1.get(
    "/notices",
    status_code=HTTPStatus.OK,
    response_model=APIResponse[tp.List[NoticeSchema]],
    tags=["Notice"],
)
def get_notices():
    notices = Notice.all()
    return APIResponse(status=200, details=notices)


@v1.post(
    "/notices",
    status_code=HTTPStatus.CREATED,
    response_model=APIResponse[NoticeSchema],
    tags=["Notice"],
)
def create_notice(notice: NoticeCreate):
    notice = Notice.create(name=notice.name, link=notice.link)
    return APIResponse(status=HTTPStatus.CREATED, details=notice)


@v1.delete(
    "/notices",
    status_code=HTTPStatus.OK,
    response_model=APIResponse[bool],
    tags=["Notice"],
)
def remove_notice(notice_id: int):
    notice = Notice.get(id=notice_id)

    if notice is not None:
        notice.delete()
        return APIResponse(status=HTTPStatus.OK, details=True)

    return APIResponse(status=HTTPStatus.BAD_REQUEST, details=False)
