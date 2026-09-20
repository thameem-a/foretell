import httpx
from fastapi import HTTPException

from app.config.settings import Settings

settings = Settings()
kalshi_url = settings.kalshi_url

print(f"Kalshi Url: {kalshi_url}")

async def get_markets(limit: int = 10):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{kalshi_url}/markets", params={"status": "open", "limit": limit, "mve_filter": "exclude",},
            )
            response.raise_for_status()
        except httpx.HTTPStatusError as exc:
            raise HTTPException(
                status_code=exc.response.status_code,
                detail=f"Kalshi returned {exc.response.status_code}: {exc.response.text}",
            ) from exc
        except httpx.RequestError as exc:
            raise HTTPException(
                status_code=502,
                detail=f"Could not reach Kalshi: {exc}",
            ) from exc

        return response.json()
