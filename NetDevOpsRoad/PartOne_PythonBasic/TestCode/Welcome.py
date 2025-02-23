import re


# Function to validate name input
def get_valid_name(prompt):
    while True:
        name = input(prompt).strip()
        # Allow only letters, spaces, and basic symbols like hyphens
        if re.match(r"^[a-zA-Z\s\-\']+$", name) and len(name) > 1:
            return name.title()  # Capitalize first letter of each word
        else:
            print("Invalid input. Please use letters, spaces, or basic punctuation, and ensure it's not empty.")


# Function to validate gender input
def get_valid_gender(prompt):
    valid_genders = ["male", "female", "other", "non-binary", "genderqueer", "transgender"]
    print(f"Valid options: {', '.join(valid_genders)}")  # Display valid genders to the user
    while True:
        gender = input(prompt).strip().lower()
        if gender in valid_genders:
            return gender.capitalize()  # Consistent capitalization
        else:
            print(f"Invalid input. Please choose from the listed options: {', '.join(valid_genders)}.")


# Function to validate age input (positive integer)
def get_valid_age(prompt):
    while True:
        age = input(prompt)
        if age.isdigit() and int(age) > 0:
            return int(age)  # Return as integer for further processing
        else:
            print("Invalid input. Please enter a positive number for your age.")


# Main execution flow
if __name__ == "__main__":
    # Collect user inputs with validation
    name = get_valid_name("Please enter your GIVEN name: ")
    gender = get_valid_gender("Please enter the gender you identify with: ")
    age = get_valid_age("Please enter your age: ")

    # Create a personalized greeting message
    print("\n--- USER PROFILE ---")
    print(f"Name   : {name}")
    print(f"Gender : {gender}")
    print(f"Age    : {age}")
    print("\nHello, {name}! You are a {gender} and {age} years old. Nice to meet you!")