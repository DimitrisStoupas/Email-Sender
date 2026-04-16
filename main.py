import smtplib
from email.mime.text import MIMEText

# SMTP Configuration
SMTP_SERVER = ""  # Replace with actual SMTP server
SMTP_PORT = 587  # 465 for SSL, 587 for TLS
USERNAME = ""
PASSWORD = ""

# Email Details
sender_email = "info@worldepic.gr"
receiver_emails = "dimitrisstoupas@worldepic.gr"
subject = "Test Email from Python"
body = "Hello, this is a test email sent using\n\n Python! \n O Yea\n YK YK YK Who \n it\n is!"

# Create the email
message = MIMEText(body, "plain")
message["Subject"] = subject
message["From"] = sender_email
message["To"] = receiver_emails

# Send the email
with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.starttls()  # Secure connection
    server.login(USERNAME, PASSWORD)
    server.sendmail(sender_email, receiver_emails, message.as_string())

print("Email sent successfully!")
