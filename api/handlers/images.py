import base64
import logging
from io import BytesIO

import httpx
from PIL import Image

# Setup logger
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# Function to load an image from the web, gs or a binary string
def load_image(image_src: str) -> Image:
    """Function that takes in a string, determines the source and returns a correctly formatted PIL Image"""
    # Load the image depending on the type
    # TODO: This is a little shabby and fails if the file is not an image without a specific error message
    if image_src.startswith(("http://", "https://")):
        try:
            response = httpx.get(image_src)
            # Try to interpret the bytes as an image
            image = Image.open(BytesIO(response.content))
        except Exception as e:
            logger.error(f"Error loading image from web url: {e}")
            raise e
    else:
        try:
            # Try to interpret the bytes as an image
            image_binary = base64.decodebytes(image_src.encode())
            image = Image.open(BytesIO(image_binary))
        except Exception as e:
            logger.error(f"Error loading image from binary string: {e}")
            raise e
    return image
