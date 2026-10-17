from app.models.dummy_model import predict_incidents
from app.schemas.analysis import (
    TripAnalysisRequest,
    TripAnalysisResponse,
)


def analyze_trip( request: TripAnalysisRequest, ) -> TripAnalysisResponse:
    readings = [
        reading.model_dump()
        for reading in request.sensor_readings
    ]

    incidents = predict_incidents(readings)

    return TripAnalysisResponse(
        trip_id=request.trip_id,
        status="completed",
        incidents=incidents,
    )