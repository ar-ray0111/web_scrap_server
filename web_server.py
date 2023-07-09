from fastapi import FastAPI
from scraping_script import scrape_website

app = FastAPI()

@app.post("/scrape")
async def handle_scraping_request(url: str):
    content = scrape_website(url)
    return {"content": content}
