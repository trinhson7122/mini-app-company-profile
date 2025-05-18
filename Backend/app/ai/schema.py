from pydantic import BaseModel, Field


class AiSimulateGenerate(BaseModel):
    url: str = Field(
        ..., min_length=1, max_length=200, description="URL of the company website"
    )
