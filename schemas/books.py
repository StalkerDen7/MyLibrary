from pydantic import BaseModel, Field, ConfigDict


class SBookBase(BaseModel):
    title: str
    author: str
    year: int 
    pages: int = Field(..., gt=10, description="Number of pages must be greater than 10")
    is_read: bool = False

class SBookAdd(SBookBase):
    pass

class SBook(SBookBase):
    id: int

    model_config = ConfigDict(from_attributes=True)