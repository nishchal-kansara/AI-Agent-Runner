from fastapi import FastAPI, Request

# Create a FastAPI application instance
# This app acts as a webhook receiver
app = FastAPI()

# Endpoint that receives webhook calls
# Used to confirm that external integration works correctly
@app.post("/webhook")
async def receive_webhook(req: Request):
    # Read the incoming JSON payload
    # Represents data sent by the IntegrationAgent
    data = await req.json()

    # Print the received data to the console
    # This helps verify webhook execution during testing
    print("Webhook received", data)

    # Return a simple success response
    # Confirms that the webhook was processed
    return {"status": "ok"}