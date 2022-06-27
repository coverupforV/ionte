from typing import List, Any, Union

from fastapi import APIRouter, Depends

from core import deps
from models import Note
from scheams import Note_Pydantic, NoteIn_Pydantic, Response200, Response400

note = APIRouter(tags=["笔记相关"])


@note.get("/note", summary="笔记列表", response_model=Union[Response200, Response400])
async def note_list(limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    data = {
        "total": await Note.all().count(),
        "notes": await Note_Pydantic.from_queryset(Note.all().offset(skip).limit(limit).order_by('-id'))
    }
    return Response200(data=data)


@note.post("/note", summary="新增笔记")
async def note_create(note_form: NoteIn_Pydantic, token: Any = Depends(deps.get_current_user)):
    return Response200(data=await Note_Pydantic.from_tortoise_orm(await Note.create(**Note_form.dict())))


@note.put("/note/{pk}", summary="编辑笔记")
async def note_update(pk: int, note_form: NoteIn_Pydantic, token: Any = Depends(deps.get_current_user)):
    if await Note.filter(pk=pk).update(**note_form.dict()):
        return Response200()
    return Response400(msg="更新失败")


@note.delete("/note/{pk}", summary="删除笔记")
async def note_delete(pk: int, token: Any = Depends(deps.get_current_user)):
    if await Note.filter(pk=pk).delete():
        return Response200()
    return Response400(msg="删除失败")
