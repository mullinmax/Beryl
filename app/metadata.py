from dataclasses import dataclass
import os
from flask import url_for

from config import config

@dataclass
class metadata:
    data:dict

    def __getitem__(self, key):
        if isinstance(key, list):
            return {k:self[k] for k in key}
        if key in self.data:
            return self.data[key]
        if key in config['default_metadata']:
            return config['default_metadata'][key]
        else:
            return None

    def __setitem__(self, key, value):
        self.data[key] = value

    def __flag_mapper__(self, value:str) -> bool:
        clean_value = value.strip().lower()
        if clean_value in ['y', 'yes', 't', 'true']:
            return True
        if clean_value in ['n', 'no', 'f', 'false']:
            return False
        return None

    def __post_init__(self):
        # markdown's metadata engine likes to return everything as a list, this gets us back to k-v pairs
        for key, val in self.data.items():
            if isinstance(val, list) and len(val) == 1:
                self.data[key] = val[0]
        
        # for these we don't need to do "if in self.data" since getitem falls back to defaults
        self.data['style_structure'] = os.path.join('theme/structure/', self['style_structure'])
        self.data['style_colorway'] = os.path.join('theme/colorway/', self['style_colorway'])
        self.data['style_code'] = os.path.join('theme/code/', self['style_code'])
        self.data['hidden'] = self.__flag_mapper__(self['hidden'])
        self.data['url_ext'] = self['path'].removeprefix(config['articles_dir']).removesuffix('.md')
        self.data['nav_group'] = os.path.dirname(self['url_ext'])
        if 'nav_order' not in self.data:
            self.data['nav_order'] = 0
        else:
            self.data['nav_order'] = int(self.data['nav_order'])