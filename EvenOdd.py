from time import sleep

def handle_invalid_attempt(attempts, max_attempts, message):
    attempts += 1
    remaining = max_attempts - attempts
    if attempts < max_attempts:
        print(f"{message} ({remaining} {'attempt' if remaining == 1 else 'attempts'} left)")
        return attempts, False
    else:
        print('Too many invalid attempts. Try again later.')
        return attempts, True

def get_valid_input(attempts, max_attempts):
    try:
        number = int(input('Enter a valid non-negative integer: '))
        if number < 0:
            attempts, too_many_attempts = handle_invalid_attempt(attempts, max_attempts, "Invalid input! Please enter a non-negative integer.")
            return None, attempts, False, too_many_attempts
        if number > 10**6:
            attempts, too_many_attempts = handle_invalid_attempt(attempts, max_attempts, "Number too large! Please enter a smaller non-negative integer!")
            return None, attempts, False, too_many_attempts
        return number, attempts, True, False
    except ValueError:
        attempts, too_many_attempts = handle_invalid_attempt(attempts, max_attempts, "Invalid input! Please enter a non-negative integer.")
        return None, attempts, False, too_many_attempts

def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is even. 😊")
    else:
        print(f"{number} is odd. 🤔")
max_attempts = 3 #Total attempts
while True:
    attempts = 0 #Current attempts
    number = None #Initial number
    print('This program checks if a number is even or odd.')
    too_many_attempts = False
    while attempts < max_attempts and not too_many_attempts:
        number, attempts, valid, too_many_attempts = get_valid_input(attempts, max_attempts)
        if valid:
            break
    if number is not None:
        check_even_odd(number)    
    retry = input("Check another number? (yes/no): ").lower()
    if retry != 'yes':
        break
input("Press enter to exit...")
