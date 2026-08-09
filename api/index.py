import os
import sys

# Add the project root to sys.path
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BACKEND_DIR = os.path.join(ROOT_DIR, "backend")
sys.path.insert(0, BACKEND_DIR)

# Import the application factory from the backend
from app import create_app

# Vercel's Python runtime requires the 'app' variable to be exposed
app = create_app()
