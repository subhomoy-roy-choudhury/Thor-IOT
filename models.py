from pydantic import BaseModel
from typing import Optional

class Script(BaseModel):
    filepath: str
    device: str