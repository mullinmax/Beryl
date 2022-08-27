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

# object where we store pre-rendered articles
all_articles = {}

@app.route('/')
def root():
    return redirect(config['landing_page'], code=302)

@app.route('/download_resume_md')
def download_resume_md():
    return send_file('./static/md/maxwell_mullin_resume.md', as_attachment=True)

@app.before_first_request
def parse_all_articles():
    article_paths = []
    for directory in os.walk(config['articles_dir'], followlinks=True):
        for file in directory[2]:
            article_paths.append(os.path.join(directory[0], file))

    for path in article_paths:
        a = article(path=path)
        all_articles[a.metadata['url_ext']] = a

@app.route('/a/<url_ext>')
def get_article(url_ext):
    if url_ext in all_articles:
        return all_articles[url_ext].render(all_articles)
    return all_articles['404'].render(all_articles)




serve(app, host="0.0.0.0", port=5000)

