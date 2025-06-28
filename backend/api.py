from livekit.agents import llm
import enum
import logging
from db_driver import DatabaseDriver
from pydantic import BaseModel, Field

logger = logging.getLogger("user-data")
logger.setLevel(logging.INFO)

DB = DatabaseDriver()

class CarDetails(enum.Enum):
    VIN = "vin"
    Make = "make"
    Model = "model"
    Year = "year"

class LookupCarRequest(BaseModel):
    vin: str = Field(..., description="The VIN of the car to lookup")

class CreateCarRequest(BaseModel):
    vin: str = Field(..., description="The VIN of the car")
    make: str = Field(..., description="The make of the car")
    model: str = Field(..., description="The model of the car")
    year: int = Field(..., description="The year of the car")

class AssistantFnc:
    def __init__(self):
        self._car_details = {
            CarDetails.VIN: "",
            CarDetails.Make: "",
            CarDetails.Model: "",
            CarDetails.Year: ""
        }
    
    def get_car_str(self):
        return "\n".join(f"{k}: {v}" for k, v in self._car_details.items())
    
    async def lookup_car(self, vin: str) -> str:
        """Lookup car by VIN (simplified for new pattern)"""
        logger.info("lookup car - vin: %s", vin)
        result = DB.get_car_by_vin(vin)
        if not result:
            return "Car not found"
        
        self._car_details = {
            CarDetails.VIN: result.vin,
            CarDetails.Make: result.make,
            CarDetails.Model: result.model,
            CarDetails.Year: result.year
        }
        return f"The car details are: {self.get_car_str()}"
    
    async def get_car_details(self) -> str:
        return f"The car details are: {self.get_car_str()}"
    
    async def create_car(self, vin: str, make: str, model: str, year: int) -> str:
        logger.info("create car - vin: %s, make: %s, model: %s, year: %s", 
                    vin, make, model, year)
        
        result = DB.create_car(vin, make, model, year)
        if not result:
            return "Failed to create car"
        
        self._car_details = {
            CarDetails.VIN: vin,
            CarDetails.Make: make,
            CarDetails.Model: model,
            CarDetails.Year: year
        }
        return "Car created successfully!"
    
    def has_car(self):
        return bool(self._car_details[CarDetails.VIN])