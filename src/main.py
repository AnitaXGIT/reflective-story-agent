
"""
Main entry point for the Reflective Story Article Generator
"""

import sys
import os

# Add parent directory to Python path so we can import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ui.interface import story_interface
from config.settings import settings

if __name__ == "__main__":
    story_interface.launch()