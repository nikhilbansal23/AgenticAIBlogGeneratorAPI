from typing import TypedDict
from pydantic import BaseModel, Field

class Blog(BaseModel):
    title: str = Field(..., description="Title of the blog")
    content: str = Field(..., description="The main content of the blog")

class BlogState(TypedDict):
    topic:str
    blog: Blog
    current_language:str