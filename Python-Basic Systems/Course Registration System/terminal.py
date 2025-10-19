# This is the main file for running the terminal
from command import check_command


def main():
    while True:
        # Simulate a terminal
        value = input("User>")
        check_command(value)


if __name__ == '__main__':
    main()
