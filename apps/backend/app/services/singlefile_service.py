import asyncio
import subprocess
import tempfile
import time
from pathlib import Path

from app.models.capture import ArchiveResult


async def archive_with_singlefile(
    url: str, capture_id: str, timeout_ms: int = 30000
) -> ArchiveResult:
    start_time = time.time()

    try:
        with tempfile.TemporaryDirectory() as tmp_dir:
            output_path = Path(tmp_dir) / f"{capture_id}.html"

            cmd = [
                "single-file",
                url,
                output_path.as_posix(),
                "--browser-executable-path",
                "chromium",
                "--browser-headless",
                "--browser-wait-until",
                "networkidle0",
                "--compress-HTML",
                "--remove-hidden-elements",
                "--remove-unused-styles",
                "--remove-unused-fonts",
            ]

            timeout_sec = timeout_ms / 1000

            process = await asyncio.create_subprocess_exec(
                *cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )

            try:
                stdout, stderr = await asyncio.wait_for(
                    process.communicate(),
                    timeout=timeout_sec,
                )
            except asyncio.TimeoutError:
                process.kill()
                await process.wait()
                raise TimeoutError(f"SingleFile timeout after {timeout_sec}s")

            if process.returncode != 0:
                error_msg = stderr.decode() if stderr else "Unknown error"
                raise RuntimeError(f"SingleFile failed: {error_msg}")

            if not output_path.exists():
                raise RuntimeError("SingleFile output file not found")

            html_content = output_path.read_bytes()

            elapsed_ms = int((time.time() - start_time) * 1000)

            return ArchiveResult(
                success=True,
                html_path=f"captures/{capture_id}/archive.html",
                elapsed_ms=elapsed_ms,
            )

    except Exception as e:
        elapsed_ms = int((time.time() - start_time) * 1000)
        return ArchiveResult(
            success=False,
            error=str(e),
            elapsed_ms=elapsed_ms,
        )


def is_singlefile_available() -> bool:
    try:
        result = subprocess.run(
            ["single-file", "--version"],
            capture_output=True,
            timeout=5,
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False
