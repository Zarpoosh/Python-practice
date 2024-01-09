# from twilio.rest import Client
# import random

# # Your Twilio account SID and auth token
# account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
# auth_token = 'YOUR_TWILIO_AUTH_TOKEN'

# # Create a Twilio client
# client = Client(account_sid, auth_token)

# # Function to generate a random number string
# def generate_random_number(length):
#     return ''.join(random.choices('0123456789', k=length))

# # Send SMS function
# def send_sms(to_number, from_number, message):
#     message = client.messages.create(
#         body=message,
#         from_=from_number,
#         to=to_number
#     )
#     print(f"SMS with Message SID '{message.sid}' has been successfully sent.")

# # Specify the recipient and sender mobile numbers
# to_number = 'RECIPIENT_PHONE_NUMBER_WITH_COUNTRY_CODE'
# from_number = 'YOUR_TWILIO_PHONE_NUMBER_WITH_COUNTRY_CODE'

# # Generate a random number string
# random_number = generate_random_number(6)

# # Compose the message
# message = f"Here is your random number: {random_number}"

# # Send the SMS
# send_sms(to_number, from_number, message)

import random
import requests

def send_sms(to_number, message):
    # Twilio API credentials
    account_sid = 'YOUR_ACCOUNT_SID'
    auth_token = 'YOUR_AUTH_TOKEN'
    twilio_number = 'YOUR_TWILIO_PHONE_NUMBER'

    # Twilio API endpoint
    url = 'https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json'.format(account_sid)

    # Generate random numbers
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(10))

    payload = {
        'To': to_number,
        'From': twilio_number,
        'Body': message + random_numbers
    }

    # Send the SMS using Twilio API
    response = requests.post(url, auth=(account_sid, auth_token), data=payload)

    if response.status_code == 201:
        print('SMS sent successfully!')
    else:
        print('Failed to send SMS. Error:', response.text)