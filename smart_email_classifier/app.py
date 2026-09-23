from flask import Flask, request, jsonify, render_template
import os
import traceback

# Import our NLP modules
from nlp.preprocessing import preprocess_text
from nlp.classifier import classify_email
from nlp.sentiment import analyze_sentiment
from nlp.entity_extractor import extract_entities
from nlp.summarizer import summarize_email
from nlp.reply_generator import generate_reply

app = Flask(__name__)

# Basic error handling for unhandled exceptions
@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "Internal server error", "details": str(e)}), 500

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/health')
def health_check():
    return jsonify({"status": "ok"})

@app.route('/api/analyze', methods=['POST'])
def analyze():
    try:
        data = request.json
        if not data or 'email' not in data:
            return jsonify({"error": "No email content provided"}), 400
            
        email_text = data['email']
        if not email_text or len(email_text.strip()) == 0:
            return jsonify({"error": "Please enter an email before analyzing."}), 400
            
        tone = data.get('tone', 'Professional')
        
        # 1. Preprocess
        cleaned_text = preprocess_text(email_text)
        
        # 2. Classify Category
        category, cat_conf = classify_email(cleaned_text)
        
        # 3. Sentiment Analysis
        sentiment, sent_conf = analyze_sentiment(cleaned_text)
        
        # 4. Extract Entities
        entities = extract_entities(email_text) # Extract from original to preserve formatting
        
        # 5. Summarize
        summary = summarize_email(email_text)
        
        # 6. Generate Reply
        reply = generate_reply(category, sentiment, entities, tone, email_text)
        
        return jsonify({
            "category": str(category),
            "category_confidence": cat_conf,
            "sentiment": str(sentiment),
            "sentiment_confidence": sent_conf,
            "summary": summary,
            "entities": entities,
            "reply": reply
        })
        
    except FileNotFoundError as e:
         return jsonify({"error": str(e), "fallback": True}), 500
    except Exception as e:
         traceback.print_exc()
         return jsonify({"error": "An error occurred during analysis", "details": str(e)}), 500

if __name__ == '__main__':
    # Start the app
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
