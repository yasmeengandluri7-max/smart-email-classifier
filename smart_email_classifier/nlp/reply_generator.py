import random

def generate_reply(category, sentiment, entities, tone, text):
    """
    Generates a reply based on category, tone, and extracted information.
    Uses random variations so that regenerating the reply produces different text.
    """
    reply = ""
    
    # Base templates with variations
    if category == "Meeting":
        if tone == "Professional":
            reply = random.choice([
                "Thank you for the update regarding the meeting. I have noted the details and will adjust my schedule accordingly.",
                "I have received your email about the meeting. I will review the agenda and be prepared.",
                "Thank you for scheduling this. I will make sure to attend the meeting as discussed."
            ])
        elif tone == "Friendly":
            reply = random.choice([
                "Got it, thanks for letting me know about the meeting! Looking forward to it.",
                "Thanks for the heads-up on the meeting. See you then!",
                "Awesome, I've got the meeting details saved. Catch you later!"
            ])
        elif tone == "Short":
            reply = random.choice(["Acknowledged. Thanks.", "Got it.", "Noted, thank you."])
        else:
            reply = random.choice([
                "Thank you for the meeting details. I will review the schedule and get back to you if needed.",
                "Received the meeting invitation. Let me know if anything changes."
            ])
            
    elif category == "Job/Career":
        if tone == "Professional":
            reply = random.choice([
                "Thank you for reaching out regarding the opportunity. I appreciate the information and will review the details.",
                "I have received your email concerning the job opportunity. Thank you for your time and consideration.",
                "Thank you for the update on the application process. I look forward to the next steps."
            ])
        else:
            reply = random.choice([
                "Thanks for the update on the application! I appreciate your time.",
                "Thank you so much for reaching out about this opportunity!",
                "Got your email regarding the job. Thanks for keeping me in the loop."
            ])
            
    elif category == "Complaint":
        reply = random.choice([
            "Thank you for bringing this issue to our attention. We apologize for any inconvenience caused and are looking into the matter immediately.",
            "We are very sorry to hear about your experience. Our team is investigating this issue and will resolve it as soon as possible.",
            "I apologize for the frustration this has caused. We are taking your feedback seriously and working on a fix."
        ])
        
    elif category == "Customer Support":
        reply = random.choice([
            "Thank you for reaching out to our support team. We have received your request and a representative will be with you shortly.",
            "We have received your support ticket. Our team is reviewing the details and will get back to you soon.",
            "Thanks for contacting support. We are currently looking into your issue and will provide an update shortly."
        ])
        
    elif category == "Finance":
        reply = random.choice([
            "Thank you for the financial update. We have received your email and will process the information accordingly.",
            "We have received your invoice/financial document. It has been forwarded to the billing department for processing.",
            "This confirms receipt of your financial communication. Thank you."
        ])
        
    elif category == "Personal":
        if tone == "Friendly":
            reply = random.choice([
                "Hey! Great to hear from you. Let's catch up soon!",
                "Hi! So nice to hear from you. Hope everything is going well.",
                "Hey there! Thanks for the message. Let's talk soon!"
            ])
        else:
            reply = random.choice([
                "Thank you for your message. I hope you are doing well.",
                "I received your email. Thank you for keeping in touch."
            ])
            
    elif category == "Education":
        reply = random.choice([
            "Thank you for the academic update. I have noted the information.",
            "I have received your email regarding the educational materials/update. Thank you.",
            "This confirms receipt of your academic communication."
        ])
        
    elif category == "Spam":
        reply = "No reply needed."
        
    else:
        if tone == "Professional":
            reply = random.choice([
                "Thank you for your email. I have received your message and will review it shortly.",
                "This is an automated acknowledgment that we have received your email. We will process it shortly."
            ])
        elif tone == "Friendly":
            reply = random.choice([
                "Thanks for reaching out! I've got your message.",
                "Got your email! I'll take a look as soon as I can.",
                "Thanks for getting in touch!"
            ])
        elif tone == "Short":
            reply = random.choice(["Received, thank you.", "Got it.", "Thanks."])
        else:
            reply = random.choice([
                "Thank you for your message. I will respond in detail if required.",
                "Message received. Thank you."
            ])

    # Incorporate entities if possible
    has_time = any(e['type'] == 'Time' for e in entities)
    has_date = any(e['type'] == 'Date' for e in entities)
    
    if category == "Meeting" and has_time and has_date:
         reply += random.choice([
             " I have marked the specified date and time in my calendar.",
             " I've blocked out the date and time on my end.",
             " The date and time are noted on my schedule."
         ])
         
    if tone == "Formal":
         reply = "Dear Sender,\n\n" + reply + "\n\nSincerely,\n[Your Name]"

    return reply
