from pydantic import BaseModel, Field,schema
from typing import Optional, List

class postschema(BaseModel):
    id : int = Field(default=None)
    title : str = Field(default=None)
    desc : str = Field(default=None)