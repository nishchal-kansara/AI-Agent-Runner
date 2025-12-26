from agents.base import BaseAgent, AgentResult

# This agent is responsible for planning tasks
# It helps break a complex request into clear steps
# Used when the user needs guidance on execution order
class TaskPlannerAgent(BaseAgent):
    # Name used for routing and trace logging
    name = "TaskPlannerAgent"

    # Declares the type of capability this agent provides
    # Helps the router select this agent for planning tasks
    capabilities = ["task_planning"]

    # Main execution method for task planning
    # Receives user input context and safety decision
    # Returns a structured AgentResult
    def run(self, prompt, context, guardrails):
        return AgentResult(
            # High level response indicating a plan is provided
            response="Here is a step-by-step execution plan.",
            # Ordered list of actions to guide the user
            action_items=[
                "Clarify goal",
                "Break into tasks",
                "Execute sequentially"
            ],
            # No external configuration is required
            required_configs={},
            # Trace information for auditing and evaluation
            trace={"agent": self.name}
        )
