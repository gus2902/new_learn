import time
from datetime import datetime, timezone
from typing import List

from fastapi import APIRouter, BackgroundTasks, HTTPException

from app.models.capture import (
    ArchiveRequest,
    ArchiveResult,
    BenchmarkResult,
    CaptureRequest,
    CaptureResponse,
    CaptureStatus,
    HealthResponse,
)
from app.services.capture_service import (
    archive_capture,
    create_capture,
    full_capture_pipeline,
)

router = APIRouter()

TEST_SITES = [
    "https://www.bbc.com",
    "https://medium.com",
    "https://reddit.com",
    "https://github.com",
    "https://stackoverflow.com",
    "https://www.nytimes.com",
    "https://dev.to",
    "https://hackernews.com",
    "https://wikipedia.org",
    "https://example.com",
]


@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    return HealthResponse(
        status="healthy",
        version="0.0.1",
        timestamp=datetime.now(timezone.utc),
    )


@router.post("/capture", response_model=CaptureResponse)
async def capture_url(
    request: CaptureRequest,
    background_tasks: BackgroundTasks,
) -> CaptureResponse:
    start_time = time.time()

    response = await create_capture(request)

    elapsed_ms = int((time.time() - start_time) * 1000)

    if elapsed_ms > 2000:
        response.message = f"Warning: Capture took {elapsed_ms}ms (target: <2000ms)"

    background_tasks.add_task(
        archive_capture,
        capture_id=response.id,
        url=str(request.url),
    )

    return response


@router.post("/archive", response_model=ArchiveResult)
async def archive_url(request: ArchiveRequest) -> ArchiveResult:
    result = await archive_capture(
        capture_id=request.capture_id,
        url=str(request.url),
    )
    return result


@router.get("/benchmark", response_model=List[BenchmarkResult])
async def run_benchmark() -> List[BenchmarkResult]:
    results: List[BenchmarkResult] = []

    for url in TEST_SITES:
        capture_start = time.time()

        try:
            capture_response = await create_capture(CaptureRequest(url=url))
            capture_time_ms = int((time.time() - capture_start) * 1000)

            archive_start = time.time()
            archive_result = await archive_capture(
                capture_id=capture_response.id,
                url=url,
            )
            archive_time_ms = int((time.time() - archive_start) * 1000)

            results.append(
                BenchmarkResult(
                    url=url,
                    capture_time_ms=capture_time_ms,
                    archive_time_ms=archive_time_ms,
                    success=archive_result.success,
                    error=archive_result.error,
                    status=CaptureStatus.ARCHIVED
                    if archive_result.success
                    else CaptureStatus.FAILED,
                )
            )

        except Exception as e:
            capture_time_ms = int((time.time() - capture_start) * 1000)
            results.append(
                BenchmarkResult(
                    url=url,
                    capture_time_ms=capture_time_ms,
                    archive_time_ms=0,
                    success=False,
                    error=str(e),
                    status=CaptureStatus.FAILED,
                )
            )

    return results


@router.get("/benchmark/summary")
async def benchmark_summary() -> dict:
    results = await run_benchmark()

    successful = [r for r in results if r.success]
    failed = [r for r in results if not r.success]

    if successful:
        avg_capture = sum(r.capture_time_ms for r in successful) / len(successful)
        avg_archive = sum(r.archive_time_ms for r in successful) / len(successful)
        p95_capture = (
            sorted([r.capture_time_ms for r in successful])[int(len(successful) * 0.95)]
            if len(successful) > 1
            else successful[0].capture_time_ms
        )
    else:
        avg_capture = 0
        avg_archive = 0
        p95_capture = 0

    success_rate = len(successful) / len(results) * 100 if results else 0

    go_decision = "GO" if avg_capture < 2000 and success_rate >= 95 else "NO-GO"
    if avg_capture < 3000 and success_rate >= 90 and go_decision == "NO-GO":
        go_decision = "CONDITIONAL GO"

    return {
        "total_sites": len(results),
        "successful": len(successful),
        "failed": len(failed),
        "success_rate_percent": round(success_rate, 1),
        "avg_capture_time_ms": round(avg_capture, 0),
        "avg_archive_time_ms": round(avg_archive, 0),
        "p95_capture_time_ms": p95_capture,
        "go_decision": go_decision,
        "details": [
            {
                "url": r.url,
                "capture_ms": r.capture_time_ms,
                "archive_ms": r.archive_time_ms,
                "success": r.success,
                "error": r.error,
            }
            for r in results
        ],
    }
