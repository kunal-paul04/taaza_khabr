from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pygooglenews import GoogleNews
import time
import os


route = APIRouter()
templates = Jinja2Templates(directory="app/templates")

state_list = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
    "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram",
    "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu",
    "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"
]


@route.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    top_news = get_top_news()
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"top_news": top_news, "state_list": state_list}
    ) 


def get_top_news(max_results=6):
    """Fetches top news"""
    gn = GoogleNews(lang='en', country='IN')  # Ensure news is localized to India
    top_news = gn.top_news()  # Fetch top news
    entries = top_news.get("entries", [])[:max_results]  # Limit to max_results
    # Extract required fields
    news_list = []
    for entry in entries:
        news_item = {
            "title": entry.get("title", "No Title"),
            "publisher": entry.get("source", {}).get("title", "Unknown Publisher"),
            "link": entry.get("link", "#")
        }
        news_list.append(news_item)
    return news_list


def get_state_news(state_name, max_results=6):
    """Fetches top news for a specific state."""
    gn = GoogleNews(lang='en', country='IN')  # Ensure news is localized to India
    search = gn.search(state_name, when='0d')  # Search for news in the last day
    entries = search["entries"][:max_results]  # Limit to max_results
    # Extract required fields
    news_list = []
    for entry in entries:
        news_item = {
            "title": entry.get("title", "No Title"),
            "publisher": entry.get("source", {}).get("title", "Unknown Publisher"),
            "link": entry.get("link", "#")
        }
        news_list.append(news_item)
    return news_list


@route.get("/state_news", response_class=HTMLResponse)
async def read_item(request: Request, st: str = ""):
    state_name = st  # Assign the query parameter value to state_name
    state_news = get_state_news(state_name)
    return templates.TemplateResponse(
        request=request,
        name="state_news.html",
        context={"state_news": state_news, "state_list": state_list, "state_name": state_name}
    ) 


@route.get("/about", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="about.html",
        context={"state_list": state_list}
    ) 
