# Email Automation Script

A simple Python script that helps you send automated emails using Gmail's SMTP server.

## 🚀 Features

- Send automated emails using Gmail
- Customizable email subject and body
- Error handling and success notifications
- Secure email sending with TLS encryption

## 📋 Prerequisites

Before using this script, you need:

1. Python 3.x installed on your computer
2. A Gmail account
3. Gmail App Password (see setup instructions below)

## 🔧 Setup Instructions

### 1. Gmail App Password Setup

1. Go to your Google Account settings (https://myaccount.google.com/)
2. Click on "Security"
3. Enable "2-Step Verification" if not already enabled
4. Go back to Security and find "App Passwords"
5. Select "Mail" and your device
6. Click "Generate"
7. Copy the 16-character password that appears

### 2. Script Setup

1. Download or clone this repository
2. Open `email_automation.py`
3. Replace the following information in the `main()` function:
   ```python
   sender_email = "your_email@gmail.com"  # Your Gmail address
   sender_password = "your_app_password"   # The App Password you generated
   receiver_email = "recipient@example.com"  # Where to send the email
   ```

## 💻 How to Use

1. Open your terminal/command prompt
2. Navigate to the script's directory
3. Run the script:
   ```bash
   python email_automation.py
   ```

## 📝 Customizing the Email

You can customize the email content by modifying these parts in the `main()` function:

```python
subject = "Your Subject Here"
body = """
Your email message here.
You can write multiple lines.
"""
```

## ⚠️ Important Notes

- Never share your App Password with anyone
- Keep your email credentials secure
- The script uses Gmail's SMTP server (smtp.gmail.com)
- Make sure you have an active internet connection

## 🔍 Troubleshooting

If you get an error:
1. Check if your Gmail address is correct
2. Verify your App Password is correct
3. Ensure you have an active internet connection
4. Check if 2-Step Verification is enabled on your Google Account

## 📚 Dependencies

This script uses Python's built-in libraries:
- smtplib
- email.mime.text
- email.mime.multipart
- datetime

No additional packages are required!

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## 📄 License

This project is open source and available under the MIT License. 