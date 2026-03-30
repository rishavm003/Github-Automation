import os
import requests
import random

def get_daily_quote():
    # Try fetching a quote from an open API or use fallback
    fallback_quotes = [
        {"q": "The only way to do great work is to love what you do.", "a": "Steve Jobs"},
        {"q": "First, solve the problem. Then, write the code.", "a": "John Johnson"},
        {"q": "Simplicity is the soul of efficiency.", "a": "Austin Freeman"},
        {"q": "It always seems impossible until it's done.", "a": "Nelson Mandela"},
    ]
    try:
        response = requests.get("https://zenquotes.io/api/random", timeout=5)
        if response.status_code == 200:
            data = response.json()[0]
            return {"q": data["q"], "a": data["a"]}
    except Exception as e:
        print(f"Error fetching quote: {e}")
    
    return random.choice(fallback_quotes)

def write_daily_log(date_str, timestamp):
    quote_data = get_daily_quote()
    quote_text = f"\"{quote_data['q']}\" - {quote_data['a']}"
    
    os.makedirs("logs", exist_ok=True)
    log_file = f"logs/{date_str}.log"
    with open(log_file, "w", encoding="utf-8") as f:
        f.write(f"Timestamp: {timestamp}\n")
        f.write(f"Quote: {quote_text}\n")
        f.write("Status: Automation executed successfully.\n")
    return log_file, quote_data
