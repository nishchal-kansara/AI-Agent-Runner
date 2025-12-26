# AI/ML Dynamic Agent System

## Overview

This project implements a dynamic AI agent system using ```FastAPI```. The system routes user requests to the most suitable agent based on intent and risk level. It focuses on reasoning about data quality safe behavior and controlled execution. The design is lightweight and avoids unnecessary model training while still ensuring clarity safety and structured output.

## Key Features

The system provides the following capabilities

- Intent based routing
- Multiple specialized agents
- Dataset driven instructions
- Safety guardrails
- Training issue analysis
- Hyperparameter recommendations
- Webhook based external integration
- Environment based configuration

## System Design

The system is built using a modular approach. Each part has a clear responsibility and works independently. This makes the system easy to understand maintain and extend.

Each user request follows a fixed flow.
- User input is received from the browser or API
- The intent of the request is identified
- Safety checks are applied based on risk level
- The request is routed to the correct agent
- The agent returns a structured output

This design keeps the logic clean predictable and easy to audit.

## Dataset Handling

The dataset file is named ```dataset.jsonl```. It is loaded only once when the application starts. This avoids repeated file access and keeps the system efficient.

The dataset provides the following information.
- Intent mapping for request routing
- Risk level for safety checks
- System instruction text to guide agent behavior
- Optional diversity tags for analysis and auditing

The dataset is not used as a live database. It is used only to guide agent behavior and support safety decisions.

## Agents Overview

The system includes four agents.

1. GeneralQAAgent - Provides simple informational responses.
2. TaskPlannerAgent - Creates a clear step by step action plan.
3. DataQueryAgent - Handles data related requests safely without direct access.
4. IntegrationAgent - Sends structured data to an external system using a webhook.

All agents return output in a consistent format.

## Safety Guardrails

Every request is checked before execution. The safety check uses the risk level associated with the request.

If the risk level is high the request is blocked. This ensures that unsafe or non compliant actions are not allowed to proceed.

The guardrail logic helps keep the system safe predictable and easy to audit.

## Training Analysis

The system includes logic to analyze training behavior. This logic helps explain why a model may behave incorrectly.

It identifies common issues such as.
- Overfitting
- Safety drift
- Gradient instability

The analysis logic is exposed through an API endpoint. This allows easy review and evaluation of training related problems.

## Hyperparameter Recommendations

Recommended training parameters are provided.

These values focus on

- Stable learning
- Small dataset handling
- Reduced risk of unsafe behavior

No training is triggered by this system.

## Webhook Integration

External integration is handled using a webhook.

The webhook endpoint is configured using environment variables.

This avoids hardcoded values and keeps the system flexible.

## Environment Configuration

Create a file named ```.env``` in the project root.

Add the following line

```
WEBHOOK_URL=http://localhost:9000/webhook
APP_ENV=development
```
The ```.env``` file should not be committed to version control.

## How to Run

1. Start the webhook receiver

```uvicorn webhook_receiver:app --port 9000```

2. Start the main application

```uvicorn app:app --reload```

3. Open the browser and visit

```http://127.0.0.1:8000```

Use the Run Agent button to execute the system.

## API Endpoints

POST ```/run-ui```  
Runs the selected agent using browser input.

POST ```/diagnose```  
Analyzes training related issues.

GET ```/hyperparameters```  
Returns recommended training settings.

## Output Structure

Each agent returns output with the following fields

* response
* action_items
* required_configs
* trace

The trace includes execution and safety details.
