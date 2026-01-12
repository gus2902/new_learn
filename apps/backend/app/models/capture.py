from datetime import datetime
from enum import Enum

from pydantic import BaseModel, HttpUrl


class MoodColor(str, Enum):
    CURIOSITY = "curiosity"
    INSPIRATION = "inspiration"
    PEACE = "peace"
    PASSION = "passion"
    REFLECTION = "reflection"


class CaptureStatus(str, Enum):
    PENDING = "pending"
    SAVED = "saved"
    ARCHIVED = "archived"
    FAILED = "failed"


class CaptureRequest(BaseModel):
    url: HttpUrl
    title: str | None = None
    description: str | None = None
    mood_color: MoodColor = MoodColor.CURIOSITY


class CaptureResponse(BaseModel):
    id: str
    url: str
    title: str | None
    status: CaptureStatus
    captured_at: datetime
    message: str


class HealthResponse(BaseModel):
    status: str
    version: str
    timestamp: datetime
