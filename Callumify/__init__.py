 
def callumify(text):
    return f"{text}... but with extra chaos, courtesy of Callum!"
def grUHHHHHHHHHMble():
    print("GRUUUUUUUUUUUH!!!")
def print_loud(text):
    print(text.upper() + "!!!")
def print_quote(quote, sayer):
    print(f"as a wise {sayer} once said: '{quote}'")
import random
def print_glitch(text):
    glitched = ''.join(random.choice([c, '#', '%', '*', '/', '^', ')']) for c in text)
    print(f"{glitched}")
import requests

import requests

def quote_of_the_day():
    print("please note that the quote of the day function cannot be held liable for any emotional/physical distress caused by any quotes it gives!")
    try:
        response = requests.get("https://zenquotes.io/api/today")
        if response.status_code == 200:
            data = response.json()
            quote = data[0]['q']
            author = data[0]['a']
            print(f"🧘 Quote of the Day:\n\"{quote}\" — {author}")
        else:
            print("Zen is silent today. Try again later.")
    except Exception as e:
        print("⚠️ Failed to fetch quote. Here's a Callum classic instead:")
        print("\"NO GOD PLEASE NO!\" — Callum, probably")