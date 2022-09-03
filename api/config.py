import pathlib

import clip
import torch
from dotenv import load_dotenv

# First load all environment variables from .env file before any additional import
load_dotenv()

APP_DIR = pathlib.Path(__file__).parent.absolute()

# Next set the project root directory.
PROJECT_DIR = APP_DIR.parent

# Set the model directory & create if it doesn't exist
MODELS_DIR = PROJECT_DIR / "models"
MODELS_DIR.mkdir(exist_ok=True)

# Clip specific variables
MAX_TEXT_LENGTH = 4096
DEFAULT_CLIP_MODEL = "ViT-B/32"
DEVICE = device = "cuda" if torch.cuda.is_available() else "cpu"
AVAILABLE_MODELS = clip.available_models()
