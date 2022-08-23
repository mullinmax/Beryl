#!/home/maxwell/miniconda3/envs/done-gen/bin/python
import json
from flask import Flask, request, jsonify, render_template, redirect, url_for
from waitress import serve
import markdown
import re
from bs4 import BeautifulSoup
import bs4

from config import config

app = Flask(__name__)

@app.route('/')
def root():
    return redirect("./resume", code=302)


from bs4 import BeautifulSoup
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



@app.route('/resume')
def test():
    values = {
        'template_name_or_list':'resume/resume.tmpl',
        'title':'resume'
    }

    with open('./app/static/md/resume.md') as f:
        # https://python-markdown.github.io/extensions/attr_list/
        values['body'] = div_wrap_h_tags(add_class_to_short_lists(markdown.markdown(f.read(), extensions=['attr_list'])))

    return render_template(**config|values)

serve(app, host="0.0.0.0", port=5000)

