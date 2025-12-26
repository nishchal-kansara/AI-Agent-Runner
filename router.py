from agents.general_qa import GeneralQAAgent
from agents.task_planner import TaskPlannerAgent
from agents.data_query import DataQueryAgent
from agents.integration import IntegrationAgent

# This dictionary holds all available agents in the system
# Each key represents an intent value
# Each value is an initialized agent instance
AGENTS = {
    "general_qa": GeneralQAAgent(),
    "task_planning": TaskPlannerAgent(),
    "data_query": DataQueryAgent(),
    "integration": IntegrationAgent()
}

# This function selects the correct agent based on intent
# It enables dynamic routing of user requests
# The intent is assumed to be validated earlier
def route(intent):
    return AGENTS[intent]