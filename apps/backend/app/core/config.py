from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Moments: Mind Studio API"
    debug: bool = False

    supabase_url: str = ""
    supabase_key: str = ""

    r2_endpoint: str = ""
    r2_access_key: str = ""
    r2_secret_key: str = ""
    r2_bucket: str = "moments-archives"

    capture_timeout_ms: int = 2000
    archive_timeout_ms: int = 30000

    class Config:
        env_file = ".env"


settings = Settings()
