class Config:
    SOURCES_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    TOP_HEADLINES_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    EVERYTHING_BASE_URL = 'https://newsapi.org/v2/everything?q=trending&language=en&apikey={}'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

    
