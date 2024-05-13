import asyncio
from playwright.async_api import async_playwright
import sys
from urllib.parse import urlparse
import os
import hashlib

urlname = sys.argv[1]

#basename = urllib.parse.quote(urlname, '')
basename = urlparse(urlname).netloc
filaname = basename + ".png"
tmp_output_path = "/screenshot/" + filaname

def rename_with_hash(filepath: str) -> str:
    with open(filepath, 'rb') as file:
        fdata = file.read()
        hash_sha256 = hashlib.sha256(fdata).hexdigest()
    hashed_filepath = "/screenshot/" + basename + "-" + hash_sha256 + ".png"
    return hashed_filepath

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(urlname)
        #await page.screenshot(path=savepath, full_page=True)
        await page.screenshot(path=tmp_output_path)
        output_path = rename_with_hash(tmp_output_path)
        os.rename(tmp_output_path, output_path)
        os.chmod(output_path,0o666)
        filename = os.path.basename(output_path)
        print(filename)

asyncio.run(main())
