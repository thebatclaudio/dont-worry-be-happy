import os, json, sys

class Config(object):
    def __init__(self):
        script_dir = os.path.dirname(__file__)
        config_rel_path = 'config.json'
        config_abs_path = os.path.join(script_dir, config_rel_path)

        try:
            with open(config_abs_path) as config_file:
                config = json.load(config_file)
                self._config = config
        except IOError:
            print("Can't open configuration file "+config_abs_path)
            sys.exit(0)

    def get(self, property_name):
        if property_name not in self._config.keys(): # we don't want KeyError
            return None  # just return None if not found
        
        return self._config[property_name]