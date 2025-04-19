from pydantic import BaseModel, Field


# Using Annotated class gives unfixed warning in PyCharm
class Route(BaseModel):
    geo_from: list[float] = Field(..., min_length=2, max_length=2)
    geo_to: list[float] = Field(..., min_length=2, max_length=2)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "geo_from": [43.402440, 39.963147],
                    "geo_to": [43.411328, 39.947022]
                }
            ]
        }
    }
