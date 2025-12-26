from agents.base import BaseAgent, AgentResult
from webhook_utils import send_webhook

# This agent handles external system integration
# It uses a webhook to notify another service
# No paid tools or direct execution is involved
class IntegrationAgent(BaseAgent):
    # Unique agent name used for routing and tracing
    name = "IntegrationAgent"

    # Declares the type of capability this agent supports
    # Used by the router to select this agent
    capabilities = ["webhook"]

    # Main execution method for the integration agent
    # Receives the user prompt context and safety decision
    # Returns a structured AgentResult
    def run(self, prompt, context, guardrails):
        # Payload sent to the external webhook
        # Contains event name and original user prompt
        payload = {
            "event": "integration_triggered",
            "prompt": prompt
        }

        # Sends the payload to the webhook endpoint
        # The endpoint is configured using environment variables
        status = send_webhook(payload)

        # Returns a structured result after webhook execution
        return AgentResult(
            # Confirms successful webhook execution
            response="Webhook sent successfully.",
            # Suggested action to confirm webhook delivery
            action_items=["Verify webhook receiver logs"],
            # Indicates webhook configuration is externalized
            required_configs={
                "webhook": "Configured via environment variable"
            },
            # Trace details for auditing and evaluation
            trace={
                "agent": self.name,
                "risk": context["instruction"]["risk"],
                "webhook_status": status
            }
        )