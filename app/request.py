from app import app
import urllib.request, json
from .models import source,topHeadlines, everything

api_key = app.config['NEWS_API_KEY']
