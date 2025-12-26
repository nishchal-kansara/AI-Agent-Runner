from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from router import route
from guardrails import apply_guardrails
from data_loader import load_dataset
from instruction_store import build_instruction_store
from training.diagnosis import diagnose_training_issues
from training.hyperparams import recommended_hyperparameters

# Load the dataset once when the application starts
# This avoids reloading data on every request
DATASET = load_dataset()

# Build instruction mappings from the dataset
# Each intent gets its own system instruction and risk level
INSTRUCTION_STORE = build_instruction_store(DATASET)

# Create the FastAPI application instance
app = FastAPI()

# Defines the expected structure for API based requests
# Used for validation when JSON input is required
class RequestModel(BaseModel):
    prompt: str
    intent: str
    risk: str


# Home page rendered in the browser
# Provides a simple form to trigger agent execution
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>AI Agent</title>
        </head>
        <body>
            <h2>Run Agent</h2>

            <form action="/run-ui" method="post">
                <label>Prompt:</label><br>
                <input type="text" name="prompt" value="Trigger integration from browser"><br><br>

                <label>Intent:</label><br>
                <input type="text" name="intent" value="integration"><br><br>

                <label>Risk:</label><br>
                <input type="text" name="risk" value="low"><br><br>

                <button type="submit">Run Agent</button>
            </form>
        </body>
    </html>
    """


# Endpoint used to analyze training behavior
# Accepts training log values and explains failures
@app.post("/diagnose")
def run_diagnosis(logs: dict):
    return diagnose_training_issues(logs)


# Endpoint that exposes recommended training settings
# Helps explain how to improve training stability and safety
@app.get("/hyperparameters")
def get_hyperparameters():
    return recommended_hyperparameters()


# Browser friendly endpoint to run an agent
# Reads form input and routes the request dynamically
@app.post("/run-ui")
async def run_from_ui(request: Request):
    # Extract form data submitted from the browser
    form = await request.form()

    prompt = form["prompt"]
    intent = form["intent"]
    risk = form["risk"]

    # Apply safety rules before executing the agent
    guard = apply_guardrails(prompt, risk)

    # Select the correct agent based on intent
    agent = route(intent)

    # Attach dataset based instruction context
    # This guides agent behavior and risk awareness
    context = {
        "instruction": INSTRUCTION_STORE[intent]
    }

    # Execute the agent logic
    result = agent.run(prompt, context, guard)

    # Return a structured JSON response
    return JSONResponse(content=result.dict())