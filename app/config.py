from flask import url_for

def static_file(path):
    def get_static_file():
        return url_for('static', filename=path)
    return get_static_file

config = {
    'app_name':'max-was-here.com',
    'app_url':'https://max-was-here.com'
}