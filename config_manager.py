import os
import json

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT_DIR, 'config.json')

def load_config():
    with open (CONFIG_PATH, 'r') as file:
        config_data = json.load(file)

    return config_data

print(load_config())