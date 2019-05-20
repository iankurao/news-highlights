from app import app
import urllib.request, json
from .models import source,topHeadlines, everything

Source = source.Source
Top_Headlines = topHeadlines.Top_Headlines
Everything = everything.Everything

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


def get_top_headlines(source) :
  get_top_headlines_url = top_headlines_url.format(source, api_key)

  with urllib.request.urlopen(get_top_headlines_url) as url :
    top_headlines_data = url.read()
    top_headlines_response = json.loads(top_headlines_data)

    top_headlines_results = None 

    if top_headlines_response['articles'] :
      top_headlines_results_list = top_headlines_response['articles']
      top_headlines_results = process_top_headlines_results(top_headlines_results_list)

  return(top_headlines_results)


def process_top_headlines_results(top_headlines_results_list) :
  '''
  process Top_headlines results and transform them to a list of objects
  '''
  top_headlines_results = []
  for top_headlines_item in top_headlines_results_list :

    author = top_headlines_item.get('author')
    title = top_headlines_item.get('title')
    description = top_headlines_item.get('description')
    url = top_headlines_item.get('url')
    urlToImage = top_headlines_item.get('urlToImage')
    publishedAt = top_headlines_item.get('publishedAt')
    

    top_headlines_object = Top_Headlines(author, title, description, url, urlToImage, publishedAt)
    top_headlines_results.append(top_headlines_object)

  return top_headlines_results




def get_everything():
    get_everything_url = everything_url.format(api_key)

    with urllib.request.urlopen(get_everything_url) as url:
        get_everything_data = url.read()
        get_everything_response = json.loads(get_everything_data)
        everything_results = None

        if get_everything_response['articles']:
            everything_results_list = get_everything_response['articles']
            everything_results = process_everything_results(everything_results_list)

    return everything_results

def process_everything_results(everything_results_list):
    everything_results = []
    for everything_item in everything_results_list:
        author = everything_item.get('author')
        title = everything_item.get('title')
        description = everything_item.get('description')
        url = everything_item.get('url')
        urlToImage = everything_item.get('urlToImage')
        publishedAt = everything_item.get('publishedAt')

        everything_object = Everything(author, title, description, url, urlToImage, publishedAt)
        everything_results.append(everything_object)
        
    return everything_results


