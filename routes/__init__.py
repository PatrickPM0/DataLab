from flask import Blueprint

# import blueprints
from .main import main_bp

# list of blueprints to register in the app
blueprints = [main_bp]
