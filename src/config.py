import os

# Configuration settings
DATA_DIR = os.path.join(os.getcwd(), 'data')
MODELS_DIR = os.path.join(os.getcwd(), 'models')

# Knowledge graph settings
KG_DATABASE = 'graphdb'
KG_HOST = 'localhost'
KG_PORT = 7474

# NLP settings
NLP_MODEL = 'bert'
NLP_PRETRAINED = True
