from flask import Flask, request
from flask_mail import Mail, Message
import random
import time
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# 1 Flask-Mail Configuration- providing the details we're using to send the gmail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # SMTP Server
app.config['MAIL_PORT'] = 465  # SSL Port (for TLS use 587)
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')  # Sender Email from .env
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')  # App Password from .env
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# 2 Initialize Flask-Mail
mail = Mail(app)

# Dictionary to store OTPs and their creation times
otp_storage = {}

# 3 Function to Generate OTP using random library
def generate_otp():
    return str(random.randint(100000, 999999))  # 6-digit OTP

# 4 Route to Send OTP
@app.route('/send-otp', methods=['POST'])
def send_otp():
    data = request.json  # Get JSON data from frontend
    email = data.get('email')  # Extract email from request from frontend that user will enter

    otp = generate_otp()  # Generate OTP
    creation_time = datetime.now()  # Get current time
    
    # Store OTP and its creation time
    otp_storage[email] = {'otp': otp, 'creation_time': creation_time}
    
    # 5 Create and Send Email
    msg = Message('Your OTP Code', sender=app.config['MAIL_USERNAME'], recipients=[email])
    msg.body = f'Your OTP for logging into the PriceSPy app is: {otp}. It is valid for 5 minutes and will expire after a time limit of 5 minutes.'
    
    try:
        mail.send(msg)  # Send email
        return "", 200  # Just return success status (Frontend will show message)
    except Exception as e:
        print(e)  # Print the exception for debugging
        return "", 500  # Generic failure status (Frontend will handle error message)

# 6 Route to Verify OTP
@app.route('/verify-otp', methods=['POST'])
def verify_otp():
    data = request.json  # Get JSON data from frontend
    email = data.get('email')  # Extract email from request
    user_otp = data.get('otp')  # Extract OTP from request

    if email in otp_storage:
        stored_otp = otp_storage[email]['otp']
        creation_time = otp_storage[email]['creation_time']
        
        # Check if OTP is still valid (within 5 minutes)
        if datetime.now() - creation_time <= timedelta(minutes=5):
            if user_otp == stored_otp:
                del otp_storage[email]  # Remove OTP from storage after successful verification
                return "", 200  # OTP is valid
            else:
                return "", 401  # OTP is invalid
        else:
            del otp_storage[email]  # Remove expired OTP from storage
            return "", 410  # OTP has expired
    else:
        return "", 404  # OTP not found for the given email

# 7 Run the Flask App
if __name__ == '__main__':
    app.run(debug=True)