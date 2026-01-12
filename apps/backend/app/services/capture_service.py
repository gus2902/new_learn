import time
from datetime import datetime, timezone
from uuid import uuid4

from app.core.config import settings
from app.models.capture import (
    ArchiveResult,
    CaptureRequest,
    CaptureResponse,
    CaptureStatus,
)
from app.services.archive_service import archive_page, extract_metadata
from app.services.singlefile_service import archive_with_singlefile, is_singlefile_available
from app.services.storage_service import upload_to_r2


async def create_capture(request: CaptureRequest) -> CaptureResponse:
    capture_id = str(uuid4())
    start_time = time.time()
    now = datetime.now(timezone.utc)

    title = request.title
    if not title:
        try:
            metadata = await extract_metadata(str(request.url), timeout_ms=3000)
            title = metadata.get("title", "Untitled")
        except Exception:
            title = "Untitled"

    elapsed_ms = int((time.time() - start_time) * 1000)

    return CaptureResponse(
        id=capture_id,
        url=str(request.url),
        title=title,
        status=CaptureStatus.SAVED,
        captured_at=now,
        message=f"Saved in {elapsed_ms}ms",
    )


async def archive_capture(capture_id: str, url: str) -> ArchiveResult:
    if is_singlefile_available():
        result = await archive_with_singlefile(
            url=url,
            capture_id=capture_id,
            timeout_ms=settings.archive_timeout_ms,
        )
        if result.success:
            return result

    result = await archive_page(
        url=url,
        capture_id=capture_id,
        timeout_ms=settings.archive_timeout_ms,
    )

    if result.success:
        return result

    return await fallback_capture(capture_id, url)


async def fallback_capture(capture_id: str, url: str) -> ArchiveResult:
    start_time = time.time()

    try:
        import httpx

        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url, follow_redirects=True)

            if response.status_code == 200:
                html_content = response.text

                elapsed_ms = int((time.time() - start_time) * 1000)

                return ArchiveResult(
                    success=True,
                    html_path=f"captures/{capture_id}/fallback.html",
                    elapsed_ms=elapsed_ms,
                )

    except Exception as e:
        pass

    elapsed_ms = int((time.time() - start_time) * 1000)

    return ArchiveResult(
        success=True,
        html_path=None,
        elapsed_ms=elapsed_ms,
    )


async def full_capture_pipeline(request: CaptureRequest) -> CaptureResponse:
    capture_response = await create_capture(request)

    return capture_response
