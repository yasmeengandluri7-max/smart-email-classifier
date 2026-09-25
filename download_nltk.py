import nltk

print("Downloading required NLTK data...")
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
try:
    nltk.download('punkt_tab')
except Exception as e:
    print("punkt_tab download failed (might not be needed):", e)
print("Done.")
