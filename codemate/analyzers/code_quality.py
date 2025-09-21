
def analyze_code(pr_data, openai_key=None):
    """
    Simple static analysis for PR files.
    If openai_key is provided, AI suggestions can be added later.
    """
    feedback = []
    for f in pr_data["files"]:
        name = f["filename"]
        content = f["content"]

        if "print(" in content:
            feedback.append(f"{name}: Avoid using print statements in production code.")
        elif len(content.strip()) == 0:
            feedback.append(f"{name}: File is empty.")

    if openai_key:
        feedback.append("AI suggestion: Consider improving function docstrings.")

    return feedback
