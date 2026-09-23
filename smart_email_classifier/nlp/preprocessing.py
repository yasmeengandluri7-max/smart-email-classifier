import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# In a real environment, we'd ensure these are downloaded. 
# We will add a script or handle this in the main app.
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    if not isinstance(text, str):
        return ""
    
    # 1. Convert to lowercase
    text = text.lower()
    
    # 2. Remove URLs, email addresses, and specific entities for pure text analysis
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\S+@\S+', '', text)
    
    # 3. Remove punctuation and special characters
    text = re.sub(r'[^\w\s]', '', text)
    
    # 4. Tokenization (basic split is fine after removing punctuation)
    tokens = text.split()
    
    # 5. Stop-word removal and Lemmatization
    cleaned_tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    
    # 6. Rejoin text
    return ' '.join(cleaned_tokens)
