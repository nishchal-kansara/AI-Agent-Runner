from agents.base import BaseAgent, AgentResult

# This agent handles simple general questions
# It provides high level explanations without planning or actions
# Used when the intent is informational and low risk
class GeneralQAAgent(BaseAgent):
    # Name used for agent identification and tracing
    name = "GeneralQAAgent"

    # Declares the type of questions this agent can answer
    # Helps the router select this agent for general queries
    capabilities = ["general_questions"]

    # Main method executed when this agent is selected
    # Takes the user prompt context and safety result
    # Returns a structured AgentResult
    def run(self, prompt, context, guardrails):
        return AgentResult(
            # Simple explanation suitable for beginner users
            response="This system routes user prompts to specialized agents based on intent and safety.",
            # No follow up actions are required for general questions
            action_items=[],
            # No external configuration is needed
            required_configs={},
            # Trace information for auditing and debugging
            trace={"agent": self.name}
        )