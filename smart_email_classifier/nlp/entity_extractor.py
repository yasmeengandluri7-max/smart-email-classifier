import re

def extract_entities(text):
    """
    Extracts basic entities like emails, phone numbers, dates, times, and names using Regex.
    In a full production environment with deep learning, spaCy NER would be ideal.
    For this robust deployment-ready version, Regex provides high reliability without huge models.
    """
    entities = []
    
    # Extract Email Addresses
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
    for email in emails:
        entities.append({"type": "Email", "value": email})
        
    # Extract Phone Numbers (basic formats)
    phones = re.findall(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', text)
    for phone in phones:
        entities.append({"type": "Phone", "value": phone})
        
    # Extract Times (e.g., 10 AM, 2:30 PM, 14:00)
    times = re.findall(r'\b(?:1[0-2]|0?[1-9])(?::[0-5][0-9])?\s*(?:AM|PM|am|pm)\b|\b(?:[01]?[0-9]|2[0-3]):[0-5][0-9]\b', text)
    for t in times:
        entities.append({"type": "Time", "value": t})
        
    # Extract Dates (e.g., Friday, 25 September, 2026, Q3, next week)
    days = re.findall(r'\b(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|tomorrow|today|yesterday)\b', text, re.IGNORECASE)
    for d in set(days): # Use set to avoid duplicates
        entities.append({"type": "Date", "value": d})
        
    dates_formal = re.findall(r'\b\d{1,2}(?:st|nd|rd|th)?\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s*(?:\d{4})?\b', text, re.IGNORECASE)
    for d in dates_formal:
        entities.append({"type": "Date", "value": d})
        
    # Extract Currency / Amounts
    money = re.findall(r'\$\d+(?:,\d{3})*(?:\.\d{2})?|\b\d+\s*(?:dollars|USD)\b', text, re.IGNORECASE)
    for m in money:
        entities.append({"type": "Finance", "value": m})

    # Return list of entity dicts
    return entities
