def send_email(name: str, address: str, subject: str, body: str):
    print(f"Sending email to {name} ({address})")
    print("="*10)
    print(f"Subject: {subject}\n")
    print(body)