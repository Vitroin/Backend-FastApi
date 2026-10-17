from fastapi import APIRouter, Depends

from ..dependencies import verify_service_token
from ..schemas.analysis import TripAnalysisRequest, TripAnalysisResponse
from ..services.analysis_service import analyze_trip

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


# Plain `def` (not async): FastAPI runs it in a thread pool, so CPU-heavy
# model inference won't block other requests.
@router.post("/trip")
def analyze_trip_endpoint(request: TripAnalysisRequest) -> TripAnalysisResponse:
    return analyze_trip(request)
