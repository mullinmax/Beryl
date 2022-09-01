from flask import url_for

def static_file(path):
    def get_static_file():
        return url_for('static', filename=path)
    return get_static_file

config = {
    'app_name':'max-was-here.com',
    'app_url':'https://max-was-here.com',
    'profile_picture_url':static_file('img/headshot.jpg'),
    'maximum_pill_length':50,
    'articles_dir':'./app/static/articles/',
    'article_template_path':'article.html',
    'landing_page':'./a/about/welcome',
    'default_metadata':{
        'title':'untitled',
        'style_structure':'resume.css',
        'style_colorway':'minty.css',
        'style_code':'material.css',
        'hidden':'false'
    }
}