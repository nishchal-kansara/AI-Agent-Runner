# This function applies safety rules before an agent is executed
# It checks the risk level associated with the user request
# The goal is to prevent unsafe or restricted actions
def apply_guardrails(prompt: str, risk: str):
    # If the request is marked as high risk
    # The system blocks further processing
    if risk == "high":
        return {
            # Indicates the request is not allowed
            "allowed": False,
            # Explains why the request was blocked
            "reason": "High risk request detected"
        }

    # If no safety issue is found
    # The request is allowed to proceed
    return {"allowed": True}