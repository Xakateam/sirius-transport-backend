from pydantic import BaseModel, Field


# Using Annotated class gives unfixed warning in PyCharm
class Location(BaseModel):
    location: list[float] = Field(..., min_length=2, max_length=2)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "location": [39.94708836078644, 43.40477467446782],
                }
            ]
        }
    }
