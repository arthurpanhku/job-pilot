from fastapi import FastAPI
from app.mcp_server import mcp_router

app = FastAPI(title="JobPilot API")

@app.get("/api/health")
async def health_check():
    return {"status": "ok", "service": "JobPilot Backend"}

app.include_router(mcp_router, prefix="/mcp", tags=["mcp"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
