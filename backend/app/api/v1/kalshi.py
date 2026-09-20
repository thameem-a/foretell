from fastapi import APIRouter

from app.services.kalshi import get_markets


router = APIRouter(prefix="/kalshi", tags=["Kalshi"],)


@router.get("/markets")
async def kalshi_markets():
    return await get_markets()
