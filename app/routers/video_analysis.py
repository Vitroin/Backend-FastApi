from fastapi import APIRouter, Depends

from ..dependencies import verify_service_token

router = APIRouter(
    prefix="/analysis",
    tags=["Analysis"],
    dependencies=[Depends(verify_service_token)],
)


@router.post("/video")
async def analyze_video():
    return {
        "success": True,
        "message": "video analysis endpoint called successfully!",
    }


@router.post(
    "/trip",
    response_model=TripAnalysisResponse,
)
def analyze_trip_endpoint(
    request: TripAnalysisRequest,
) -> TripAnalysisResponse:
    return analyze_trip(request)