import json

# This function loads the dataset from a file
# It reads one record per line in JSONL format
# The dataset is used to configure agent instructions and risk levels
def load_dataset(path="dataset.jsonl"):
    # List used to store all parsed dataset records
    records = []

    # Open the dataset file using UTF eight encoding
    # This ensures text is read correctly
    with open(path, "r", encoding="utf-8") as f:
        # Read the file line by line
        # Each line represents one training style sample
        for line in f:
            # Remove extra spaces and line breaks
            line = line.strip()

            # Skip empty lines if any exist
            if line:
                # Convert the JSON text into a Python dictionary
                records.append(json.loads(line))

    # Return the full list of dataset records
    return records