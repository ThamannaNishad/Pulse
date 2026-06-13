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


import smtplib
from email.mime.text import MIMEText

SMTP_EMAIL = os.environ["SMTP_EMAIL"]
SMTP_PASSWORD = os.environ["SMTP_PASSWORD"]
TO_EMAIL = os.environ["TO_EMAIL"]

def send_email(file_path):
    with open(file_path, "r") as f:
        content = f.read()

    msg = MIMEText(content)
    msg["Subject"] = "Pulse Daily Summary"
    msg["From"] = SMTP_EMAIL
    msg["To"] = TO_EMAIL

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(SMTP_EMAIL, SMTP_PASSWORD)
    server.sendmail(SMTP_EMAIL, TO_EMAIL, msg.as_string())
    server.quit()

send_email("daily_summary.txt")    