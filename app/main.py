#!/home/maxwell/miniconda3/envs/done-gen/bin/python
import json
from flask import Flask, request, jsonify, render_template, redirect, url_for
from waitress import serve
import markdown
import re
from bs4 import BeautifulSoup

from config import config

app = Flask(__name__)

@app.route('/')
def root():
    return redirect("./resume", code=302)

@app.route('/resume')
def resume():
    values = {
        'template_name_or_list':'resume.html',
        'title':'This is the title'
    }
    return render_template(**config|values)

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

@app.route('/test')
def test():
    values = {
        'template_name_or_list':'resume/resume.tmpl',
        'title':'resume'
    }

    with open('./app/static/md/resume.md') as f:
        # https://python-markdown.github.io/extensions/attr_list/
        values['body'] = div_wrap_h_tags(markdown.markdown(f.read(), extensions=['attr_list']))

    return render_template(**config|values)

serve(app, host="0.0.0.0", port=5000)

