import pandas as pd
import os
print("KEY:", os.getenv("OPENAI_API_KEY"))
from scripts.generate_email import generate_email
from scripts.send_email import send_email

def main():
    print("=== AI Email Automation ===")

    topic = input("Enter email topic: ").strip()

    if not topic:
        print("Topic cannot be empty!")
        return

    print("\nGenerating email...\n")
    email_content = generate_email(topic)

    if not email_content:
        print("Failed to generate email.")
        return

    print("Email Generated Successfully!\n")

    try:
        contacts = pd.read_csv("data/contacts.csv")
    except Exception as e:
        print("Error reading contacts file:", e)
        return

    if "email" not in contacts.columns:
        print("contacts.csv must have 'email' column")
        return

    for email in contacts["email"]:
        send_email(email, "AI Generated Email", email_content)

    print("\nAll emails processed!")

if __name__ == "__main__":
    main()