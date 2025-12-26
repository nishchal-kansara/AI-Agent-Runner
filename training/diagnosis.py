# This function analyzes training logs
# It explains why a model may behave incorrectly
# The focus is on reasoning not on model retraining
def diagnose_training_issues(logs: dict) -> dict:
    # List used to collect detected training problems
    issues = []

    # Checks for overfitting behavior
    # Happens when training loss is lower than validation loss
    if logs.get("train_loss") < logs.get("val_loss"):
        issues.append({
            "issue": "Overfitting",
            "cause": "Model memorizing low quality samples",
            "fix": "Reduce epochs and improve data quality"
        })

    # Checks for unsafe behavior learned during training
    # Indicates instruction or safety drift
    if logs.get("unsafe_outputs_detected"):
        issues.append({
            "issue": "Safety Drift",
            "cause": "Unsafe or ambiguous training data",
            "fix": "Use stronger system instructions and guardrails"
        })

    # Checks for unstable training behavior
    # Often caused by an aggressive learning rate
    if logs.get("loss_spikes"):
        issues.append({
            "issue": "Gradient Instability",
            "cause": "Learning rate too high",
            "fix": "Lower learning rate and apply gradient clipping"
        })

    # Returns a structured explanation of all detected issues
    return {"diagnosis": issues}