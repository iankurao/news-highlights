from app import app
import urllib.request, json
from .models import source,topHeadlines, everything

api_key = app.config['NEWS_API_KEY']
source_url = app.config['SOURCES_API_BASE_URL']
top_headlines_url = app.config['TOP_HEADLINES_BASE_URL']
everything_url = app.config['EVERYTHING_BASE_URL']

