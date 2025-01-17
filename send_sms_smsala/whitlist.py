import frappe
import requests

API_KEY = ""
API_PASSWORD = ""
SENDER_ID = ""
BASE_URL = "https://api.smsala.com/api/SendSMS"

@frappe.whitelist()
def send_sms(phone_number, message):
    """
    Sends an SMS message to the specified phone number using the SMS API.

    Parameters:
    phone_number (str): The recipient's phone number, including country code (e.g., "973123123").
    message (str): The message content to be sent via SMS.

    Returns:
    None: This function prints the status of the message delivery. If the message is sent successfully, 
          it prints the response data; otherwise, it prints an error message.

    Raises:
    requests.exceptions.RequestException: If the request to the SMS API fails.
    """
    # Construct the endpoint URL
    url = BASE_URL
    # Define the parameters for the API request
    payload = {
        "api_id": API_KEY,
        "api_password": API_PASSWORD,
        "sms_type": "T",
        "encoding": "T",
        "sender_id": SENDER_ID,
        "phonenumber": phone_number,
        "textmessage": message,
    }
    # Set the headers to send JSON
    headers = {
        "Content-Type": "application/json"
    }
    try:
        # Make the POST request with JSON data
        response = requests.post(url, json=payload, headers=headers)
        response_data = response.json()
        if response.status_code == 200 and response_data.get("status") == "S":
            frappe.msgprint(f"Message sent successfully: {response_data}")
        else:
            frappe.warn(f"Failed to send message: {response_data}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")