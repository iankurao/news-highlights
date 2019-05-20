from flask import render_template, request
from app import app
from .request import get_sources, get_top_headlines, get_everything

@app.route('/')
def index():
    sources = get_sources()
    everything = get_everything()
    title = 'News Highlight'
    return render_template('index.html', sources = sources, title = title, everything = everything )

@app.route('/source/<source>')
def top_Headlines(source) :
  '''
  view Top_Headlines page function that returns the Top_Headlines from a source details page and its data 
  '''
  sources = get_sources()
  top_headlines = get_top_headlines(source)
  print(top_headlines)

  return render_template('top_headlines.html', sources = sources, top_headlines = top_headlines)
    