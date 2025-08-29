import re

def check_password_strength(password):
    # Criteria
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Calculate strength score
    errors = [length_error, lowercase_error, uppercase_error, digit_error, special_char_error]
    score = 5 - sum(errors)

    # Strength levels
    if score == 5:
        strength = "Very Strong 💪"
    elif score == 4:
        strength = "Strong ✅"
    elif score == 3:
        strength = "Medium ⚠️"
    else:
        strength = "Weak ❌"

    # Show feedback
    print(f"\nPassword: {password}")
    print(f"Strength: {strength}")

    if length_error:
        print("- Password should be at least 8 characters long")
    if lowercase_error:
        print("- Include at least one lowercase letter")
    if uppercase_error:
        print("- Include at least one uppercase letter")
    if digit_error:
        print("- Include at least one number")
    if special_char_error:
        print("- Include at least one special character (!@#$ etc.)")


# Example usage
if __name__ == "__main__":
    pwd = input("Enter a password to test: ")
    check_password_strength(pwd)