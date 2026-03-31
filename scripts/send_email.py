def send_email(to_email, subject, body):
    try:
        print(f"\n--- Email to {to_email} ---")
        print("Subject:", subject)
        print(body)
        print("-------------------------\n")

    except Exception as e:
        print(f"Failed to process email for {to_email}:", e)