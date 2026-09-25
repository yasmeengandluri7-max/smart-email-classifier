import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import pickle

# Ensure we're in the right directory
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(base_dir, 'data', 'email_dataset.csv')
model_dir = os.path.join(base_dir, 'models')

# 1. Load dataset
print("Loading dataset...")
df = pd.read_csv(data_path)

# 2. Display dataset shape
print(f"Dataset shape: {df.shape}")

# 3. Clean and preprocess data (we'll just use a simple clean here before vectorizing)
df.dropna(subset=['email_text', 'category', 'sentiment'], inplace=True)
print("Data cleaned.")

X = df['email_text']
y_cat = df['category']
y_sent = df['sentiment']

# 5. Split data
X_train, X_test, y_cat_train, y_cat_test = train_test_split(X, y_cat, test_size=0.2, random_state=42)
_, _, y_sent_train, y_sent_test = train_test_split(X, y_sent, test_size=0.2, random_state=42)

# 6. Apply TF-IDF
print("Applying TF-IDF...")
vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# 7. Train classification models
print("Training Category Classification Model...")
cat_model = LogisticRegression(max_iter=1000)
cat_model.fit(X_train_vec, y_cat_train)

print("Training Sentiment Classification Model...")
sent_model = LogisticRegression(max_iter=1000)
sent_model.fit(X_train_vec, y_sent_train)

# 8. Evaluate Category Model
y_cat_pred = cat_model.predict(X_test_vec)
print("\n--- Category Model Evaluation ---")
print(f"Accuracy: {accuracy_score(y_cat_test, y_cat_pred):.4f}")
print(f"Precision (macro): {precision_score(y_cat_test, y_cat_pred, average='macro', zero_division=0):.4f}")
print(f"Recall (macro): {recall_score(y_cat_test, y_cat_pred, average='macro', zero_division=0):.4f}")
print(f"F1-score (macro): {f1_score(y_cat_test, y_cat_pred, average='macro', zero_division=0):.4f}")
print("Confusion Matrix:\n", confusion_matrix(y_cat_test, y_cat_pred))

# Evaluate Sentiment Model
y_sent_pred = sent_model.predict(X_test_vec)
print("\n--- Sentiment Model Evaluation ---")
print(f"Accuracy: {accuracy_score(y_sent_test, y_sent_pred):.4f}")
print(f"Precision (macro): {precision_score(y_sent_test, y_sent_pred, average='macro', zero_division=0):.4f}")
print(f"Recall (macro): {recall_score(y_sent_test, y_sent_pred, average='macro', zero_division=0):.4f}")
print(f"F1-score (macro): {f1_score(y_sent_test, y_sent_pred, average='macro', zero_division=0):.4f}")
print("Confusion Matrix:\n", confusion_matrix(y_sent_test, y_sent_pred))

# 10. Save trained models
os.makedirs(model_dir, exist_ok=True)
with open(os.path.join(model_dir, 'email_classifier.pkl'), 'wb') as f:
    pickle.dump(cat_model, f)
with open(os.path.join(model_dir, 'sentiment_model.pkl'), 'wb') as f:
    pickle.dump(sent_model, f)
with open(os.path.join(model_dir, 'tfidf_vectorizer.pkl'), 'wb') as f:
    pickle.dump(vectorizer, f)

print(f"\nModels successfully saved to {model_dir}")
