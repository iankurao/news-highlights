from app import app
import urllib.request, json
from .models import source,topHeadlines, everything

Source = source.Source

api_key = app.config['NEWS_API_KEY']
source_url = app.config['SOURCES_API_BASE_URL']
top_headlines_url = app.config['TOP_HEADLINES_BASE_URL']
everything_url = app.config['EVERYTHING_BASE_URL']

def get_sources():
    get_sources_url = source_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_source_results(source_results_list)
    return source_results


def process_source_results(source_list):
    source_results = []

    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        source_object = Source( id, name, description, url, category, language, country)
        source_results.append(source_object)

    return source_results
    
