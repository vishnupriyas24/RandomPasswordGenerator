import random
import string
def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    character_set = ''
    if use_letters:
        character_set += string.ascii_letters
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation
    if not character_set:
        raise ValueError("No character types selected")
    password = ''.join(random.choice(character_set) for _ in range(length))
    return password
def get_user_preferences():
    while True:
        try:
            length = int(input("Enter the password length (must be a positive integer): "))
            if length <= 0:
                raise ValueError("Password length must be greater than zero.")
            break
        except ValueError as ve:
            print(f"Invalid input: {ve}. Please try again.")
    use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'
    if not (use_letters or use_numbers or use_symbols):
        print("At least one character type must be selected. Please try again.")
        return get_user_preferences()
    return length, use_letters, use_numbers, use_symbols
def main():
    print("Welcome to the Password Generator!")
    length, use_letters, use_numbers, use_symbols = get_user_preferences()
    try:
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()
