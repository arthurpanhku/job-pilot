from abc import ABC, abstractmethod
from typing import Optional, Dict, List
from playwright.async_api import Page, BrowserContext

class JobPlatform(ABC):
    """Base class for all job platforms (LinkedIn, Indeed, etc.)"""
    
    def __init__(self, platform_name: str):
        self.platform_name = platform_name
        self.context: Optional[BrowserContext] = None
        self.page: Optional[Page] = None

    @abstractmethod
    async def login(self, credentials: Dict[str, str]) -> bool:
        """Login to the platform using provided credentials."""
        pass

    @abstractmethod
    async def search_jobs(self, query: str, location: str) -> List[Dict]:
        """Search for jobs based on query and location."""
        pass

    @abstractmethod
    async def apply_to_job(self, job_url: str, resume_path: str) -> bool:
        """Apply to a specific job using the provided resume."""
        pass

    async def verify_human(self) -> bool:
        """Check for captchas or human verification challenges."""
        # Default implementation: assume no challenge or basic check
        return True

    async def take_screenshot(self, path: str = "screenshot.png"):
        """Take a screenshot of the current page for debugging/verification."""
        if self.page:
            await self.page.screenshot(path=path)
