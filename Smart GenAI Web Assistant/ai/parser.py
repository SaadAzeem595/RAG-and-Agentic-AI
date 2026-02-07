from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
class AIResponse(BaseModel):
    title: str = Field(description="The main topic")
    summary: str = Field(description="A brief summary")
    action_items: list = Field(description="List of steps")

def get_json_parser():
    return JsonOutputParser(pydantic_object=AIResponse)