import asyncio
from playwright.async_api import async_playwright
import sys
import urllib
import os

urlname = sys.argv[1]

filename = urllib.parse.quote(urlname, '')

savepath = "/screenshot/" + filename + ".png"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(urlname)
        await page.screenshot(path=savepath, full_page=True)
        os.chmod(savepath,0o666)

asyncio.run(main())
