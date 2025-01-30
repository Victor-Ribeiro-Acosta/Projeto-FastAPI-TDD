
from bson import Decimal128
from decimal import Decimal
from uuid import uuid4
from typing import Any
from pydantic import BaseModel, Field, UUID4, model_serializer


class Base(BaseModel):
    id: UUID4 = Field(default_factory=uuid4)

    @model_serializer
    def set_model(self) -> dict[str, Any]:
        self_dict = dict(self)
        for key, value in self_dict.items():
            if isinstance(value, Decimal):
                self_dict[key] = Decimal128(str(value))
        
        return self_dict