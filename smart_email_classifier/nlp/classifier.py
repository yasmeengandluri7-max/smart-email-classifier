import pickle
import os

_classifier = None
_vectorizer = None

def load_models():
    global _classifier, _vectorizer
    if _classifier is None or _vectorizer is None:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        model_path = os.path.join(base_dir, 'models', 'email_classifier.pkl')
        vec_path = os.path.join(base_dir, 'models', 'tfidf_vectorizer.pkl')
        
        if os.path.exists(model_path) and os.path.exists(vec_path):
            with open(model_path, 'rb') as f:
                _classifier = pickle.load(f)
            with open(vec_path, 'rb') as f:
                _vectorizer = pickle.load(f)
        else:
            raise FileNotFoundError("Models not found. Please train the model first.")

def classify_email(text):
    if _classifier is None or _vectorizer is None:
        load_models()
        
    features = _vectorizer.transform([text])
    prediction = _classifier.predict(features)[0]
    
    probabilities = _classifier.predict_proba(features)[0]
    confidence = max(probabilities)
    
    return prediction, round(confidence * 100, 2)
