import os
from dotenv import load_dotenv

load_dotenv()

def print_key_stat(name):
    val = os.getenv(name)
    if val is None:
        print(f"{name}: NOT FOUND")
    else:
        print(f"{name}: (Len: {len(val)}) Truthy: {bool(val)}")

print_key_stat('GEMINI_API_KEY')
print_key_stat('DEEPSEEK_API_KEY')
print_key_stat('OPENROUTER_API_KEY')
print_key_stat('GITHUB_TOKEN')

print(f"any: {any([os.getenv('GEMINI_API_KEY'), os.getenv('DEEPSEEK_API_KEY'), os.getenv('OPENROUTER_API_KEY')])}")
