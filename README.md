# Password Strength Assessment Tool

This Python-based tool assesses the strength of a password based on various criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters. The tool provides users with feedback on their password's strength and suggestions for improvement.

## Features
- **Length Check**: Ensures the password is at least 8 characters long.
- **Uppercase Letter Check**: Requires at least one uppercase letter.
- **Lowercase Letter Check**: Requires at least one lowercase letter.
- **Number Check**: Requires at least one number.
- **Special Character Check**: Requires at least one special character (e.g., `!@#$%^&*`).
- **Strength Assessment**: Provides a password strength rating from "Very Weak" to "Strong".
- **Feedback**: Detailed feedback on the password's adherence to the criteria.

## How It Works
1. The user inputs a password.
2. The script checks the password against the following criteria:
   - Length (minimum 8 characters)
   - Uppercase letters
   - Lowercase letters
   - Numbers
   - Special characters
3. The script calculates a strength score based on how many criteria the password meets.
4. The password strength is classified as:
   - **Strong**: Meets all criteria.
   - **Good**: Meets four criteria.
   - **Moderate**: Meets three criteria.
   - **Weak**: Meets two criteria.
   - **Very Weak**: Meets fewer than two criteria.
5. The user receives feedback on their password's strength and what can be improved.

## Prerequisites
- Python 3.x installed on your system.

## Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/tholumuzikhuboni/PRODIGY_CY_03.git
   cd PRODIGY_CY_03

2. **Run the script**:
   ```bash
   python password-strength.py

3. **Follow the on-screen instructions**:
   - Enter the password you want to assess.
   - The tool will provide feedback on its strength.
 
