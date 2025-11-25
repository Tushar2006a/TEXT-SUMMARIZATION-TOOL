# Import the HuggingFace summarization model 
from transformers import pipeline

# Loading a pretrained text summarization model
summarizer = pipeline("summarization")

# Ask user for input
text = input("Enter your paragraph to summarize:\n\n")

# Generate the summary
summary = summarizer(text, max_length=60, min_length=20, do_sample=False)

# Print original and summarized text
print("\nOriginal Text:\n", text)
print("\nSummary:\n", summary[0]['summary_text'])
