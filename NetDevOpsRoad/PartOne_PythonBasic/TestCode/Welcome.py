def get_valid_age(prompt):
    while True:
        age = input(prompt)
        if age.isdigit() and int(age) > 0:
            return int(age)  # Return age as an integer
        else:
            print("Invalid input. Please enter a positive number for age.")


# A function to ensure valid gender input
def get_valid_gender(prompt):
    while True:
        gender = input(prompt).strip().lower()
        if gender in ["male", "female", "other"]:
            return gender.capitalize()  # Capitalize first letter for uniformity
        else:
            print("Invalid input. Please enter 'male', 'female', or 'other'.")


# Get username with a simple blank check
def get_valid_name(prompt):
    while True:
        name = input(prompt).strip()
        if len(name) > 0:
            return name
        else:
            print("Invalid input. Please enter a non-empty name.")


# Prompt the user for input with validation
name = get_valid_name("Please enter your name: ")
gender = get_valid_gender("Please enter your gender (male, female, other): ")
age = get_valid_age("Please enter your age: ")

# Display a personalized greeting
print(f"Hello, {name}! You are a {gender} and {age} years old. Nice to meet you!")