import re

def check_password_strength(password):
    # Criteria for strong password
    length_criteria = len(password) >= 8
    upper_case_criteria = re.search(r'[A-Z]', password) is not None
    lower_case_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[^A-Za-z0-9]', password) is not None
    
    # Assessing password strength
    score = 0
    if length_criteria:
        score += 1
    if upper_case_criteria:
        score += 1
    if lower_case_criteria:
        score += 1
    if number_criteria:
        score += 1
    if special_char_criteria:
        score += 1

    # Providing feedback based on the score
    if score == 5:
        strength = "Strong"
    elif score == 4:
        strength = "Good"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    feedback = {
        "Strength": strength,
        "Length": "Meets criteria" if length_criteria else "Too short (min 8 characters)",
        "Uppercase": "Contains uppercase letters" if upper_case_criteria else "No uppercase letters",
        "Lowercase": "Contains lowercase letters" if lower_case_criteria else "No lowercase letters",
        "Numbers": "Contains numbers" if number_criteria else "No numbers",
        "Special Characters": "Contains special characters" if special_char_criteria else "No special characters"
    }

    return feedback

def main():
    password = input("Enter a password to check its strength: ")
    feedback = check_password_strength(password)

    print("\nPassword Strength Assessment:")
    for criterion, result in feedback.items():
        print(f"{criterion}: {result}")

if __name__ == "__main__":
    main()
