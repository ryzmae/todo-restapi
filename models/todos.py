from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str
    description: str = None
    completed: bool = False