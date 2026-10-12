import secrets
import string


def generate_password(length, use_uppercase, use_digits, use_symbols):
    """Generate a secure random password."""

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+"

    # Build the allowed character set.
    characters = lowercase

    if use_uppercase:
        characters += uppercase

    if use_digits:
        characters += digits

    if use_symbols:
        characters += symbols

    # Ensure each selected character type appears at least once.
    required = [secrets.choice(lowercase)]

    if use_uppercase:
        required.append(secrets.choice(uppercase))

    if use_digits:
        required.append(secrets.choice(digits))

    if use_symbols:
        required.append(secrets.choice(symbols))

    if length < len(required):
        raise ValueError("Password length is too short.")

    # Generate the remaining characters.
    remaining = [
        secrets.choice(characters)
        for _ in range(length - len(required))
    ]

    password_characters = required + remaining

    # Randomize the order securely.
    secrets.SystemRandom().shuffle(password_characters)

    return "".join(password_characters)


def main():
    print("\n===== PYTHON PASSWORD GENERATOR =====")

    try:
        length = int(input("Enter password length (4-128): "))

        if not 4 <= length <= 128:
            print("Error: Length must be between 4 and 128.")
            return

    except ValueError:
        print("Error: Please enter a valid whole number.")
        return

    uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == "y"
    digits = input("Include numbers? (y/n): ").strip().lower() == "y"
    symbols = input("Include symbols? (y/n): ").strip().lower() == "y"

    password = generate_password(length, uppercase, digits, symbols)

    print("\nGenerated password:")
    print(password)
    print("\nKeep your password private!")


if __name__ == "__main__":
    main()