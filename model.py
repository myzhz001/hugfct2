from transformers import pipeline

# Define the model explicitly
model_name = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"
model = pipeline("text-classification", model=model_name)

# Print the model details to ensure it's loaded correctly
print("Model loaded:", model)

