from tortoise.contrib.pydantic import pydantic_model_creator

from models import Note

Note_Pydantic = pydantic_model_creator(Note, name="Note")
NoteIn_Pydantic = pydantic_model_creator(Note, name="NoteIn", exclude_readonly=True)