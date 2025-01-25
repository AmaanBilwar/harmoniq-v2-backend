
import asyncio 
from  websockets import serve
# from transformers import pipeline, AutoModelForImageClassification, AutoImageProcessor
# from PIL import Image
# import torch

# device = 0 if torch.cuda.is_available() else -1

# # Load model and image processor with use_fast=True
# model = AutoModelForImageClassification.from_pretrained(
#     "motheecreator/vit-Facial-Expression-Recognition"
# )
# image_processor = AutoImageProcessor.from_pretrained(
#     "motheecreator/vit-Facial-Expression-Recognition", use_fast=True
# )

# # Initialize pipeline with model and image processor
# pipe = pipeline(
#     task="image-classification",
#     model=model,
#     feature_extractor=image_processor,
#     device=device,
# )


# def classify_emotion(image_path):
#     result = pipe(image_path)
#     emotion = result[0]["label"]
#     confidence = result[0]["score"]
#     return emotion, confidence


# image_path = "C:/Users/amaan/Downloads/woody.jpg"
# emotion, confidence = classify_emotion(image_path)
# print(f"Detected emotion: {emotion}")

