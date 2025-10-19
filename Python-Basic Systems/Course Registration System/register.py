import json
from user import Student, Teacher


def password_rule(password):
    # Password must be 6-length long and has at least a number and a character
    if not (len(password) >= 6 and any(char.isdigit() for char in password)
            and any(char.isalpha() for char in password) and
            not any(char.isspace() for char in password)):
        return False
    return True


def register_terminal(command, instance):
    full_name = input(f"{command}>Full Name ")
    username = input(f"{command}>Username ")
    email = input(f"{command}>Email ")

    while not email.endswith("@gmail.com"):
        print("% Invalid Input for Email.")
        email = input(f"{command}>Email ")

    while True:
        password = input(f"{command}>Password ")

        # This command cannot be chosen as a password since it violates thw whitespace rule
        if password in ['show password rules', 'sh pass r',
                        'sh password r', 'show pass r', 'show password r']:
            print("Password Rules:\n * Must be 6-character long "
                  "\n * Must contain at least one digit (range 0-9). "
                  "\n * Must contain at least one character (range A-Z or a-z). "
                  "\n * Must not contain any whitespace.")
            continue

        if not password_rule(password):
            print("% Invalid Password. Enter command 'show password rules' "
                  "to get the password rules.")
            continue

        break  # We need to break the loop to finalize everything

    confirm_password = input(f"{command}>Confirm Password ")
    while password != confirm_password:
        print("% Password do not match.")
        confirm_password = input(f"{command}>Confirm Password ")

    obj = instance(full_name, username, email, password).to_dict()
    filepath = f"{instance.get_name()}.json"

    # Add the user to json
    with open(filepath, 'r') as f:
        data = json.load(f)
        # Convert the data to list
        # Iterate through the file to check
        for d in data:
            # Check if the username already exist
            if d['username'] == username:
                print("% Username already exists. Choose a different one.")
                return
            if d['email'] == email:
                print("% Email already exists. Choose a different one.")
                return

    # Append to the data
    data.append(obj)
    # Save the dictionary to JSON file
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"{instance.get_name()} registered successfully!!")
