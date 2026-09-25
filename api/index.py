import sys
import os

# Add the smart_email_classifier directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'smart_email_classifier'))

from app import app
