from config import AVAILABLE_MODELS, DEFAULT_CLIP_MODEL, MAX_TEXT_LENGTH
from pydantic import BaseModel, Field, validator


# Pydantic validation for text input
# -----------------------------
class ClipModel(BaseModel):
    model_version: str = Field(default=DEFAULT_CLIP_MODEL, description="CLIP model to use")

    @validator("model_version")
    def model_version_validator(cls, model_version):
        if model_version not in AVAILABLE_MODELS:
            raise ValueError(f"Model version {model_version} not available. Please choose from {AVAILABLE_MODELS}")
        return model_version


class TextInput(ClipModel):
    text: str = Field(..., max_length=MAX_TEXT_LENGTH, description="Text to embed", example="A happy dog.")


class ImageInput(ClipModel):
    image: str = Field(
        ...,
        description="Image to embed (URL or base64 encoded)",
        example="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Doushouqi-dog.svg/512px-Doushouqi-dog.svg.png",
    )
