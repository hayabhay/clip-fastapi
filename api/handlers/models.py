import logging
from typing import Tuple

import clip
from config import DEVICE, MODELS_DIR

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# This is a global variable to cache loaded models
# This can be set in the loader function to have multiple models in memory or just one
MODELS = {}


def get_clip_model(model_version: str, load_multiple_models: bool = False) -> Tuple:
    """Function to load a CLIP model"""
    global MODELS

    if model_version not in MODELS:
        logger.info(f"{model_version} not in memory! Loading..")
        model, preprocess = clip.load(model_version, download_root=MODELS_DIR, device=DEVICE)

        if load_multiple_models:
            MODELS[model_version] = (model, preprocess)
        else:
            MODELS = {model_version: (model, preprocess)}
    else:
        logger.info(f"{model_version} already in memory! Using..")
        model, preprocess = MODELS[model_version]

    return model, preprocess
