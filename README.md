# OpenAI's CLIP served over FastAPI

A simple FastAPI encapsulation of OpenAI's CLIP model to embed text & images.
It also has a dockerized version (CPU) for deployment on Google Cloud Run.

To get started, clone this repo & create a fresh virtualenv with Python 3.7+ (tested on 3.10.5)
```
pip install -r requirements/requirements-dev.txt
cd api
uvicorn main:app --reload
```

Also, you can build a container (cpu-version)
```
sudo docker build -t clip .
sudo docker run -p 8000:8000 clip
```
