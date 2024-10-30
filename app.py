from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import os

app = Flask(__name__)

# Enable CORS with credentials support
CORS(app, supports_credentials=True)

# Email configuration
GMAIL_USER = "gehuautocell@gmail.com"
APP_PASSWORD = "mbsj lsll aphf dqto"  # Replace with your actual app password

# Global variable to hold OTP temporarily
otp_store = {}

def send_email(to_email, otp):


    subject = "Your One-Time Password (OTP) for Verification"
    message_body = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                .email-container {{
                    font-family: Arial, sans-serif;
                    max-width: 500px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #ffffff;
                    border-radius: 8px;
                    border: 1px solid #e0e0e0;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    text-align: center;
                }}
                .header {{
                    padding: 20px;
                    background-color: #4CAF50;
                    border-radius: 8px 8px 0 0;
                }}
                .header img {{
                    max-width: 100px;

                }}
                .header h2 {{
                    color: white;
                    font-size: 22px;
                    margin: 10px 0;
                }}
                .body-content {{
                    padding: 20px;
                    color: #333;
                }}
                .otp {{
                    font-size: 32px;
                    font-weight: bold;
                    color: #4CAF50;
                    background-color: #f1f8e9;
                    border-radius: 8px;
                    padding: 10px;
                    margin: 20px 0;
                    display: inline-block;
                    letter-spacing: 4px;
                }}
                .message {{
                    font-size: 16px;
                    color: #555;
                    line-height: 1.6;
                }}
                .footer {{
                    font-size: 12px;
                    color: #999;
                    padding: 20px;
                    border-top: 1px solid #e0e0e0;
                    margin-top: 20px;
                }}
                .footer-address {{
                    text-align: left;
                    font-size: 12px;
                    margin-top: 10px;
                    color: #666;
                    line-height: 1.4;
                }}
                .footer-address h4 {{
                    margin: 5px 0;
                    font-weight: bold;
                }}
                .footer-address p {{
                    margin: 0;
                }}
                .copyright {{
                    text-align: center;
                    color: #999;
                    margin-top: 10px;
                    font-size: 12px;
                }}
            </style>
        </head>
        <body>
            <div class="email-container">
                <div class="header">
                    <img src="https://i.ibb.co/svwHBWv/logo0.png" alt="Logo" />
                    <h2>Welcome to GEyan Portal </h2>
                </div>
                <div class="body-content">
                    <p class="message">Hello User ! </p>
                    <p class="message">Thank you for using our service. To complete your verification, please use the following One-Time Password (OTP):</p>
                    <div class="otp">{otp}</div>
                    <p class="message">This code is valid for the next 10 minutes. For security reasons, please do not share it with anyone.</p>
                    <p class="message">Once verified, you’ll be able to access your account and explore all our features.</p>
                </div>
                <div class="footer">

                    <div class="copyright">
                        © Copyright 2024, All Rights Reserved by Graphic Era 
                    </div>
                </div>
            </div>
        </body>
        </html>
        """
    msg = MIMEMultipart()
    msg["From"] = GMAIL_USER
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message_body, "html"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(GMAIL_USER, APP_PASSWORD)
            server.sendmail(GMAIL_USER, to_email, msg.as_string())
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

@app.route("/send-otp", methods=["POST"])
def send_otp():
    """Generates and sends an OTP to the provided email."""
    data = request.json
    to_email = data.get("email")

    if not to_email:
        return jsonify({"error": "Email is required"}), 400

    otp = random.randint(100000, 999999)
    otp_store[to_email] = otp  # Store OTP in a temporary dictionary
    print(f"OTP sent: {otp} to email: {to_email}.")

    if send_email(to_email, otp):
        return jsonify({"message": "OTP sent successfully"})
    else:
        return jsonify({"error": "Failed to send OTP"}), 500

@app.route("/verify-otp", methods=["POST"])
def verify_otp():
    """Verifies the OTP entered by the user."""
    data = request.json
    entered_otp = data.get("otp")
    email = data.get("email")

    if not entered_otp or not email:
        return jsonify({"error": "OTP and email must be provided"}), 400

    # Check if the OTP matches and delete it after verification
    if email in otp_store and otp_store[email] == int(entered_otp):
        del otp_store[email]  # Remove OTP after successful verification
        return jsonify({"message": "Welcome!"})
    else:
        return jsonify({"error": "Invalid OTP, please try again"}), 400

if __name__ == "__main__":
    app.run(debug=True)
