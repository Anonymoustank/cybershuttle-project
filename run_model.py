# run_model.py

import torch
from PIL import Image
import os
import argparse
import time
import tracemalloc
from transformers import AutoFeatureExtractor, ResNetForImageClassification

# Parse arguments
parser = argparse.ArgumentParser(description="Classify an input image using a pre-trained ResNet-50 model.")
parser.add_argument("--input", type=str, required=True, help="Path to input image")
parser.add_argument("--output", type=str, required=True, help="Path to save output prediction")
args = parser.parse_args()

# Set device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load model and feature extractor
model_name_or_path = "./my_local_model"

if not os.path.exists(model_name_or_path):
    model = ResNetForImageClassification.from_pretrained("microsoft/resnet-50")
    feature_extractor = AutoFeatureExtractor.from_pretrained("microsoft/resnet-50")
    os.makedirs(model_name_or_path, exist_ok=True)
    model.save_pretrained(model_name_or_path)
    feature_extractor.save_pretrained(model_name_or_path)
else:
    model = ResNetForImageClassification.from_pretrained(model_name_or_path)
    feature_extractor = AutoFeatureExtractor.from_pretrained(model_name_or_path)

model = model.to(device)

# Classify function
def classify_image(image_path, feature_extractor, model):
    image = Image.open(image_path)
    inputs = feature_extractor(image, return_tensors="pt")
    inputs = {k: v.to(device) for k, v in inputs.items()}

    with torch.no_grad():
        logits = model(**inputs).logits
    predicted_label = logits.argmax(-1).item()
    return model.config.id2label[predicted_label]

# Start measuring
start_time = time.time()
tracemalloc.start()

# Run classification
predicted_class = classify_image(args.input, feature_extractor, model)

# End measuring
current, peak = tracemalloc.get_traced_memory()
end_time = time.time()

# Save prediction and metrics
with open(args.output, "w") as f:
    f.write(f"Predicted class: {predicted_class}\n")
    f.write(f"Execution time: {end_time - start_time:.4f} seconds\n")
    f.write(f"Peak memory usage: {peak / 10**6:.4f} MB\n")

# Print to terminal
print(f"✅ Classification complete. Result saved to {args.output}")
print(f"⏱️ Execution time: {end_time - start_time:.4f} seconds")
print(f"💾 Peak memory usage: {peak / 10**6:.4f} MB")
