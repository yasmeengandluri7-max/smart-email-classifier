import pandas as pd
import random
import os

def generate_dataset(output_path, num_samples=1200):
    categories = [
        "Work", "Personal", "Education", "Meeting", "Finance", 
        "Complaint", "Customer Support", "Job/Career", "Promotion", 
        "Important", "Spam", "Other"
    ]
    
    sentiments = ["Positive", "Neutral", "Negative"]
    
    templates = {
        "Work": [
            ("Please find attached the report for Q3. Let me know if you need any revisions.", "Neutral"),
            ("Great job on the presentation today! The client was very impressed.", "Positive"),
            ("I am disappointed with the delay in the project delivery. We need to discuss this.", "Negative"),
            ("Can you send me the latest source code for the new feature?", "Neutral"),
            ("The server is down again. This is unacceptable, please fix it ASAP.", "Negative")
        ],
        "Personal": [
            ("Hey, are we still on for dinner tonight at 8 PM?", "Neutral"),
            ("It was wonderful seeing you over the weekend. Let's catch up again soon!", "Positive"),
            ("I'm sorry, I won't be able to make it to your party. Feeling a bit sick.", "Negative"),
            ("Happy Birthday! Hope you have a fantastic day.", "Positive"),
            ("Can you pick up some groceries on your way back?", "Neutral")
        ],
        "Education": [
            ("Your assignment is due on Friday by 11:59 PM via the student portal.", "Neutral"),
            ("Congratulations on passing the final exam with flying colors!", "Positive"),
            ("I am struggling with chapter 4. Could you explain the main concept again?", "Negative"),
            ("The lecture has been rescheduled to tomorrow at 10 AM in Room 302.", "Neutral"),
            ("I am writing to request an extension on my project deadline due to a family emergency.", "Negative")
        ],
        "Meeting": [
            ("Let's schedule a meeting for tomorrow at 2 PM to discuss the roadmap.", "Neutral"),
            ("I am looking forward to our catch-up meeting next week.", "Positive"),
            ("We need to postpone the meeting because key stakeholders are unavailable.", "Negative"),
            ("Here is the zoom link for our daily standup at 9:30 AM.", "Neutral"),
            ("The meeting yesterday was very productive. Thanks for organizing.", "Positive")
        ],
        "Finance": [
            ("Your invoice #4923 is attached. Please process the payment by the 15th.", "Neutral"),
            ("Your payment has been successfully received. Thank you for your business.", "Positive"),
            ("We noticed an overdue balance on your account. Please pay immediately to avoid fees.", "Negative"),
            ("Here is the budget breakdown for the next fiscal year.", "Neutral"),
            ("I am disputing the recent charge of $50 on my credit card. It was not authorized.", "Negative")
        ],
        "Complaint": [
            ("The product I received is damaged. I want a full refund immediately.", "Negative"),
            ("The service at your restaurant was terrible. I waited an hour for my food.", "Negative"),
            ("I have been trying to reach support for days with no response. This is frustrating.", "Negative"),
            ("My internet connection keeps dropping every five minutes. Fix it.", "Negative"),
            ("The software update completely broke my application workflow.", "Negative")
        ],
        "Customer Support": [
            ("How do I reset my password? I forgot it.", "Neutral"),
            ("Thank you for resolving my issue so quickly! Great support.", "Positive"),
            ("I need help configuring the API settings on my dashboard.", "Neutral"),
            ("The new feature is amazing, thanks for adding it based on my request.", "Positive"),
            ("Can someone please guide me on how to upgrade my subscription plan?", "Neutral")
        ],
        "Job/Career": [
            ("Please find my resume attached for the Software Engineer position.", "Neutral"),
            ("We are excited to offer you the position of Data Scientist at our company!", "Positive"),
            ("Unfortunately, we will not be moving forward with your application at this time.", "Negative"),
            ("I would like to schedule an interview with you for next Tuesday at 11 AM.", "Neutral"),
            ("Thank you for your guidance, I learned a lot during my internship.", "Positive")
        ],
        "Promotion": [
            ("Get 50% off your next purchase using this exclusive promo code!", "Positive"),
            ("Our Black Friday sale starts now! Don't miss out on these huge discounts.", "Positive"),
            ("Upgrade now to premium and get the first month entirely free.", "Positive"),
            ("Flash sale! All items are 20% off for the next 24 hours.", "Positive"),
            ("Check out our new collection of winter wear.", "Neutral")
        ],
        "Important": [
            ("URGENT: The production database is down. We need immediate assistance.", "Negative"),
            ("Action Required: Update your account security settings before the deadline.", "Neutral"),
            ("Critical update regarding the company policy changes starting next month.", "Neutral"),
            ("Emergency maintenance will be performed tonight from 12 AM to 4 AM.", "Negative"),
            ("Important notice: Your account will be suspended if you do not verify your email.", "Negative")
        ],
        "Spam": [
            ("You have won $1,000,000! Click here to claim your prize immediately.", "Positive"),
            ("Lose weight fast with this miracle pill. Buy now!", "Neutral"),
            ("Congratulations! You are the 100th visitor today. Claim your free iPhone.", "Positive"),
            ("Make money from home with zero investment. Join our scheme today.", "Neutral"),
            ("Your computer is infected with a virus! Call this number to fix it.", "Negative")
        ],
        "Other": [
            ("Just testing if this email address works.", "Neutral"),
            ("Here is the recipe for the chocolate cake.", "Neutral"),
            ("Do you know what time the library closes today?", "Neutral"),
            ("The weather looks nice outside.", "Positive"),
            ("I left my umbrella at the office.", "Neutral")
        ]
    }
    
    data = []
    
    # Generate variations by tweaking templates slightly
    for _ in range(num_samples):
        cat = random.choice(categories)
        template, sentiment = random.choice(templates[cat])
        
        # Minor variation logic (adding names, changing times)
        names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"]
        times = ["10 AM", "2 PM", "4:30 PM", "9 AM", "12 PM"]
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "tomorrow", "next week"]
        
        text = template
        if "tomorrow" in text or "next week" in text:
            text = text.replace("tomorrow", random.choice(days)).replace("next week", random.choice(days))
        if "10 AM" in text or "2 PM" in text or "8 PM" in text:
            text = text.replace("10 AM", random.choice(times)).replace("2 PM", random.choice(times)).replace("8 PM", random.choice(times))
            
        # Add random greeting sometimes
        if random.random() > 0.5 and not text.startswith(("Hey", "Dear", "URGENT")):
            greeting = random.choice(["Hi, ", "Hello, ", "Dear team, ", "Hey there, "])
            text = greeting + text
            
        data.append({"email_text": text, "category": cat, "sentiment": sentiment})
        
    df = pd.DataFrame(data)
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Generated {len(df)} samples and saved to {output_path}")
    print(df['category'].value_counts())

if __name__ == "__main__":
    generate_dataset("c:/Users/HP/Desktop/smart_email/smart_email_classifier/data/email_dataset.csv")
