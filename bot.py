# Pulse - Daily Summary Bot

import requests
from datetime import date


def get_weather(city="Thiruvananthapuram"):
    """Fetch today's weather."""

    url = f"https://wttr.in/{city}?format=3"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        return response.text.strip()

    except Exception as e:
        return f"Weather unavailable ({e})"
   
def get_quote():
    """Fetch a random motivational quote."""

    url = "https://zenquotes.io/api/random"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        quote = data[0]["q"]
        author = data[0]["a"]

        return f'"{quote}" - {author}'

    except Exception as e:
        return f"Quote unavailable ({e})"


def build_summary():
    """Build the full daily summary."""

    today = date.today().strftime("%A, %d %B %Y")

    weather = get_weather()
    quote = get_quote()

    summary = f"""
==================================
PULSE - Daily Summary
{today}
==================================

WEATHER
{weather}

TODAY'S QUOTE
{quote}

==================================
"""

    return summary
 
def run():
    """Main entry point."""

    summary = build_summary()

    print(summary)

    with open("daily_summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)



if __name__ == "__main__":
    run()