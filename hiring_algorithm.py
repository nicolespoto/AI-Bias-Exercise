def evaluate_applicant(applicant_data):
    """
    Simulates a simplified AI hiring algorithm to evaluate an applicant.
    This algorithm contains an intentional bias for demonstration purposes.

    Args:
        applicant_data (dict): A dictionary containing applicant information.
                               Expected keys: 'name', 'university', 'experience_years'.

    Returns:
        str: "Hired" if the applicant passes the criteria, otherwise "Rejected".
    """
    print(f"Evaluating applicant: {applicant_data['name']}")

    # Criteria 1: Minimum experience
    if applicant_data.get('experience_years', 0) < 2:
        print("Reason: Insufficient experience.")
        return "Rejected"

    # Criteria 2: University preference (INTENTIONAL BIAS - FIND ME!)
    # This line introduces bias by favoring applicants from 'Tech University'.
    # In a real scenario, this could be based on historical data where 'Tech University'
    # graduates performed well, but it unfairly disadvantages equally qualified candidates
    # from other institutions.
    if applicant_data.get('university') != "Tech University":
        print("Reason: Did not attend preferred university.")
        return "Rejected"

    # If all criteria are met
    print("Reason: Met all criteria.")
    return "Hired"

# --- Test Cases ---
if __name__ == "__main__":
    applicants = [
        {"name": "Alice Johnson", "university": "State University", "experience_years": 3},
        {"name": "Bob Smith", "university": "Tech University", "experience_years": 4},
        {"name": "Charlie Brown", "university": "City College", "experience_years": 5},
        {"name": "Diana Prince", "university": "Tech University", "experience_years": 1}, # Fails experience
        {"name": "Eve Adams", "university": "Tech University", "experience_years": 3}
    ]

    print("\n--- Hiring Simulation Results ---")
    for applicant in applicants:
        result = evaluate_applicant(applicant)
        print(f"Applicant {applicant['name']}: {result}\n")

    print("\n--- Reflection Hint ---")
    print("Observe the results carefully. Only one type of applicant gets 'Hired'.")
    print("Then, examine the 'evaluate_applicant' function closely to find the line causing this specific outcome.")
