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

app = Flask(__name__)

# object where we store pre-rendered articles
all_articles = {}

@app.route('/')
def root():
    return redirect(config['landing_page'], code=302)

def div_wrap_h_tags(html:str)->str:
    # split on h tags
    soup=BeautifulSoup(html.strip(),'html.parser')
    output = []
    html_prefix = ''
    for child in soup.contents:
        if child.name in ['h1','h2','h3','h4','h5','h6']:
            output.append([str(child)])
        elif len(output) == 0:
            html_prefix += str(child)
        else:
            output[-1].append(str(child))
    
    # concat tags
    output = [''.join(l) for l in output]

    # div wrap
    output_str = ''
    levels = []
    for tag in output:
        try:
            cur_level = int(tag[2])
        except:
            print(tag)
        while len(levels) > 0 and cur_level <= levels[-1]:
                levels.pop()
                output_str += '</div>'
        levels.append(cur_level)
        output_str += f'<div class="h{cur_level}-section">' + tag
    output_str += '</div>'*len(levels)
    return html_prefix + output_str         

def total_text_length(tag) -> int:
    if isinstance(tag, bs4.element.NavigableString):
        return len(str(tag))
    if isinstance(tag, list):
        return sum([total_text_length(c) for c in tag])
    try:
        return total_text_length(tag.contents)
    except:
        return len(str(tag))

def add_class_to_short_lists(html:str) -> str:
    # TODO filter out lists with child bullet points
    soup = BeautifulSoup(html.strip(),'html.parser')
    ul_tags = soup.find_all('ul')
    for ul_tag in ul_tags:
        if max([total_text_length(c) for c in ul_tag.children]) < config['maximum_pill_length']:
            ul_tag['class'] = ul_tag.get('class', []) + ['pill-list']
    return ''.join([str(c) for c in soup.contents])


# @app.route('/resume', methods=['GET', 'POST'])
# def test():
#     values = {
#         'template_name_or_list':'resume/resume.tmpl',
#         'title':'resume'
#     }

#     with open('./app/static/md/maxwell_mullin_resume_ats_optomized.md') as f:
#         # https://python-markdown.github.io/extensions/attr_list/
#         values['body'] = div_wrap_h_tags(add_class_to_short_lists(markdown.markdown(f.read(), extensions=['attr_list', 'tables', 'meta'])))

#     return render_template(**config|values)

# @app.route('/cia_guide_to_sucsess', methods=['GET', 'POST'])
# def cia():
#     values = {
#         'template_name_or_list':'resume/resume.tmpl',
#         'title':'resume'
#     }

#     with open('./app/static/md/cia_guide_to_sucsess.md') as f:
#         # https://python-markdown.github.io/extensions/attr_list/
#         values['body'] = div_wrap_h_tags(add_class_to_short_lists(markdown.markdown(f.read(), extensions=['attr_list', 'tables', 'footnotes', 'meta'])))

#     return render_template(**config|values)


@app.route('/download_resume_md')
def download_resume_md():
    return send_file('./static/md/maxwell_mullin_resume.md', as_attachment=True)

def get_metadata_value(markdown_obj, key):
    if key in markdown_obj.Meta:
        return markdown_obj.Meta[key]
    if key in config['default_metadata']:
        return config['default_metadata'][key]
    return None

def render_article(path):
    # parse them markdown from path
    with open(path) as f:
        # create parser
        md = markdown.Markdown(extensions = ['attr_list', 'tables', 'footnotes', 'meta'])

        # parse  markdown to html
        html = md.convert(f.read())

        # restructure html to allow for more styling
        html = add_class_to_short_lists(html)
        html = div_wrap_h_tags(html)

        values = {
            'template_name_or_list':'article.tmpl',
            'title': get_metadata_value(md, 'title'),
            'author': get_metadata_value(md, 'author'),
            'theme_url': url_for('static', filename=os.path.join('themes', get_metadata_value(md, 'theme'))),
            'body':html
        }

        # render via template
        all_articles[path.removeprefix(config['articles_dir']).removesuffix('.md')] = render_template(**config|values)

@app.before_first_request
def render_all_articles():
    article_paths = []
    for directory in os.walk(config['articles_dir'], followlinks=True):
        for file in directory[2]:
            article_paths.append(os.path.join(directory[0], file))
    # look for files
    for path in article_paths:
        render_article(path)

@app.route('/a/<path>')
def get_article(path):
    print(all_articles.keys())
    if path in all_articles:
        return all_articles[path]
    return all_articles['404']




serve(app, host="0.0.0.0", port=5000)

