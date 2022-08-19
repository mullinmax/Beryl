from flask import url_for

def static_file(path):
    def get_static_file():
        return url_for('static', filename=path)
    return get_static_file

config = {
    'app_name':'max-was-here.com',
    'app_url':'https://max-was-here.com',
    'resume_data': {
        'profile_picture_url':static_file('img/headshot.jpg'),
        'contact_information':{
            'full_name':'Maxwell Mullin',
            'email':'inbox@max-was-here.com',
            'phone':'555.555.5555'
        }
    }
}