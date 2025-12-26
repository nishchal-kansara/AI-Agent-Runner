from pydantic import BaseModel
from typing import List, Dict

# This model defines the standard output format
# Every agent must return results in this structure
# This ensures consistency across all agents in the system
class AgentResult(BaseModel):
    # Final message shown to the user
    response: str

    # List of next steps or follow up actions
    # Helps make the agent output actionable
    action_items: List[str]

    # Configuration details required to complete actions
    # Example webhook endpoint or environment setup
    required_configs: Dict

    # Execution details used for tracing and auditing
    # Includes agent name risk level and data source
    trace: Dict


# This is the base class for all agents in the system
# It defines a common interface that every agent must follow
class BaseAgent:
    # Name of the agent
    # Used for routing and traceability
    name: str

    # List of tasks the agent is capable of handling
    # Helps the router decide which agent to use
    capabilities: List[str]

    # Core method that every agent must implement
    # Takes user input context and safety rules
    # Returns a structured AgentResult object
    def run(self, prompt, context, guardrails) -> AgentResult:
        # This method is intentionally not implemented here
        # Each specific agent provides its own logic
        raise NotImplementedError