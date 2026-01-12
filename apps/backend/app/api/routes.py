from datetime import datetime, timezone

from fastapi import APIRouter

from app.models.capture import CaptureRequest, CaptureResponse, HealthResponse
from app.services.capture_service import create_capture

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    return HealthResponse(
        status="healthy",
        version="0.0.1",
        timestamp=datetime.now(timezone.utc),
    )


@router.post("/capture", response_model=CaptureResponse)
async def capture_url(request: CaptureRequest) -> CaptureResponse:
    return await create_capture(request)
