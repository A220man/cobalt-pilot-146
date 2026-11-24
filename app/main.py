from fastapi import FastAPI
from app.api.v1.routes import router as v1_router

app = FastAPI(
    title="cobalt-pilot-146",
    description="Open-source Grok Bot alternative with a virtual machine that bots can use",
    version="0.1.0",
)

app.include_router(v1_router)

@app.get("/")
async def root():
    return {"message": "cobalt-pilot-146 API is running", "version": "0.1.0"}


@app.get("/health")
async def health():
    return {"status": "healthy", "service": "cobalt-pilot-146"}
