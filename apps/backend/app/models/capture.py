from datetime import datetime
from enum import Enum

from pydantic import BaseModel, HttpUrl, Field


class MoodColor(str, Enum):
    CURIOSITY = "curiosity"
    INSPIRATION = "inspiration"
    PEACE = "peace"
    PASSION = "passion"
    REFLECTION = "reflection"


class CaptureStatus(str, Enum):
    PENDING = "pending"
    SAVED = "saved"
    ARCHIVING = "archiving"
    ARCHIVED = "archived"
    FAILED = "failed"


class CaptureRequest(BaseModel):
    url: HttpUrl
    title: str | None = None
    description: str | None = None
    mood_color: MoodColor = MoodColor.CURIOSITY
    user_id: str | None = None


class CaptureResponse(BaseModel):
    id: str
    url: str
    title: str | None
    status: CaptureStatus
    captured_at: datetime
    message: str
    archive_path: str | None = None
    screenshot_url: str | None = None


class ArchiveResult(BaseModel):
    success: bool
    html_path: str | None = None
    screenshot_path: str | None = None
    wacz_path: str | None = None
    error: str | None = None
    elapsed_ms: int = 0


class ArchiveRequest(BaseModel):
    capture_id: str
    url: HttpUrl
    timeout_ms: int = Field(default=30000, ge=1000, le=120000)


class HealthResponse(BaseModel):
    status: str
    version: str
    timestamp: datetime


class BenchmarkResult(BaseModel):
    url: str
    capture_time_ms: int
    archive_time_ms: int
    success: bool
    error: str | None = None
    status: CaptureStatus
