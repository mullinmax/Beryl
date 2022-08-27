from dataclasses import dataclass
import os
from flask import url_for

from config import config

@dataclass
class metadata:
    data:dict

    def __getitem__(self, key):
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
        
        # we don't need to check if these are in self.data since getitem falls back to defaults
        self.data['theme_url'] = url_for('static', filename=os.path.join('themes', self['theme']))
        self.data['url_ext'] = self['path'].removeprefix(config['articles_dir']).removesuffix('.md')
        self.data['hidden'] = self.__flag_mapper__(self['hidden'])