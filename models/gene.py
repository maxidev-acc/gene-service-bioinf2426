from typing import List, Union
from pydantic import BaseModel, ConfigDict
from typing import Optional
from bson import ObjectId
#Interfaces
from enum import Enum




class RangeModel(BaseModel):
    start: int
    end: int


class MutationTypes(Enum):
    DELETION = "deletion"
    INSERTION = "insertion"
    POINT_MUTATION = "point_mutation"


class PointMutationModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str = MutationTypes.POINT_MUTATION.value      
    location: str                        
    original: Optional[str] = None
    mutated: Optional[str] = None

class DeletionModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str = MutationTypes.DELETION.value
    location: str
    length: int

class InsertionModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str = MutationTypes.INSERTION.value
    location: str
    sequence: str


class GeneModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    symbol: str
    chromosome: str
    position: str
    function: str
    mutations: List[Union[PointMutationModel, DeletionModel, InsertionModel]]
  
class GeneFields(Enum):
    NAME= "name"
    SYMBOL = "symbol"
    CHROMOSOME = "chromosome"
    POSITION = "position"
    FUNCTION = "function"