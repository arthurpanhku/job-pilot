from fastapi import APIRouter
from pydantic import BaseModel

mcp_router = APIRouter()

class ServerStatus(BaseModel):
    status: str
    active_agents: int

@mcp_router.get("/status", response_model=ServerStatus)
async def get_server_status():
    """
    Get the status of the MCP server.
    """
    return ServerStatus(status="running", active_agents=0)
