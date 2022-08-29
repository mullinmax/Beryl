from dataclasses import dataclass, field
import markdown
from bs4 import BeautifulSoup, element
from flask import render_template
import os

from config import config
from metadata import metadata

@dataclass
class article:
    
    path: str
    metadata:metadata = None
    body:str = None
    
    def __post_init__(self):
        with open(self.path) as f:
            # create parser
            md = markdown.Markdown(extensions = ['attr_list', 'tables', 'footnotes', 'meta', 'nl2br', 'toc', 'codehilite', 'fenced_code'])

            # parse  markdown to html
            self.body = md.convert(f.read())

            # restructure html to allow for more styling
            self.body = self.__add_class_to_short_lists__(self.body)
            self.body = self.__div_wrap_h_tags__(self.body)

            # save metadata
            self.metadata = metadata(data = md.Meta|{'path':self.path})

            
    def render(self, navigation=[]):
        args = {
            'template_name_or_list':config['article_template_path'],
            'title': self.metadata['title'],
            'url_ext': self.metadata['url_ext'],
            'active_nav_group':self.metadata['nav_group'],
            'style_structure': self.metadata['style_structure'],
            'style_colorway': self.metadata['style_colorway'],
            'style_code':self.metadata['style_code'],
            'body':self.body,
            'navigation':navigation
        }

        # render via template
        return render_template(**config|args)    
    
    def __div_wrap_h_tags__(self, html:str)->str:
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

    def __total_text_length__(self, tag) -> int:
        if isinstance(tag, element.NavigableString):
            return len(str(tag))
        if isinstance(tag, list):
            return sum([total_text_length(c) for c in tag])
        try:
            return total_text_length(tag.contents)
        except:
            return len(str(tag))

    def __add_class_to_short_lists__(self, html:str) -> str:
        # TODO filter out lists with child bullet points
        soup = BeautifulSoup(html.strip(),'html.parser')
        ul_tags = soup.find_all('ul')
        for ul_tag in ul_tags:
            if max([self.__total_text_length__(c) for c in ul_tag.children]) < config['maximum_pill_length']:
                ul_tag['class'] = ul_tag.get('class', []) + ['pill-list']
        return ''.join([str(c) for c in soup.contents])