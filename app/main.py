#!/home/maxwell/miniconda3/envs/done-gen/bin/python
import json
from flask import Flask, request, jsonify, render_template, redirect, url_for
from waitress import serve

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

serve(app, host="0.0.0.0", port=5000)

