# This function builds an instruction store from the dataset
# The store maps each intent to its system instruction and metadata
# It allows agents to behave consistently based on training examples
def build_instruction_store(dataset):
    # Dictionary used to hold instructions for each intent
    store = {}

    # Loop through each dataset record
    for item in dataset:
        # Extract the intent associated with this record
        intent = item["intent"]

        # Find the system message from the chat messages
        # This message defines how the agent should behave
        system_msg = next(
            m["content"] for m in item["messages"]
            if m["role"] == "system"
        )

        # Store instruction details for this intent
        store[intent] = {
            # System level instruction used to guide the agent
            "system_instruction": system_msg,

            # Risk level associated with this intent
            # Used by guardrails for safety decisions
            "risk": item["risk"],

            # Optional tags describing user diversity
            # Useful for analysis and auditing
            "diversity_tags": item.get("diversity_tags", [])
        }

    # Return the completed instruction store
    return store