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


def send_email_hr(gmail_user, app_password, to_email, company_name, hr_name):
    # Set up the SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create the email
    subject = "Exploring Opportunities at {}".format(company_name)
    message_body = f"""
  <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exploring Opportunities at {company_name}")</title>
    <style>
        /* General Reset */
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            color: #333;
            padding: 20px;
        }}
        .email-container {{
            max-width: 650px;
            margin: auto;
            background-color: #ffffff;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            overflow: hidden;
            border: 1px solid #e0e0e0;
        }}

        /* Header */
        .header {{
            background:  linear-gradient(135deg, #9b59b6, #e84393);
            color: #ffffff;
            padding: 30px;
            text-align: center;
        }}
        .header h1 {{
            font-size: 24px;
            font-weight: 700;
            margin-bottom: 5px;
        }}
        .header p {{
            font-size: 16px;
            margin-top: 5px;
        }}
        /* Content */
        .content {{
            padding: 25px 30px;
            font-size: 16px;
            line-height: 1.6;
            color: #555;
        }}
        .content p {{
            margin: 15px 0;
        }}
        .highlight {{
            color: #9b59b6;
            font-weight: 600;
        }}
        .cta-button {{
            display: inline-block;
            padding: 12px 24px;
            margin-top: 20px;
            background-color: #3498db; /* Solid background for desktop */
            color: #ffffff;
            text-decoration: none;
            font-weight: 600;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }}
        .cta-button:hover {{
            background-color: #2980b9; /* Darker shade on hover for desktop */
        }}

        /* Responsive styles */
        @media (max-width: 600px) {{
            .cta-button {{
                background-color: #e84393; /* Different color for mobile */
                padding: 10px 18px;
                font-size: 15px;
                }}
            .cta-button:hover {{
                background-color: #d6336c; /* Darker shade on hover for mobile */}}
                }}


        /* Footer */
        .footer {{
            background-color: #e7e7e7;
            padding: 20px;
            text-align: center;
            font-size: 14px;
            color: #333;
            border-top: 1px solid #e0e0e0;
        }}
        .footer a {{
            color: black;
            text-decoration: none;
            font-weight: 500;
            margin: 0 10px;
        }}
        .footer .icon {{
            margin: 0 5px;
            vertical-align: middle;
        }}
        .footer img {{
            width: 20px; /* Size of the icons */
            height: 20px;
            vertical-align: middle;
            margin-right: 5px;
        }}

        /* Media Queries for Mobile */
        @media (max-width: 600px) {{
            .content {{
                padding: 20px;
            }}
            .header h1 {{
                font-size: 20px;
            }}
            .cta-button {{
                padding: 10px 18px;
                font-size: 15px;
            }}
            .footer {{
                padding: 15px;
            }}
        }}
    </style>
</head>
<body>
    <div class="email-container">
        <!-- Header Section -->
        <div class="header">
            <h1>Exploring Opportunities at {company_name}</h1>
            <p>An Enthusiastic Candidate Ready to Make an Impact</p>
        </div>

        <!-- Content Section -->
        <div class="content">
            <p>Dear <span class="highlight">{hr_name}</span>,</p>

            <p>I hope you’re well. My name is Ayush Arya, and I am currently pursuing a Bachelor’s in Computer Science and Engineering with a focus on Machine Learning at Graphic Era Hill University. I am reaching out to inquire about potential internship opportunities within <span class="highlight">{company_name}</span>’s data and AI teams, as I am very interested in contributing to your innovative work.</p>

            <p>In my recent role as an AI Application Intern at Astroverse Pvt Ltd, I developed a chatbot that improved customer support response speed by 20% and increased engagement by 30%. Additionally, my internship with IIT BHU allowed me to enhance language translation tools, making them more accessible for research workflows.</p>

            <p>With skills in Python, SQL, TensorFlow, and frameworks like Flask and React, I am eager to bring my experience in AI and data analysis to <span class="highlight">{company_name}</span>. I would appreciate the opportunity to discuss how I could add value to your team.</p>

            <a href="mailto:ayusharya.personal@gmail.com" class="cta-button">Let’s Connect</a>

            <p>Thank you very much for your time and consideration. I look forward to hearing from you.</p>

            <p>Warm regards,<br>
            Ayush Arya</p>
        </div>

        <!-- Footer Section -->
        <div class="footer">
            <p>
                <a href="https://ayusharya.me">
                    <img src="https://img.icons8.com/ios-filled/50/domain.png" class="icon" alt="Website">Website
                </a> | 
                <a href="tel:+918081133775">
                    <img src="https://img.icons8.com/ios-filled/50/000000/phone.png" class="icon" alt="Phone">+91-8081133775
                </a> | 
                <a href="https://linkedin.com/in/ayusharya25">
                    <img src="https://img.icons8.com/ios-filled/50/000000/linkedin.png" class="icon" alt="LinkedIn">LinkedIn
                </a>
                </a> | 

            </p>
        </div>
    </div>
</body>
</html>"""

    msg = MIMEMultipart()
    msg["From"] = gmail_user
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message_body, "html"))

    try:
        # Connect to the server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(gmail_user, app_password)
        server.sendmail(gmail_user, to_email, msg.as_string())
        server.quit()
        return "Email sent successfully!"
    except Exception as e:
        return f"Failed to send email. Error: {e}"


@app.route('/send_email_hr', methods=['POST'])
def api_send_email():
    data = request.json
    gmail_user = "ayusharya.personal@gmail.com"
    app_password = "uclx fhnh plxf jgjh"  # Replace with your Gmail App Password

    to_email = data.get("to_email")
    company_name = data.get("company_name")
    hr_name = data.get("hr_name")

    result = send_email_hr(gmail_user, app_password, to_email, company_name, hr_name)
    return jsonify({"message": result})

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
