import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Sender and receiver details
sender_email = "monikaayyalusamy2007@gmail.com"
receiver_email = "monikaayyalusamy2007@gmail.com"
password = "****************"  # Use App Password for security

# Create the email message
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "Test Email from Python"

# Email body
body = "Hello, this is a test email sent using Python."
msg.attach(MIMEText(body, "plain"))

try:
    # Setup SMTP session
    server = smtplib.SMTP("smtp.gmail.com", 587)  # Use correct SMTP server
    server.starttls()  # Secure connection
    server.login(sender_email, password)  # Login

    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())

    # Close the SMTP session
    server.quit()
    print("Email sent successfully!")

except Exception as e:
    print(f"Error: {e}")

