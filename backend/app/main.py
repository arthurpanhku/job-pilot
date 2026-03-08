from fastapi import FastAPI
from app.mcp_server import mcp_router
from app.automation.router import router as automation_router

app = FastAPI(title="JobPilot API", version="0.1.0")

@app.get("/api/health")
async def health_check():
    return {"status": "ok", "service": "JobPilot Backend"}

app.include_router(mcp_router, prefix="/mcp", tags=["mcp"])
app.include_router(automation_router, prefix="/api/automation", tags=["automation"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
