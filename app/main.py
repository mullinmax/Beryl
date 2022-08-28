#!/home/maxwell/miniconda3/envs/done-gen/bin/python
import json
from flask import Flask, request, jsonify, render_template, redirect, url_for, send_file
from waitress import serve
import markdown
import re
from bs4 import BeautifulSoup
import bs4
import os

from config import config
from article import article

app = Flask(__name__)

all_articles = {}

@app.route('/')
def root():
    return redirect(config['landing_page'], code=302)

@app.route('/download_resume_md')
def download_resume_md():
    return send_file('./static/md/maxwell_mullin_resume.md', as_attachment=True)

@app.before_first_request
def precalculate():
    parse_all_articles()
    navigation = generate_navigation()
    render_all_articles(navigation)
    
def parse_all_articles():    
    article_paths = []
    for directory in os.walk(config['articles_dir'], followlinks=True):
        for file in directory[2]:
            article_paths.append(os.path.join(directory[0], file))

    for path in article_paths:
        a = article(path=path)
        all_articles[a.metadata['url_ext']] = a

def generate_navigation():    
    
    # get list of all navigation items (which are basically snippets of article metadata)
    navigation_items = [a.metadata[['nav_group', 'url_ext', 'title', 'nav_order']] for a in all_articles.values() if not a.metadata['hidden']]

    # get set of all groups
    groups = {nav['nav_group'] for nav in navigation_items if nav['nav_group'] != ''}

    navigation = []    
    for group in groups:
        navigation.append([a for a in navigation_items if a['nav_group'] == group])
    navigation += [[a] for a in navigation_items if a['nav_group'] == '']

    # sort articles within each group
    for group in navigation:
        group.sort(key=lambda x: x['nav_order'])
    
    # sort all groups within navigation
    navigation.sort(key=lambda x: x[0]['nav_order'])
    print(navigation)
    return navigation
    
def render_all_articles(navigation):
    for key, val in all_articles.items():
        all_articles[key]=val.render(navigation)

@app.route('/a/<group>/<url_ext>')
@app.route('/a/<url_ext>')
def get_article(url_ext, group=None):
    if group is not None:
        path = os.path.join(group, url_ext)
    else:
        path = url_ext
        
    if path in all_articles:
        return all_articles[path]
    return all_articles['404']




serve(app, host="0.0.0.0", port=5000)

