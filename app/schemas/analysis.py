from typing import Literal
from pydantic import BaseModel, Field


class SensorReading(BaseModel):
    timestamp: float
    acceleration_x: float
    acceleration_y: float = 0.0
    acceleration_z: float = 0.0


class TripAnalysisRequest(BaseModel):
    trip_id: str
    sensor_readings: list[SensorReading]


class IncidentResult(BaseModel):
    type: Literal["harsh_braking"]
    timestamp: float
    severity: Literal["low", "medium", "high"]
    confidence: float = Field(ge=0, le=1)


class TripAnalysisResponse(BaseModel):
    trip_id: str
    status: Literal["completed"]
    incidents: list[IncidentResult]