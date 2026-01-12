from datetime import datetime, timezone
from uuid import uuid4

from app.models.capture import (
    CaptureRequest,
    CaptureResponse,
    CaptureStatus,
)


async def create_capture(request: CaptureRequest) -> CaptureResponse:
    capture_id = str(uuid4())
    now = datetime.now(timezone.utc)

    return CaptureResponse(
        id=capture_id,
        url=str(request.url),
        title=request.title or "Untitled",
        status=CaptureStatus.SAVED,
        captured_at=now,
        message="Saved successfully",
    )
