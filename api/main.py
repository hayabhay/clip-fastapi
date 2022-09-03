import clip
import torch
from config import DEVICE
from fastapi import FastAPI
from handlers.images import load_image
from handlers.models import get_clip_model
from handlers.schemas import ImageInput, TextInput

# Initialize the FastAPI app
app = FastAPI()


@app.post("/embed/text/")
def get_text_embedding(text_input: TextInput) -> dict:
    """Function to get text embedding from CLIP model"""
    # First get the model
    model, _ = get_clip_model(text_input.model_version)

    with torch.no_grad():
        # Encode and normalize the description using CLIP
        embedding = model.encode_text(clip.tokenize(text_input.text).to(DEVICE))
        embedding /= embedding.norm(dim=-1, keepdim=True)

    embedding = embedding.tolist()[0]

    return {"text": text_input.text, "embedding": embedding}


@app.post("/embed/image/")
def get_image_embedding(image_input: ImageInput) -> dict:
    """Function to get text embedding from CLIP model"""
    # First get the model
    model, preprocess = get_clip_model(image_input.model_version)

    # Next download the image
    raw_image = load_image(image_input.image)

    with torch.no_grad():
        # Encode and normalize the description using CLIP
        embedding = model.encode_image(preprocess(raw_image).unsqueeze(0).to(DEVICE))
        embedding /= embedding.norm(dim=-1, keepdim=True)

    embedding = embedding.tolist()[0]

    return {"image": image_input.image[:512], "embedding": embedding}


@app.get("/")
def home():
    return "I'm alive & healthy! To interact with me, go to /docs for Swagger UI or /redoc for ReDoc."
