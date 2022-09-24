from transformers import pipeline
#generator = pipeline("text-generation")
#generated_text = generator("In this tutorial, we will teach you how to find the best pot size for tomatoes", max_length=600)[0]["generated_text"]
# downloads model weights
classifier = pipeline("sentiment-analysis")
classifier("I've been waiting for a HuggingFace course my whole life.")