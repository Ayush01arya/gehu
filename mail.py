# # import smtplib
# # from email.mime.multipart import MIMEMultipart
# # from email.mime.text import MIMEText
# #
# # def send_email(gmail_user, app_password, to_email, subject, message_body):
# #     # Set up the SMTP server
# #     smtp_server = "smtp.gmail.com"
# #     smtp_port = 587
# #
# #     # Create the email
# #     msg = MIMEMultipart()
# #     msg["From"] = gmail_user
# #     msg["To"] = to_email
# #     msg["Subject"] = subject
# #     msg.attach(MIMEText(message_body, "plain"))
# #
# #     try:
# #         # Connect to the server and send the email
# #         server = smtplib.SMTP(smtp_server, smtp_port)
# #         server.starttls()  # Secure the connection
# #         server.login(gmail_user, app_password)
# #         server.sendmail(gmail_user, to_email, msg.as_string())
# #         server.quit()
# #
# #         print("Email sent successfully!")
# #     except Exception as e:
# #         print(f"Failed to send email. Error: {e}")
# #
# # # Example usage
# # gmail_user = "ayusharya11oct@gmail.com"
# # app_password = "lijp ekzb cuyp fsej"  # Use your Gmail App Password here
# # to_email = "ayusharya.personal@gmail.com"
# # subject = "Test Email"
# # message_body = "This is a test email sent using Gmail's SMTP server."
# #
# # send_email(gmail_user, app_password, to_email, subject, message_body)
# import smtplib
# import random
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
# def send_email(gmail_user, app_password, to_email, subject, message_body):
#     # Set up the SMTP server
#     smtp_server = "smtp.gmail.com"
#     smtp_port = 587
#
#     # Create the email
#     msg = MIMEMultipart()
#     msg["From"] = gmail_user
#     msg["To"] = to_email
#     msg["Subject"] = subject
#     msg.attach(MIMEText(message_body, "plain"))
#
#     try:
#         # Connect to the server and send the email
#         server = smtplib.SMTP(smtp_server, smtp_port)
#         server.starttls()  # Secure the connection
#         server.login(gmail_user, app_password)
#         server.sendmail(gmail_user, to_email, msg.as_string())
#         server.quit()
#
#         print("OTP sent successfully!")
#     except Exception as e:
#         print(f"Failed to send OTP. Error: {e}")
#
# def generate_otp():
#     # Generate a 6-digit OTP
#     return random.randint(100000, 999999)
#
# def main():
#     gmail_user = "gehuautocell@gmail.com"
#     app_password = "sqyj oljf cotg wxga"  # Replace with your Gmail App Password
#
#     # Get the recipient's email
#     to_email = input("Enter the recipient's email address: ")
#
#     # Generate and send OTP
#     otp = generate_otp()
#     subject = "Your One-Time Password (OTP) for Verification"
#     message_body = f"""
#     <!DOCTYPE html>
#     <html lang="en">
#     <head>
#         <meta charset="UTF-8">
#         <meta name="viewport" content="width=device-width, initial-scale=1.0">
#         <style>
#             /* Card container styling */
#             .email-container {{
#                 font-family: Arial, sans-serif;
#                 max-width: 500px;
#                 margin: 0 auto;
#                 padding: 20px;
#                 background-color: #f9f9f9;
#                 border-radius: 8px;
#                 border: 1px solid #e0e0e0;
#                 box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
#             }}
#             .header {{
#                 background-color: #4CAF50;
#                 color: white;
#                 padding: 10px;
#                 text-align: center;
#                 border-radius: 8px 8px 0 0;
#             }}
#             .body-content {{
#                 padding: 20px;
#                 text-align: center;
#                 color: #333;
#             }}
#             .otp {{
#                 font-size: 24px;
#                 font-weight: bold;
#                 color: #4CAF50;
#                 margin: 20px 0;
#             }}
#             .message {{
#                 font-size: 16px;
#                 color: #555;
#             }}
#             .footer {{
#                 font-size: 12px;
#                 color: #999;
#                 padding-top: 20px;
#                 text-align: center;
#                 border-top: 1px solid #e0e0e0;
#             }}
#         </style>
#     </head>
#     <body>
#         <div class="email-container">
#             <div class="header">
#                 <h2>Your Verification Code</h2>
#             </div>
#             <div class="body-content">
#                 <p>Hello!</p>
#                 <p>Thank you for using our service. To complete your verification, please use the following One-Time Password (OTP):</p>
#                 <div class="otp">{otp}</div>
#                 <p class="message">This code is valid for the next 10 minutes. For security reasons, please do not share it with anyone.</p>
#                 <p class="message">Once verified, you’ll be able to access your account and explore our features.</p>
#             </div>
#             <div class="footer">
#                 <p>If you did not request this code, please ignore this email or contact our support team.</p>
#                 <p>Best regards,</p>
#                 <p>Your Service Team</p>
#             </div>
#         </div>
#     </body>
#     </html>
#     """
#
#     send_email(gmail_user, app_password, to_email, subject, message_body)
#
#     # Ask the user to enter the OTP
#     user_otp = int(input("Enter the OTP sent to your email: "))
#
#     # Verify the OTP
#     if user_otp == otp:
#         print("Welcome!")
#     else:
#         print("Wrong OTP. Please try again.")
#
# # Run the main function
# main()
import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(gmail_user, app_password, to_email, subject, message_body):
    # Set up the SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create the email
    msg = MIMEMultipart()
    msg["From"] = gmail_user
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message_body, "html"))  # Set to "html" to render HTML in the email

    try:
        # Connect to the server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(gmail_user, app_password)
        server.sendmail(gmail_user, to_email, msg.as_string())
        server.quit()

        print("OTP sent successfully!")
    except Exception as e:
        print(f"Failed to send OTP. Error: {e}")

def generate_otp():
    # Generate a 6-digit OTP
    return random.randint(1000, 9999)

def main():
    gmail_user = "gehuautocell@gmail.com"
    app_password = "sqyj oljf cotg wxga" # Replace with your Gmail App Password

    # Get the recipient's email
    to_email = input("Enter the recipient's email address: ")

    # Generate and send OTP
    otp = generate_otp()
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

    # https://i.ibb.co/tB6TVNb/LOGOi.png

    send_email(gmail_user, app_password, to_email, subject, message_body)

    # Ask the user to enter the OTP
    user_otp = int(input("Enter the OTP sent to your email: "))

    # Verify the OTP
    if user_otp == otp:
        print("Welcome!")
    else:
        print("Wrong OTP. Please try again.")

# Run the main function
main()
