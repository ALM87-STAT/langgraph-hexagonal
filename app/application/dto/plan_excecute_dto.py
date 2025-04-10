from pydantic import BaseModel


class PlanExcecuteDto(BaseModel):
    input: str
