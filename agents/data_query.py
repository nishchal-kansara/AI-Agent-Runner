from agents.base import BaseAgent, AgentResult

# This agent handles requests related to data access
# It focuses on safe and compliant data usage
# It never performs direct database operations
class DataQueryAgent(BaseAgent):
    # Unique name used for routing and trace logging
    name = "DataQueryAgent"

    # Declares the type of tasks this agent can handle
    # Used by the router to select the correct agent
    capabilities = ["data_query"]

    # Main execution method for the agent
    # Receives user input system context and safety decision
    # Returns a structured AgentResult object
    def run(self, prompt, context, guardrails):
        # If the request is marked unsafe by guardrails
        # The agent blocks execution to prevent misuse
        if not guardrails["allowed"]:
            return AgentResult(
                # Message explains why the request was blocked
                response="Request blocked due to safety risk.",
                # Suggested next steps for safe handling
                action_items=["Escalate to compliance"],
                # No configuration is required for blocked requests
                required_configs={},
                # Trace records agent name and block status
                trace={"agent": self.name, "blocked": True}
            )

        # If the request is allowed
        # The agent provides a high level compliant approach
        # No real data is accessed or exposed
        return AgentResult(
            # Safe response describing compliant access
            response="Here is a compliant data access plan.",
            # Action steps that follow legal and ethical rules
            action_items=["Request approval", "Use anonymized fields"],
            # Indicates read only access to prevent data changes
            required_configs={"db": "read-only"},
            # Trace information used for auditing
            trace={"agent": self.name}
        )