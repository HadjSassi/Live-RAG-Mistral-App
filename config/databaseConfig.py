# databaseConfig.py

import json
import os

config_path = os.path.join(os.path.dirname(__file__), 'databaseConfig.json')
with open(config_path, 'r') as f:
    CONFIG = json.load(f)
