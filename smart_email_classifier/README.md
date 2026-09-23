# Smart Email Classifier and Reply Generator

A full-stack Natural Language Processing (NLP) web application that intelligently classifies emails, analyzes sentiment, extracts important information, generates summaries, and provides editable auto-replies based on tone.

## Features
- **Email Classification:** Categorizes emails into 12 categories (Work, Personal, Education, Meeting, Finance, Complaint, Customer Support, Job/Career, Promotion, Important, Spam, Other).
- **Sentiment Analysis:** Detects if the email tone is Positive, Neutral, or Negative.
- **Entity Extraction:** Identifies emails, phone numbers, dates, times, and financial amounts.
- **Summarization:** Generates an extractive summary of the original text.
- **Smart Reply Generator:** Creates context-aware replies with customizable tones (Professional, Friendly, Formal, Short).
- **Full-Stack Dashboard:** A modern UI built with Bootstrap and vanilla JS, communicating via a Flask API.

## Technologies Used
- **Frontend:** HTML5, CSS3, JavaScript (ES6), Bootstrap 5
- **Backend:** Python, Flask
- **NLP & Machine Learning:** NLTK, Scikit-Learn, TF-IDF Vectorizer, Logistic Regression
- **Data Manipulation:** Pandas, NumPy
- **Deployment:** Gunicorn

## System Architecture & NLP Workflow
1. **Input:** User submits an email via the UI.
2. **API Layer:** Flask endpoint `/api/analyze` receives the request.
3. **Preprocessing:** Lowercasing, punctuation removal, stop-word removal, and lemmatization (using NLTK).
4. **Classification:** TF-IDF transformation followed by Logistic Regression prediction.
5. **Entity & Summary:** Extractive summarization and Regex/Rule-based NER.
6. **Reply Generation:** Template-based generation mapped to the model's classification and tone.
7. **Response:** JSON payload returned and rendered interactively on the Dashboard.

## Dataset & Model Information
- **Dataset:** Contains ~1200 procedurally generated synthetic emails with diverse templates mapped to sentiments and categories.
- **Model:** Logistic Regression trained on TF-IDF vectors. Two models are used, one for Category and one for Sentiment.

---

## Local Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/smart-email-classifier.git
cd smart-email-classifier
```

### 2. Create a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Download NLTK Resources
```bash
python download_nltk.py
```

### 5. Train the Model
*Note: Pre-trained models are already provided in the `models/` directory, but you can retrain them if you update the dataset.*
```bash
python training/train_model.py
```

### 6. Run the Application
```bash
python app.py
```
Open your browser and navigate to `http://localhost:5000`.

---

## API Documentation

### `POST /api/analyze`
**Request Body:**
```json
{
  "email": "Dear team, let's schedule a meeting for tomorrow at 2 PM.",
  "tone": "Professional"
}
```
**Response:**
```json
{
  "category": "Meeting",
  "category_confidence": 92.4,
  "sentiment": "Neutral",
  "sentiment_confidence": 88.1,
  "summary": "Dear team, let's schedule a meeting for tomorrow at 2 PM.",
  "entities": [
    {"type": "Date", "value": "tomorrow"},
    {"type": "Time", "value": "2 PM"}
  ],
  "reply": "Thank you for the update regarding the meeting. I have marked the specified date and time in my calendar."
}
```

### `GET /api/health`
**Response:** `{"status": "ok"}`

---

## Deployment Instructions (Render)

This project is fully ready for deployment on [Render](https://render.com).

1. **Create a GitHub Repository:** Create a new repo and push all these files.
2. **Log into Render:** Go to Render Dashboard and click **New > Web Service**.
3. **Connect Repository:** Authorize GitHub and select your repository.
4. **Configuration:**
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt && python download_nltk.py`
   - **Start Command:** `gunicorn app:app`
5. **Environment Variables (Optional):**
   - You can add `FLASK_ENV=production` in the advanced settings.
6. **Deploy:** Click **Create Web Service**. Render will automatically build and deploy your app.
7. **Verify:** Once deployed, click the provided `.onrender.com` URL to use the live app!

---
*Developed as a Full-Stack NLP Mini Project.*
