from fastapi import APIRouter

router = APIRouter(prefix="/v1", tags=["v1"])

@router.get("/status")
async def status():
    """Check API status"""
    return {"status": "ok", "version": "v1"}


@router.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "healthy", "service": "cobalt-pilot-146 v1"}


@router.get("/info")
async def info():
    """Application info endpoint"""
    return {
        "service": "cobalt-pilot-146",
        "version": "v1",
        "description": "Open-source Grok Bot alternative with a virtual machine that bots can use"
    }
