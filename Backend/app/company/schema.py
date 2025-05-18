from pydantic import BaseModel, Field


class CompanyBase(BaseModel):
    company_name: str = Field(..., description="Company Name")
    what_you_do: str = Field(..., description="What does your company do?")
    products_services: str = Field(
        ...,
        description="What are your main products or services?",
    )
    problems_solved: str = Field(
        ...,
        description="What problems do you solve for your clients?",
    )
    what_makes_special: str = Field(
        ...,
        description="What makes your company special?",
    )
    success_stories: str = Field(
        ...,
        description="Share some success stories. What results have you achieved for clients?",
    )
    client_process: str = Field(
        ...,
        description="How do you typically work with new clients? Describe your process.",
    )
    expected_results: str = Field(
        ...,
        description="What results can clients typically expect?",
    )


class CompanyCreate(CompanyBase):
    company_name: str = Field(
        ..., min_length=1, max_length=200, description="Company Name"
    )
    what_you_do: str = Field(
        ..., min_length=1, max_length=200, description="What does your company do?"
    )
    products_services: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="What are your main products or services?",
    )
    problems_solved: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="What problems do you solve for your clients?",
    )
    what_makes_special: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="What makes your company special?",
    )
    success_stories: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Share some success stories. What results have you achieved for clients?",
    )
    client_process: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="How do you typically work with new clients? Describe your process.",
    )
    expected_results: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="What results can clients typically expect?",
    )


class CompanyRead(CompanyBase):
    id: int

    class Config:
        from_attributes = True
