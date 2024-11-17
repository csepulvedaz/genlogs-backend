from pydantic import BaseModel


class Carrier(BaseModel):
    name: str
    trucks_per_day: str
