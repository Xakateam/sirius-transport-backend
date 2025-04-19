from pydantic import BaseModel, Field


# Using Annotated class gives unfixed warning in PyCharm
class Route(BaseModel):
    geo_from: list[float] = Field(..., min_length=2, max_length=2)
    geo_to: list[float] = Field(..., min_length=2, max_length=2)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "geo_from": [39.94708836078644, 43.40477467446782],
                    "geo_to": [39.973280131816864, 43.40896417341828]
                }
            ]
        }
    }
