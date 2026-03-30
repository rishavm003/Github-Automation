import os
import requests

def get_ai_response(prompt):
    try:
        import google.generativeai as genai
    except ImportError:
        genai = None

    gemini_key = os.getenv("GEMINI_API_KEY")
    deepseek_key = os.getenv("DEEPSEEK_API_KEY")
    openrouter_key = os.getenv("OPENROUTER_API_KEY")

    if not any([gemini_key, deepseek_key, openrouter_key]):
        raise Exception("Missing AI API keys.")

    # 1. Try Gemini
    if gemini_key and genai:
        try:
            genai.configure(api_key=gemini_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Gemini failed: {e}. Falling back...")
    
    # 2. Try DeepSeek
    if deepseek_key:
        try:
            headers = {
                "Authorization": f"Bearer {deepseek_key}",
                "Content-Type": "application/json"
            }
            data = {
                "model": "deepseek-chat",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7
            }
            resp = requests.post("https://api.deepseek.com/chat/completions", headers=headers, json=data, timeout=10)
            resp.raise_for_status()
            return resp.json()["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"DeepSeek failed: {e}. Falling back...")

    # 3. Try OpenRouter
    if openrouter_key:
        try:
            headers = {
                "Authorization": f"Bearer {openrouter_key}",
                "Content-Type": "application/json"
            }
            data = {
                "model": "openrouter/auto",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7
            }
            resp = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data, timeout=10)
            resp.raise_for_status()
            return resp.json()["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"OpenRouter failed: {e}.")
    
    raise Exception("All configured AI providers failed")
