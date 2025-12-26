import requests
import os
from dotenv import load_dotenv

# Load environment variables at application startup
# This allows configuration to stay outside the code
load_dotenv()

# This function sends data to an external webhook
# The webhook address is read from environment variables
def send_webhook(payload):
    # Read the webhook URL from the environment
    # Keeps sensitive or changeable values out of code
    webhook_url = os.getenv("WEBHOOK_URL")

    # Send the payload to the webhook endpoint
    # Uses an HTTP POST request with JSON data
    response = requests.post(
        webhook_url,
        json=payload,
        timeout=5
    )

    # Return the HTTP status code
    # Used to confirm successful delivery
    return response.status_code
