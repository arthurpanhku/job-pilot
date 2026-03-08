import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from app.automation.linkedin import LinkedInPlatform
from app.automation.indeed import IndeedPlatform

@pytest.mark.asyncio
async def test_linkedin_initialization():
    """Test LinkedInPlatform initialization."""
    with patch("app.automation.linkedin.async_playwright") as mock_playwright:
        mock_context = AsyncMock()
        mock_browser = AsyncMock()
        mock_page = AsyncMock()
        mock_p = MagicMock()
        
        # Setup mock chain
        # async_playwright().start() should be awaitable and return mock_p
        mock_playwright.return_value.start = AsyncMock(return_value=mock_p)
        
        # mock_p.chromium.launch() should be awaitable and return mock_browser
        mock_p.chromium.launch = AsyncMock(return_value=mock_browser)
        
        mock_browser.new_context.return_value = mock_context
        mock_context.new_page.return_value = mock_page

        bot = LinkedInPlatform(headless=True, use_stealth=False)
        await bot.initialize()
        
        assert bot.context is not None
        assert bot.page is not None
        assert bot.platform_name == "LinkedIn"

@pytest.mark.asyncio
async def test_indeed_initialization():
    """Test IndeedPlatform initialization."""
    with patch("app.automation.indeed.async_playwright") as mock_playwright:
        mock_context = AsyncMock()
        mock_browser = AsyncMock()
        mock_page = AsyncMock()
        mock_p = MagicMock()
        
        # Setup mock chain
        mock_playwright.return_value.start = AsyncMock(return_value=mock_p)
        mock_p.chromium.launch = AsyncMock(return_value=mock_browser)
        
        mock_browser.new_context.return_value = mock_context
        mock_context.new_page.return_value = mock_page

        bot = IndeedPlatform(headless=True, use_stealth=False)
        await bot.initialize()
        
        assert bot.context is not None
        assert bot.page is not None
        assert bot.platform_name == "Indeed"

@pytest.mark.asyncio
async def test_linkedin_search_jobs():
    """Test LinkedIn search jobs logic with mocked page."""
    with patch("app.automation.linkedin.async_playwright") as mock_playwright:
        bot = LinkedInPlatform()
        # Mock initialize to avoid real browser launch
        bot.initialize = AsyncMock() 
        bot.page = AsyncMock()
        
        # Mock query_selector_all to return a list of mock elements
        mock_card = AsyncMock()
        mock_title = AsyncMock()
        mock_company = AsyncMock()
        mock_link = AsyncMock()
        
        mock_title.inner_text.return_value = "Software Engineer"
        mock_company.inner_text.return_value = "Tech Corp"
        mock_link.get_attribute.return_value = "/jobs/view/123"
        
        mock_card.query_selector.side_effect = [mock_title, mock_company, mock_link]
        bot.page.query_selector_all.return_value = [mock_card]
        
        jobs = await bot.search_jobs("python", "remote")
        
        assert len(jobs) == 1
        assert jobs[0]["title"] == "Software Engineer"
        assert jobs[0]["company"] == "Tech Corp"
        assert "LinkedIn" in jobs[0]["platform"]

@pytest.mark.asyncio
async def test_indeed_apply_dry_run():
    """Test Indeed apply dry run."""
    with patch("app.automation.indeed.async_playwright") as mock_playwright:
        bot = IndeedPlatform()
        bot.initialize = AsyncMock()
        bot.page = AsyncMock()
        
        # Mock apply button found
        mock_btn = AsyncMock()
        bot.page.query_selector.return_value = mock_btn
        
        success = await bot.apply_to_job("http://fake.url", "resume.pdf", dry_run=True)
        
        assert success is True
        bot.page.goto.assert_called_with("http://fake.url", wait_until="networkidle")
        # Ensure screenshot was called for dry run
        bot.page.screenshot.assert_called()
