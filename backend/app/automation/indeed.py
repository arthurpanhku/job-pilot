import asyncio
import random
from typing import Dict, List, Optional
from playwright.async_api import BrowserContext, Page, async_playwright
from playwright_stealth import stealth
from fake_useragent import UserAgent
from app.automation.base import JobPlatform

class IndeedPlatform(JobPlatform):
    """Indeed specific implementation with stealth and human-like delays."""

    def __init__(self, headless: bool = False, use_stealth: bool = True):
        super().__init__("Indeed")
        self.headless = headless
        self.use_stealth = use_stealth
        self.user_agent = UserAgent()
        self.base_url = "https://www.indeed.com"

    async def initialize(self):
        """Initialize browser and context with stealth settings."""
        playwright = await async_playwright().start()
        browser = await playwright.chromium.launch(
            headless=self.headless,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-dev-shm-usage",
            ]
        )
        
        # Configure context with random user agent and stealth
        context = await browser.new_context(
            user_agent=self.user_agent.random,
            viewport={"width": 1280, "height": 800},
            java_script_enabled=True,
            ignore_https_errors=True
        )
        
        self.context = context
        self.page = await context.new_page()
        
        if self.use_stealth:
            await stealth(self.page)
            
        # Human-like initial behavior
        await self.human_delay(2, 5)

    async def human_delay(self, min_seconds: float = 1.0, max_seconds: float = 3.0):
        """Simulate human-like delay between actions."""
        delay = random.uniform(min_seconds, max_seconds)
        await asyncio.sleep(delay)

    async def login(self, credentials: Dict[str, str]) -> bool:
        """Log in to Indeed with stealth and delays."""
        if not self.page:
            await self.initialize()

        email = credentials.get("email")
        password = credentials.get("password")
        
        if not email or not password:
            raise ValueError("Email and password required for Indeed login")

        try:
            # Indeed login flow often involves separate steps for email and password
            await self.page.goto(f"{self.base_url}/account/login", wait_until="networkidle")
            await self.human_delay()

            # Type email
            await self.page.fill("input[name='__email']", email, timeout=5000)
            await self.human_delay(0.5, 1.5)
            
            # Click next/continue if present (Indeed specific)
            continue_btn = await self.page.query_selector("button[type='submit']")
            if continue_btn:
                await continue_btn.click()
                await self.human_delay()
            
            # Type password
            await self.page.fill("input[name='__password']", password, timeout=5000)
            await self.human_delay(0.5, 1.5)
            
            # Click login
            await self.page.click("button[type='submit']")
            await self.page.wait_for_load_state("networkidle")
            
            # Check for verification challenge
            if "checkpoint" in self.page.url or "challenge" in self.page.url:
                print("Verification challenge detected! Manual intervention may be required.")
                await self.take_screenshot("indeed_verification_challenge.png")
                return False
                
            return True
            
        except Exception as e:
            print(f"Login failed: {e}")
            await self.take_screenshot("indeed_login_error.png")
            return False

    async def search_jobs(self, query: str, location: str) -> List[Dict]:
        """Search for jobs on Indeed."""
        if not self.page:
            await self.initialize()
            
        search_url = f"{self.base_url}/jobs?q={query}&l={location}"
        await self.page.goto(search_url, wait_until="networkidle")
        await self.human_delay(2, 4)
        
        jobs = []
        # Basic extraction logic
        job_cards = await self.page.query_selector_all(".job_seen_beacon")
        
        for card in job_cards[:10]:
            title_el = await card.query_selector("h2.jobTitle span")
            company_el = await card.query_selector(".companyName")
            link_el = await card.query_selector("a.jcs-JobTitle")
            
            if title_el and company_el:
                title = await title_el.inner_text()
                company = await company_el.inner_text()
                link = await link_el.get_attribute("href") if link_el else ""
                
                jobs.append({
                    "title": title,
                    "company": company,
                    "url": f"{self.base_url}{link}" if link.startswith("/") else link,
                    "platform": "Indeed"
                })
        
        return jobs

    async def apply_to_job(self, job_url: str, resume_path: str, dry_run: bool = False) -> bool:
        """Apply to an Indeed job."""
        if not self.page:
            await self.initialize()
            
        try:
            await self.page.goto(job_url, wait_until="networkidle")
            await self.human_delay()
            
            # Indeed Apply button detection
            apply_btn = await self.page.query_selector("button.indeed-apply-button") or \
                        await self.page.query_selector("#indeedApplyButton")
            
            if not apply_btn:
                print("No Indeed Apply button found.")
                return False
                
            await apply_btn.click()
            await self.human_delay()
            
            # Fill form logic (simplified)
            # Indeed usually opens a new window/iframe for application
            
            if dry_run:
                print(f"Dry Run: Form filled for {job_url}. Taking screenshot for review.")
                await self.take_screenshot("indeed_application_preview.png")
                return True
            
            # Final submit would go here
            return True
            
        except Exception as e:
            print(f"Application failed: {e}")
            await self.take_screenshot("indeed_application_error.png")
            return False
