from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel
from typing import List, Optional
from app.automation.linkedin import LinkedInPlatform
from app.automation.indeed import IndeedPlatform

router = APIRouter()

class SearchRequest(BaseModel):
    platform: str  # "linkedin" or "indeed"
    query: str
    location: str

class ApplyRequest(BaseModel):
    platform: str
    job_url: str
    resume_path: str
    dry_run: bool = True  # Default to safer dry_run

class JobResult(BaseModel):
    title: str
    company: str
    url: str
    platform: str

@router.post("/search", response_model=List[JobResult])
async def search_jobs(request: SearchRequest):
    if request.platform.lower() == "linkedin":
        bot = LinkedInPlatform(headless=True)  # Use headless for search
    elif request.platform.lower() == "indeed":
        bot = IndeedPlatform(headless=True)
    else:
        raise HTTPException(status_code=400, detail="Unsupported platform")
    
    try:
        jobs = await bot.search_jobs(request.query, request.location)
        await bot.context.close() if bot.context else None
        await bot.browser.close() if bot.page and bot.page.context.browser else None
        return jobs
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/apply")
async def apply_to_job(request: ApplyRequest, background_tasks: BackgroundTasks):
    """
    Trigger an application process. 
    If dry_run is True, it will stop before submission and save a screenshot.
    """
    if request.platform.lower() == "linkedin":
        bot = LinkedInPlatform(headless=False)  # Headful for debugging/visuals
    elif request.platform.lower() == "indeed":
        bot = IndeedPlatform(headless=False)
    else:
        raise HTTPException(status_code=400, detail="Unsupported platform")
    
    # Run in background to avoid blocking API
    background_tasks.add_task(run_application, bot, request)
    
    return {"status": "Application process started", "dry_run": request.dry_run}

async def run_application(bot, request):
    try:
        # In a real app, you'd handle login here or reuse a session
        # await bot.login(...) 
        await bot.apply_to_job(request.job_url, request.resume_path, dry_run=request.dry_run)
    except Exception as e:
        print(f"Background application failed: {e}")
    finally:
        # Don't close immediately if we want to inspect, but for now we close
        # await bot.context.close()
        pass
