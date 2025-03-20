import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def send_email(sender_email, sender_password, receiver_email, subject, body):
    """
    Function to send an email using SMTP
    """
    try:
        # Create message container
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # Add body to email
        msg.attach(MIMEText(body, 'plain'))

        # Create SMTP session
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        # Login to the server
        server.login(sender_email, sender_password)
        
        # Send email
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        
        print(f"Email sent successfully at {datetime.now()}")
        return True
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

def main():
    # Email configuration
    sender_email = "your_email@gmail.com"  # Replace with your email
    sender_password = "your_app_password"   # Replace with your app password
    receiver_email = "recipient@example.com"  # Replace with recipient's email
    
    # Email content
    subject = "Automated Email Test"
    body = """
    Hello!
    
    This is an automated email sent using Python's smtplib library.
    
    Best regards,
    Your Name
    """
    
    # Send the email
    send_email(sender_email, sender_password, receiver_email, subject, body)

if __name__ == "__main__":
    main() 