import pickle
import os

_sentiment_model = None
_vectorizer = None

def load_sentiment_model():
    global _sentiment_model, _vectorizer
    if _sentiment_model is None or _vectorizer is None:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        model_path = os.path.join(base_dir, 'models', 'sentiment_model.pkl')
        vec_path = os.path.join(base_dir, 'models', 'tfidf_vectorizer.pkl') # Reuse same vectorizer for simplicity
        
        if os.path.exists(model_path) and os.path.exists(vec_path):
            with open(model_path, 'rb') as f:
                _sentiment_model = pickle.load(f)
            with open(vec_path, 'rb') as f:
                _vectorizer = pickle.load(f)
        else:
             raise FileNotFoundError("Sentiment models not found. Please train the model first.")

def analyze_sentiment(text):
    if _sentiment_model is None or _vectorizer is None:
        load_sentiment_model()
        
    features = _vectorizer.transform([text])
    prediction = _sentiment_model.predict(features)[0]
    
    probabilities = _sentiment_model.predict_proba(features)[0]
    confidence = max(probabilities)
    
    return prediction, round(confidence * 100, 2)
